import $ from 'jquery';

export class ChartTile extends ts.Events {

    static initialize(context) {
        $('div.cone-chart', context).each(function() {
            let elem = $(this),
                settings = elem.data('chart-settings'),
                factory_path = settings.factory,
                factory = ts.object_by_path(factory_path),
                inst = new factory(elem, settings);
            ts.ajax.attach(inst, elem);
        });
    }

    constructor(elem, settings) {
        super();
        this.elem = elem;
        this.canvas = $('canvas', elem);
        this.id = elem.attr('id');

        this.options = settings.options;
        this.data_source = settings.data_source;
        this.params = settings.params;

        // raw chart data from server
        this.data = null;
        // the chartjs Chart instance
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
                this.prepare_data()
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
        // set defaults on options if necessary
    }

    prepare_params() {
        // set chart configuration parameters sent to server when requesting
        // chart data
    }

    prepare_data() {
        // prepare data for chart
    }

    create_chart() {
        // abstract create chart
    }
}
