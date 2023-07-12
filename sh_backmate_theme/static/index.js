odoo.define("sh_backmate_theme.pwa", function (require) {
    var ajax = require("web.ajax");
    var rpc = require("web.rpc");
    var session = require('web.session');
    var enable_web_push_notification = false

    $(document).ready(function (require) {
        rpc.query({
            model: 'res.company',
            method: 'search_read',
            fields: ['enable_web_push_notification'],
            domain: [['id', '=', session.company_id]]
        }, { async: false }).then(function (data) {
            if (data) {
                _.each(data, function (company) {
                    if (company.enable_web_push_notification) {

                        enable_web_push_notification = true
                        if ("serviceWorker" in navigator) {
                            navigator.serviceWorker.register("/firebase-messaging-sw.js").then(function () {
                            });
                        }
    
                    }
                });
    
            }
        });


        
    });
});
