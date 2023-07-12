/** @odoo-module **/

import { ListController } from "@web/views/list/list_controller";
import core from "web.core";
var _t = core._t;
import { patch } from "@web/core/utils/patch";

patch(ListController.prototype, 'sh_backmate_theme/static/src/js/list_controller.js', {
   
    _onClickRefreshView (ev) { 
        this.actionService.switchView('list');
    }
  
});

// odoo.define('sh_backmate_theme.ListController', function (require) {
//     "use strict";

//     var ListController = require('web.ListController');
//     var FormRenderer = require('web.FormRenderer');

//     FormRenderer.include({

        

//         _renderStatusbarButtons: function (buttons) {
//             var $statusbarButtons = $('<div>', {class: 'o_statusbar_buttons'});
//             buttons.forEach(button => $statusbarButtons.append(button));
//             var show_status_bar = false
//             _.each(buttons , function (button) {
//                     console.log(">>>>>>>>..",button.hasClass('o_invisible_modifier'))
//                 if(!button.hasClass('o_invisible_modifier')){
//                     show_status_bar = true
//                 }

//             });
            
//             if(!show_status_bar){
//                console.log(">>>>>>>>>>>.",$('.o_form_statusbar'))
//                console.log("999999",$statusbarButtons)
//                $statusbarButtons.remove()
//             }
//             return $statusbarButtons;
//         },
//     });


//     var ListRenderer = require('web.ListRenderer');

// 	ListRenderer.include({
// 		async _renderView() {
// 			// Fix issue of sticky three dots
// 			var self = this;
// 			return this._super.apply(this, arguments).then(function () {
// 				self.$el.find('thead').append(
// 								$('<i class="o_optional_columns_dropdown_toggle fa fa-ellipsis-v"/>')
// 							);
// 			});


// 		}
		    
// 	});

    
// });
