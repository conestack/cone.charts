import {ChartTile} from './chart.js';

export class LineChartTile extends ChartTile {

    constructor(elem, settings) {
        super(elem, settings);
    }

    create_chart() {
        this.chart = new Chart(this.canvas, {
            type: 'line',
            data: this.data,
            options: this.options
        });
    }
}
