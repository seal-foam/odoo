from odoo import api, fields, models


class Production(models.Model):
    _inherit = "mrp.production"

    effective_date = fields.Datetime(
        string="Fecha de transferencia",
        compute="_compute_effective_date"
    )
    suaje_id = fields.Many2one(comodel_name="product.template", related="bom_id.x_suaje", string="Suaje")

    @api.depends("location_src_id", "picking_ids.date_done", "picking_ids.location_dest_id")
    def _compute_effective_date(self):
        for record in self:
            record.effective_date = fields.first(
                record.picking_ids.filtered(lambda s: s.location_dest_id == record.location_src_id)
            ).date_done
