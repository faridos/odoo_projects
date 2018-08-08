from odoo import models, fields, api

class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    
    instructor_id = fields.Many2one('res.partner', string="Instructor", domain=['|', ('is_instructor', '=', True),
                     ('category_id.name', 'ilike', "Teacher")])
    course_id = fields.Many2one('openacademy.course', string="Course",ondelete='cascade',required=True)
    
    attendee_ids = fields.One2many('openacademy.attendee', 'session_id',string="Attendees")
    
    taken_seats = fields.Float(compute="_taken_seats",string='Taken seats', store=True)
#     
#
    @api.depends('seats','attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats=0.0
                
            else:
                r.taken_seats=100.0 * len(r.attendee_ids)/ r.seats
    