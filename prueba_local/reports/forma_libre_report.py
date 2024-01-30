from odoo import models, fields, api

class FormaLibreReport(models.AbstractModel):
    _name = 'report.prueba_local.forma_libre_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        factura = self.env['account.move'].browse(docids)
        cliente = factura.partner_id
        lineas_factura = self._get_lineas_factura(factura)
        plazos_pago = factura.invoice_payment_term_id

        dict_return = {
            'doc_ids': docids,
            'doc_model': 'account.move',#modelo donde se va a llamar el reporte
            'docs': factura,#devuelve la data del registro en el que estamos posicionados actualmente (en la UI)
            'self': self,
            'cliente': cliente,
            'lineas_factura': lineas_factura,
            'plazos_pago': plazos_pago
        }
        return dict_return

    def _get_lineas_factura(self, factura_id):
        lines = []
        for line in factura_id.invoice_line_ids:
            lines.append({
                'producto': line.product_id.name,
                'descripcion': line.name,
                'precio_unitario': line.price_unit,
                'subtotal': line.price_subtotal
            })
        return lines