/** @odoo-module **/
import { WebClient } from "@web/webclient/webclient";
var rpc = require('web.rpc');
var debrand_title = "System";
var debrand_url = "System";
import { useOwnDebugContext } from "@web/core/debug/debug_context";
import { DebugMenu } from "@web/core/debug/debug_menu";
import { localization } from "@web/core/l10n/localization";
import { registry } from "@web/core/registry";
import { useBus, useService } from "@web/core/utils/hooks";

import { onMounted, useExternalListener, useState } from "@odoo/owl";

var debrand_title = ''; 
var debrand_url = '';


rpc.query({
    model: 'sh.debranding.config',
    method: 'search_read',
    limit: 1,
   args: [[],['name','url']],
} ,{async: false}).then(function(output) {
	if(output && output[0]){
		 debrand_title = output[0]['name']; 
		 debrand_url = output[0]['url']; 
	}
});

import { patch } from 'web.utils';

const components = { WebClient };

patch(components.WebClient.prototype, 'sh_all_in_one_debranding/sh_backend_debranding/static/src/js/system_name.js', {
	 setup() {
		this.menuService = useService("menu");
        this.actionService = useService("action");
        this.title = useService("title");
        this.router = useService("router");
        this.user = useService("user");
        useService("legacy_service_provider");
        useOwnDebugContext({ categories: ["default"] });
        if (this.env.debug) {
            registry.category("systray").add(
                "web.debug_mode_menu",
                {
                    Component: DebugMenu,
                },
                { sequence: 100 }
            );
        }
        this.localization = localization;
        this.state = useState({
            fullscreen: false,
        });		
        this.title.setParts({ zopenerp: debrand_title }); // zopenerp is easy to grep
        useBus(this.env.bus, "ROUTE_CHANGE", this.loadRouterState);
        useBus(this.env.bus, "ACTION_MANAGER:UI-UPDATED", ({ detail: mode }) => {
            if (mode !== "new") {
                this.state.fullscreen = mode === "fullscreen";
            }
        });
        onMounted(() => {
            this.loadRouterState();
            // the chat window and dialog services listen to 'web_client_ready' event in
            // order to initialize themselves:
            this.env.bus.trigger("WEB_CLIENT_READY");
        });
        useExternalListener(window, "click", this.onGlobalClick, { capture: true });
	 }
	
	
});