from odoo import models, fields

class Segundaprueba(models.Model):
    _name = 'segunda.prueba'
    _description = 'segunda prueba'

    name = fields.Char(string='Nombre', required=True)
    active = fields.Boolean(string='Activo', default=True)
