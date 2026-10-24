import $ from 'jquery';
import ts from 'treibstoff';

import { ChartTile } from './chart.js';

export * from './chart.js';

$(() => {
    ts.ajax.register(ChartTile.initialize, true);
});
