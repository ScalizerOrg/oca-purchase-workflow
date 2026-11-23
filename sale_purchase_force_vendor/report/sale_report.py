# Copyright 2026 Tecnativa - Víctor Martínez
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    vendor_id = fields.Many2one(
        comodel_name="res.partner",
        readonly=True,
    )

    def _select_dict(self, table):
        return super()._select_dict(table) | {"vendor_id": table.vendor_id}

    def _groupby_list(self, table):
        return super()._groupby_list(table) + [table.vendor_id]
