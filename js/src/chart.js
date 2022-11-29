import $ from 'jquery';

export class ChartTile extends ts.Events {

    static initialize(context) {
        /* initializes a chart instance for each `div.cone-chart` element 
            in context
        */
        function test(factory_path) {
            console.log('test', factory_path);
            return ts.object_by_path(factory_path);
        }

        $('div.cone-chart', context).each(function() {
            let elem = $(this),
                settings = elem.data('chart-settings'),
                factory_path = settings.factory,
                factory = test(factory_path),
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

        // binding event handlers
        this.on_data_load = this.on_data_load.bind(this);

        // calling abstract methods for subclasses
        this.prepare_options();
        this.prepare_params();

        // calling chart loader function
        this.load();
    }

    load() {
        /* loads the corresponding chart data from the server and 
            calls on_data_load when done
         */
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
        /* destroys the chart 
        */
        if (this.chart !== null) {
            this.chart.destroy();
        }
    }

    destroy() {
        /* gets called when a ts.ajax instance is destroyed
        */
        this.unload();
    }

    on_data_load() {
        /*  called when data is loaded from server
            can be overridden to prepare data before creating chart
        */
        this.create_chart();
    }

    prepare_options() {
        // can be overridden to prepare chart options
        // set defaults on options if necessary
    }

    prepare_params() {
        /* abstract method
            can be overridden to prepare params
            set chart configuration parameters sent to server when requesting
        */
    }

    prepare_data() {
        /* abstract method
            can be overridden to prepare data before creating chart
        */
    }

    create_chart() {
        /* abstract method
            must be overridden to create the chart
        */
        throw new Error('create_chart must be overridden');
    }
}
