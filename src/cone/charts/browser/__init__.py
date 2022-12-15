import os
import webresource as wr


resources_dir = os.path.join(os.path.dirname(__file__), 'static')


chartjs_resources = wr.ResourceGroup(
    name='cone.charts-chartjs',
    directory=os.path.join(resources_dir, 'chartjs'),
    path='chartjs'
)
chartjs_resources.add(wr.ScriptResource(
    name='chart-js',
    resource='chart.umd.js',
    compressed='chart.umd.min.js'
))

luxon_resources = wr.ResourceGroup(
    name='cone.charts-luxon',
    directory=os.path.join(resources_dir, 'luxon'),
    path='luxon'
)
luxon_resources.add(wr.ScriptResource(
    name='luxon-js',
    resource='luxon.js',
    compressed='luxon.min.js'
))

chartjs_adapterluxon_resources = wr.ResourceGroup(
    name='cone.charts-chartjs-adapter-luxon',
    directory=os.path.join(resources_dir, 'chartjs-adapter-luxon'),
    path='chartjs-adapter-luxon'
)
chartjs_adapterluxon_resources.add(wr.ScriptResource(
    name='chartjs-adapter-luxon-js',
    depends=[
        'chart-js',
        'luxon-js'
    ],
    resource='chartjs-adapter-luxon.js',
    compressed='chartjs-adapter-luxon.min.js'
))

cone_charts_resources = wr.ResourceGroup(
    name='cone.charts-charts',
    directory=os.path.join(resources_dir, 'cone_charts'),
    path='cone_charts'
)
cone_charts_resources.add(wr.ScriptResource(
    name='cone-charts-js',
    resource='cone.charts.js',
    compressed='cone.charts.min.js'
))


def configure_resources(config, settings):
    config.register_resource(chartjs_resources)
    config.register_resource(luxon_resources)
    config.register_resource(chartjs_adapterluxon_resources)
    config.register_resource(cone_charts_resources)

    config.set_resource_include('chart-js', 'authenticated')
    config.set_resource_include('cone-charts-js', 'authenticated')

    include = settings.get('cone.charts.luxon') in ['True', 'true', '1']
    include = 'authenticated' if include else False
    config.set_resource_include('luxon-js', include)
    config.set_resource_include('chartjs-adapter-luxon-js', include)
