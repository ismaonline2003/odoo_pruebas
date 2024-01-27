from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    pasaporte = fields.Char(string="Pasaporte")