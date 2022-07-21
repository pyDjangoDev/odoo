from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.estate.property.tag"
    _description = "Tag characterize esate properties"

    name = fields.Char(required=True)
