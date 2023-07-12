//===========================================
// Full Screen Mode
//===========================================

odoo.define('sh_backmate_theme.full_screen_systray', function (require) {
    "use strict";

    var core = require('web.core');
    var Dialog = require('web.Dialog');
    var Widget = require('web.Widget');
    var rpc = require('web.rpc');
    var SystrayMenu = require('web.SystrayMenu');
    var session = require('web.session');
    var _t = core._t;
    var QWeb = core.qweb;


    var FullScreenTemplate = Widget.extend({
        template: "FullScreenTemplate",
        events: {
            'click .expand_img': '_click_expand_button',
            'click .compress_img': '_click_compress_button',
        },
        init: function () {
            this._super.apply(this, arguments);
            var self = this;
        },

        _click_expand_button: function (ev) {
            ev.preventDefault();
            var self = this;
            $('.expand_img').css("display", "none");
            $('.compress_img').css("display", "block");
            var elem = document.querySelector('body');
            if (elem.requestFullscreen) {
                elem.requestFullscreen();
            } else if (elem.mozRequestFullScreen) { /* Firefox */
                elem.mozRequestFullScreen();
            } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari & Opera */
                elem.webkitRequestFullscreen();
            } else if (elem.msRequestFullscreen) { /* IE/Edge */
                elem.msRequestFullscreen();
            }
        },
        _click_compress_button: function (ev) {
            ev.preventDefault();
            var self = this;
            $('.compress_img').css("display", "none");
            $('.expand_img').css("display", "block");

            $('.expand_img').css("position", "relative");
            $('.expand_img').css("top", "0");
            var elem = document.querySelector('body');
            if (document.exitFullscreen) {
                document.exitFullscreen();
            } else if (document.mozCancelFullScreen) { /* Firefox */
                document.mozCancelFullScreen();
            } else if (document.webkitExitFullscreen) { /* Chrome, Safari and Opera */
                document.webkitExitFullscreen();
            } else if (document.msExitFullscreen) { /* IE/Edge */
                document.msExitFullscreen();
            }
        },

    });

    FullScreenTemplate.prototype.sequence = 2;
    // session.user_has_group('sh_backmate_theme.group_full_screen_mode').then(function (has_group) {
    //     if (has_group) {
    //         SystrayMenu.Items.push(FullScreenTemplate);
    //     }
    // });
    rpc.query({
        model: 'res.users',
        method: 'search_read',
        fields: ['sh_enable_full_screen_mode'],
        domain: [['id', '=', session.uid]]
      }, { async: false }).then(function (data) {
        if (data) {
          _.each(data, function (user) {
            if (user.sh_enable_full_screen_mode) {
              SystrayMenu.Items.push(FullScreenTemplate);
    
            }
          });
    
        }
      });


    return {
        FullScreenTemplate: FullScreenTemplate,
    };
});