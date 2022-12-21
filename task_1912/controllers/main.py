from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers import main


# class WebsiteSaleInherit(main.WebsiteSale):

    # @http.route(['/shop/cart'], type='http', auth="public", website=True, sitemap=False)
    # def cart(self, access_token=None, revive='', **post):
    # # def checkout_values(self, **kw):
    #     res = super(WebsiteSaleInherit, self).cart(**post)
    #     show_preferred_time = request.env['ir.config_parameter'].sudo().get_param('task_1912.preferred_time')
    #     res.qcontext['show_preferred_time'] = show_preferred_time
    #     order = request.website.sale_get_order()
    #     # print("==========================================",post,order)
    #     return res


    # @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True)
    # def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
    #     res = super(WebsiteSaleInherit,self).cart_update(product_id, **kw)
    #     # print("111111111111111111111111111111111111111",kw)
    #     return res

    # @http.route(['/shop/cart/update_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    # def cart_update_json(self, product_id, line_id=None, add_qty=None, set_qty=None, display=True, **kw):
    #     res = super(WebsiteSaleInherit,self).cart_update_json(product_id,line_id,add_qty,set_qty,display,**kw)
    #     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", request.session['sale_order_id'],"+++",kw)
    #     # res.update({
    #     #     'preferred_time':order
    #     # })
    #     return res
    # @http.route('/shop/payment', type='http', auth='public', website=True, sitemap=False)
    # def shop_payment(self, **post):
    #     res = super(WebsiteSaleInherit, self).shop_payment(**post)
    #     # print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",post)
    #     return res