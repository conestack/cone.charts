import {ChartTile} from './chart.js';

export class PolarChartTile extends ChartTile {

    constructor(elem, settings) {
        super(elem, settings);
    }

    create_chart() {
        /* creates the chartjs chart instance for a polar chart
        */
        this.chart = new Chart(this.canvas, {
            type: 'polarArea',
            data: this.data,
            options: this.options
        });
    }
}
