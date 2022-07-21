from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.estate.property.type"
    _description = "The Type of Esate property"

    name = fields.Char(required=True)
