import $ from 'jquery';

export class ChartTile extends ts.Events {

    /**
     * Initializes a chart instance for each div DOM element with
     * ``cone-chart`` CSS class set
     *
     * @param {$} jQuery wrapped context
     */
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

    /**
     * Create a Chart object.
     *
     * @param {$}  jQuery wrapped chart container element.
     * @param {Object} settings chart setting object for type, options, 
     * data_source and params
     */
    constructor(elem, settings) {
        super();
        this.elem = elem;
        this.canvas = $('canvas', elem);
        this.id = elem.attr('id');

        this.type = settings.type;
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

    /**
     * Loads the chart data from the server.
     * calls ``on_data_load`` when data is loaded
    */
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

    /**
     * Unloads the chart.
     */
    unload() {
        if (this.chart !== null) {
            this.chart.destroy();
        }
    }

    /**
     * Event handler gets called when ts.ajax instance is destroyed.
     */
    destroy() {
        this.unload();
    }


    /**
     * Event handler gets called when chart data is loaded.
     * can be overridden to prepare data before creating chart
     * calls ``create_chart`` to create the chart
     */
    on_data_load() {
        this.create_chart();
    }

    /**
     * abstract method
     * can be overridden to prepare options
     */
    prepare_options() {
    }

    /**
     * abstract method
     * can be overridden to prepare params
     */
    prepare_params() {
    }

    /**
     * abstract method
     * can be overridden to prepare data
     */
    prepare_data() {
    }

    /**
     * Creates the actual chart.
     */
    create_chart() {
        this.chart = new Chart(this.canvas, {
            type: this.type,
            data: this.data,
            options: this.options
        });
    }
}
