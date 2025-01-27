app_name = "tenant_management"
app_title = "Tenant Management"
app_publisher = "Emmanuel Gbadamosi"
app_description = "Tenant Management System"
app_email = "ecovenant75@gmail.com"
app_license = "mit"

doc_events = {
    "Payment": {
        "on_submit": "tenant_management.tenant_management.doctype.payment.payment.update_bill_status"
    }
}