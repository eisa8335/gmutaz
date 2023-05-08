/** @odoo-module **/

import { registry } from "@web/core/registry";
import core from 'web.core';
import { qweb } from 'web.core';
import { useListener } from "@web/core/utils/hooks";

 const { Component,useExternalListener,useEffect } = owl;

export class KsImageWidget extends Component{

    setup(){
        this.props.ksSelectedIcon = false
        //     this.props.ks_default_icon="bar-chart"
        this.props.ks_icon_set = ['home', 'puzzle-piece', 'clock-o', 'comments-o', 'car', 'calendar', 'calendar-times-o', 'bar-chart', 'commenting-o', 'star-half-o', 'address-book-o', 'tachometer', 'search', 'money', 'line-chart', 'area-chart', 'pie-chart', 'check-square-o', 'users', 'shopping-cart', 'truck', 'user-circle-o', 'user-plus', 'sun-o', 'paper-plane', 'rss', 'gears', 'check', 'book'];
        var ks_self = this.props;
        var url = this.placeholder;
        useExternalListener(document, 'click', this.document_event);
    }

    document_event(event) {
        if (event.path[0].classList[0]==='fa' && event.path.length==11){
            if (event.path[0].classList[1].split('-').length < 3){
                this.props.update(event.path[0].classList[1].split('-')[1]);
            }
            else{
                var value = event.path[0].classList[1].split('-')[1] + '-' + event.path[0].classList[1].split('-')[2]
                this.props.update(value);
            }
        }
        else if ($(event.path[0])[0].innerHTML == 'Close'&& event.path.length==9){
            this.modal.hide();
        }
        else if ([...event.path[0].classList].includes('fa-trash-o')){
            this.props.update('');
        }

    }

     ks_image_widget_icon_container(ev){
         this.props.ks_icon_set = ['home', 'puzzle-piece', 'clock-o', 'comments-o', 'car', 'calendar', 'calendar-times-o', 'bar-chart', 'commenting-o', 'star-half-o', 'address-book-o', 'tachometer', 'search', 'money', 'line-chart', 'area-chart', 'pie-chart', 'check-square-o', 'users', 'shopping-cart', 'truck', 'user-circle-o', 'user-plus', 'sun-o', 'paper-plane', 'rss', 'gears', 'check', 'book']
         var $modal=$(qweb.render("ks_icon_container_modal_template",{ ks_fa_icons_set: this.props.ks_icon_set}));
         const modal_new=new Modal($modal[0]);
         this.modal = modal_new;
         modal_new.show();
     }
}
KsImageWidget.template="image_widget";
KsImageWidget.supportedTypes = ["char"];
registry.category("fields").add("ks_image_widget",KsImageWidget);
