from cone.app.model import BaseNode
from cone.app.testing import Security
from cone.charts import browser
from cone.charts.browser.bar import BarChartTile
from cone.charts.browser.bubble import BubbleChartTile
from cone.charts.browser.chart import ChartTile
from cone.charts.browser.chart import chart_tile
from cone.charts.browser.doughnut import DoughnutChartTile
from cone.charts.browser.line import LineChartTile
from cone.charts.browser.pie import PieChartTile
from cone.charts.browser.polar import PolarChartTile
from cone.charts.browser.radar import RadarChartTile
from cone.charts.browser.scatter import ScatterChartTile
from cone.tile import render_tile
from node.tests import NodeTestCase
import os
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
        class Model(BaseNode):
            ...

        with self.layer.hook_tile_reg():
            @chart_tile(
                name='test_chart',
                interface=Model,
                permission='view')
            class TestChartTile(ChartTile):
                @staticmethod
                def chart_data(model, request):
                    return 'CHART DATA'

        model = Model()
        request = self.layer.new_request()
        with self.layer.authenticated('manager'):
            res = render_tile(model, request, 'test_chart')
        self.assertEqual(res, (
            '<div class="cone-chart"'
            '     id="cone-chart"'
            '     data-chart-settings=\'{'
                     '"factory": "cone_charts.ChartTile", '
                     '"type": null, '
                     '"options": null, '
                     '"params": {}, '
                     '"data_source": "http://example.com/test_chart_chart_data"'
                 '}\' >'
            '  <canvas></canvas>'
            '</div>'
        ))

        from cone.charts.tests import test_chart_chart_data
        self.assertEqual(test_chart_chart_data.__doc__,
            'Dynamically created by cone.chart.browser.chart.chart_tile'
        )

        with self.layer.authenticated('manager'):
            res = test_chart_chart_data(model, request)
        self.assertEqual(res, 'CHART DATA')


def np(path):
    return path.replace('/', os.path.sep)


class TestResources(unittest.TestCase):
    layer = charts_layer

    def test_chartjs_resources(self):
        resources_ = browser.chartjs_resources
        self.assertTrue(resources_.directory.endswith(np('/static/chartjs')))
        self.assertEqual(resources_.name, 'cone.charts-chartjs')
        self.assertEqual(resources_.path, 'chartjs')

        scripts = resources_.scripts
        self.assertEqual(len(scripts), 1)

        self.assertTrue(scripts[0].directory.endswith(np('/static/chartjs')))
        self.assertEqual(scripts[0].path, 'chartjs')
        self.assertEqual(scripts[0].file_name, 'chart.umd.min.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        styles = resources_.styles
        self.assertEqual(len(styles), 0)

    def test_luxon_resources(self):
        resources_ = browser.luxon_resources
        self.assertTrue(resources_.directory.endswith(np('/static/luxon')))
        self.assertEqual(resources_.name, 'cone.charts-luxon')
        self.assertEqual(resources_.path, 'luxon')

        scripts = resources_.scripts
        self.assertEqual(len(scripts), 1)

        self.assertTrue(scripts[0].directory.endswith(np('/static/luxon')))
        self.assertEqual(scripts[0].path, 'luxon')
        self.assertEqual(scripts[0].file_name, 'luxon.min.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        styles = resources_.styles
        self.assertEqual(len(styles), 0)

    def test_chartjs_adapterluxon_resources(self):
        resources_ = browser.chartjs_adapterluxon_resources
        self.assertTrue(resources_.directory.endswith(np('/static/chartjs-adapter-luxon')))
        self.assertEqual(resources_.name, 'cone.charts-chartjs-adapter-luxon')
        self.assertEqual(resources_.path, 'chartjs-adapter-luxon')

        scripts = resources_.scripts
        self.assertEqual(len(scripts), 1)

        self.assertTrue(scripts[0].directory.endswith(np('/static/chartjs-adapter-luxon')))
        self.assertEqual(scripts[0].path, 'chartjs-adapter-luxon')
        self.assertEqual(scripts[0].file_name, 'chartjs-adapter-luxon.min.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        styles = resources_.styles
        self.assertEqual(len(styles), 0)

    def test_cone_charts_resources(self):
        resources_ = browser.cone_charts_resources
        self.assertTrue(resources_.directory.endswith(np('/static/cone_charts')))
        self.assertEqual(resources_.name, 'cone.charts-charts')
        self.assertEqual(resources_.path, 'cone_charts')

        scripts = resources_.scripts
        self.assertEqual(len(scripts), 1)

        self.assertTrue(scripts[0].directory.endswith(np('/static/cone_charts')))
        self.assertEqual(scripts[0].path, 'cone_charts')
        self.assertEqual(scripts[0].file_name, 'cone.charts.min.js')
        self.assertTrue(os.path.exists(scripts[0].file_path))

        styles = resources_.styles
        self.assertEqual(len(styles), 0)


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
