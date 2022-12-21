from odoo import fields,models


class Picking(models.Model):
    _inherit = "stock.picking"

    preferred_time = fields.Many2one("preferred.time",related="sale_id.preferred_time",string="Preferred Time")