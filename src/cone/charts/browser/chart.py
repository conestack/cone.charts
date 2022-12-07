from cone.app.browser.utils import make_url
from cone.tile import register_tile
from cone.tile import Tile
from cone.tile import tile
import json
import sys
import venusian


class chart_tile(tile):
    """Extended tile decorator for registering chart tiles.

    Additionally to the tile, a JSON view gets registered which is used in
    browser to query chart data from server.

    Usage:

    .. code-block:: python

        @chart_tile(
            name='examplelinechart',
            interface=ExampleModel,
            permission='view')
        class ExampleLineChartTile(LineChartTile):

            @staticmethod
            def chart_data(model, request):
                # This function is the actual JSON view callable.
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
    """Tile for rendering a chart."""

    chart_factory = 'cone_charts.ChartTile'
    """JavaScript factory used for chart creation in browser.

    The defined factory must accept the chart related DOM element and the
    chart settings as arguments and is responsible for creating the chart.

    It points to a class or function and gets searched by dot separated path
    on browser ``window``, e.g ``cone_charts.ChartTile`` corresponds to:

    .. code-block:: js

        window.cone_charts: {
            ChartTile: ...
        }

    If JS chart implementation needs to be customized, it can be done by
    subclassing ``cone_chart.ChartTile`` and setting it as ``chart_factory``:

    .. code-block:: js

        my_namespace = {};

        my_namespace.MyChart = class extends cone_charts.ChartTile {
            constructor(elem, settings) {
                ...
            }
        }
    """

    chart_type = None
    """Type of the chart. Used by JavaScript implementation to define the
    chart type."""

    chart_id = 'cone-chart'
    """ID of the chart DOM element."""

    chart_css = 'cone-chart'
    """CSS class of the chart DOM element.

    The default JS chart implementation searches for all ``div`` elements with
    ``cone-chart`` CSS class and initializes a chart instance for each of them.
    """

    chart_options = None
    """Chart options passed to the Chart.js constructor.

    Refer to
    `documentation <https://www.chartjs.org/docs/4.0.1/general/options.html>`_
    for detailed information about chart options.

    Example:

    .. code-block:: python
    
        chart_options = {
            'responsive': True,
            'plugins': {
                'legend': {
                    'position': 'top',
                },
                'title': {
                    'display': True,
                    'text': 'My Chart'
                }
            }
        }
    """

    chart_params = {}
    """Dict containing request parameters which gets sent to server when
    querying chart data.

    Defaults to an empty dict.
    """

    @property
    def chart_settings(self):
        """Dictionary containing chart settings. These settings get passed to
        the chart factory on client side.

        This property can be customized to pass additional settings to
        custom chart factory if needed.
        """
        return dict(
            factory=self.chart_factory,
            type=self.chart_type,
            options=self.chart_options,
            params=self.chart_params,
            data_source=make_url(
                self.request,
                node=self.model,
                resource='{}_chart_data'.format(self.name)
            )
        )

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.

        This function gets registered as JSON view by ``chart_tile`` decorator
        and gets called from client side to query chart data.

        Refer to
        `documentation <https://www.chartjs.org/docs/4.0.1/charts>`_
        for detailed information about chart data.
        """
        raise NotImplementedError(
            'Abstract ``ChartTile``does implement ``chart_data``'
        )

    def render(self):
        """Renders a ``div`` element with chart settings as JSON data attribute
        and a canvas which get used by the ``Chart.js`` library to render the
        actual chart.
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
