from frappe import _

def get_data():
	return [
		{
			"label": _("Reports"),
			"icon": "icon-paper-clip",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Ledger Normal",
					"doctype": "Stock Ledger Entry",
				},
			]
		}
	]
