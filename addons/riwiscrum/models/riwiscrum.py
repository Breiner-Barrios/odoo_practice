from odoo import models, fields

class Riwiscrum(models.Model):
    _name = 'riwiscrum'
    _description = 'Riwiscrum'

    name = fields.Char(
        string='Nombre',
        required=True
    )

    status = fields.Selection(
        [
            ("draft", "Borrador"),
            ("review", "En revisión"),
            ("running", "En ejecución"),
            ("paused", "Pausado"),
            ("accepted", "Aceptado"),
            ("refused", "Rechazado"),
            ("cancel", "Cancelado"),
        ],
        string="Estado",
        required=True,
        readonly=True,
        default="draft"
    )

    required_by = fields.Many2one(
        "res.users",
        string="Solicitado por",
        required=True
    )

    active = fields.Boolean(
        string='Activo',
        default=True
    )


    

