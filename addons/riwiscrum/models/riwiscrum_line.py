from odoo import models, fields, api, _

class RiwiscrumLine(models.Model):
    _name = 'riwiscrum.line'
    _description = 'Líneas de Tarea Riwiscrum'

    riwiscrum_id = fields.Many2one('riwiscrum', string='Referencia Riwiscrum', ondelete='cascade')
    code = fields.Char(string='Task ID', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    
    tipo_tarea = fields.Selection([
        ('back', 'Back'),
        ('front', 'Front'),
        ('cicd', 'CI/CD'),
        ('cloud', 'Cloud Inf.'),
        ('db', 'DB'),
        ('analisis', 'Análisis DD')
    ], string='Tipo de Tarea')
    
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')
    
    status = fields.Selection([
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], string='Status', default='todo')
    
    asignado_a_ids = fields.Many2many('res.users', string='Asignado a')
    
    prioridad = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta')
    ], string='Prioridad', default='1')
    
    descripcion = fields.Text(string='Descripción')
    tiempo_estimado = fields.Float(string='Tiempo Estimado (Horas)')

    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('riwiscrum.task.sequence') or _('New')
        result = super(RiwiscrumLine, self).create(vals)
        return result