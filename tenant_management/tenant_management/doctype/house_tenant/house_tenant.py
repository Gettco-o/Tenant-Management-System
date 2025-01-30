# Copyright (c) 2025, Emmanuel Gbadamosi and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime

from frappe.model.document import Document

class HouseTenant(Document):
	def autoname(self):
		for ag in self.agreement:
			ag.tenant_name = self.house_tenant_name
			ag.ref = self.generate_transaction_reference(self.house_tenant_name)

	
	def generate_transaction_reference(self, name):
		current_date = datetime.now().strftime("%d%m%Y")
		transaction_reference = f"RT-AG-{name}-{current_date}"
		return transaction_reference

def update_house_status(doc, method):
	frappe.msgprint(f"Updating house status: {doc.house_rented}")

	house = frappe.get_doc("House", doc.house_rented)
    
	if house.status == "Available":
		house.status = "Taken"
		frappe.msgprint(f"House {house.house_name} updated successfully. New status: {house.status}")

	elif house.status == "Taken":
			frappe.throw(f"House {house.house_name} already taken")

	house.save()