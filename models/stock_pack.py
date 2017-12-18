from openerp import fields,models,api

class plantillas_wni_ro_stock_pack_operation(models.Model):

    _name = 'stock.pack.operation'
    _inherit ='stock.pack.operation'
    @api.one
    def _compute_faltante(self):
        self.faltante = self.product_qty - self.qty_done

    faltante = fields.Float(compute='_compute_faltante')