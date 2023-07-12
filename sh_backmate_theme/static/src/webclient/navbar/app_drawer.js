/** @odoo-module **/


	import Widget from 'web.Widget';
	var core = require('web.core');
	var QWeb = core.qweb;
	const session = require("web.session");
	var rpc = require("web.rpc");
	// var app_list = []
	import  AppGlobalSearch  from './global_search'
	var app_icon_style = 'style_3';
	rpc.query({
		model: 'sh.back.theme.config.settings',
		method: 'search_read',
		domain: [['id', '=', 1]],
		fields: ['app_icon_style']
	}).then(function (data) {
		// console.log("KKKKKKKKKKdata",data)
		if (data) {
		
			if (data[0]['app_icon_style']) {
				app_icon_style = data[0]['app_icon_style'];
			}
		}
	});





// app drawer animation 
	
var appDrawer = Widget.extend({
	name: 'appDrawer',
	template: 'appDrawer',
	events: {
		'click .sh_app' : '_click_sh_app',
		'click .sh_fav_icon':'_addToPinned',
		'click .sh_remove_icon':'_removeToPinned',
		'click .sh_new_app_icon':'_ClickPinnedMenu',
		'click .sh_pin_remove_icon':'_clickRemovePinned',
		'click .app_drawer_layout':'_clicKAppDrawer',

	},

	
	init: function (parent, record, nodeInfo) {
        this._super.apply(this, arguments);
		this.menuService = parent
		this.user_id = session.uid
		this.username = session.name
		this.app_list = []
    },
	
	willStart: function () {
		return this._super.apply(this, arguments).then(
			() => Promise.all([
				this._fetchData(),
			])
		);
	},
	async _fetchData() {
		var app_list = []
		const res = await rpc.query({
			model: 'sh.pinned.app',
			method: 'search_read',
			fields: ['app_id'],
			domain: [['user_id', '=', session.uid]]
			}).then(async function (data) {
			if (data) {

				for (let i = 0; i < data.length; i++) {
					await rpc.query({
						model: 'ir.ui.menu',
						method: 'search_read',
						domain: [['id', '=', data[i]['app_id'][0]]],
					}).then(function (app_data) {
						console.log("App Data =========",app_data)
						if(app_data){
							app_list.push(app_data[0])
						}
						
					});
				  }
			
			}
		});
		this.app_list = app_list;	       
		
	},
	_clicKAppDrawer: function (ev) {
		$(".sh_search_results").css("display", "none");
		$(".usermenu_search_input").val('');
	},

	start: function () { 
		
		var self = this;
		
		self._getMyApps()
		

		var pinned_app_drawer_menu_html = '<span class="dropdown-item o_app sh_add_pin_icon"><img class="sh_new_app_icon rounded" src="sh_backmate_theme/static/src/img/new1.png"/></span>'
		_.each(self.getPinnedApps() , function (app) {
			const parts = [`menu_id=${app.id}`];
			if (app.actionID) {
				parts.push(`action=${app.actionID}`);
			}
			var href= "#" + parts.join("&")

			pinned_app_drawer_menu_html += QWeb.render("pinned_app_drawer_menu", {
				app:app,
				app_icon:self.menuService.getMenuAsTree(app.id).xmlid.replace('.','_'),
				href: href,
				widget: self,
			})
			
		
		});
		$("#pinned_app_drawer_menu").html(pinned_app_drawer_menu_html);
		const globalsearh = new AppGlobalSearch()
		globalsearh.appendTo($('.sh_app_drawer_search')).then(function () {
			// $('.app_drawer_layout').addClass('sh_theme_model');
		});
		
		return this._super();
	},
	_getMyApps: function(){
		var app_drawer_menu_html = ''
		var self = this;
		_.each(this.menuService.getApps() , function (app) {
			const parts = [`menu_id=${app.id}`];
			if (app.actionID) {
				parts.push(`action=${app.actionID}`);
			}
			var href= "#" + parts.join("&")

			var app_pinned = false
			for (let i = 0; i < self.app_list.length; i++) {
				if(app.id == self.app_list[i]['id']){
					app_pinned = true
				}
			}
			if(app_pinned){
				app_drawer_menu_html += QWeb.render("appDrawerMenu", {
					app:app,
					app_icon:self.menuService.getMenuAsTree(app.id).xmlid.replace('.','_'),
					pinned:true,
					href: href,
					widget: self,
				})

			}else{
				app_drawer_menu_html += QWeb.render("appDrawerMenu", {
					app:app,
					app_icon:self.menuService.getMenuAsTree(app.id).xmlid.replace('.','_'),
					pinned:false,
					href: href,
					widget: self,
				})
			}
			
			
		$("#app_drawer_menu").html(app_drawer_menu_html);
		});
	},
	
	getPinnedApps:  function (ev) {		
		return this.app_list;
	},
	// getAppClassName(app){
	// 	var app_name = app.xmlid
    //     return app_name.replaceAll('.', '_')
    // },
    getIconStyle() {
        return app_icon_style;
    },
	_clickRemovePinned: function (ev) {
		ev.preventDefault();
		// ev.stopPropagation();
	},
	_close_app_drawer: function (ev) {
		ev.preventDefault();
		$('.app_drawer_layout').removeClass('sh_theme_model');
		$('.o_web_client').removeClass('sh_overlay_app_drawer');
	},


	animateClone: function ($cart, $elem, offsetTop, offsetLeft) {
		return new Promise(function (resolve, reject) {
			var $imgtodrag = $elem.find('img').eq(0);
			if ($imgtodrag.length) {
				var $imgclone = $imgtodrag.clone()
					.offset({
						top: $imgtodrag.offset().top,
						left: $imgtodrag.offset().left
					})
					.addClass('sh_pinned_app_animate')
					.appendTo(document.body)
					.animate({
						top: $cart.offset().top + offsetTop,
						left: $cart.offset().left + offsetLeft,
						width: 75,
						height: 75,
					}, 1000, 'easeInOutExpo');
	
				$imgclone.animate({
					width: 0,
					height: 0,
				}, function () {
					resolve();
					$(this).detach();
				});
			} else {
				resolve();
			}
		});
	},


	_ClickPinnedMenu:function (ev) {
		ev.preventDefault();
		this._onClickPinnedMenu()	
	},
	_onClickPinnedMenu : function(){
		if($('.sh_app').hasClass("sh_pinned_active")){
			$('.sh_app').removeClass("sh_pinned_active")
			$('.pinned_div').removeClass("sh_pinned_active")
			// $('.sh_new_app_icon').remove()
		}else{
			$('.sh_app').addClass("sh_pinned_active")
			$('.pinned_div').addClass("sh_pinned_active")
			this.renderPinnedApp()
		}
	},
	renderApp : function(ev){
		var self = this;
		self._getMyApps()
		self._onClickPinnedMenu()
	},

	

	renderPinnedApp : function(ev){
		var self = this;
		var pinned_app_drawer_menu_html = '<span class="dropdown-item o_app sh_add_pin_icon"><img class="sh_new_app_icon rounded" src="sh_backmate_theme/static/src/img/new1.png"/></span>'
			
		_.each(this.getPinnedApps() , function (app) {
			const parts = [`menu_id=${app.id}`];
			if (app.actionID) {
				parts.push(`action=${app.actionID}`);
			}
			var href= "#" + parts.join("&")

			pinned_app_drawer_menu_html += QWeb.render("pinned_app_drawer_menu", {
				app:app,
				app_icon:self.menuService.getMenuAsTree(app.id).xmlid.replace('.','_'),
				href: href,
				widget: self,
			})
		});	
		$("#pinned_app_drawer_menu").html(pinned_app_drawer_menu_html);

	},
	 
	_click_sh_app: async function (ev) { 
		var self = this;
		// ev.preventDefault();
		// ev.stopPropagation();
		if(!$(ev.currentTarget).hasClass('sh_pinned_active')){
			$('.app_drawer_layout').removeClass('sh_theme_model');
			$('.o_web_client').removeClass('sh_overlay_app_drawer');
			if($('.pinned_div').hasClass('sh_pinned_active')){
				this._onClickPinnedMenu();
			}
		}else{
			ev.preventDefault();
			// ev.stopPropagation();
			var $current_el = $(ev.currentTarget)

			var app_pinned = false
			for (let i = 0; i < self.app_list.length; i++) {
				if($current_el.attr('menu_id') == self.app_list[i]['id']){
					app_pinned = true
				}
			}
			if(!app_pinned){

				
				var self = this;
				var $el = $current_el.closest('.sh_app');
				await this.animateClone($('.sh_new_app_icon'), $el, 20, 10);
				rpc.query({
					model: 'sh.pinned.app',
					method: 'create',
					args: [{user_id: session.uid,app_id:$el.attr('menu_id')}],
				});

				var app_list = this.app_list
				rpc.query({
					model: 'ir.ui.menu',
					method: 'search_read',
					domain: [['id', '=', $el.attr('menu_id')]],
				}).then(function (app_data) {
					if(app_data){
						app_list.push(app_data[0])
						self.renderPinnedApp()
					}
					
				});	
				this.app_list = app_list
				console.log("$(ev.currentTarget).find('.sh_fav_icon')",$current_el)
				$current_el.find('.sh_fav_icon').css("display","none");
				$current_el.find('.sh_fav_icon_div').css("display","none");
				$current_el.find('.sh_pin_remove_icon').css("display","block");
			}
		}
		
		

	},

	_addToPinned :async function (ev) {
		ev.preventDefault();
		ev.stopPropagation();
		var self = this;
		var $el = $(ev.currentTarget).closest('.sh_app');
		await this.animateClone($('.sh_new_app_icon'), $el, 20, 10);
		rpc.query({
			model: 'sh.pinned.app',
			method: 'create',
			args: [{user_id: session.uid,app_id:$el.attr('menu_id')}],
		});

		var app_list = this.app_list
		rpc.query({
			model: 'ir.ui.menu',
			method: 'search_read',
			domain: [['id', '=', $el.attr('menu_id')]],
		}).then(function (app_data) {
			if(app_data){
				app_list.push(app_data[0])
				self.renderPinnedApp()
			}
			
		});	
		this.app_list = app_list
		$(ev.currentTarget).parents('.sh_app').find('.sh_fav_icon').css("display","none");
		$(ev.currentTarget).parents('.sh_app').find('.sh_fav_icon_div').css("display","none");
		$(ev.currentTarget).parents('.sh_app').find('.sh_pin_remove_icon').css("display","block");
		
	},
	_removeToPinned : function (ev) {
		ev.preventDefault();
		ev.stopPropagation();
		var self = this;
		var $el = $(ev.currentTarget).closest('.sh_app')
		$el.remove()
		rpc.query({
			model: 'sh.pinned.app',
			method: 'search_read',
			domain: [['app_id', '=', parseInt($el.attr('menu_id'))]],
		}).then(function (app_data) {
			if(app_data){
				rpc.query({
					model: 'sh.pinned.app',
					method: 'unlink',
					args: [[app_data[0]['id']]],
				})
				var new_app_list = []
				for (let i = 0; i < self.app_list.length; i++) {
					if(app_data[0]['app_id'][0] != self.app_list[i]['id']){
						new_app_list.push(self.app_list[i])
					}
				}
				self.app_list = new_app_list
				self.renderApp()
			}
			
		});	
	},

	
});
	
export default appDrawer