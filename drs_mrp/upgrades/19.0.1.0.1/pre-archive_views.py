from odoo.upgrade import util


def migrate(cr, version):
    util.explode_execute(
        cr,
        """
        UPDATE ir_ui_view v
           SET active = False
         WHERE id in (1667, 1664, 4471)
        """,
        table="ir_ui_view",
        alias="v",
    )
