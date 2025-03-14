from odoo import api, fields, models


class Production(models.Model):
    _inherit = "mrp.production"

    effective_date = fields.Datetime(
        string="Fecha de transferencia",
        compute="_compute_effective_date"
    )

    @api.depends("location_src_id", "picking_ids")
    def _compute_effective_date(self):
        for record in self:
            record.effective_date = fields.first(
                record.picking_ids.filtered(lambda s: s.location_dest_id == record.location_src_id)
            ).date_done
