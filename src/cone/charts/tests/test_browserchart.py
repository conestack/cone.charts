from node.tests import NodeTestCase
from cone.app.model import BaseNode
from cone.charts.browser.chart.chart import ChartTile
from cone.charts.browser.chart.line import LineChartTile
from cone.charts.browser.chart.pie import PieChartTile
from cone.charts.browser.chart.bar import BarChartTile
from cone.charts.browser.chart.polar import PolarChartTile
from cone.charts import testing


class TestBrowserCharts(NodeTestCase):
    layer = testing.conechart_layer

    def test_line_chart(self):
        request = self.layer.new_request()
        chart_tile = LineChartTile()
        chart_tile.request = request
        chart_tile.model = BaseNode()

        self.assertEqual(chart_tile.chart_id, 'cone-chart')
        self.assertEqual(chart_tile.chart_css, 'cone-chart')
        self.assertEqual(chart_tile.chart_factory, 'cone_charts.LineChartTile')
        self.assertEqual(chart_tile.chart_options, None)
        self.assertEqual(chart_tile.chart_params, {})
        chart_tile.render()

    def test_pie_chart(self):
        request = self.layer.new_request()
        chart_tile = PieChartTile()
        chart_tile.request = request
        chart_tile.model = BaseNode()

        self.assertEqual(chart_tile.chart_id, 'cone-chart')
        self.assertEqual(chart_tile.chart_css, 'cone-chart')
        self.assertEqual(chart_tile.chart_factory, 'cone_charts.PieChartTile')
        self.assertEqual(chart_tile.chart_options, None)
        self.assertEqual(chart_tile.chart_params, {})
        chart_tile.render()

    def test_bar_chart(self):
        request = self.layer.new_request()
        chart_tile = BarChartTile()
        chart_tile.request = request
        chart_tile.model = BaseNode()

        self.assertEqual(chart_tile.chart_id, 'cone-chart')
        self.assertEqual(chart_tile.chart_css, 'cone-chart')
        self.assertEqual(chart_tile.chart_factory, 'cone_charts.BarChartTile')
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

    def test_polar_chart(self):
        request = self.layer.new_request()
        chart_tile = PolarChartTile()
        chart_tile.request = request
        chart_tile.model = BaseNode()

        self.assertEqual(chart_tile.chart_id, 'cone-chart')
        self.assertEqual(chart_tile.chart_css, 'cone-chart')
        self.assertEqual(chart_tile.chart_factory,
                         'cone_charts.PolarChartTile')
        self.assertEqual(chart_tile.chart_options, None)
        self.assertEqual(chart_tile.chart_params, {})
        chart_tile.render()
