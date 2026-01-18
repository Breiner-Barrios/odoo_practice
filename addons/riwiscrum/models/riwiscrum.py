from odoo import models, fields, api, _

class Riwiscrum(models.Model):
    _name = 'riwiscrum'
    _description = 'riwiscrum'

    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string='Project ID', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    user_id = fields.Many2one('res.users', string='Responsable', default=lambda self: self.env.user)
    
    # Relación con las líneas de tarea
    line_ids = fields.One2many('riwiscrum.line', 'riwiscrum_id', string='Tareas')

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
    
    #los campos del form
    required_by = fields.Many2one("res.users", string="Solicitado por", required=False)
    accepted_by = fields.Many2one("res.users", string="Aceptado por", required=False)
    active = fields.Boolean(string='Activo', default=True)

    fecha_review = fields.Datetime("Fecha a review", readonly=True)
    fecha_running = fields.Datetime("Fecha a ejecución", readonly=True)
    fecha_paused = fields.Datetime("Fecha a pausa", readonly=True)
    fecha_accepted = fields.Datetime("Fecha a aceptado", readonly=True)
    fecha_refused = fields.Datetime("Fecha a rechazado", readonly=True)
    fecha_cancel = fields.Datetime("Fecha a cancelado", readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('riwiscrum.sequence') or _('New')
        result = super(Riwiscrum, self).create(vals)
        return result

    # Métodos de cambio de estado
    def pasar_review(self):
        for record in self:
            if record.status != "review":
                record.status = "review"
                record.fecha_review = fields.Datetime.now()
            
    def reset_to_draft(self):
        for record in self:
            if record.status != "draft":
                record.status = "draft"

    def pasar_running(self):
        for record in self:
            if record.status != "running":
                record.status = "running"
                record.fecha_running = fields.Datetime.now()

    def pasar_paused(self):
        for record in self:
            if record.status != "paused":
                record.status = "paused"
                record.fecha_paused = fields.Datetime.now()

    def pasar_accepted(self):
        for record in self:
            if record.status != "accepted":
                record.status = "accepted"
                record.fecha_accepted = fields.Datetime.now()

    def pasar_refused(self):
        for record in self:
            if record.status != "refused":
                record.status = "refused"
                record.fecha_refused = fields.Datetime.now()

    def pasar_cancel(self):
        for record in self:
            if record.status != "cancel":
                record.status = "cancel"
                record.fecha_cancel = fields.Datetime.now()