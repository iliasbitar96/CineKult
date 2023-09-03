from odoo import models, fields, api


class CastMember(models.Model):
    _name = 'cast.member'
    _description = 'All cast members'
    
    name = fields.Char('name')
    firstname = fields.Char('First name')
    lastname = fields.Char('Last name')
    movie_ids = fields.Many2many('movie', string='Movies')
    member_type = fields.Selection([('actor', 'Actor'), ('director', 'Director'), ('production', 'Production Company')])

    def write(self, vals):
        firstname = self.firstname
        lastname = self.lastname
        if vals.get('firstname'):
            firstname = vals.get('firstname')
        if vals.get('lastname'):
            lastname = vals.get('lastname')
        if self.lastname and self.firstname:
            vals['name'] = firstname + ' ' + lastname
        return super().write(vals)

    # @api.onchange('lastname', 'firstname')
    # def onchange_name(self):
    #     for record in self:
    #         if record.firstname and record.lastname:
    #             record.name = record.firstname + ' ' + record.lastname
