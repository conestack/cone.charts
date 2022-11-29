from cone.app.browser.utils import make_url
from cone.tile import Tile
from cone.tile import register_tile
from cone.tile import tile
import json
import sys
import venusian


class chart_tile(tile):
    """Extended tile decorator for registering chart tiles.

    Additionally registers a JSON view which gets used to query chart data from
    browser.
    """

    def create_data_view(self, ob):
        def chart_data_view(model, request):
            return ob.chart_data(model, request)

        view_name = '{}_chart_data'.format(self.name)
        chart_data_view.__doc__ = (
            'Dynamically created by '
            'cone.chart.browser.chart.chart_tile'
        )
        chart_data_view.__name__ = view_name
        chart_data_view.__qualname__ = view_name
        chart_data_view.__module__ = ob.__module__
        module = sys.modules[ob.__module__]
        setattr(module, view_name, chart_data_view)

        def callback(context, name, ob_):
            config = context.config.with_package(info.module)
            config.add_view(
                view=ob_,
                name='{}_chart_data'.format(self_.name),
                context=self_.interface,
                permission=self_.permission,
                accept='application/json',
                renderer='json'
            )
        self_ = self
        info = self.venusian.attach(
            chart_data_view,
            callback,
            category='pyramid',
            depth=2
        )

    def __call__(self, ob):
        self.venusian = venusian
        self.create_data_view(ob)

        def callback(context, name, ob_):
            register_tile(
                name=self_.name,
                path=self_.path,
                attribute=self_.attribute,
                interface=self_.interface,
                class_=ob_,
                permission=self_.permission,
                strict=self_.strict
            )
        self_ = self
        self.venusian.attach(ob, callback, category='pyramid', depth=1)
        return ob


class ChartTile(Tile):
    """Tile rendering a chart.
    """

    chart_factory = ''
    """ Factory used for chart creation in javascript.

    The defined factory must accept the chart related DOM element and the
    chart settings as arguments and is responsible for creating the chart.
    
    It points to a class or function and gets searched by dot separated path
    on window, e.g. 

    'cone_charts.BarChartTile'

    corresponds to

    window.cone_charts:{
        BarChartTile: ....
    }

    If JS chart factory needs to be customized, it can be done by
    subclassing 'cone_chart.ChartTile':
        my_namespace = {}
        my_namespace.Chart = class extends cone_charts.ChartTile {
            constructor(element, settings) {
                super(element, settings);
                // custom code
            }
            // custom code
        }
    """

    chart_id = 'cone-chart'
    """ ID of chart DOM element."""

    chart_css = 'cone-chart'
    """ CSS class of chart DOM element.

    The default JS chart implementation searches for all `div` elements with
    `cone-chart` class and initializes a chart instances for each of them.

    If chart instance needs to be customized clientside this property must be
    overwritten and the custom JS chart implementation must be adapted to
    search for the custom CSS class.
    """

    chart_options = None
    """
    Chart settings passed to the ChartJS constructor.
    Reference: https://www.chartjs.org/docs/latest/general/options.html

    e.g.
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Chart.js Line Chart'
                }
            }
        }

    """

    chart_params = {}
    """Dict containing request parameters which gets sent to server when
    querying chart data.

    by default empty, can be overwritten by subclassing.
    handy for passing additional parameters to chart data view.
    """

    @property
    def chart_settings(self):
        """Dictionary containing chart settings. This settings get passed to
        the JS chart constructor.

        This property can be customized to pass additional settings to
        custom chart factory if needed.
        """
        return dict(
            factory=self.chart_factory,
            options=self.chart_options,
            params=self.chart_params,
            data_source=make_url(
                self.request,
                node=self.model,
                resource='{}_chart_data'.format(self.name)
            ),
        )

    @staticmethod
    def chart_data(model, request):
        """Return data configuration for chartjs.

        Please refer to official chartjs documentation for details.
        https://www.chartjs.org/docs/latest/

        e.g.
            {
                labels: labels,
                datasets: [
                    {
                        label: 'Dataset 1',
                        data: [10, 20, 30],
                        borderColor: Utils.CHART_COLORS.red,
                        backgroundColor: Utils.transparentize(Utils.CHART_COLORS.red, 0.5),
                    },
                    {
                        label: 'Dataset 2',
                        data: [20, 10, 40],
                        borderColor: Utils.CHART_COLORS.blue,
                        backgroundColor: Utils.transparentize(Utils.CHART_COLORS.blue, 0.5),
                    }
                ]
            }
        """
        raise NotImplementedError(
            'Abstract ``ChartDataProvider``does implement ``data``.'
        )

    def render(self):
        """Renders a div element with chart settings as JSON data attribute.
        and a canvas with get used by the chartjs library to render the chart.

        When editing of the chart appearance is needed, this can be done by
        editing the div element.
        """
        return (
            u'<div class="{css}"'
            u'     id="{id}"'
            u'     data-chart-settings=\'{settings}\' >'
            u'  <canvas></canvas>'
            u'</div>'
        ).format(
            css=self.chart_css,
            id=self.chart_id,
            settings=json.dumps(self.chart_settings)
        )
