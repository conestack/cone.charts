from .chart import ChartTile


class LineChartTile(ChartTile):
    """Tile rendering a line chart.
    Reference: https://www.chartjs.org/docs/latest/charts/line.html
    """

    chart_type = 'line'
    """Setting chart type to 'line'. """

    @staticmethod
    def chart_data(model, request):
        """Return chart data as dict.
        See ChartTile.chart_data for details.
        Example:
            return {
                labels: labels,
                datasets: [
                    {
                        label: 'Dataset 1',
                        data: [10, 20, 30],
                        borderColor: rgb(255, 99, 132),
                        backgroundColor: rgba(255, 99, 132, 0.2),
                    },
                    {
                        label: 'Dataset 2',
                        data: [20, 10, 40],
                        borderColor: rgb(54, 162, 235),
                        backgroundColor: rgba(54, 162, 235, 0.2),
                    }
                ]
            }
        """
        raise NotImplementedError('Chart data not implemented')
