import $ from 'jquery';

import { ChartTile } from './chart.js';

export * from './chart.js';

$(function () {
    ts.ajax.register(ChartTile.initialize, true);
});
