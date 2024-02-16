from . import agency
from odoo import models, fields

class Vehicle(models.Model):
    _name = 'agency.vehicle'
    _description = 'Information about the Agency Vehicle'

    capacity = fields.Integer(string='Capacity')
    registration = fields.Char(string='Registration Number')

class Travel(models.Model):
    _name = 'agency.travel'
    _description = 'Information about the Travel'

    origin = fields.Char(string='Origin')
    destination = fields.Char(string='Destination')
    vehicle = fields.Many2one('agency.vehicle', string='Vehicle')
    datetime = fields.Datetime(string='Datetime')
    traveller = fields.Many2many('agency.traveller', string='Traveller')
    price = fields.Float(string='Price')
    travel_id = fields.Many2one('agency.travel', string='Travel ID')

class Driver(models.Model):
    _name = 'agency.driver'
    _description = 'Information about the Agency Driver'

    documentation = fields.Char(string='Documentation')
    license = fields.Char(string='License')
    vehicle = fields.Many2many('agency.vehicle', string='Vehicle')
    travel = fields.One2many('agency.travel', 'travel_id', string='Travel')

class Traveller(models.Model):
    _name = 'agency.traveller'
    _description = 'Information about the Clients'

    name = fields.Char(string='Name')
    surname = fields.Char(string='Surname')
    documentation = fields.Char(string='Documentation')
    travel = fields.Many2many('agency.travel', string='Travel')
