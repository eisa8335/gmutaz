$(document).ready(function () {

    $(document).on("click", ".app_drawer_overlay_background", function (ev) {
        if($(ev.target).is('.app_drawer_overlay_background')){
            $('.app_drawer_layout').removeClass('sh_theme_model');
            $('.o_web_client').removeClass('sh_overlay_app_drawer');
        }
    });
    $(document).on("click", ".sh_close_notification", function () {
        $("#object").css("display", "none");
        $("#object1").css("display", "none");
    });
   
    $('.o_web_client').on('click', ".o_action_manager", function (ev) {

         //$('.sh_search_results').css("display","none");
         $('.backmate_theme_layout').removeClass("sh_theme_model");
         $('.todo_layout').removeClass("sh_theme_model");
         if ($('.sh_calc_util').hasClass('active')) {
             $('.open_calc').click();
         }
         //	$('.o_action_manager').css("margin-right","0px")
         $('.sh_search_results').css("display", "none");

         if($('.sh_user_language_list_cls').css("display") != 'none'){
            $('.sh_user_language_list_cls').css("display","none")
         }
         if($('.sh_wqm_quick_menu_submenu_list_cls').css("display") != 'none'){
            $('.sh_wqm_quick_menu_submenu_list_cls').css("display","none")
         }

         if($('.sh_calc_util').hasClass("active")){
            $('.sh_calc_util').removeClass("active")
         }
         
    });
    
    $(document).on("click", ".sh_close_notification", function () {
        $("#object").css("display", "none");
        $("#object1").css("display", "none");
    });




    $('body').keydown(function (e) {
        if ($("body").hasClass("sh_sidebar_background_enterprise")) {
            $(".sh_search_container").css("display", "block");
            $(".usermenu_search_input").focus();
            $(".sh_backmate_theme_appmenu_div").css("opacity", "0")
            if(!$("body").hasClass("sh_detect_first_keydown")){
                $(".usermenu_search_input").keydown()
            }
         
        }
    });

});