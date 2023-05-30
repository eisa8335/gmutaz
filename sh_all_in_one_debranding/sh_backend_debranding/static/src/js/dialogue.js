/** @odoo-module **/

import { Dialog } from "@web/core/dialog/dialog";


var debrand_title = ''; 
var rpc = require('web.rpc');


rpc.query({
    model: 'sh.debranding.config',
    method: 'search_read',
    limit: 1,
   args: [[],['name']],
} ,{async: false}).then(function(output) {
	if(output && output[0]){
        debrand_title = output[0]['name'];        
	}
});

import { patch } from 'web.utils';

const components = { Dialog };
import { useHotkey } from "@web/core/hotkeys/hotkey_hook";
import { useActiveElement } from "@web/core/ui/ui_service";
import { useForwardRefToParent } from "@web/core/utils/hooks";

import { useChildSubEnv, useState } from "@odoo/owl";
patch(components.Dialog.prototype, 'sh_all_in_one_debranding/sh_backend_debranding/static/src/js/dialog.js', {
	setup() {
        this.modalRef = useForwardRefToParent("modalRef");
        useActiveElement("modalRef");
        this.data = useState(this.env.dialogData);
        useHotkey("escape", () => {
            this.data.close();
        });
        this.id = `dialog_${this.data.id}`;
        useChildSubEnv({ inDialog: true, dialogId: this.id, closeDialog: this.data.close });
        this.props.title = debrand_title
        owl.onWillDestroy(() => {
            if (this.env.isSmall) {
                this.data.scrollToOrigin();
            }
        });
    },

    get isFullscreen() {
        return this.props.fullscreen || this.env.isSmall;
    }
	
	
});
