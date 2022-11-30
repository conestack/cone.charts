from cone.app.testing import Security


class ChartLayer(Security):

    def make_app(self):
        plugins = [
            'cone.sql',
            'cone.ugm'
        ]
        kw = dict()
        kw['cone.plugins'] = '\n'.join(plugins)
        super().make_app(**kw)


chart_layer = ChartLayer()
