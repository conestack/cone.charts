import {ChartTile} from './chart.js';

export class PolarChartTile extends ChartTile {

    constructor(elem, settings) {
        super(elem, settings);
    }

    create_chart() {
        let options = this.options;
        let chart_data = [];
        this.chart = new Chart(this.canvas, {
            type: 'polarArea',
            data: this.data,
            options: this.options
        });
    }
}