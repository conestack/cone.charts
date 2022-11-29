import { ChartTile } from './chart.js';

export class PieChartTile extends ChartTile {

    constructor(elem, settings) {
        super(elem, settings);
    }

    create_chart() {
        /* creates the chartjs chart instance for a pie chart
        */
        this.chart = new Chart(this.canvas, {
            type: 'pie',
            data: this.data,
            options: this.options
        });
    }
}