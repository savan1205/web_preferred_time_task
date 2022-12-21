from odoo import fields,models

class PreferredTime(models.Model):
    _name = "preferred.time"
    _description = "preferred time"

    name = fields.Char(string = "preferred time")
