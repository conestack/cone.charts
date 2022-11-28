import $ from 'jquery';

import { ChartTile } from './chart.js';

export * from './chart.js';
export * from './line.js';
export * from './polar.js';
export * from './bar.js';
export * from './pie.js';
/* 
    Export all chart types and initialize all charts with treibstoff or bdajax
*/
$(function() {
    if (window.ts !== undefined) {
        ts.ajax.register(ChartTile.initialize, true);
    } else {
        bdajax.register(ChartTile.initialize, true);
    }
});