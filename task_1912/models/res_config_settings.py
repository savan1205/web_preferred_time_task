from odoo import api,fields,models

class ResConfigSettings(models.TransientModel):
   _inherit = 'res.config.settings'

   preferred_time = fields.Boolean(related="company_id.preferred_time",config_parameter="task_1912.preferred_time",string="Preferred Time",readonly=False)

class Company(models.Model):
   _inherit="res.company"

   preferred_time = fields.Boolean(string="Preferred Time")



