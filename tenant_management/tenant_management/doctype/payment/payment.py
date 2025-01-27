# Copyright (c) 2025, Emmanuel Gbadamosi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime


class Payment(Document):
	def autoname(self):
		if not self.ref:
			self.ref = self.generate_transaction_reference()



	def validate(self):
		if not self.ref:
			frappe.throw("Ref is required")

	def generate_transaction_reference(self):
		current_time = datetime.now().strftime("%H%M")
		current_date = datetime.now().strftime("%d%m%Y")
		transaction_reference = f"PAY-{self.tenant_name}-{current_time}{current_date}"
		return transaction_reference
