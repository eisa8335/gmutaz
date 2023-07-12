 # -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api, _
import base64


dict_theme_style = {
    'style_1':  {
       'primary_color': '#673AB7',
       'primary_hover': '#553098',
       'primary_active': '#553098',
       'secondary_color': '#e6e6e6',
       'secondary_hover': '#CDCDCD',
       'secondary_active': '#CDCDCD',
       'header_background_color': '#673AB7',
       'header_font_color': '#FFFFFF',
       'header_hover_color': '#FFFFFF',
       'header_active_color': '#FFFFFF',
       'h1_color': '#4E4E4E',
       'h2_color': '#4E4E4E',
       'h3_color': '#4E4E4E',
       'h4_color': '#4E4E4E',
       'h5_color': '#4E4E4E',
       'h6_color': '#4E4E4E',
       'p_color': '#4E4E4E',
       'h1_size': 28,
       'h2_size': 17,
       'h3_size': 18,
       'h4_size': 15,
       'h5_size': 13,
       'h6_size': 12,
       'p_size': 13,
       'body_font_color': '#4E4E4E',
       'body_background_color': '#FFFFFF',
       'body_font_family': 'custom_google_font',
       'button_style': 'style_2',
       'separator_style': 'style_2',
       'separator_color': '#9C27B0',
       'sidebar_background_color': '#FFFFFF',
       'sidebar_font_color': '#4E4E4E',
       'sidebar_font_hover_color': '#FFFFFF',
       'sidebar_font_hover_background_color': '#553098',
       'sidebar_style': 'style_2',
       'body_background_type': 'bg_color',
       'sidebar_background_type': 'bg_color',
       'is_button_with_icon_text': False,

        'body_google_font_family': 'Arimo',
        'is_used_google_font': True,

        'predefined_list_view_boolean': False,
        'predefined_list_view_style': 'style_1',
        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#ccc',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_0',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': '#FFFFFF',
        'modal_popup_style': 'style_1',
        'mobile_icon_style': 'floating',
        'tab_style': 'horizontal',
        'tab_style_mobile': 'vertical',
        'horizontal_tab_style': 'style_1',
        'vertical_tab_style': 'style_1',
        'form_element_style': 'style_1',
        'chatter_position':  'normal',
        'breadcrumb_style': 'style_1',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#906bd1',
        'loading_style': 'style_2',
        'checkbox_style':'custom',
        'radio_style':'custom',
        'scrollbar_style' : 'style_1',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_1',
        'dual_tone_icon_color_1' : '#b8b8b8',
        'dual_tone_icon_color_2' : '#4e4e4e',
        'backend_all_icon_style' : 'backend_fontawesome_icon',
        'festival_style': 'default',
    },
    'style_2':  {
       'primary_color': '#2196F3',
       'primary_hover': '#1C80D0',
       'primary_active': '#1C80D0',
       'secondary_color': '#E6E6E6',
       'secondary_hover': '#CDCDCD',
       'secondary_active': '#CDCDCD',
       'header_background_color': '#2196F3',
       'header_font_color': '#FFFFFF',
       'header_hover_color': '#FFFFFF',
       'header_active_color': '#FFFFFF',
       'h1_color': '#4E4E4E',
       'h2_color': '#4E4E4E',
       'h3_color': '#4E4E4E',
       'h4_color': '#4E4E4E',
       'h5_color': '#4E4E4E',
       'h6_color': '#4E4E4E',
       'p_color': '#4E4E4E',
       'h1_size': 28,
       'h2_size': 17,
       'h3_size': 18,
       'h4_size': 15,
       'h5_size': 13,
       'h6_size': 12,
       'p_size': 13,
       'body_font_color': '#4E4E4E',
       'body_background_color': '#FFFFFF',
       'body_font_family': 'Raleway',
       'button_style': 'style_1',
       'separator_style': 'style_1',
       'separator_color': '#3F51B5',
       'sidebar_background_color': '#FFFFFF',
       'sidebar_font_color': '#4E4E4E',
       'sidebar_font_hover_color': '#FFFFFF',
       'sidebar_font_hover_background_color': '#1C80D0',
       'sidebar_style': 'style_1',
       'body_background_type': 'bg_color',
       'sidebar_background_type': 'bg_color',
       'is_button_with_icon_text': False,
        'body_google_font_family': False,
        'is_used_google_font': False,

        'predefined_list_view_boolean': True,
        'predefined_list_view_style': 'style_1',
        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#dedede',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#f5f5f5',

        'login_page_style': 'style_0',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': '#FFFFFF',
        'modal_popup_style': 'style_1',
        'mobile_icon_style': 'floating',
        'tab_style': 'horizontal',
        'tab_style_mobile': 'vertical',
        'horizontal_tab_style': 'style_5',
        'vertical_tab_style': 'style_5',
        'form_element_style': 'style_2',
        'chatter_position':  'normal',
        'breadcrumb_style': 'style_2',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#1d6cab',
        'loading_style': 'style_1',
        'checkbox_style':'style_3',
        'radio_style':'style_3',
        'scrollbar_style' : 'style_2',
        'discuss_chatter_style' : 'style_2',
        'app_icon_style' : 'style_1',
        'dual_tone_icon_color_1' : '#b8b8b8',
        'dual_tone_icon_color_2' : '#4e4e4e',
        'backend_all_icon_style' : 'backend_regular_icon',
        'festival_style': 'default',
     },

    'style_3':  {
       'primary_color': '#720d5d',
       'primary_hover': '#5d1049',
       'primary_active': '#5d1049',
       'secondary_color': '#E6E6E6',
       'secondary_hover': '#CDCDCD',
       'secondary_active': '#CDCDCD',
       'header_background_color': '#720d5d',
       'header_font_color': '#FFFFFF',
       'header_hover_color': '#FFFFFF',
       'header_active_color': '#FFFFFF',
       'h1_color': '#4E4E4E',
       'h2_color': '#4E4E4E',
       'h3_color': '#4E4E4E',
       'h4_color': '#4E4E4E',
       'h5_color': '#4E4E4E',
       'h6_color': '#4E4E4E',
       'p_color': '#4E4E4E',
       'h1_size': 28,
       'h2_size': 17,
       'h3_size': 18,
       'h4_size': 15,
       'h5_size': 13,
       'h6_size': 12,
       'p_size': 13,
       'body_font_color': '#4E4E4E',
       'body_background_color': '#FFFFFF',
       'body_font_family': 'Poppins',
       'button_style': 'style_3',
       'separator_style': 'style_3',
       'separator_color': '#5D1049',
       'sidebar_background_color': '#FFFFFF',
       'sidebar_font_color': '#FFFFFF',
       'sidebar_font_hover_color': '#FFFFFF',
       'sidebar_font_hover_background_color': '#5D1049',
       'sidebar_style': 'style_3',
       'body_background_type': 'bg_color',
       'sidebar_background_type': 'bg_img',
       'is_button_with_icon_text': True,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'predefined_list_view_boolean': True,
        'predefined_list_view_style': 'style_2',
        'list_view_border': 'bordered',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#dadada',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_0',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': '#FFFFFF',
        'modal_popup_style': 'style_1',
        'mobile_icon_style': 'floating',
        'tab_style': 'horizontal',
        'tab_style_mobile': 'vertical',
        'horizontal_tab_style': 'style_6',
        'vertical_tab_style': 'style_6',
        'form_element_style': 'style_5',
        'chatter_position':  'normal',
        'breadcrumb_style': 'style_3',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#bf4da7',
        'loading_style': 'style_11',
        'checkbox_style':'style_2',
        'radio_style':'style_2',
        'scrollbar_style' : 'style_3',
        'discuss_chatter_style' : 'style_3',
        'app_icon_style' : 'style_3',
        'dual_tone_icon_color_1' : '#8b8b8b',
        'dual_tone_icon_color_2' : '#ffffff',
        'backend_all_icon_style' : 'backend_light_icon',
        'festival_style': 'default',
     },

    'style_4':  {
       'primary_color': '#4A6572',
       'primary_hover': '#344955',
       'primary_active': '#344955',
       'secondary_color': '#E6E6E6',
       'secondary_hover': '#CDCDCD',
       'secondary_active': '#CDCDCD',
       'header_background_color': '#4A6572',
       'header_font_color': '#FFFFFF',
       'header_hover_color': '#FFFFFF',
       'header_active_color': '#FFFFFF',
       'h1_color': '#4E4E4E',
       'h2_color': '#4E4E4E',
       'h3_color': '#4E4E4E',
       'h4_color': '#4E4E4E',
       'h5_color': '#4E4E4E',
       'h6_color': '#4E4E4E',
       'p_color': '#4E4E4E',
       'h1_size': 28,
       'h2_size': 17,
       'h3_size': 18,
       'h4_size': 15,
       'h5_size': 13,
       'h6_size': 12,
       'p_size': 13,
       'body_font_color': '#4E4E4E',
       'body_background_color': '#FFFFFF',
       'body_font_family': 'Oxygen',
       'button_style': 'style_4',
       'separator_style': 'style_4',
       'separator_color': '#344955',
       'sidebar_background_color': '#FFFFFF',
       'sidebar_font_color': '#4E4E4E',
       'sidebar_font_hover_color': '#FFFFFF',
       'sidebar_font_hover_background_color': '#344955',
       'sidebar_style': 'style_4',
       'body_background_type': 'bg_color',
       'sidebar_background_type': 'bg_color',
       'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'predefined_list_view_boolean': True,
        'predefined_list_view_style': 'style_3',
        'list_view_border': 'bordered',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#dadada',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#f5f5f5',

        'login_page_style': 'style_0',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': '#FFFFFF',
        'modal_popup_style': 'style_1',
        'mobile_icon_style': 'floating',
        'tab_style': 'horizontal',
        'tab_style_mobile': 'vertical',
        'horizontal_tab_style': 'style_2',
        'vertical_tab_style': 'style_2',
        'form_element_style': 'style_4',
        'chatter_position':  'normal',
        'breadcrumb_style': 'style_4',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#79a5ba',
        'loading_style': 'style_4',
        'checkbox_style':'style_3',
        'radio_style':'style_3',
        'scrollbar_style' : 'style_4',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_2',
        'dual_tone_icon_color_1' : '#9cb7c1',
        'dual_tone_icon_color_2' : '#4A6572',
        'backend_all_icon_style' : 'backend_regular_icon',
        'festival_style': 'default',
     },

    'style_5': {
       'primary_color': '#43A047',
       'primary_hover': '#388E3C',
       'primary_active': '#388E3C',
       'secondary_color': '#E6E6E6',
       'secondary_hover': '#CDCDCD',
       'secondary_active': '#CDCDCD',
       'header_background_color': '#43A047',
       'header_font_color': '#FFFFFF',
       'header_hover_color': '#FFFFFF',
       'header_active_color': '#FFFFFF',
       'h1_color': '#4E4E4E',
       'h2_color': '#4E4E4E',
       'h3_color': '#4E4E4E',
       'h4_color': '#4E4E4E',
       'h5_color': '#4E4E4E',
       'h6_color': '#4E4E4E',
       'p_color': '#4E4E4E',
       'h1_size': 28,
       'h2_size': 17,
       'h3_size': 18,
       'h4_size': 15,
       'h5_size': 13,
       'h6_size': 12,
       'p_size': 13,
       'body_font_color': '#4E4E4E',
       'body_background_color': '#FFFFFF',
       'body_font_family': 'OpenSans',
       'button_style': 'style_5',
       'separator_style': 'style_5',
       'separator_color': '#388E3C',
       'sidebar_background_color': '#FFFFFF',
       'sidebar_font_color': '#4E4E4E',
       'sidebar_font_hover_color': '#FFFFFF',
       'sidebar_font_hover_background_color': '#388E3C',
       'sidebar_style': 'style_5',
       'body_background_type': 'bg_color',
       'sidebar_background_type': 'bg_color',
       'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'predefined_list_view_boolean': False,
        'predefined_list_view_style': 'style_1',
        'list_view_border': 'bordered',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#dadada',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#f5f5f5',

        'login_page_style': 'style_0',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': '#FFFFFF',
        'modal_popup_style': 'style_1',
        'mobile_icon_style': 'floating',
        'tab_style': 'horizontal',
        'tab_style_mobile': 'vertical',
        'horizontal_tab_style': 'style_4',
        'vertical_tab_style': 'style_4',
        'form_element_style': 'style_3',
        'chatter_position':  'normal',
        'breadcrumb_style': 'style_5',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#8de091',
        'loading_style': 'style_5',
        'checkbox_style':'default',
        'radio_style':'default',
        'scrollbar_style' : 'style_5',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_4',
        'dual_tone_icon_color_1' : '#B8B8B8',
        'dual_tone_icon_color_2' : '#4E4E4E',
        'backend_all_icon_style' : 'backend_thin_icon',
        'festival_style': 'default',
     },


    'style_6': {
       'primary_color': '#C8385E',
       'primary_hover': '#AA2F50',
       'primary_active': '#AA2F50',
       'secondary_color': '#E6E6E6',
       'secondary_hover': '#CDCDCD',
       'secondary_active': '#CDCDCD',
       'header_background_color': '#C8385E',
       'header_font_color': '#FFFFFF',
       'header_hover_color': '#FFFFFF',
       'header_active_color': '#FFFFFF',
       'h1_color': '#4E4E4E',
       'h2_color': '#4E4E4E',
       'h3_color': '#4E4E4E',
       'h4_color': '#4E4E4E',
       'h5_color': '#4E4E4E',
       'h6_color': '#4E4E4E',
       'p_color': '#4E4E4E',
       'h1_size': 28,
       'h2_size': 17,
       'h3_size': 18,
       'h4_size': 15,
       'h5_size': 13,
       'h6_size': 12,
       'p_size': 13,
       'body_font_color': '#4E4E4E',
       'body_background_color': '#F9F9F9',
       'body_font_family': 'OpenSans',
       'button_style': 'style_5',
       'separator_style': 'style_5',
       'separator_color': '#AA2F50',
       'sidebar_background_color': '#FFFFFF',
       'sidebar_font_color': '#FFFFFF',
       'sidebar_font_hover_color': '#FFFFFF',
       'sidebar_font_hover_background_color': '#AA2F50',
       'sidebar_style': 'style_6',
       'body_background_type': 'bg_img',
       'sidebar_background_type': 'bg_img',
       'is_button_with_icon_text': True,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'predefined_list_view_boolean': True,
        'predefined_list_view_style': 'style_5',
        'list_view_border': 'bordered',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#dadada',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#f5f5f5',

        'login_page_style': 'style_0',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': '#FFFFFF',
        'modal_popup_style': 'style_1',
        'mobile_icon_style': 'floating',
        'tab_style': 'horizontal',
        'tab_style_mobile': 'vertical',
        'horizontal_tab_style': 'style_3',
        'vertical_tab_style': 'style_3',
        'form_element_style': 'style_6',
        'chatter_position':  'normal',
        'breadcrumb_style': 'style_6',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#e0879e',
        'loading_style': 'style_12',
        'checkbox_style':'default',
        'radio_style':'default',
        'scrollbar_style' : 'style_1',
        'discuss_chatter_style' : 'style_1',
        'app_icon_style' : 'style_3',
        'dual_tone_icon_color_1' : '#6E6E6E',
        'dual_tone_icon_color_2' : '#ffffff',
        'backend_all_icon_style' : 'backend_light_icon',
        'festival_style': 'default',
     },


    'style_7':  {
        'primary_color': '#017e84',
        'primary_hover': '#015a5e',
        'primary_active': '#015a5e',
       'secondary_color': '#E6E6E6',
       'secondary_hover': '#CDCDCD',
       'secondary_active': '#CDCDCD',
       'header_background_color': '#714B67',
       'header_font_color': '#FFFFFF',
       'header_hover_color': '#FFFFFF',
       'header_active_color': '#FFFFFF',
       'h1_color': '#4E4E4E',
       'h2_color': '#4E4E4E',
       'h3_color': '#4E4E4E',
       'h4_color': '#4E4E4E',
       'h5_color': '#4E4E4E',
       'h6_color': '#4E4E4E',
       'p_color': '#4E4E4E',
       'h1_size': 28,
       'h2_size': 17,
       'h3_size': 18,
       'h4_size': 15,
       'h5_size': 13,
       'h6_size': 12,
       'p_size': 13,
       'body_font_color': '#4E4E4E',
       'body_background_color': '#F9F9F9',
       'body_font_family': 'Roboto',
       'button_style': 'style_4',
       'separator_style': 'style_6',
       'separator_color': '#5D1049',
       'sidebar_background_color': '#FFFFFF',
       'sidebar_font_color': '#FFFFFF',
       'sidebar_font_hover_color': '#FFFFFF',
       'sidebar_font_hover_background_color': '#5D1049',
       'sidebar_style': 'style_3',
       'body_background_type': 'bg_color',
       'sidebar_background_type': 'bg_color',
       'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'predefined_list_view_boolean': False,
        'predefined_list_view_style': 'style_1',
        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#f5f5f5',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_3',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': '#FFFFFF',
        'modal_popup_style': 'style_11',
        'mobile_icon_style': 'default',
        'sidebar_color_1': '#917878',
        'sidebar_img': 'style_1',
        'tab_style': 'horizontal',
        'tab_style_mobile': 'vertical',
        'horizontal_tab_style': 'style_7',
        'vertical_tab_style': 'style_7',
        'form_element_style': 'style_1',
        'chatter_position':  'sided',
        'breadcrumb_style': 'style_7',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#ad86a3',
        'loading_style': 'style_10',
        'checkbox_style':'default',
        'radio_style':'default',
        'scrollbar_style' : 'style_1',
        'discuss_chatter_style' : 'default',
        'app_icon_style' : 'style_1',
        'dual_tone_icon_color_1' : '#BBB3B9',
        'dual_tone_icon_color_2' : '#ffffff',
        'backend_all_icon_style' : 'backend_fontawesome_icon',
        'festival_style': 'default',
     },

     'style_8':  {
        'primary_color': '#573285',
        'primary_hover': '#4f2d78',
        'primary_active': '#4f2d78',
        'gradient_color': '#7e2a4a',
        'extra_color': '#e77b5a',
       'secondary_color': '#eceef7',
       'secondary_hover': '#f0f2fb',
       'secondary_active': '#f0f2fb',
       'header_background_color': '#573285',
       'header_font_color': '#FFFFFF',
       'header_hover_color': '#FFFFFF',
       'header_active_color': '#FFFFFF',
       'h1_color': '#4E4E4E',
       'h2_color': '#4E4E4E',
       'h3_color': '#4E4E4E',
       'h4_color': '#4E4E4E',
       'h5_color': '#4E4E4E',
       'h6_color': '#4E4E4E',
       'p_color': '#4E4E4E',
       'h1_size': 28,
       'h2_size': 17,
       'h3_size': 18,
       'h4_size': 15,
       'h5_size': 13,
       'h6_size': 12,
       'p_size': 13,
       'body_font_color': '#4E4E4E',
       'body_background_color': '#ECEEF7',
       'body_font_family': 'Comfortaa',
       'button_style': 'style_6',
       'separator_style': 'style_6',
       'separator_color': '#573285',
       'sidebar_background_color': '#573285',
       'sidebar_background_additional_color': '#7e2a4a',
       'sidebar_font_color': '#FFFFFF',
       'sidebar_font_hover_color': '#FFFFFF',
       'sidebar_font_hover_background_color': 'transparent',
       'sidebar_style': 'style_3',
       'body_background_type': 'bg_color',
       'sidebar_background_type': 'bg_color',
       'is_button_with_icon_text': False,

        'body_google_font_family': False,
        'is_used_google_font': False,

        'predefined_list_view_boolean': False,
        'predefined_list_view_style': 'style_1',
        'list_view_border': 'without_border',
        'list_view_is_hover_row': True,
        'list_view_hover_bg_color': '#FFFFFF',
        'list_view_even_row_color': '#FFFFFF',
        'list_view_odd_row_color': '#FFFFFF',

        'login_page_style': 'style_4',
        'login_page_background_type': 'bg_color',
        'login_page_background_color': '#B3FFB8',
        'login_page_box_color': '#FFFFFF',
        'modal_popup_style': 'style_1',
        'mobile_icon_style': 'floating',
        'sidebar_color_1': '#917878',
        'sidebar_img': 'style_1',
        'tab_style': 'horizontal',
        'tab_style_mobile': 'vertical',
        'horizontal_tab_style': 'style_8',
        'vertical_tab_style': 'style_8',
        'form_element_style': 'style_8',
        'chatter_position':  'normal',
        'breadcrumb_style': 'style_3',
        'progress_style': 'style_1',
        'progress_height': '4px',
        'progress_color':  '#ad86a3',
        'loading_style': 'style_3',
        'checkbox_style':'style_2',
        'radio_style':'custom',
        'scrollbar_style' : 'style_1',
        'discuss_chatter_style' : 'style_2',
        'is_sticky_form' : False,
        'is_sticky_chatter' : False,
        'is_sticky_list' : True,
        'is_sticky_list_inside_form' : True,
        'is_sticky_pivot' : False,
        'app_icon_style' : 'style_3',
        'dual_tone_icon_color_1' : '#e77b5a',
        'dual_tone_icon_color_2' : '#ffffff',
        'backend_all_icon_style' : 'backend_light_icon',
        'festival_style': 'default',
     },


    }




class sh_backmate_theme_settings(models.Model):
    _name = 'sh.back.theme.config.settings'
    _description = 'Back Theme Config Settings'

    name = fields.Char(string="Theme Settings")

    theme_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Enterprise'),
        ('style_8', 'Crescent'),
        ], string="Theme Style")

    festival_style = fields.Selection([
        ('default', 'Default'),
        ('christmas', 'Christmas'),
        ('new_year', 'New Year'),
        ], string="Festival Style")

    primary_color = fields.Char(string='Primary Color')
    primary_hover = fields.Char(string='Primary Hover')
    primary_active = fields.Char(string='Primary Active')
    gradient_color = fields.Char(string='Gradient Color')
    extra_color = fields.Char(string='Extra Color')

    secondary_color = fields.Char(string='Secondary Color')
    secondary_hover = fields.Char(string='Secondary Hover')
    secondary_active = fields.Char(string='Secondary Active')

    header_background_color = fields.Char(string='Header Background Color')
    header_font_color = fields.Char(string='Header Font Color')
    header_hover_color = fields.Char(string='Header Hover Color')
    header_active_color = fields.Char(string='Header Active Color')


    h1_color = fields.Char(string='H1 Color')
    h2_color = fields.Char(string='H2 Color')
    h3_color = fields.Char(string='H3 Color')
    h4_color = fields.Char(string='H4 Color')
    h5_color = fields.Char(string='H5 Color')
    h6_color = fields.Char(string='H6 Color')
    p_color = fields.Char(string='P Color')

    h1_size = fields.Integer(string='H1 Size')
    h2_size = fields.Integer(string='H2 Size')
    h3_size = fields.Integer(string='H3 Size')
    h4_size = fields.Integer(string='H4 Size')
    h5_size = fields.Integer(string='H5 Size')
    h6_size = fields.Integer(string='H6 Size')
    p_size = fields.Integer(string='P Size')

    body_font_color = fields.Char(string='Body Font Color')
    body_background_type = fields.Selection([
        ('bg_color', 'Color'),
        ('bg_img', 'Image')
        ], string="Body Background Type", default="bg_color")

    body_background_color = fields.Char(string='Body Background Color')
    body_background_image = fields.Binary(string='Body Background Image')
    body_font_family = fields.Selection([
        ('Roboto', 'Roboto'),
        ('Raleway', 'Raleway'),
        ('Poppins', 'Poppins'),
        ('Oxygen', 'Oxygen'),
        ('OpenSans', 'OpenSans'),
        ('KoHo', 'KoHo'),
        ('Ubuntu', 'Ubuntu'),
        ('Comfortaa','Comfortaa'),
        ('inherit', 'Default'),
        ('custom_google_font', 'Custom Google Font'),
        ], string='Body Font Family')

    body_google_font_family = fields.Char(string="Google Font Family")
    is_used_google_font = fields.Boolean(string="Is use google font?")

    button_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ], string='Button Style')
    is_button_with_icon_text = fields.Boolean(
        string="Button with text and icon?")

    separator_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Default'),
        ], string='Separator Style')

    separator_color = fields.Char(string="Separator Color")

    sidebar_color_1 = fields.Char(string="Background Color 1")
    sidebar_img = fields.Selection([('style_1', 'Style 1'), ('style_2', 'Style 2'), ('style_3', 'Style 3'), (
        'style_4', 'Style 4'), ('style_5', 'Style 5'), ('style_6', 'Style 6')], string="Background Image", default='style_1')

    sidebar_background_type = fields.Selection([
        ('bg_color', 'Color'),
        ('bg_img', 'Image')
        ], string="Sidebar Background Type", default="bg_color")

    sidebar_background_color = fields.Char(string='Sidebar Background Color')
    sidebar_background_additional_color = fields.Char(string='Sidebar Background Additional Color')
    sidebar_background_image = fields.Binary(string='Sidebar Background Image')

    sidebar_font_color = fields.Char(string='Sidebar Font Color')
    sidebar_font_hover_color = fields.Char(string='Sidebar Font Hover Color')
    sidebar_font_hover_background_color = fields.Char(
        string='Sidebar Font Hover Background Color')
    sidebar_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Style 7'),
        ('style_8', 'Style 8'),
        ], string='Sidebar Style')


    loading_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Style 7'),
        ('style_8', 'Style 8'),
        ('style_9', 'Style 9'),
        ('style_10', 'Style 10'),
        ('style_11', 'Style 11'),
        ('style_12', 'Style 12'),
        ], string='Loading Style', default="style_1")

    progress_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('none', 'None'),
        ], string='Progress Bar Style', default="style_1")


    progress_height = fields.Char("Height")
    progress_color = fields.Char("Color")

    loading_gif = fields.Binary(string="Loading GIF")
    loading_gif_file_name = fields.Char(string="Loading GIF File Name")

    predefined_list_view_boolean = fields.Boolean(string="Is Predefined List View?")
    predefined_list_view_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5')
        ], default='style_1', string="Predefined List View Style")
    list_view_border = fields.Selection([
        ('bordered', 'Bordered'),
        ('without_border', 'Without Border')
        ], default='without_border', string="List View Border")

    list_view_is_hover_row = fields.Boolean(string="Rows Hover?")
    list_view_hover_bg_color = fields.Char(string="Hover Background Color")
    list_view_even_row_color = fields.Char(string="Even Row Color")
    list_view_odd_row_color = fields.Char(string="Odd Row Color")


    login_page_style = fields.Selection([
        ('style_0', 'Odoo Standard'),
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ], default="style_0", string="Style")

    login_page_background_type = fields.Selection([
        ('bg_color', 'Color'),
        ('bg_img', 'Image')
        ], string="Background Type", default="bg_color")

    login_page_background_color = fields.Char(string='Background Color')
    login_page_background_image = fields.Binary(string='Background Image ')
    login_page_box_color = fields.Char(string='Box Color')
    login_page_banner_image = fields.Binary(string='Banner Image')

    # Sticky
    is_sticky_form = fields.Boolean(string="Form Status Bar")
    is_sticky_chatter = fields.Boolean(string="Chatter")
    is_sticky_list = fields.Boolean(string="List View")
    is_sticky_list_inside_form = fields.Boolean(string="List View Inside Form")
    is_sticky_pivot = fields.Boolean(string="Pivot View")

    # Modal Popup
    modal_popup_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Style 7'),
        ('style_8', 'Style 8'),
        ('style_9', 'Style 9'),
        ('style_10', 'Style 10'),
        ('style_11', 'Default'),
        ], string='Popup Style')

    # mobile icon style
    mobile_icon_style = fields.Selection(
        [('default', 'Default'), ('floating', 'Floating')], string='Mobile Icon', default='default')


    # New checkbox icon style
    checkbox_style = fields.Selection([
        ('custom','Style 1'),
        ('style_2','Style 2'),
        ('style_3','Style 3'),
        ('default','Default'),                 
        ],string = 'Checkbox Style',default='custom')

    # New Radio icon style
    radio_style = fields.Selection([
        ('custom','Style 1'),
        ('style_2','Style 2'),
        ('style_3','Style 3'),
        ('default','Default'),                  
        ],string = 'Radio Button Style',default='custom')

    scrollbar_style = fields.Selection([
        ('style_1','Style 1'),  
        ('style_2','Style 2'),  
        ('style_3','Style 3'),  
        ('style_4','Style 4'),  
        ('style_5','Style 5'),                 
        ],string = 'Scrollbar Style',default='style_1')

    discuss_chatter_style = fields.Selection([
        ('style_1','Style 1'),
        ('style_2','Style 2'),
        ('style_3','Style 3'),      
        ('default','default'),          
        ],string = 'Discuss Chatter Style',default='style_1')

    discuss_chatter_style_image_two = fields.Binary(string='discuss chatter Image')
    discuss_chatter_style_image_three = fields.Binary(string='discuss chatter Image')
    
    app_icon_style = fields.Selection([
        ('style_1', 'Standard'),
        ('style_2', 'Line Icon'),
        ('style_3', '3D Icon'),
        ('style_4', 'Dual Tone'),
        ], string='App Icon Style', default='style_1')

    dual_tone_icon_color_1 = fields.Char(string='Dual Tone Icon Color 1')
    dual_tone_icon_color_2 = fields.Char(string='Dual Tone Icon Color 2')

    backend_all_icon_style = fields.Selection([
        ('backend_fontawesome_icon', 'Standard FontAwesome Icon'),
        ('backend_regular_icon', 'Regular Icon'),
        ('backend_light_icon', 'Light Icon'),
        ('backend_thin_icon', 'Thin Icon'),
        ], string='Backend Icon Style', default='backend_fontawesome_icon')

    tab_style = fields.Selection([('horizontal', 'Horizontal'), (
        'vertical', 'Vertical')], string="Tab Style (Desktop)", default='horizontal')
    tab_style_mobile = fields.Selection([('horizontal', 'Horizontal'), (
        'vertical', 'Vertical')], string="Tab Style (Mobile)", default='horizontal')

    horizontal_tab_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Style 7'),
        ('style_8', 'Style 8'),
        ], string='Tab Style', default='style_1')

    vertical_tab_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Style 7'),
        ('style_8', 'Style 8'),
        ], string='Vertical Tab Style', default='style_1')


    form_element_style = fields.Selection([
        ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Style 7'),
        ('style_8', 'Style 8'),
        ], string='Form Element Style', default='style_1')


    chatter_position = fields.Selection(
        [('normal', 'Normal'), ('sided', 'Sided')], string="Chatter Position", default='normal')


    breadcrumb_style = fields.Selection([
       ('style_1', 'Style 1'),
        ('style_2', 'Style 2'),
        ('style_3', 'Style 3'),
        ('style_4', 'Style 4'),
        ('style_5', 'Style 5'),
        ('style_6', 'Style 6'),
        ('style_7', 'Style 7'),
        ], string='Breadcrumb Style', default='style_1')


    @ api.onchange('body_font_family')
    def onchage_body_font_family(self):
        if self.body_font_family == 'custom_google_font':
            self.is_used_google_font = True
        else:
            self.is_used_google_font = False
            self.body_google_font_family = False


    def action_preview_theme_style(self):
        if self:

            context = dict(self.env.context or {})
            img_src = ""
            if context and context.get('which_style', '') == 'theme':
                img_src = "/sh_backmate_theme/static/src/img/preview/theme/theme_style_img.png"

            if context and context.get('which_style', '') == 'button':
                img_src = "/sh_backmate_theme/static/src/img/preview/button/style_button.png"

            if context and context.get('which_style', '') == 'separator':
                img_src = "/sh_backmate_theme/static/src/img/preview/separator/style_separator.png"

            if context and context.get('which_style', '') == 'sidebar':
                img_src = "/sh_backmate_theme/static/src/img/preview/sidebar/style sidebar.png"

            if context and context.get('which_style', '') == 'login_page':
                img_src = "/sh_backmate_theme/static/src/img/preview/login_page/login_style_preview.png"

            if context and context.get('which_style', '') == 'mobile':
                img_src = "/sh_backmate_theme/static/src/img/preview/mobile_preview.png"

            if context and context.get('which_style', '') == 'checkbox':
                img_src = "/sh_backmate_theme/static/src/img/preview/checkbox_style_preview.png"

            if context and context.get('which_style', '') == 'radio':
                img_src = "/sh_backmate_theme/static/src/img/preview/radio_btn_style_preview.png"

            if context and context.get('which_style', '') == 'scrollbar_style':
                img_src = "/sh_backmate_theme/static/src/img/preview/scrollbar_style_gif.gif"

            if context and context.get('which_style', '') == 'discuss_chatter_style':
                img_src = "/sh_backmate_theme/static/src/img/preview/discuss_chatter/discuss_chatter_preview.png"

            if context and context.get('which_style', '') == 'app_icon_style':
                img_src = "/sh_backmate_theme/static/src/img/preview/app_icon_style.png"

            if context and context.get('which_style', '') == 'backend_all_icon_style':
                img_src = "/sh_backmate_theme/static/src/img/preview/backend_icon_style.png"
            
            if context and context.get('which_style', '') == 'enterprise_svg':
                img_src = "/sh_backmate_theme/static/src/img/preview/enterprise_sidebar_svg_preview.png"

            if context and context.get('which_style', '') == 'loading':
                img_src = "/sh_backmate_theme/static/src/img/preview/loading-gif.gif"

            if context and context.get('which_style', '') == 'predefined_list_view':
                img_src = "/sh_backmate_theme/static/src/img/preview/predefined_list_view_style.png"

            if context and context.get('which_style', '') == 'breadcrumb_style':
                img_src = "/sh_backmate_theme/static/src/img/preview/breadcrumb_style.png"

            if context and context.get('which_style', '') == 'horizontal_tab_style':
                img_src = "/sh_backmate_theme/static/src/img/preview/horizontal_tab.png"
        
            if context and context.get('which_style', '') == 'vertical_tab_style':
                img_src = "/sh_backmate_theme/static/src/img/preview/vertical_tab_style.png"
            
            if context and context.get('which_style', '') == 'form_element_style':
                img_src = "/sh_backmate_theme/static/src/img/preview/form_element_style.png"

            if context and context.get('which_style', '') == 'festival_style':
                img_src = "/sh_backmate_theme/static/src/img/preview/navbar-background-style-gifnew.gif"


            context['default_img_src'] = img_src

            return {
                'name': _('Preview Style'),
                'view_mode': 'form',
                'res_model': 'sh.theme.preview.wizard',
                'view_id': self.env.ref('sh_backmate_theme.sh_back_theme_config_theme_preview_wizard_form').id,
                'type': 'ir.actions.act_window',
                'context': context,
                'target': 'new',
                'flags': {'form': {'action_buttons': False}}
            }





    def action_change_theme_style(self):
        if self:
            return


    @ api.onchange('theme_style')
    def onchage_theme_style(self):

        if self and self.theme_style:
            selected_theme_style_dict = dict_theme_style.get(
                self.theme_style, False)
            if selected_theme_style_dict:
                self.update(selected_theme_style_dict)



    def write(self, vals):
        """
           Write theme settings data in a less file
        """

        res = super(sh_backmate_theme_settings, self).write(vals)
        print("\n\n\n Write is called")
        if self:
            for rec in self:

                content = """
$o-enterprise-color: %s;
$primaryColor:%s;
$primary_hover:%s;
$primary_active:%s;
$gradient_color:%s;
$extra_color:%s;
$secondaryColor:%s;
$secondary_hover:%s;
$secondary_active:%s;
$list_td_th:0.75rem !important;

$header_bg_color:%s;
$header_font_color:%s;
$header_hover_color:%s;
$header_active_color:%s;

$h1_color:%s;
$h2_color:%s;
$h3_color:%s;
$h4_color:%s;
$h5_color:%s;
$h6_color:%s;
$p_color:%s;

$h1_size:%spx;
$h2_size:%spx;
$h3_size:%spx;
$h4_size:%spx;
$h5_size:%spx;
$h6_size:%spx;
$p_size:%spx;

$body_font_color:%s;
$body_background_type:%s;
$body_background_color:%s;
$body_font_family:%s;

$button_style:%s;
$o-mail-attachment-image-size: 100px !default;


$sidebar_background_type:%s;
$sidebar_bg_color:%s;
$sidebar_bg_additional_color:%s;
$sidebar_font_color:%s;
$sidebar_font_hover_color:%s;
$sidebar_font_hover_bg_color:%s;
$sidebar_style:%s;

$separator_style:%s;
$separator_color:%s;

$o-community-color:%s;
$o-tooltip-background-color:%s;
$o-brand-secondary:%s;
$o-brand-odoo: $o-community-color;
$o-brand-primary: $o-community-color;

$is_button_with_icon_text:%s;

$body_google_font_family:%s;
$is_used_google_font:%s;

$predefined_list_view_boolean:%s;
$predefined_list_view_style:%s;
$list_view_border:%s;
$list_view_is_hover_row:%s;
$list_view_hover_bg_color:%s;
$list_view_even_row_color:%s;
$list_view_odd_row_color:%s;

$login_page_style: %s;
$login_page_background_type: %s;
$login_page_background_color:%s;
$login_page_box_color:%s;
$theme_style: %s;

$is_sticky_form:%s;
$is_sticky_chatter:%s;
$is_sticky_list:%s;
$is_sticky_list_inside_form:%s;
$is_sticky_pivot:%s;

$modal_popup_style:%s;
$mobile_icon_style:%s;
$checkbox_style:%s;
$radio_style:%s;
$scrollbar_style:%s;
$discuss_chatter_style:%s;
$app_icon_style:%s;
$backend_all_icon_style:%s;
$dual_tone_icon_color_1:%s;
$dual_tone_icon_color_2:%s;

$sidebar_color_1:%s;
$sidebar_img:%s;
$tab_style:%s;
$tab_style_mobile:%s;
$horizontal_tab_style:%s;
$vertical_tab_style:%s;
$form_element_style:%s;
$chatter_position:%s;
$breadcrumb_style:%s;
$loading_style:%s;
$progress_style:%s;
$progress_height:%s;
$progress_color:%s;
$festival_style:%s;


                """ % (

                    rec.primary_color,
                    rec.primary_color,
                    rec.primary_hover,
                    rec.primary_active,
                    rec.gradient_color,
                    rec.extra_color,

                    rec.secondary_color,
                    rec.secondary_hover,
                    rec.secondary_active,

                    rec.header_background_color,
                    rec.header_font_color,
                    rec.header_hover_color,
                    rec.header_active_color,


                    rec.h1_color,
                    rec.h2_color,
                    rec.h3_color,
                    rec.h4_color,
                    rec.h5_color,
                    rec.h6_color,
                    rec.p_color,


                    rec.h1_size,
                    rec.h2_size,
                    rec.h3_size,
                    rec.h4_size,
                    rec.h5_size,
                    rec.h6_size,
                    rec.p_size,

                    rec.body_font_color,
                    rec.body_background_type,
                    rec.body_background_color,
                    rec.body_font_family,

                    rec.button_style,


                    rec.sidebar_background_type,
                    rec.sidebar_background_color,
                    rec.sidebar_background_additional_color,
                    rec.sidebar_font_color,
                    rec.sidebar_font_hover_color,
                    rec.sidebar_font_hover_background_color,
                    rec.sidebar_style,

                    rec.separator_style,
                    rec.separator_color,

                    rec.primary_color,
                    rec.primary_color,
                    rec.secondary_color,
                    rec.is_button_with_icon_text,

                    rec.body_google_font_family,
                    rec.is_used_google_font,

                    rec.predefined_list_view_boolean,
                    rec.predefined_list_view_style,
                    rec.list_view_border,
                    rec.list_view_is_hover_row,
                    rec.list_view_hover_bg_color,
                    rec.list_view_even_row_color,
                    rec.list_view_odd_row_color,

                    rec.login_page_style,
                    rec.login_page_background_type,
                    rec.login_page_background_color,
                    rec.login_page_box_color,
                    rec.theme_style,

                    rec.is_sticky_form,
                    rec.is_sticky_chatter,
                    rec.is_sticky_list,
                    rec.is_sticky_list_inside_form,
                    rec.is_sticky_pivot,

                    rec.modal_popup_style,
                    rec.mobile_icon_style,
                    rec.checkbox_style,
                    rec.radio_style,
                    rec.scrollbar_style,
                    rec.discuss_chatter_style,
                    rec.app_icon_style,
                    rec.backend_all_icon_style,
                    rec.dual_tone_icon_color_1,
                    rec.dual_tone_icon_color_2,

                    rec.sidebar_color_1,
                    rec.sidebar_img,
                    rec.tab_style,
                    rec.tab_style_mobile,
                    rec.horizontal_tab_style,
                    rec.vertical_tab_style,
                    rec.form_element_style,
                    rec.chatter_position,
                    rec.breadcrumb_style,
                    rec.loading_style,
                    rec.progress_style,
                    rec.progress_height,
                    rec.progress_color,
                    rec.festival_style,
                       )



                IrAttachment = self.env["ir.attachment"]
                # search default attachment by url that will created when app installed...
                url = "/sh_backmate_theme/static/src/scss/back_theme_config_main_scss.scss"

                search_attachment = IrAttachment.sudo().search([
                    ('url', '=', url),
                    ], limit=1)


                # Check if the file to save had already been modified
                datas = base64.b64encode((content or "\n").encode("utf-8"))
                print("\n\n\n search_attachment",search_attachment,content)
                if search_attachment:
                    # If it was already modified, simply override the corresponding attachment content
                    if 'website_id' in search_attachment._fields:
                        search_attachment.sudo().write({"website_id": False})
                    search_attachment.sudo().write({"datas": datas})

                else:
                    # If not, create a new attachment
                    new_attach = {
                        "name": "Back Theme Settings scss File",
                        "type": "binary",
                        "mimetype": "text/scss",
                        "datas": datas,
                        "url": url,
                        "public": True,
                        "res_model": "ir.ui.view",
                    }

                    IrAttachment.sudo().create(new_attach)


                # clear the catch to applied our new theme effects.
                self.env["ir.qweb"].clear_caches()

        return res