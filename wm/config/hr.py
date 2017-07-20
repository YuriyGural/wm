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
					"name": "Attendance Performance Analysis",
					"doctype": "Attendance",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Employee Attendance",
					"doctype": "Attendance",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Leave Application Report",
					"doctype": "Leave Application",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "List of Holidays",
					"doctype": "Holiday List",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Monthly Attendance Time Based",
					"doctype": "Attendance",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Salary Structure",
					"doctype": "Salary Structure",
				}
			]
		}
	]
