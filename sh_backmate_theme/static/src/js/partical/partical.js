odoo.define("sh_backmate_theme.festive_style", function (require) {
    $(document).ready(function () {
        const myTimeout = setTimeout(myGreeting, 1000);

        var rpc = require("web.rpc");
        var festival_style = 'default';

        rpc.query({
        model: 'sh.back.theme.config.settings',
        method: 'search_read',
        domain: [['id', '=', 1]],
        fields: ['festival_style']
        }).then(function (data) {
            if (data) {
                festival_style = data[0]['festival_style']
            
            }
        });




        function myGreeting() {
            console.log("-----------222--------", $('#particles-js'));

                if(festival_style == 'christmas'){
                    particlesJS("particles-js", {"particles":{"number":{"value":600,"density":{"enable":true,"value_area":1000}},"color":{"value":"#fff"},"shape":{"type":"circle","stroke":{"width":0,"color":"#000000"},"polygon":{"nb_sides":5},"image":{"src":"https://i.ibb.co/R6m6820/Odoo-Contacts.png","width":100,"height":100}},"opacity":{"value":1,"random":true,"anim":{"enable":false,"speed":8.851641614084663,"opacity_min":0.89,"sync":true}},"size":{"value":5,"random":true,"anim":{"enable":false,"speed":40,"size_min":0.1,"sync":false}},"line_linked":{"enable":false,"distance":500,"color":"#ffffff","opacity":0.4,"width":2},"move":{"enable":true,"speed":2,"direction":"bottom","random":false,"straight":false,"out_mode":"out","bounce":false,"attract":{"enable":false,"rotateX":600,"rotateY":1200}}},"interactivity":{"detect_on":"canvas","events":{"onhover":{"enable":true,"mode":"bubble"},"onclick":{"enable":true,"mode":"repulse"},"resize":true},"modes":{"grab":{"distance":400,"line_linked":{"opacity":0.5}},"bubble":{"distance":400,"size":4,"duration":0.3,"opacity":1,"speed":3},"repulse":{"distance":200,"duration":0.4},"push":{"particles_nb":4},"remove":{"particles_nb":2}}},"retina_detect":true});

                }else if(festival_style == 'new_year'){

                }else{
                    
                }

               
        }
    });

});