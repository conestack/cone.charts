from cone.app import main_hook
from cone.charts.browser import configure_resources
import logging


logger = logging.getLogger('cone.charts')


@main_hook
def initialize_charts(config, global_config, settings):
    # application startup initialization

    # static resources
    configure_resources(config, settings)

    # scan browser package
    config.scan('cone.charts.browser')
