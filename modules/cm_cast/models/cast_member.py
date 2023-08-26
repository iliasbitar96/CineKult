from odoo import models, fields, api


class CastMember(models.Model):
    _name = 'cast.member'
    _description = 'All cast members'
    
    name = fields.Char('name')
    firstname = fields.Char('First name')
    lastname = fields.Char('Last name')
    movie_ids = fields.Many2many('movie', string='Movies')
    member_type = fields.Selection([('actor', 'Actor'), ('director', 'Director'), ('production', 'Production Company')])

    @api.onchange('firstname', 'lastname')
    def onchange_name(self):
        for record in self:
            record.name = record.firstname + ' ' + record.lastname
