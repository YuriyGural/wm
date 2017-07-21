# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "wm"
app_title = "Western Millwork"
app_publisher = "Western Millwork Ltd."
app_description = "Western Millwork Extensions"
app_icon = "octicon octicon-color-mode"
app_color = "#561919"
app_email = "yuriy@westernmillwork.com"
app_url = "https://github.com/YuriyGural/wm"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/wm/css/wm.css"
# app_include_js = "/assets/wm/js/wm.js"

# include js, css files in header of web template
# web_include_css = "/assets/wm/css/wm.css"
# web_include_js = "/assets/wm/js/wm.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Installation
# ------------

# before_install = "wm.install.before_install"
# after_install = "wm.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "wm.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

#scheduler_events = {
#	"all": [
# 		"wm.tasks.all"
# 	],
# 	"daily": [
# 		"wm.tasks.daily"
# 	],
# 	"hourly": [
# 		"wm.tasks.hourly"
# 	],
# 	"weekly": [
# 		"wm.tasks.weekly"
# 	]
# 	"monthly": [
# 		"wm.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "wm.install.before_tests"

