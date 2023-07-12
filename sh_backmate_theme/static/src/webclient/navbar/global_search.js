/** @odoo-module **/

    import Widget from 'web.Widget';
    var core = require('web.core');
    var QWeb = core.qweb;
    const session = require("web.session");
    var rpc = require("web.rpc");
   
    var show_company = false;




    session.user_has_group('base.group_multi_company').then(function (has_group) {
        show_company = has_group
    });

    var AppGlobalSearch = Widget.extend({
        name:"GlobalSearch",
        template: "GlobalSearch",
        events: {
            "keydown .sh_search_input input.usermenu_search_input": "_onSearchResultsNavigate",
            "click #topbar_search_icon": "_onclick_search_top_bar"
        },
        init: function () {
            this._search_def = $.Deferred();
            this._super.apply(this, arguments);
            this.show_company = show_company
        },
        _onclick_search_top_bar: function (event) {
            if ($(".usermenu_search_input").css("display") == "block") {
                $(".usermenu_search_input").css("display", "none");
            } else {
                $(".usermenu_search_input").css("display", "block");
            }

        },
        _linkInfo: function (key) {
            var original = this._searchableMenus[key];
            return original;
        },
        _getFieldInfo: function (key) {
            key = key.split('|')[1]
            return key;
        },
        _getcompanyInfo: function (key) {
            key = key.split('|')[0]
            return key;
        },
        _checkIsMenu: function (key) {
            key = key.split('|')[0]
            if (key == 'menu') {
                return true;
            } else {
                return false;
            }

        },


        _searchData: function () {
            console.log("this.$search_input",this.$el.find('.usermenu_search_input'))
            
            var query =this.$el.find('.usermenu_search_input').val();
            if (query === "") {
                this.$(".sh_search_container").removeClass("has-results");
                $(".sh_backmate_theme_appmenu_div").css("opacity", "1");
                this.$(".sh_search_results").empty();
                return;
            }
            var self = this;
            console.log("query",query)
            rpc.query({
                model: 'global.search',
                method: 'get_search_result',
                args: [[query]]
            }).then(function (data) {
                if (data) {
                    console.log("data",data)
                    self._searchableMenus = data
                    console.log("self._searchableMenus",self._searchableMenus)
                    // var results = fuzzy.filter(query, _.keys(self._searchableMenus), {
                    // });

                    var results = _.keys(self._searchableMenus)
                    self.$(".sh_search_container").toggleClass("has-results", Boolean(results.length));
                    if (results.length > 0) {
                        $(".sh_search_results").css("display", "block");
                        self.$(".sh_search_results").html(QWeb.render("sh_backmate_theme.MenuSearchResults", {
                            results: results,
                            widget: self,
                        }));

                    } else {
                        $(".sh_backmate_theme_appmenu_div").css("opacity", "1");
                        $(".sh_search_results").css("display", "none");
                    }


                }
            });

        },
        _onSearchResultsNavigate: function (event) {
            $("body").addClass("sh_detect_first_keydown")
            $(".sh_search_container").css("display", "block");
            this._search_def.reject();
            this._search_def = $.Deferred();
            setTimeout(this._search_def.resolve.bind(this._search_def), 50);
            this._search_def.done(this._searchData.bind(this));
            return;
        },
        start: function () {
            var self = this;

            this._rpc({
                model: 'sh.back.theme.config.settings',
                method: 'search_read',
                domain: [['id', '=', 1]],
                fields: ['theme_style']
            }).then(function (data) {
                if (data) {

                    // self.$search_input = self.$(".sh_search_input input.usermenu_search_input");
                    self.$search_input = self.$el.find('.usermenu_search_input')
                }
            });
            return this._super();

        },


    });






    export default AppGlobalSearch