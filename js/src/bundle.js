import $ from 'jquery';

import { ChartTile } from './chart.js';

export * from './chart.js';

$(function () {
    if (window.ts !== undefined) {
        ts.ajax.register(ChartTile.initialize, true);
    } else {
        bdajax.register(ChartTile.initialize, true);
    }
});
