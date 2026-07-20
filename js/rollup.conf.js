import cleanup from 'rollup-plugin-cleanup';
import terser from '@rollup/plugin-terser';

const out_dir = 'src/cone/charts/browser/static/cone_charts';

export default args => {
    let conf = {
        input: 'js/src/bundle.js',
        plugins: [
            cleanup()
        ],
        output: [{
            name: 'cone_charts',
            file: `${out_dir}/cone.charts.js`,
            format: 'iife',
            globals: {
                jquery: 'jQuery',
                treibstoff: 'treibstoff'
            },
            interop: 'default',
            sourcemap: false
        }],
        external: [
            'jquery',
            'treibstoff'
        ]
    };
    if (args.configDebug !== true) {
        conf.output.push({
            name: 'cone_charts',
            file: `${out_dir}/cone.charts.min.js`,
            format: 'iife',
            plugins: [
                terser()
            ],
            globals: {
                jquery: 'jQuery',
                treibstoff: 'treibstoff'
            },
            interop: 'default',
            sourcemap: false
        });
    }
    return conf;
};
