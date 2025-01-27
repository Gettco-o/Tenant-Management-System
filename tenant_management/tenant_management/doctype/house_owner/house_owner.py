# Copyright (c) 2025, Emmanuel Gbadamosi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class HouseOwner(Document):
	def before_save(self):
		for house in self.houses_owned:
			house.owner_name = self.owner_name