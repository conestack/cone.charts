/** @module cone_charts */
import $ from 'jquery';

export class ChartTile extends ts.Events {

    /**
     * Initializes a chart instance for each div DOM element with
     * ``cone-chart`` CSS class set.
     *
     * @param {$} context - jQuery wrapped DOM context.
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
     * @param {$} elem - jQuery wrapped chart container DOM element.
     * @param {Object} settings - Object containing chart settings.
     * @param {String} settings.type - Type of the chart.
     * @param {Object} settings.options - Options of the chart.
     * @param {String} settings.data_source - URL to fetch chart data from.
     * @param {Object} settings.params - Request params which gets sent when
     * fetching chart data.
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
        this.on_before_load = this.on_before_load.bind(this);
        this.on_data_loaded = this.on_data_loaded.bind(this);

        // calling chart loader function
        this.load();
    }

    /**
     * Loads the chart data from the server.
     *
     * ``on_before_load`` event is fired before request gets sent.
     * ``on_data_loaded`` event is fired when data is loaded.
     */
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

    /**
     * Unloads the chart.
     */
    unload() {
        if (this.chart !== null) {
            this.chart.destroy();
            this.chart = null;
        }
    }

    /**
     * Destroy chart instance.
     *
     * This function gets called if chart instance was attached by
     * ``ts.ajax.attach`` as soon as treibstoff removes part of DOM
     * containing the chart DOM element related to this instance.
     */
    destroy() {
        this.unload();
    }

    /**
     * Default event handler for ``on_before_load`` event.
     *
     * Does nothing.
     */
    on_before_load() {
    }

    /**
     * Default event handler for ``on_data_loaded`` event.
     *
     * Calls ``create_chart``
     */
    on_data_loaded() {
        this.create_chart();
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
