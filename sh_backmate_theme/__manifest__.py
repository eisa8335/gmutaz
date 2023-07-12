# -*- coding: utf-8 -*-
{
    "name": "Backmate Backend Theme Basics [For Community Edition]",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "license": "OPL-1",
    "category": "Themes/Backend",
    "summary": "Material Backend, Responsive, Backmate Backend Theme, fully functional Backend Theme, flexible Backend Theme, fast Backend Theme, lightweight Backend Theme, animated Backend Theme, modern multipurpose theme Odoo",
    "description": """Are you bored with your standard odoo backend theme? Are You are looking for modern, creative, clean, clear, materialize Odoo theme for your backend? So you are at right place, We have made sure that this theme is highly customizable and it comes with a premium look and feel. Our theme is not only beautifully designed but also fully functional, flexible, fast, lightweight, animated and modern multipurpose theme. Our backend theme is suitable for almost every purpose.""",
    "version": "16.0.5",
    "depends":
    [
        "web",
        "mail"
    ],

    "data":
    [   
         "security/base_security.xml",
        "security/backmate_security.xml",
        "data/theme_config_data.xml",
        "views/back_theme_config_view.xml",
        "views/assets_backend.xml",
        "views/global_search_view.xml",
        "wizard/theme_preview_wizard.xml",

        
        "security/ir.model.access.csv",
        "data/pwa_configuraion_data.xml",
        "views/assets.xml",
        "views/login_layout.xml",
        "views/pwa_configuration_view.xml",
        "views/views.xml",
        "views/notifications_view.xml",
        "views/send_notifications.xml",
        "views/web_push_notification.xml",
        "views/login_testimonial.xml",
    ],

    'images': [
        'static/description/splash-screen.png',
        'static/description/splash-screen_screenshot.gif'
    ],

    'assets': {

        'web.assets_backend': [
             'sh_backmate_theme/static/src/scss/fonts.scss',
            'sh_backmate_theme/static/src/scss/theme.scss',
            'sh_backmate_theme/static/src/scss/font.scss',
            'sh_backmate_theme/static/src/scss/buttons.scss',
            'sh_backmate_theme/static/src/scss/background/background-img.scss',
            'sh_backmate_theme/static/src/scss/saidbar.scss',
            'sh_backmate_theme/static/src/scss/navbar.scss',
            'sh_backmate_theme/static/src/scss/form_view.scss',
            'sh_backmate_theme/static/src/scss/button_icon.scss',
            'sh_backmate_theme/static/src/scss/sidebar_bg.scss',
            'sh_backmate_theme/static/src/scss/menu_mobile.scss',
            'sh_backmate_theme/static/src/scss/nprogress.scss',
            'sh_backmate_theme/static/src/scss/background/background-color.scss',
            
            #partical style
            "sh_backmate_theme/static/src/scss/particle/particle.scss",
            "sh_backmate_theme/static/src/js/partical/particles.js",
            "sh_backmate_theme/static/src/js/partical/stats.js",
            "sh_backmate_theme/static/src/js/partical/partical.js",
            "sh_backmate_theme/static/src/js/partical/particles.min.js",

            #Menu Structure
            "sh_backmate_theme/static/src/xml/menu.xml",
            'sh_backmate_theme/static/src/webclient/navbar/navbar.js',

            #app Global Search - app drawer
            "sh_backmate_theme/static/src/webclient/navbar/global_search.js",
            "sh_backmate_theme/static/src/xml/app_drawer.xml",
            'sh_backmate_theme/static/src/webclient/navbar/app_drawer.js',
            'sh_backmate_theme/static/src/scss/app_drawer.scss',

            #Full form width
            "sh_backmate_theme/static/src/js/FullFormWidth.js",
            'sh_backmate_theme/static/src/scss/form_full_width.scss',

            #Odoo standard js
            "sh_backmate_theme/static/src/js/route_service.js",
            "sh_backmate_theme/static/src/js/action_service.js",
            "sh_backmate_theme/static/src/js/dropdown.js",

            #On refresh custom js
            "sh_backmate_theme/static/src/js/On_refresh.js",

            # Progress bar and loading
            "sh_backmate_theme/static/src/js/nprogress.js",
            'sh_backmate_theme/static/src/js/progressbar.js',

            # Refresh Feature
            "sh_backmate_theme/static/src/js/kanban_controller.js",
            "sh_backmate_theme/static/src/js/list_controller.js",
            'sh_backmate_theme/static/src/js/calendar_controller.js',
            "sh_backmate_theme/static/src/xml/refresh.xml",
            'sh_backmate_theme/static/src/scss/refresh_page.scss',

            # Quick Menu Feature
            "sh_backmate_theme/static/src/js/quick_menu.js",
            "sh_backmate_theme/static/src/xml/web_quick_menu.xml",
            "sh_backmate_theme/static/src/scss/quick_menu.scss",

            #separator 
            'sh_backmate_theme/static/src/scss/separtor.scss',

            #Scrollbar style
            'sh_backmate_theme/static/src/scss/scrollbar/scrollbar_style.scss',

            #breadcrumb style 
            'sh_backmate_theme/static/src/scss/breadcrumb.scss',

            #form element style
            'sh_backmate_theme/static/src/scss/form_element_style.scss',

            # Calculator
            "sh_backmate_theme/static/src/js/calculator.js",
            "sh_backmate_theme/static/src/xml/Calculator.xml",
            "sh_backmate_theme/static/src/scss/calculator.scss",

            #popup animation style
            'sh_backmate_theme/static/src/scss/popup_style.scss',

            # FullScreen
            "sh_backmate_theme/static/src/js/fullscreen.js",
            "sh_backmate_theme/static/src/xml/FullScreen.xml",

            # Language
            "sh_backmate_theme/static/src/js/language_selector.js",
            "sh_backmate_theme/static/src/xml/Language.xml",

            #Todo feature
            "sh_backmate_theme/static/src/js/todo_widget.js",
            "sh_backmate_theme/static/src/js/todo.js",
            "sh_backmate_theme/static/src/xml/todo.xml",
            "sh_backmate_theme/static/src/scss/todo/todo.scss",

            #Global Search
            "sh_backmate_theme/static/src/js/global_search.js",
            "sh_backmate_theme/static/src/scss/global_search.scss",
            "sh_backmate_theme/static/src/xml/global_search.xml",

            #Zoom Widget
            "sh_backmate_theme/static/src/webclient/web_client.js",
            "sh_backmate_theme/static/src/webclient/zoomwidget/zoomwidget.js",
            "sh_backmate_theme/static/src/xml/Zoom.xml",
            'sh_backmate_theme/static/src/scss/zoom_in_out/zoom_in_out.scss',

            #Night Mode
            "sh_backmate_theme/static/src/js/night_mode.js",
            "sh_backmate_theme/static/src/scss/night_mode_user.scss",
            "sh_backmate_theme/static/src/xml/NightMode.xml",

            #Sticky
            "sh_backmate_theme/static/src/scss/sticky/sticky_chatter.scss",
            "sh_backmate_theme/static/src/scss/sticky/sticky_form.scss",
            "sh_backmate_theme/static/src/scss/sticky/sticky_list_inside_form.scss",
            "sh_backmate_theme/static/src/scss/sticky/sticky_list.scss",
            "sh_backmate_theme/static/src/scss/sticky/sticky_pivot.scss",
            "sh_backmate_theme/static/src/js/pivot_view_sticky/pivot_sticky_dropdown.js",

            #checkbox and radio button style
            'sh_backmate_theme/static/src/scss/checkbox_style/checkbox_style.scss',
            'sh_backmate_theme/static/src/scss/radio_btn_style/radio_btn_style.scss',

            #control_panel
            "sh_backmate_theme/static/src/scss/control_panel/control_panel.scss",

            #Predefined list view
            "sh_backmate_theme/static/src/scss/predefine_list_view/predefine_list_view.scss",

            # App icon and Font icon style
            "sh_backmate_theme/static/src/scss/icon_style/icon_style.scss",
            "sh_backmate_theme/static/src/scss/font_awesome_light_icon.scss",
            "sh_backmate_theme/static/src/scss/font_awesome_thin_icon.scss",
            "sh_backmate_theme/static/src/scss/font_awesome_std_icon.scss",
            "sh_backmate_theme/static/src/scss/font_awesome_regular_icon.scss",
            "sh_backmate_theme/static/src/scss/oi_light_icon.scss",
            "sh_backmate_theme/static/src/scss/oi_regular_icon.scss",
            "sh_backmate_theme/static/src/scss/oi_thin_icon.scss",
            "sh_backmate_theme/static/src/scss/style.css",  

            #Loader style
            'sh_backmate_theme/static/src/scss/loader.scss', 


            # Theme Style_8 
            'sh_backmate_theme/static/src/scss/theme_style_8/theme_8.scss',
            'sh_backmate_theme/static/src/scss/theme_style_8/theme_8_responsive.scss',
            'sh_backmate_theme/static/src/scss/theme_style_8/theme_8_night_mode.scss', 

            #Firebase and PWA  and bus Notification
            "sh_backmate_theme/static/index.js",
            "https://www.gstatic.com/firebasejs/8.4.3/firebase-app.js",
            "https://www.gstatic.com/firebasejs/8.4.3/firebase-messaging.js",
            "sh_backmate_theme/static/src/js/firebase.js",
            "sh_backmate_theme/static/src/js/bus_notification.js",

            #web notification
            'sh_backmate_theme/static/src/scss/notification.scss',

            #Mobile
            # "sh_backmate_theme/static/src/xml/form_view.xml",

            #Horizontal/vertical Tab
            'sh_backmate_theme/static/src/js/notebook.js',
            'sh_backmate_theme/static/src/scss/tab.scss',


            # Chatter
            "sh_backmate_theme/static/src/components/message/message.js",
            "sh_backmate_theme/static/src/xml/message.xml",
            'sh_backmate_theme/static/src/scss/discuss_chatter/discuss_chatter.scss',


            #Multi Tab
            "sh_backmate_theme/static/src/webclient/navtab/navtab.js",
            "sh_backmate_theme/static/src/xml/navbar.xml",
            "sh_backmate_theme/static/src/scss/multi_tab_at_control_panel/multi_tab.scss",
            "sh_backmate_theme/static/src/webclient/action_container.js",
            "sh_backmate_theme/static/src/js/owl.carousel.js",  #Third party

            # enterprise_theme
            "sh_backmate_theme/static/src/scss/enterprise_theme.scss",

            # responsive_theme
            "/sh_backmate_theme/static/src/scss/responsive.scss",

            # Disable Auto edit feature
            "sh_backmate_theme/static/src/js/form_controller.js",
            "sh_backmate_theme/static/src/xml/form_controller.xml",
            "sh_backmate_theme/static/src/scss/form_controller.scss",


        ],
         'web.assets_frontend': [
             'sh_backmate_theme/static/src/scss/fonts.scss',
            'sh_backmate_theme/static/src/scss/login_style.scss'
           
        ],
         
         'web._assets_primary_variables': [
          ('after', 'web/static/src/scss/primary_variables.scss', '/sh_backmate_theme/static/src/scss/back_theme_config_main_scss.scss'),        
        ],
    },
    "live_test_url": "https://softhealer.com/support?ticket_type=demo_request",
    "installable": True,
    "application": True,
    "price": 130.60,
    "currency": "EUR",
    "bootstrap": True
}
