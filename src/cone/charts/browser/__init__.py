from cone.app.browser.resources import resources
from cone.app.browser.resources import set_resource_include
import webresource as wr
import os


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
    resource='chart.js',
    compressed='chart.min.js'
))


def configure_resources(settings):
    set_resource_include(settings, 'chart-js', 'authenticated')
