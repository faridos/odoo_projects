from odoo import models, fields, api

class Attendee(models.Model):
    _name = 'openacademy.attendee'

    name = fields.Char()
    partner_id = fields.Many2one('res.partner', string="Partner"
                ,required=True
                  , ondelete='cascade'
                 )
    session_id = fields.Many2one('openacademy.session', string="Session",
                 required=True, ondelete='cascade')