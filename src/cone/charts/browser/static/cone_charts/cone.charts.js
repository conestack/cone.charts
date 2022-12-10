var cone_charts = (function (exports, $) {
    'use strict';

    class ChartTile extends ts.Events {
        static initialize(context) {
            $('div.cone-chart', context).each(function () {
                let elem = $(this),
                    settings = elem.data('chart-settings'),
                    factory_path = settings.factory,
                    factory = ts.object_by_path(factory_path);
                let inst = new factory(elem, settings);
                ts.ajax.attach(inst, elem);
            });
        }
        constructor(elem, settings) {
            super();
            this.elem = elem;
            this.canvas = $('canvas', elem);
            this.id = elem.attr('id');
            this.type = settings.type;
            this.options = settings.options;
            this.data_source = settings.data_source;
            this.params = settings.params;
            this.data = null;
            this.chart = null;
            this.on_data_load = this.on_data_load.bind(this);
            this.prepare_options();
            this.prepare_params();
            this.load();
        }
        load() {
            this.unload();
            ts.ajax.request({
                url: this.data_source,
                type: 'json',
                method: 'GET',
                cache: false,
                params: this.params,
                success: (data) => {
                    this.data = data;
                    this.prepare_data();
                    this.trigger('on_data_load');
                }
            });
        }
        unload() {
            if (this.chart !== null) {
                this.chart.destroy();
            }
        }
        destroy() {
            this.unload();
        }
        on_data_load() {
            this.create_chart();
        }
        prepare_options() {
        }
        prepare_params() {
        }
        prepare_data() {
        }
        create_chart() {
            this.chart = new Chart(this.canvas, {
                type: this.type,
                data: this.data,
                options: this.options
            });
        }
    }

    $(function () {
        if (window.ts !== undefined) {
            ts.ajax.register(ChartTile.initialize, true);
        } else {
            bdajax.register(ChartTile.initialize, true);
        }
    });

    exports.ChartTile = ChartTile;

    Object.defineProperty(exports, '__esModule', { value: true });

    return exports;

})({}, jQuery);
