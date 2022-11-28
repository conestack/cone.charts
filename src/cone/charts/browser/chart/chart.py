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

    chart_id = 'cone-chart'

    chart_css = 'cone-chart'

    chart_options = None
    """
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
    querying chart data."""

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
        """Return data for chartjs.

        Please refer to official chartjs documentation for details.
        https://www.chartjs.org/docs/latest/

        Example::
            {
                labels: labels,
                datasets: [
                    {
                        label: 'Dataset 1',
                        data: Utils.numbers(NUMBER_CFG),
                        borderColor: Utils.CHART_COLORS.red,
                        backgroundColor: Utils.transparentize(Utils.CHART_COLORS.red, 0.5),
                    },
                    {
                        label: 'Dataset 2',
                        data: Utils.numbers(NUMBER_CFG),
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
