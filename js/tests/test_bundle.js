import $ from 'jquery';
import ts from 'treibstoff';

QUnit.module('cone_charts.bundle', (hooks) => {
    const ts_ajax_register_origin = ts.ajax.register;

    hooks.afterEach(() => {
        ts.ajax.register = ts_ajax_register_origin;
    });

    QUnit.test('bundle exports ChartTile and registers it on DOM ready', async (assert) => {
        const registered = [];
        ts.ajax.register = (func, instant) => {
            registered.push({ func, instant });
        };

        const bundle = await import('../src/bundle.js');
        // ready callbacks run in registration order, this one after the bundle's
        await new Promise((resolve) => $(resolve));

        assert.deepEqual(Object.keys(bundle), ['ChartTile'], 'exported names');
        assert.strictEqual(registered.length, 1, 'one registration');
        assert.strictEqual(
            registered[0].func,
            bundle.ChartTile.initialize,
            'initialize registered',
        );
        assert.true(registered[0].instant, 'registered for instant execution');
    });
});
