from cone.app.model import BaseNode
from cone.charts import testing
from cone.charts.browser.chart.bar import BarChartTile
from cone.charts.browser.chart.chart import chart_tile
from cone.charts.browser.chart.line import LineChartTile
from cone.charts.browser.chart.pie import PieChartTile
from cone.charts.browser.chart.polar import PolarChartTile
from node.tests import NodeTestCase


class TestBrowserCharts(NodeTestCase):
    layer = testing.chart_layer

    def test_line_chart(self):
        """Testing the line chart tile and the pre-configurations
        """
        request = self.layer.new_request()
        chart_tile = LineChartTile()
        chart_tile.request = request
        chart_tile.model = BaseNode()

        self.assertEqual(chart_tile.chart_id, 'cone-chart')
        self.assertEqual(chart_tile.chart_css, 'cone-chart')
        self.assertEqual(chart_tile.chart_factory, 'cone_charts.ChartTile')
        self.assertEqual(chart_tile.chart_type, 'line')
        self.assertEqual(chart_tile.chart_options, None)
        self.assertEqual(chart_tile.chart_params, {})
        chart_tile.render()
        with self.assertRaises(NotImplementedError):
            chart_tile.chart_data(chart_tile.model, chart_tile.request)

    def test_pie_chart(self):
        """Testing the pie chart tile and the pre-configurations
        """
        request = self.layer.new_request()
        chart_tile = PieChartTile()
        chart_tile.request = request
        chart_tile.model = BaseNode()

        self.assertEqual(chart_tile.chart_id, 'cone-chart')
        self.assertEqual(chart_tile.chart_css, 'cone-chart')
        self.assertEqual(chart_tile.chart_factory, 'cone_charts.ChartTile')
        self.assertEqual(chart_tile.chart_type, 'pie')
        self.assertEqual(chart_tile.chart_options, None)
        self.assertEqual(chart_tile.chart_params, {})
        chart_tile.render()
        with self.assertRaises(NotImplementedError):
            chart_tile.chart_data(chart_tile.model, chart_tile.request)

    def test_bar_chart(self):
        """Testing the bar chart tile and the pre-configurations
        """
        request = self.layer.new_request()
        chart_tile = BarChartTile()
        chart_tile.request = request
        chart_tile.model = BaseNode()

        self.assertEqual(chart_tile.chart_id, 'cone-chart')
        self.assertEqual(chart_tile.chart_css, 'cone-chart')
        self.assertEqual(chart_tile.chart_factory, 'cone_charts.ChartTile')
        self.assertEqual(chart_tile.chart_type, 'bar')
        self.assertEqual(chart_tile.chart_options, {
            'options': {
                'scales': {
                    'y': {
                        'beginAtZero': True
                    }
                }
            }
        })
        self.assertEqual(chart_tile.chart_params, {})
        chart_tile.render()
        with self.assertRaises(NotImplementedError):
            chart_tile.chart_data(chart_tile.model, chart_tile.request)

    def test_polar_chart(self):
        """Testing the polar chart tile and the pre-configurations
        """
        request = self.layer.new_request()
        chart_tile = PolarChartTile()
        chart_tile.request = request
        chart_tile.model = BaseNode()

        self.assertEqual(chart_tile.chart_id, 'cone-chart')
        self.assertEqual(chart_tile.chart_css, 'cone-chart')
        self.assertEqual(chart_tile.chart_factory, 'cone_charts.ChartTile')
        self.assertEqual(chart_tile.chart_type, 'polarArea')
        self.assertEqual(chart_tile.chart_options, None)
        self.assertEqual(chart_tile.chart_params, {})
        chart_tile.render()
        with self.assertRaises(NotImplementedError):
            chart_tile.chart_data(chart_tile.model, chart_tile.request)

    def test_chart_tile_decorator(self):
        """ Testing the chart tile decorator
            @chart_tile(
                name='test',
                interface=BaseNode,
                permission='view',
            )
            class TestChartTile(LineChartTile):
                ...
        """
        request = self.layer.new_request()
        obj = LineChartTile()
        obj.request = request
        obj.model = BaseNode()
        obj = chart_tile()(obj)
        view, view_name, arg1, arg2 = obj.__venusian_callbacks__['pyramid'][0]
        self.assertEqual(view_name, 'cone.charts.tests.test_browserchart')
