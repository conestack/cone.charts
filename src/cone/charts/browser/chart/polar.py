from .chart import ChartTile


class PolarChartTile(ChartTile):
    chart_factory = 'cone_charts.PolarChartTile'
    # polarchart options documentation:
    # https://www.chartjs.org/docs/latest/charts/polar.html

    @staticmethod
    def chart_data(model, request):
        if not model.data:
            raise ValueError('No data available')
        return {
            'labels': [str(i) for i in range(len(model.data))],
            'datasets': [{
                'label': 'My First Dataset',
                'data': model.data,
                'fill': False,
                'borderColor': 'rgb(75, 192, 192)',
                'tension': 0.1
            }]
        }
