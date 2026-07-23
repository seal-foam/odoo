from odoo import api, models


class UomUom(models.Model):
    _inherit = "uom.uom"

    @api.model
    def _can_view_uom_form(self):
        return self.env.user.has_group("drs_uom_visibility.group_view_uom")

    @api.model
    def _get_view_cache_key(self, view_id=None, view_type="form", **options):
        key = super()._get_view_cache_key(view_id, view_type, **options)
        if view_type == "form":
            key += (self._can_view_uom_form(),)
        return key

    @api.model
    def _get_view(self, view_id=None, view_type="form", **options):
        if view_type == "form" and not self._can_view_uom_form():
            view = self.env.ref(
                "drs_uom_visibility.uom_uom_no_access_form_view"
            ).sudo()
            return view._get_combined_arch(), view
        return super()._get_view(view_id, view_type, **options)
