/** @odoo-module **/


import { ActionDialog } from "@web/webclient/actions/action_dialog";
import { ActionContainer } from '@web/webclient/actions/action_container';
const { Component, tags } = owl;
import {NavTab} from "./navtab/navtab"
import { patch } from 'web.utils';

import { onWillDestroy } from "@odoo/owl";
const {Markup} = require('web.utils');
const components = { ActionContainer };

var session = require('web.session');
// var ActionManager = require('web.ActionManager');
// var AbstractWebClient = require('web.AbstractWebClient');
// var dom = require('web.dom');
var rpc = require("web.rpc");
var display_notice = false;
var font_color = '#ffffff';
var background_color = '#212121';
var font_size = 12;
var font_family = 'Roboto';
var padding = 5;
var content = ''
var is_animation = false;
var direction = 'right';
var simple_text = false;
var is_popup_notification = false;
var close_notification = false;

var notification_template = '';



rpc.query({
    model: 'sh.announcement',
    method: 'search_read',
    args: [[['is_popup_notification', '=', false], ['user_ids.id', 'in', [session.user_context.uid]]], ['is_popup_notification', 'font_size', 'font_family', 'padding', 'name', 'description', 'is_animation', 'direction', 'user_ids', 'simple_text', 'background_color', 'font_color', 'description_text']],
}, { async: false }).then(function (output) {
    if (output) {
        var i;
        for (i = 0; i < output.length; i++) {
            console.log("output", output)
            if (output[i]['user_ids'].includes(session.user_context.uid)) {
                display_notice = true;
                background_color = output[i]['background_color']
                font_size = output[i]['font_size']
                font_family = output[i]['font_family']
                padding = output[i]['padding']
                font_color = output[i]['font_color']
                is_animation = output[i]['is_animation']
                direction = output[i]['direction']
                simple_text = output[i]['simple_text']
                is_popup_notification = output[i]['is_popup_notification']
                if (simple_text) {
                    content = output[i]['description_text'] || ''
                } else {
                    content = output[i]['description']
                }
            }

        }
        if (display_notice && !is_popup_notification) {
            if (simple_text) {
                var style = "position:relative;background:" + background_color + ";color:" + font_color + ";font-size:" + font_size + "px;font-family:" + font_family + ";padding:" + padding + "px;"
                if (is_animation) {
                    notification_template += "<div id='object'  style='position:relative;'><marquee direction=" + direction + " style=" + style + "><div id='object1'>" + content + "</div></marquee><div class=\"sh_animated_notification\" style='position: absolute;right: 5px;font-size: 15px;top: 0px;cursor: pointer;'><span class='fa fa-times sh_close_notification' /><div></div>"
                } else {
                    notification_template += "<div id='object1' style=" + style + ">" + content + "<div class=\"sh_simple_text_notification\" style='position: absolute;right: 5px;font-size: 15px;top: 0px;cursor: pointer;'><span class='fa fa-times sh_close_notification'/></div></div>"
                }
            } else {
                if (is_animation) {
                    notification_template += "<div id='object'  style='position:relative;'><marquee direction=" + direction + "><div id='object1'>" + content + "</div></marquee><div class=\"sh_animated_notification\" style='position: absolute;right: 5px;font-size: 15px;top: 0px;cursor: pointer;'><span class='fa fa-times sh_close_notification' /></div></div>"
                } else {
                    notification_template += "<div id='object1' style='position:relative;'>" + content + "<div class=\"sh_simple_text_notification\" style='position: absolute;right: 5px;font-size: 15px;top: 0px;cursor: pointer;'><span class='fa fa-times sh_close_notification' /></div></div>"
                }

            }

        }
        
        notification_template= Markup( notification_template );



    }
});



patch(components.ActionContainer.prototype, 'sh_backmate_theme/static/src/js/action_container.js', {
    setup() {
        this.info = {};
        this.notification_template = notification_template;
        this.info = {};
        this.onActionManagerUpdate = ({ detail: info }) => {
            this.info = info;
            this.render();
        };
        this.env.bus.addEventListener("ACTION_MANAGER:UPDATE", this.onActionManagerUpdate);
        onWillDestroy(() => {
            this.env.bus.removeEventListener("ACTION_MANAGER:UPDATE", this.onActionManagerUpdate);
        });
    }


});

ActionContainer.components = { ActionDialog, NavTab };
ActionContainer.template = "sh_backmate_theme.ActionContainer";

