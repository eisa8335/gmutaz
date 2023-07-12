/** @odoo-module **/


import { BlockUI } from "@web/core/ui/block_ui";


import { patch } from 'web.utils';


const components = { BlockUI };


import { xml } from "@odoo/owl";

var rpc = require("web.rpc");

var progress_style = 'default';


rpc.query({
    model: 'sh.back.theme.config.settings',
    method: 'search_read',
    domain: [['id', '=', 1]],
    fields: ['progress_style']
}).then(function (data) {
    if (data) {
        if (data[0]['progress_style'] == 'style_1') {
            progress_style = 'style_1';
        } else {
            progress_style = 'default';
        }
    }
});

patch(components.BlockUI.prototype, 'sh_backmate_theme/static/src/js/progressbar.js', {
    setup(...args) {

        this._super(...args)
    },
    block() {
        if (progress_style == 'style_1') {
            NProgress.configure({ showSpinner: false });
            NProgress.start();
        }
        this.state.blockUI = true;
        this.replaceMessage(0);

    },
    unblock() {
        NProgress.done();
        this.state.blockUI = false;
        clearTimeout(this.msgTimer);
        this.state.line1 = "";
        this.state.line2 = "";
    }


});

BlockUI.template = xml`
    <div t-att-class="state.blockUI ? 'o_blockUI fixed-top d-flex justify-content-center align-items-center flex-column vh-100 bg-black-50' : ''">
      <t t-if="state.blockUI">
        <div class="o_spinner mb-4">
            <img src="/web/static/img/spin.svg" alt="Loading..."/>
        </div>
        <div class="o_message text-center px-4">
            <t t-esc="state.line1"/> <br/>
            <t t-esc="state.line2"/>
        </div>
      </t>
    </div>`;
