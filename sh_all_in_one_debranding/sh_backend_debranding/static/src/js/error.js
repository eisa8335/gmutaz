/** @odoo-module **/

import { ErrorDialog, RPCErrorDialog, odooExceptionTitleMap ,ClientErrorDialog, NetworkErrorDialog, WarningDialog} from "@web/core/errors/error_dialogs";

const { Component, hooks } = owl;
import { patch } from 'web.utils';

var debrand_title = ''; 
var rpc = require('web.rpc');

rpc.query({
    model: 'sh.debranding.config',
    method: 'search_read',
    limit: 1,
   args: [[],['name','url']],
} ,{async: false}).then(function(output) {
	if(output && output[0]){
		 debrand_title = output[0]['name']; 
		 ErrorDialog.title = debrand_title;
		 ClientErrorDialog.title = debrand_title+' Client Error'
		 NetworkErrorDialog.title = debrand_title+' Network Error' 


	}
});


const components = { WarningDialog, RPCErrorDialog };

patch(components.WarningDialog.prototype, 'sh_all_in_one_debranding/sh_backend_debranding/static/src/js/error.js', {
	setup() {
        this._super();
        this.title = this.env._t("Warning");
        this.inferTitle();
        const { data, message } = this.props;
        if (data && data.arguments && data.arguments.length > 0) {
            this.message = data.arguments[0];
        } else {
            this.message = message;
        }
    }
	
	
});
	




patch(components.RPCErrorDialog.prototype, 'sh_all_in_one_debranding/sh_backend_debranding/static/src/js/error.js', {
	setup() {
		this._super(),
        this.inferTitle();
//        this.traceback = this.props.traceback;
        this.traceback = this.props.traceback.replace(/Odoo/gi, debrand_title); 
        
        if (this.props.data && this.props.data.debug) {
//            this.traceback = `${this.props.data.debug}`;
            this.traceback = this.props.data.debug.replace(/Odoo/gi, debrand_title); 
        }
//        console.log(">>>>>>>>>>>>>.",this.props.data.debug)
    },
	inferTitle() {
        // If the server provides an exception name that we have in a registry.
        if (this.props.exceptionName && odooExceptionTitleMap.has(this.props.exceptionName)) {
            this.title = odooExceptionTitleMap.get(this.props.exceptionName).toString();
            return;
        }
        // Fall back to a name based on the error type.
        if (!this.props.type) return;
        switch (this.props.type) {
            case "server":
                this.title = debrand_title+' Server Error'
                //this.env._t("Server Error");
                break;
            case "script":
                this.title =  debrand_title+' Client Error'
                //this.title = this.env._t("Client Error");
                break;
            case "network":
                this.title = debrand_title+' Network Error'
//                this.title = this.env._t("Network Error");
                break;
        }
    }
	
	
});
	



