# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import frappe
from frappe import msgprint
from frappe.utils import getdate, cint, add_months, date_diff, add_days, nowdate, \
	get_datetime_str, cstr, get_datetime, time_diff, time_diff_in_seconds
from datetime import datetime, timedelta

def on_update(doc,method):
	validate(doc,method)

def validate(doc,method):
	global attendance_date
	att_tt = []
	att_time = []
	attendance_date = getdate(doc.attendance_date)
	if doc.status <> "Present" and doc.status <> "Half Day":
		frappe.throw(("Only Present or Half Day Attendance is Allowed Check {0}").format(doc.name))

	check_employee (doc, method)
	

				
#Function to check if the attendance is not for a NON-WORKING employee
def check_employee(doc, method):
	#Check if the employee is Active for the Dates
	emp = frappe.get_doc("Employee", doc.employee)
	if emp.status == "Left":
		if emp.relieving_date < attendance_date:
			frappe.throw(("Cannot create attendance for {0} as he/she has left on {1}").\
			format(emp.employee_name, emp.relieving_date))
	else:
		if emp.date_of_joining > attendance_date:
			frappe.throw(("Cannot create attendance for {0} as he/she has joined on {1}").\
			format(emp.employee_name, emp.date_of_joining))

