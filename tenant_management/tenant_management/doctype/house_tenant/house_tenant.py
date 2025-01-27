# Copyright (c) 2025, Emmanuel Gbadamosi and contributors
# For license information, please see license.txt

# import frappe
from datetime import datetime

from frappe.model.document import Document

class HouseTenant(Document):
	def autoname(self):
		for ag in self.agreement:
			ag.tenant_name = self.house_tenant_name
			ag.ref = self.generate_transaction_reference(self.house_tenant_name)
			print("look: ", self.house_tenant_name)
			print("look: ", ag.tenant_name)
			print("look: ", ag.ref)

	
	def generate_transaction_reference(self, name):
		current_date = datetime.now().strftime("%d%m%Y")
		transaction_reference = f"RT-AG-{name}-{current_date}"
		return transaction_reference
