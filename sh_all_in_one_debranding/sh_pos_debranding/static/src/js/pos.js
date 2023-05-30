odoo.define('sh_pos_debranding.pos', function(require) {
    'use strict';
    

    const Chrome = require("point_of_sale.Chrome");
    const Registries = require("point_of_sale.Registries");
    var rpc = require('web.rpc');


    const PosResChrome = (Chrome) =>
        class extends Chrome {
            async start() {
                super.start() 
                var avatar = '';
                await rpc.query({
                    model: 'sh.debranding.config',
                    method: 'search_read',
                    limit: 1,
                    args: [[]],
                }).then(function(output) { 
                    if(output && output[0]){ 
                         avatar = output[0]['id']; 
                    }
                });
                this.shAvatarID = avatar
            }
            get getLOGO(){ 
                var ID = this.shAvatarID
                return `/web/image/sh.debranding.config/${ID}/avatar`;
            }
        }


    Registries.Component.extend(Chrome, PosResChrome);

    return Chrome
});