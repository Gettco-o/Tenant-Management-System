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


def update_bill_status(doc, method):
	print("Bill status update is running please")
	frappe.msgprint(f"Updating bill status: {doc.bill}")

	bill = frappe.get_doc("Billing", doc.bill)
    
	if bill.status == "Unpaid":
		bill.status = "Paid"
		doc.bill_status = "Paid"
		frappe.msgprint(f"Bill {bill.ref} updated successfully. New status: {bill.status}")

	elif bill.status == "Paid":
			frappe.throw(f"Bill {bill.ref} already paid")

	bill.save()