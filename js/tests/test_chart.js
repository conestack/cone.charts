import $ from 'jquery';
import ts from 'treibstoff';
import {ChartTile} from '../src/chart.js';

QUnit.module('cone_charts.ChartTile', hooks => {

    let container,
        ts_ajax_request_origin,
        ts_ajax_attach_origin,
        ts_object_by_path_origin,
        Chart_origin;

    hooks.beforeEach(() => {
        container = $('<div />').appendTo('body');

        // Store originals
        ts_ajax_request_origin = ts.ajax.request;
        ts_ajax_attach_origin = ts.ajax.attach;
        ts_object_by_path_origin = ts.object_by_path;
        Chart_origin = window.Chart;
    });

    hooks.afterEach(() => {
        container.remove();

        // Restore originals
        ts.ajax.request = ts_ajax_request_origin;
        ts.ajax.attach = ts_ajax_attach_origin;
        ts.object_by_path = ts_object_by_path_origin;
        window.Chart = Chart_origin;
    });

    QUnit.test('ChartTile.initialize finds and initializes charts', assert => {
        // Create mock factory that tracks instantiation
        let created_instances = [];

        // Mock ajax.request to prevent actual loading
        ts.ajax.request = function(opts) {};

        class MockChart extends ChartTile {
            constructor(elem, settings) {
                super(elem, settings);
                created_instances.push(this);
            }
        }

        ts.object_by_path = function(path) {
            assert.step('object_by_path');
            assert.strictEqual(path, 'MockChart');
            return MockChart;
        };

        ts.ajax.attach = function(inst, elem) {
            assert.step('attach');
        };

        // Create chart elements
        let settings = {
            factory: 'MockChart',
            type: 'bar',
            options: {},
            data_source: '/data',
            params: {},
        };

        $('<div class="cone-chart" />')
            .data('chart-settings', settings)
            .append('<canvas />')
            .appendTo(container);

        ChartTile.initialize(container);

        assert.strictEqual(created_instances.length, 1);
        assert.verifySteps(['object_by_path', 'attach']);
    });

    QUnit.test('ChartTile constructor initializes properties', assert => {
        let request_opts;
        ts.ajax.request = function(opts) {
            request_opts = opts;
        };

        let elem = $('<div id="test-chart" />')
            .append('<canvas />')
            .appendTo(container);

        let settings = {
            type: 'line',
            options: {responsive: true},
            data_source: '/api/chart-data',
            params: {year: 2024},
        };

        let chart = new ChartTile(elem, settings);

        assert.strictEqual(chart.elem, elem);
        assert.strictEqual(chart.id, 'test-chart');
        assert.strictEqual(chart.type, 'line');
        assert.deepEqual(chart.options, {responsive: true});
        assert.strictEqual(chart.data_source, '/api/chart-data');
        assert.deepEqual(chart.params, {year: 2024});
        assert.strictEqual(chart.data, null);
        assert.strictEqual(chart.chart, null);
    });

    QUnit.test('ChartTile.load sends AJAX request', assert => {
        let request_opts;
        ts.ajax.request = function(opts) {
            request_opts = opts;
        };

        let elem = $('<div />')
            .append('<canvas />')
            .appendTo(container);

        let settings = {
            type: 'bar',
            options: {},
            data_source: '/api/data',
            params: {filter: 'test'},
        };

        new ChartTile(elem, settings);

        assert.strictEqual(request_opts.url, '/api/data');
        assert.strictEqual(request_opts.type, 'json');
        assert.strictEqual(request_opts.method, 'GET');
        assert.strictEqual(request_opts.cache, false);
        assert.deepEqual(request_opts.params, {filter: 'test'});
    });

    QUnit.test('ChartTile.load triggers on_before_load event', assert => {
        ts.ajax.request = function(opts) {};

        let elem = $('<div />')
            .append('<canvas />')
            .appendTo(container);

        let settings = {
            type: 'bar',
            options: {},
            data_source: '/api/data',
            params: {},
        };

        let chart = new ChartTile(elem, settings);

        chart.on('on_before_load', () => {
            assert.step('on_before_load');
        });

        chart.load();

        assert.verifySteps(['on_before_load']);
    });

    QUnit.test('ChartTile.load triggers on_data_loaded on success', assert => {
        let request_callback;
        ts.ajax.request = function(opts) {
            request_callback = opts.success;
        };

        let elem = $('<div />')
            .append('<canvas />')
            .appendTo(container);

        let settings = {
            type: 'pie',
            options: {},
            data_source: '/api/data',
            params: {},
        };

        let chart = new ChartTile(elem, settings);
        chart.on('on_data_loaded', () => {
            assert.step('on_data_loaded');
        });

        // Mock Chart constructor
        window.Chart = function(canvas, config) {
            assert.step('chart_created');
        };

        let test_data = {labels: ['A', 'B'], datasets: []};
        request_callback(test_data);

        assert.deepEqual(chart.data, test_data);
        assert.verifySteps(['chart_created', 'on_data_loaded']);
    });

    QUnit.test('ChartTile.create_chart creates Chart instance', assert => {
        ts.ajax.request = function(opts) {
            opts.success({labels: [], datasets: []});
        };

        let created_config;
        window.Chart = function(canvas, config) {
            created_config = config;
            return {destroy: function() {}};
        };

        let elem = $('<div />')
            .append('<canvas />')
            .appendTo(container);

        let settings = {
            type: 'doughnut',
            options: {cutout: '50%'},
            data_source: '/api/data',
            params: {},
        };

        let chart = new ChartTile(elem, settings);

        assert.strictEqual(created_config.type, 'doughnut');
        assert.deepEqual(created_config.options, {cutout: '50%'});
        assert.deepEqual(created_config.data, {labels: [], datasets: []});
    });

    QUnit.test('ChartTile.unload destroys existing chart', assert => {
        ts.ajax.request = function(opts) {};

        let elem = $('<div />')
            .append('<canvas />')
            .appendTo(container);

        let settings = {
            type: 'bar',
            options: {},
            data_source: '/api/data',
            params: {},
        };

        let chart = new ChartTile(elem, settings);

        // Mock an existing chart
        let destroyed = false;
        chart.chart = {
            destroy: function() {
                destroyed = true;
            },
        };

        chart.unload();

        assert.true(destroyed);
        assert.strictEqual(chart.chart, null);
    });

    QUnit.test('ChartTile.unload does nothing when no chart exists', assert => {
        ts.ajax.request = function(opts) {};

        let elem = $('<div />')
            .append('<canvas />')
            .appendTo(container);

        let settings = {
            type: 'bar',
            options: {},
            data_source: '/api/data',
            params: {},
        };

        let chart = new ChartTile(elem, settings);
        chart.chart = null;

        // Should not throw
        chart.unload();

        assert.strictEqual(chart.chart, null);
    });

    QUnit.test('ChartTile.destroy calls unload', assert => {
        ts.ajax.request = function(opts) {};

        let elem = $('<div />')
            .append('<canvas />')
            .appendTo(container);

        let settings = {
            type: 'bar',
            options: {},
            data_source: '/api/data',
            params: {},
        };

        let chart = new ChartTile(elem, settings);

        let destroyed = false;
        chart.chart = {
            destroy: function() {
                destroyed = true;
            },
        };

        chart.destroy();

        assert.true(destroyed);
        assert.strictEqual(chart.chart, null);
    });

    QUnit.test('ChartTile.load unloads existing chart before loading', assert => {
        let request_count = 0;
        ts.ajax.request = function(opts) {
            request_count++;
        };

        let elem = $('<div />')
            .append('<canvas />')
            .appendTo(container);

        let settings = {
            type: 'bar',
            options: {},
            data_source: '/api/data',
            params: {},
        };

        let chart = new ChartTile(elem, settings);

        let destroy_count = 0;
        chart.chart = {
            destroy: function() {
                destroy_count++;
            },
        };

        chart.load();

        assert.strictEqual(destroy_count, 1);
        assert.strictEqual(request_count, 2); // Initial + reload
    });
});
