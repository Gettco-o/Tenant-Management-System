// Copyright (c) 2025, Emmanuel Gbadamosi and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Billing", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Billing', {
    refresh: function (frm) {
        $(frm.fields_dict['period'].wrapper)
            .html(`
                <div class="form-group horizontal">
					<div class="clearfix">
						<label class="control-label reqd" style="padding-right: 5px;">Period</label>
						<span class="help"></span>
					</div>
					<div class="control-input-wrapper">
						<div class="control-input"><input type="month" id="period" class="input-with-feedback form-control bold" data-fieldtype="Data" data-fieldname="period" placeholder="" data-doctype="Billing"></div>
						<div class="control-value like-disabled-input bold" style="display: none;"></div>
						<div class="help-box small text-extra-muted hide"></div>
					</div>
				</div>
			<span class="tooltip-content">period</span></div><div class="frappe-control input-max-width" data-fieldtype="Currency" data-fieldname="due_amount">
                `)
            .find('#period')
            .on('change', function () {
                const selectedMonth = $(this).val(); // Get the selected value
                console.log(`Selected Month: ${selectedMonth}`);
                frappe.msgprint(`You selected: ${selectedMonth}`);
                frm.set_value('period', selectedMonth);
            });
    }
});
