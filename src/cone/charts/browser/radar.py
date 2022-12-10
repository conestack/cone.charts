from .chart import ChartTile


class RadarChartTile(ChartTile):
    """A radar chart.

    Refer to
    `documentation <https://www.chartjs.org/docs/4.0.1/charts/radar.html>`_
    for detailed information about valid options and data.
    """

    chart_type = 'radar'
    """Tell JavaScript side to render a radar chart."""

    @staticmethod
    def chart_data(model, request):
        """Radar chart data.

        Example:

        .. code-block:: python

            return {
                'labels': [
                    'Eating',
                    'Drinking',
                    'Sleeping',
                    'Designing',
                    'Coding',
                    'Cycling',
                    'Running'
                ],
                'datasets': [{
                    'label': 'Dataset 1',
                    'data': [65, 59, 90, 81, 56, 55, 40]
                }, {
                    'label': 'Dataset 2',
                    'data': [28, 48, 40, 19, 96, 27, 100]
                }]
            }
        """
        raise NotImplementedError(
            'Abstract ``RadarChartTile`` does not implement ``chart_data``'
        )
