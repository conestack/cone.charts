import { ChartTile } from './chart.js';

export class BarChartTile extends ChartTile {

    constructor(elem, settings) {
        super(elem, settings);
    }

    create_chart() {
        /* creates the chartjs chart instance for a bar chart
        */
        this.chart = new Chart(this.canvas, {
            type: 'bar',
            data: this.data,
            options: this.options
        });
    }
}
