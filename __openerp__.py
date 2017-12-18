{
'name': "Reportes WNI",
'description' : "cambio de esquelto de factura",
'version' : "1.0.0",
'author' : "Nayeli Valencia Díaz,Raul Ovalle",
'depends' : ['account_accountant','sale','stock_barcode','stock', 'delivery','website_sale_delivery'],
'data': ['reports/formats.xml',
         'reports/invoice_report.xml',
         'reports/layout.xml',
         'reports/embarque_report1.xml',
         'reports/remision_report.xml',
         'reports/report_purchaseorderwni.xml'],
'images':['img/logowni.png'],
'installable' : True,
}

