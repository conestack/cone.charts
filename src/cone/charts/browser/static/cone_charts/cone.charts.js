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
            this.on_before_load = this.on_before_load.bind(this);
            this.on_data_loaded = this.on_data_loaded.bind(this);
            this.load();
        }
        load() {
            this.unload();
            this.trigger('on_before_load');
            ts.ajax.request({
                url: this.data_source,
                type: 'json',
                method: 'GET',
                cache: false,
                params: this.params,
                success: (data) => {
                    this.data = data;
                    this.trigger('on_data_loaded');
                }
            });
        }
        unload() {
            if (this.chart !== null) {
                this.chart.destroy();
                this.chart = null;
            }
        }
        destroy() {
            this.unload();
        }
        on_before_load() {
        }
        on_data_loaded() {
            this.create_chart();
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
        ts.ajax.register(ChartTile.initialize, true);
    });

    exports.ChartTile = ChartTile;

    Object.defineProperty(exports, '__esModule', { value: true });

    return exports;

})({}, jQuery);
