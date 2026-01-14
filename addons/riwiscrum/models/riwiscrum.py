from odoo import models, fields

class Riwiscrum(models.Model):
    _name = 'riwiscrum'
    _description = 'riwiscrum'

    name = fields.Char(string='Nombre', required=True)

    status = fields.Selection(
        [
            ("draft","Borrador"),
            ("review","En revisión"),
            ("running","En ejecución"),
            ("paused","Pausado"),
            ("accepted","Aceptado"),
            ("refused","Rechazado"),
            ("cancel","Cancelado"),
            
        ],
        string="Estado",
        required=True,
        readonly=True,
        default="draft"
    )

    required_by = fields.Many2one("res.users",string="Solicitado por", required=False)
    accepted_by = fields.Many2one("res.users",string="Aceptado por", required=False)
    active = fields.Boolean(string='Activo', default=True)

    def pasar_a_revision(self):
        for record in self:
            record.status = "review"
