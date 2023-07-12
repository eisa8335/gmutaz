/** @odoo-module **/

import { CalendarController } from "@web/views/calendar/calendar_controller";
import core from "web.core";
var _t = core._t;
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";


patch(CalendarController.prototype, 'sh_backmate_theme/static/src/js/calendar_controller.js', {
   
    setup(...args) {
        this._super(...args)
        this.actionService = useService('action');
    },
    _onClickRefreshView (ev) { 
        this.actionService.switchView('calendar');
    }
  
});
