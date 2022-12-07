from cone.app.model import BaseNode
from cone.app.testing import Security
from cone.charts.browser.bar import BarChartTile
from cone.charts.browser.bubble import BubbleChartTile
from cone.charts.browser.chart import chart_tile
from cone.charts.browser.doughnut import DoughnutChartTile
from cone.charts.browser.line import LineChartTile
from cone.charts.browser.pie import PieChartTile
from cone.charts.browser.polar import PolarChartTile
from cone.charts.browser.radar import RadarChartTile
from cone.charts.browser.scatter import ScatterChartTile
from node.tests import NodeTestCase
import sys
import unittest


class ChartsLayer(Security):

    def make_app(self):
        plugins = ['cone.charts']
        kw = dict()
        kw['cone.plugins'] = '\n'.join(plugins)
        super().make_app(**kw)


charts_layer = ChartsLayer()


class TestCharts(NodeTestCase):
    layer = charts_layer

    def test_line_chart(self):
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
        self.assertEqual(chart_tile.render(), (
            '<div class="cone-chart"'
            '     id="cone-chart"'
            '     data-chart-settings=\'{'
                     '"factory": "cone_charts.ChartTile", '
                     '"type": "line", '
                     '"options": null, '
                     '"params": {}, '
                     '"data_source": "http://example.com/None_chart_data"'
                 '}\' >'
            '  <canvas></canvas>'
            '</div>'
        ))
        with self.assertRaises(NotImplementedError) as arc:
            chart_tile.chart_data(chart_tile.model, chart_tile.request)
        self.assertEqual(
            str(arc.exception),
            'Abstract ``LineChartTile`` does not implement ``chart_data``'
        )

    def test_pie_chart(self):
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
        self.assertEqual(chart_tile.render(), (
            '<div class="cone-chart"'
            '     id="cone-chart"'
            '     data-chart-settings=\'{'
                     '"factory": "cone_charts.ChartTile", '
                     '"type": "pie", '
                     '"options": null, '
                     '"params": {}, '
                     '"data_source": "http://example.com/None_chart_data"'
                 '}\' >'
            '  <canvas></canvas>'
            '</div>'
        ))
        with self.assertRaises(NotImplementedError) as arc:
            chart_tile.chart_data(chart_tile.model, chart_tile.request)
        self.assertEqual(
            str(arc.exception),
            'Abstract ``PieChartTile`` does not implement ``chart_data``'
        )

    def test_bar_chart(self):
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
        self.assertEqual(chart_tile.render(), (
            '<div class="cone-chart"'
            '     id="cone-chart"'
            '     data-chart-settings=\'{'
                     '"factory": "cone_charts.ChartTile", '
                     '"type": "bar", '
                     '"options": {'
                         '"options": {'
                             '"scales": {'
                                 '"y": {'
                                     '"beginAtZero": true'
                                 '}'
                             '}'
                         '}'
                     '}, '
                     '"params": {}, '
                     '"data_source": "http://example.com/None_chart_data"'
                 '}\' >'
            '  <canvas></canvas>'
            '</div>'
        ))
        with self.assertRaises(NotImplementedError) as arc:
            chart_tile.chart_data(chart_tile.model, chart_tile.request)
        self.assertEqual(
            str(arc.exception),
            'Abstract ``BarChartTile`` does not implement ``chart_data``'
        )

    def test_polar_chart(self):
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
        self.assertEqual(chart_tile.render(), (
            '<div class="cone-chart"'
            '     id="cone-chart"'
            '     data-chart-settings=\'{'
                     '"factory": "cone_charts.ChartTile", '
                     '"type": "polarArea", '
                     '"options": null, '
                     '"params": {}, '
                     '"data_source": "http://example.com/None_chart_data"'
                 '}\' >'
            '  <canvas></canvas>'
            '</div>'
        ))
        with self.assertRaises(NotImplementedError) as arc:
            chart_tile.chart_data(chart_tile.model, chart_tile.request)
        self.assertEqual(
            str(arc.exception),
            'Abstract ``PolarChartTile`` does not implement ``chart_data``'
        )

    def test_radar_chart(self):
        request = self.layer.new_request()
        chart_tile = RadarChartTile()
        chart_tile.request = request
        chart_tile.model = BaseNode()

        self.assertEqual(chart_tile.chart_id, 'cone-chart')
        self.assertEqual(chart_tile.chart_css, 'cone-chart')
        self.assertEqual(chart_tile.chart_factory, 'cone_charts.ChartTile')
        self.assertEqual(chart_tile.chart_type, 'radar')
        self.assertEqual(chart_tile.chart_options, None)
        self.assertEqual(chart_tile.chart_params, {})
        self.assertEqual(chart_tile.render(), (
            '<div class="cone-chart"'
            '     id="cone-chart"'
            '     data-chart-settings=\'{'
                     '"factory": "cone_charts.ChartTile", '
                     '"type": "radar", '
                     '"options": null, '
                     '"params": {}, '
                     '"data_source": "http://example.com/None_chart_data"'
                 '}\' >'
            '  <canvas></canvas>'
            '</div>'
        ))
        with self.assertRaises(NotImplementedError) as arc:
            chart_tile.chart_data(chart_tile.model, chart_tile.request)
        self.assertEqual(
            str(arc.exception),
            'Abstract ``RadarChartTile`` does not implement ``chart_data``'
        )

    def test_scatter_chart(self):
        request = self.layer.new_request()
        chart_tile = ScatterChartTile()
        chart_tile.request = request
        chart_tile.model = BaseNode()

        self.assertEqual(chart_tile.chart_id, 'cone-chart')
        self.assertEqual(chart_tile.chart_css, 'cone-chart')
        self.assertEqual(chart_tile.chart_factory, 'cone_charts.ChartTile')
        self.assertEqual(chart_tile.chart_type, 'scatter')
        self.assertEqual(chart_tile.chart_options, None)
        self.assertEqual(chart_tile.chart_params, {})
        self.assertEqual(chart_tile.render(), (
            '<div class="cone-chart"'
            '     id="cone-chart"'
            '     data-chart-settings=\'{'
                     '"factory": "cone_charts.ChartTile", '
                     '"type": "scatter", '
                     '"options": null, '
                     '"params": {}, '
                     '"data_source": "http://example.com/None_chart_data"'
                 '}\' >'
            '  <canvas></canvas>'
            '</div>'
        ))
        with self.assertRaises(NotImplementedError) as arc:
            chart_tile.chart_data(chart_tile.model, chart_tile.request)
        self.assertEqual(
            str(arc.exception),
            'Abstract ``ScatterChartTile`` does not implement ``chart_data``'
        )

    def test_bubble_chart(self):
        request = self.layer.new_request()
        chart_tile = BubbleChartTile()
        chart_tile.request = request
        chart_tile.model = BaseNode()

        self.assertEqual(chart_tile.chart_id, 'cone-chart')
        self.assertEqual(chart_tile.chart_css, 'cone-chart')
        self.assertEqual(chart_tile.chart_factory, 'cone_charts.ChartTile')
        self.assertEqual(chart_tile.chart_type, 'bubble')
        self.assertEqual(chart_tile.chart_options, None)
        self.assertEqual(chart_tile.chart_params, {})
        self.assertEqual(chart_tile.render(), (
            '<div class="cone-chart"'
            '     id="cone-chart"'
            '     data-chart-settings=\'{'
                     '"factory": "cone_charts.ChartTile", '
                     '"type": "bubble", '
                     '"options": null, '
                     '"params": {}, '
                     '"data_source": "http://example.com/None_chart_data"'
                 '}\' >'
            '  <canvas></canvas>'
            '</div>'
        ))
        with self.assertRaises(NotImplementedError) as arc:
            chart_tile.chart_data(chart_tile.model, chart_tile.request)
        self.assertEqual(
            str(arc.exception),
            'Abstract ``BubbleChartTile`` does not implement ``chart_data``'
        )

    def test_doughnut_chart(self):
        request = self.layer.new_request()
        chart_tile = DoughnutChartTile()
        chart_tile.request = request
        chart_tile.model = BaseNode()

        self.assertEqual(chart_tile.chart_id, 'cone-chart')
        self.assertEqual(chart_tile.chart_css, 'cone-chart')
        self.assertEqual(chart_tile.chart_factory, 'cone_charts.ChartTile')
        self.assertEqual(chart_tile.chart_type, 'doughnut')
        self.assertEqual(chart_tile.chart_options, None)
        self.assertEqual(chart_tile.chart_params, {})
        self.assertEqual(chart_tile.render(), (
            '<div class="cone-chart"'
            '     id="cone-chart"'
            '     data-chart-settings=\'{'
                     '"factory": "cone_charts.ChartTile", '
                     '"type": "doughnut", '
                     '"options": null, '
                     '"params": {}, '
                     '"data_source": "http://example.com/None_chart_data"'
                 '}\' >'
            '  <canvas></canvas>'
            '</div>'
        ))
        with self.assertRaises(NotImplementedError) as arc:
            chart_tile.chart_data(chart_tile.model, chart_tile.request)
        self.assertEqual(
            str(arc.exception),
            'Abstract ``DoughnutChartTile`` does not implement ``chart_data``'
        )

    def test_chart_tile_decorator(self):
        request = self.layer.new_request()
        obj = LineChartTile()
        obj.request = request
        obj.model = BaseNode()
        obj = chart_tile()(obj)
        view, view_name, arg1, arg2 = obj.__venusian_callbacks__['pyramid'][0]
        self.assertEqual(view_name, 'cone.charts.tests')


def run_tests():
    from cone.charts import tests
    from zope.testrunner.runner import Runner

    suite = unittest.TestSuite()
    suite.addTest(unittest.findTestCases(tests))

    runner = Runner(found_suites=[suite])
    runner.run()
    sys.exit(int(runner.failed))


if __name__ == '__main__':
    run_tests()