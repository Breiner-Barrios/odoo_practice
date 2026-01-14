from odoo import models, fields

class Modulopython(models.Model):
    _name = 'modulo.python'
    _description = 'modulo python'

    name = fields.Char(string='Nombre', required=True)
    active = fields.Boolean(string='Activo', default=True)
