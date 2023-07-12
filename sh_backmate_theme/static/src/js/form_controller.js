/** @odoo-module **/

import { FormController } from "@web/views/form/form_controller";
import { FormStatusIndicator } from "@web/views/form/form_status_indicator/form_status_indicator"
import core from "web.core";
var _t = core._t;
import { patch } from "@web/core/utils/patch";
var sh_disable_auto_edit_model = false
var rpc = require('web.rpc');
var session = require('web.session');

rpc.query({
    model: 'res.users',
    method: 'search_read',
    fields: ['sh_disable_auto_edit_model'],
    domain: [['id', '=', session.uid]]
}, { async: false }).then(function (data) {
    if (data) {
        _.each(data, function (user) {
            if (user.sh_disable_auto_edit_model) {
                sh_disable_auto_edit_model = user.sh_disable_auto_edit_model
            }
        });

    }
});



patch(FormController.prototype, 'sh_backmate_theme/static/src/js/form_controller.js', {

    setup(...args) {
        this._super(...args)
        if (this.footerArchInfo) {
            // If dialogue box then need to give edit permission
            this.props.preventEdit = false
        } else if (sh_disable_auto_edit_model) {
            this.hideEdit = false
            this.model.initialMode = 'readonly'
        }
    },
    disableEditButton() {
        if (sh_disable_auto_edit_model) {
            return true
        } else {
            return false
        }
    },
    _onClickEditView(ev) {
        this.model.root.switchMode("edit");
        this.shDisplayButtons()
        this.hideEdit = true
    },
    async saveButtonClicked(params = {}) {
        this._super();
        if (sh_disable_auto_edit_model) {
            this.hideEdit = false
            this.model.root.switchMode("readonly");
        }
        
    },
    async discard() {
        this._super();
        if (sh_disable_auto_edit_model) {
            this.hideEdit = false
            this.model.root.switchMode("readonly");
        }
        
    },

    shDisplayButtons() {
        if (this.hideEdit || this.model.root.isDirty) {
            return "btn btn-outline-primary sh_form_button_edit dirty";
        }
        else {
            return "btn btn-outline-primary sh_form_button_edit saved";
        }
    },

});

// patch(FormStatusIndicator.prototype, 'sh_backmate_theme/static/src/js/form_controller.js', {

//     get displayButtons() {
//         if(sh_disable_auto_edit_model){
//             return false
//         }else{
//             return this.indicatorMode !== "saved";
//         }
        
//     }


// });
