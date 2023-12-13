$(document).ready(function () {

    var employeeDetails = $("#servicerDetails");
    var employeeCode = $("#employeeCode");
    var employeeContact = $("#employeeContact");

    employeeDetails.hide();

    

    $("#formServicerName").change(function () {

        var selectedValue = $(this).val();

        console.log(selectedValue);

        $.ajax({
            url: `/fetch_servicer/${selectedValue}`,
            type: "GET",
            dataType: "json",
            success: function (data) {
                employeeDetails.show();
                employeeCode.val(data.employee.employee_code);
                employeeContact.val(data.employee.mobile);
            },
            error: function (error) {
                console.error(error);
            }
        });

        // employeeCode.hide();
        // employeeCode.hide();

    });
});