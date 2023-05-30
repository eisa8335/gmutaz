odoo.define('sh_all_in_one_debranding.bot', function (require) {
    "use strict";

   
    var Message = require('mail.model.Message');
    var session = require('web.session');

    Message.include({
        getAvatarSource: function () {
            if (this._isOdoobotAuthor()) {
                return '/web/binary/company_logo?company_id=' + session.company_id;
            }
            return this._super.apply(this, arguments);
        }
    });
});
