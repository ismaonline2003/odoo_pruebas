from odoo import models, fields, exceptions

class Prueba(models.Model):
    _name = "prueba"

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")
    nro_intentos = fields.Integer(string="Número de Intentos")
    porcentaje_exito = fields.Float(string="Porcentaje de Exito")
    fue_exitoso = fields.Boolean(string="Fue exitoso?")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Contacto")
    #Many2one
    #One2many
    #Many2many

    def hola_mundo(self):
        print('Hola Mundo')
        raise exceptions.UserError("Hola Mundo.")
