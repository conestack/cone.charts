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
        raise NotImplementedError('Chart data not implemented')
