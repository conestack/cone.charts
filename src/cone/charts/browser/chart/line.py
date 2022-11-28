from .chart import ChartTile


class LineChartTile(ChartTile):
    chart_factory = 'cone_charts.LineChartTile'
    # linechart options documentation:
    # https://www.chartjs.org/docs/latest/charts/line.html

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


"""
Example chart:
@chart_tile(
    name='my_fancy_linechart',
    interface=PersonCounter,
    permission='view')
class MyFancyLinechart(LineChartTile):
    chart_factory = 'touch_personcounter.LineChartTile'

    @staticmethod
    def chart_data(model, request):
        import random

        def random_data():
            data1 = []
            data2 = []
            for i in range(100):
                data1.append([str(i), random.randint(0, 100)])
            for i in range(50):
                data2.append([str(i), random.randint(0, 100)])
            return [data1, data2]
        data = random_data()

        # data layout = [[x1, y1], [x2, y2], ...] x = string, y = value
        # data need to be converted to format: {labels: [x1, x2, ...], datasets: [{data: [y1, y2, ...]}]}
        # we can have multiple datasets
        datasets = []
        for dataset in data:
            color = 'rgb({},{},{})'.format(
                *[random.randint(0, 255) for _ in range(3)])
            datasets.append({
                'data': [point[1] for point in dataset],
                'borderColor': color,
                'tension': 0.3,
                'label': 'Dataset {}'.format(len(datasets) + 1),
            })
        return {
            'labels': [point[0] for point in data[0]],
            'datasets': datasets,
        }
"""
