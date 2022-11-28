from .chart import ChartTile


class BarChartTile(ChartTile):
    """
    barchart options documentation:
    https://www.chartjs.org/docs/latest/charts/bar.html
    """
    chart_factory = 'cone_charts.BarChartTile'

    chart_options ={
        'options': {
            'scales': {
                'y': {
                    'beginAtZero': True
                }
            }
        }
    }

    @staticmethod
    def chart_data(model, request):
        """
        {
            'labels': [str(i) for i in range(len(model.data))],
            'datasets': [{
                'label': 'My First Dataset',
                'data': model.data,
                'fill': False,
                'borderColor': 'rgb(75, 192, 192)',
                'tension': 0.1
            }]
        }
        """
        raise NotImplementedError('')
