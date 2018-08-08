from odoo import models, fields, api
from mako.runtime import _inherit_from

class Partner(models.Model):
    ''' Inherited res.partner''' 
    _inherit = 'res.partner'
    is_instructor = fields.Boolean('IS Instructor', default=False)
    session_ids = fields.Many2many('openacademy.session',
        string="Attended Sessions", readonly=True)