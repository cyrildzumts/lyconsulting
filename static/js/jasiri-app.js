requirejs.config({
    baseUrl :'/static/js/lib',
    paths:{
        vendor: '../vendors'
    },
    waitSeconds: 0
});

requirejs(['ajax_api', 'commons'], function(ajax_api){
    console.log("jasiri app ready");
});