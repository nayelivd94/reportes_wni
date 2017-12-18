from openerp import fields,models,api

class plantillas_wni_invoice(models.Model):

    _inherit = 'account.invoice.line'
    serie= fields.Text('series')
