/** @odoo-module **/

import { KanbanController } from "@web/views/kanban/kanban_controller";
import core from "web.core";
var _t = core._t;
import { patch } from "@web/core/utils/patch";

patch(KanbanController.prototype, 'sh_backmate_theme/static/src/js/kanban_controller.js', {
   
    _onClickRefreshView (ev) { 
        this.actionService.switchView('kanban');
    }
  
});
