from .chart import ChartTile


class RadarChartTile(ChartTile):
    """ Tile rendering a radar chart.
    Reference: https://www.chartjs.org/docs/latest/charts/radar.html
    """

    chart_type = 'radar'
    """Setting chart type to 'line'. """

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.
        See ChartTile.chart_data for details.
        Example:
            return {
                labels: [
                    'Eating',
                    'Drinking',
                    'Sleeping',
                    'Designing',
                    'Coding',
                    'Cycling',
                    'Running'
                ],
                datasets: [{
                    label: 'My First Dataset',
                    data: [65, 59, 90, 81, 56, 55, 40]
                }, {
                    label: 'My Second Dataset',
                    data: [28, 48, 40, 19, 96, 27, 100]
                }]
            }
        """
        raise NotImplementedError('Chart data not implemented')
