from odoo import api, models
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            default_code = vals.get("default_code", False)
            if not default_code:
                continue
            if self.search_count([("default_code", "=", default_code)]) > 0:
                raise UserError(f"La referencia interna '{default_code}' ya existe.")
        return super().create(vals_list)

    def write(self, vals):
        default_code = vals.get("default_code", False)
        if default_code:
            for tmpl in self:
                if self.search_count([("default_code", "=", default_code), ("id", "!=", tmpl.id)]) > 0:
                    raise UserError(f"La referencia interna '{default_code}' ya existe.")
        return super().write(vals)
