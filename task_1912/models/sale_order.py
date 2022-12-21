from odoo import fields,models,api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    preferred_time = fields.Many2one("preferred.time",string="Preferred Time")

    @api.model
    def update_preffered_time(self,arg):
        print ("dsssssssssssssssssssssssssss",self,arg)
        sale = self.browse(arg[1]).preferred_time = arg[0]


    # @api.onchange('partner_id')
    # def abcd(self):
    #     for rec in self.order_line:
    #         print("......................................",rec.id)



