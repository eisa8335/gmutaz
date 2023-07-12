# Part of Softhealer Technologies.
import json
from odoo import http
from odoo.http import request
import base64
from io import BytesIO
from odoo.tools.misc import file_open
from datetime import datetime
from odoo.tools.safe_eval import safe_eval

class Main(http.Controller):

    @http.route('/firebase-messaging-sw.js', type='http', auth="public")
    def sw_http(self):
        if request.env.company and request.env.company.enable_web_push_notification:
            config_obj = request.env.company.config_details
            
            js = """
            this.addEventListener('install', function(e) {
         e.waitUntil(
           caches.open('video-store').then(function(cache) {
             return cache.addAll([
                 '/sh_backmate_theme/static/index.js'
             ]);
           })
         );
        });
        
        this.addEventListener('fetch', function(e) {
          e.respondWith(
            caches.match(e.request).then(function(response) {
              return response || fetch(e.request);
            })
          );
        });
            importScripts('https://www.gstatic.com/firebasejs/8.4.2/firebase-app.js');
            importScripts('https://www.gstatic.com/firebasejs/8.4.2/firebase-messaging.js');
            var firebaseConfig =
            """+ config_obj +""" ;
            firebase.initializeApp(firebaseConfig);
    
            const messaging = firebase.messaging();
    
            messaging.setBackgroundMessageHandler(function(payload) {
            const notificationTitle = "Background Message Title";
            const notificationOptions = {
                body: payload.notification.body,
                icon:'https://i.pinimg.com/originals/3f/77/56/3f7756330cd418e46e642254a900a507.jpg',
            };
            return self.registration.showNotification(
                notificationTitle,
                notificationOptions,
            );
            });
    
            """
            return http.request.make_response(js, [('Content-Type', 'text/javascript')])
        else:
            
            js = """
           this.addEventListener('install', function(e) {
         e.waitUntil(
           caches.open('video-store').then(function(cache) {
             return cache.addAll([
                 '/sh_backmate_theme/static/index.js'
             ]);
           })
         );
        });
        
        this.addEventListener('fetch', function(e) {
          e.respondWith(
            caches.match(e.request).then(function(response) {
              return response || fetch(e.request);
            })
          );
        });
    
            """
            return http.request.make_response(js, [('Content-Type', 'text/javascript')])
        
    @http.route('/web/push_token', type='http', auth="public", csrf=False)
    def getToken(self,**post):
        device_search = request.env['sh.push.notification'].sudo().search(
            [('register_id', '=', post.get('name'))], limit=1)
        
        if device_search and not request.env.user._is_public() and device_search.user_id != request.env.user.id:
            if request.env.user.has_group('base.group_portal'):
                device_search.write({'user_id':request.env.user.id,'user_type':'portal'})
            elif request.env.user:
                device_search.write({'user_id':request.env.user.id,'user_type':'internal'})
                
        if not device_search:
            vals = {
                'register_id' : post.get('name'),
                'datetime' : datetime.now()
            }
            print("\n\n\n\n self.env.user.has_group('base.group_portal')",request.env.user.has_group('base.group_portal'))
            if request.env.user._is_public():
                public_users = request.env['res.users'].sudo()
                public_groups = request.env.ref("base.group_public", raise_if_not_found=False)
                if public_groups:
                    public_users = public_groups.sudo().with_context(active_test=False).mapped("users")
                    if public_users:
                        vals.update({'user_id':public_users[0].id,'user_type':'public'})
            elif request.env.user.has_group('base.group_portal'):
                vals.update({'user_id':request.env.user.id,'user_type':'portal'})
            elif request.env.user:
                vals.update({'user_id':request.env.user.id,'user_type':'internal'})
            
            request.env['sh.push.notification'].sudo().create(vals)

    @http.route('/web/_config', type='json', auth="public")
    def sendConfig(self):

        config_vals = {}
        if request.env.company and request.env.company.enable_web_push_notification:

            config_obj = request.env.company.config_details.replace(" ","")
            config_obj = request.env.company.config_details.replace("\n","").replace("\t","").replace(" ","").replace("\"","'").replace('apiKey','\'apiKey\'').replace('authDomain','\'authDomain\'').replace('projectId','\'projectId\'').replace('storageBucket','\'storageBucket\'').replace('messagingSenderId','\'messagingSenderId\'').replace('appId','\'appId\'').replace('measurementId','\'measurementId\'')

            config_vals['apiKey'] = safe_eval(config_obj)['apiKey']
            config_vals['authDomain'] =  safe_eval(config_obj)['authDomain']
            config_vals['projectId'] =  safe_eval(config_obj)['projectId']
            config_vals['storageBucket'] =  safe_eval(config_obj)['storageBucket']
            config_vals['messagingSenderId'] = safe_eval(config_obj)['messagingSenderId']
            config_vals['appId'] = safe_eval(config_obj)['appId']
            config_vals['measurementId'] =  safe_eval(config_obj)['measurementId']
            
            vals = {
                'vapid' : request.env.company.vapid,
                'config':   config_vals
            }
            print(vals)
            json_vals = json.dumps(vals)
            return json_vals
               

    def _get_manifest_json(self, company):
        if not company:
            company = 1
        pwa_config = http.request.env['sh.pwa.config'].sudo().search(
            [('company_id', '=', int(company))], limit=1)
        vals = {
            "name": "Softhealer-APP",
            "short_name": "SH-APP",
            "scope": "/",
            "start_url": "/web",
            "background_color": "purple",
            "display": "standalone",
        }
        if pwa_config:
            if pwa_config.name:
                vals.update({'name': pwa_config.name})
            if pwa_config.short_name:
                vals.update({'short_name': pwa_config.short_name})
            if pwa_config.theme_color:
                vals.update({'theme_color': pwa_config.theme_color})
            if pwa_config.background_color:
                vals.update({'background_color': pwa_config.background_color})
            if pwa_config.display:
                vals.update({'display': pwa_config.display})
            if pwa_config.orientation:
                vals.update({'orientation': pwa_config.orientation})

            default_icon_list = []
            if pwa_config.icon_small and pwa_config.icon_small_mimetype and pwa_config.icon_small_size:
                default_icon_list.append({
                    'src': '/sh_backmate_theme/pwa_icon_small/'+str(company),
                    'type': pwa_config.icon_small_mimetype,
                    'sizes': pwa_config.icon_small_size
                })
            if pwa_config.icon and pwa_config.icon_mimetype and pwa_config.icon_size:
                default_icon_list.append({
                    'src': '/sh_backmate_theme/pwa_icon/'+str(company),
                    'type': pwa_config.icon_mimetype,
                    'sizes': pwa_config.icon_size
                })

            if len(default_icon_list) == 0:
                default_icon_list = [
                    {
                        "src": "/sh_backmate_theme/static/icon/sh.png",
                        "sizes": "192x192",
                        "type": "image/png"
                    }
                ]

            vals.update({'icons': default_icon_list})

        return vals

    @http.route('/manifest.json/<string:cid>', type='http', auth="public")
    def manifest_http(self, **post):
        company = post.get('cid')
        print("\n\n\n ================",company)
        return json.dumps(self._get_manifest_json(company))


    def get_icon(self, field_icon, company):
        pwa_config = http.request.env['sh.pwa.config'].sudo().search(
            [('company_id', '=', int(company))], limit=1)
        if pwa_config:
            icon = pwa_config.icon
            if field_icon == 'icon_small':
                icon = pwa_config.icon_small

            icon_mimetype = getattr(pwa_config, field_icon + '_mimetype')
            if icon:
                icon = BytesIO(base64.b64decode(icon))
            return http.request.make_response(
                icon.read(), [('Content-Type', icon_mimetype)])

    @http.route('/sh_backmate_theme/pwa_icon/<string:cid>', type='http', auth="none")
    def icon_small(self, **post):
        company = post.get('cid')
        return self.get_icon('icon', company)

    @http.route('/sh_backmate_theme/pwa_icon_small/<string:cid>', type='http', auth="none")
    def icon(self, **post):
        company = post.get('cid')
        return self.get_icon('icon_small', company)


    @http.route('/iphone.json/<string:cid>', type='http', auth="public")
    def iphone_http(self,**post):
        company = post.get('cid')
        pwa_config = http.request.env['sh.pwa.config'].sudo().search([('company_id','=',int(company))] , limit=1)
        if pwa_config:
            icon = pwa_config.icon_iphone
            icon_mimetype = getattr(pwa_config, 'icon' + '_mimetype')
            if icon:
                icon = BytesIO(base64.b64decode(icon))
                return http.request.make_response(
                    icon.read(), [('Content-Type', icon_mimetype)])

