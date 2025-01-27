# Copyright (c) 2025, Emmanuel Gbadamosi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class House(Document):
	def validate(self):
		if not self.owner_name:
			frappe.throw("Owner Name is required")