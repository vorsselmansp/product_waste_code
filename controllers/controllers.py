# -*- coding: utf-8 -*-

from odoo import http


class ProductWasteCode(http.Controller):
     @http.route('/product_waste_code/product_waste_code', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/product_waste_code/product_waste_code/objects', auth='public')
     def list(self, **kw):
        return http.request.render('product_waste_code.listing', {
            'root': '/product_waste_code/product_waste_code',
            'objects': http.request.env['product_waste_code.product_waste_code'].search([]),
        })

     @http.route('/product_waste_code/product_waste_code/objects/<model("product_waste_code.product_waste_code"):obj>', auth='public')
     def object(self, obj, **kw):
        return http.request.render('product_waste_code.object', {
            'object': obj
        })