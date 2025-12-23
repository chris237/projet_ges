# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    dossier_id = fields.Many2one(
        "gespros.project",
        string="Numero de dossier",
        help="Dossier lié à cette facture client ou fournisseur.",
    )
