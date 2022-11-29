from cone.sql.testing import SQLLayer


class ConeChartTestingLayer(SQLLayer):

    def tearDown(self):
        super().tearDown()

    def make_app(self):
        plugins = [
            'cone.sql',
            'cone.ugm',
            ]
        kw = dict()
        kw['cone.plugins'] = '\n'.join(plugins)
        super().make_app(**kw)


conechart_layer = ConeChartTestingLayer()