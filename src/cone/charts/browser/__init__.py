from cone.app.browser.resources import resources
from cone.app.browser.resources import set_resource_include
import os
import webresource as wr


resources_dir = os.path.join(os.path.dirname(__file__), 'static')


# chartjs
chartjs_resources = wr.ResourceGroup(
    name='cone.charts-chartjs',
    directory=os.path.join(resources_dir, 'chartjs'),
    path='chartjs',
    group=resources
)
chartjs_resources.add(wr.ScriptResource(
    name='chart-js',
    resource='chart.umd.js',
    compressed='chart.umd.min.js'
))

luxon_resources = wr.ResourceGroup(
    name='cone.charts-luxon',
    directory=os.path.join(resources_dir, 'luxon'),
    path='luxon',
    group=resources
)
luxon_resources.add(wr.ScriptResource(
    name='luxon-js',
    resource='luxon.js',
    compressed='luxon.min.js'
))

chartjsadapterluxon_resources = wr.ResourceGroup(
    name='cone.charts-chartjs-adapter-luxon',
    directory=os.path.join(resources_dir, 'chartjs-adapter-luxon'),
    path='chartjs-adapter-luxon',
    group=resources
)
chartjsadapterluxon_resources.add(wr.ScriptResource(
    name='chartjs-adapter-luxon-js',
    depends=[
        'chart-js',
        'luxon-js'
    ],
    resource='chartjs-adapter-luxon.js',
    compressed='chartjs-adapter-luxon.min.js'
))

cone_charts_resources = wr.ResourceGroup(
    name='cone.cone_charts',
    directory=os.path.join(resources_dir, 'cone_charts'),
    path='cone_charts',
    group=resources
)
cone_charts_resources.add(wr.ScriptResource(
    name='cone_charts-js',
    resource='cone.charts.js',
    compressed='cone.charts.min.js'
))

def configure_resources(settings):
    def included(name):
        return settings.get(name, 'false') == 'true'

    set_resource_include(settings, 'chart-js', 'authenticated')
    set_resource_include(settings, 'cone_charts-js', 'authenticated')

    include =  False if included('cone.charts.luxon') else 'authenticated'
    set_resource_include(settings, 'luxon-js', include)
    set_resource_include(settings, 'chartjs-adapter-luxon-js', include)
