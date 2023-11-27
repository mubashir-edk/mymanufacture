$(document).ready(function () {
    console.log("hello world!");
    $('#openModalLink').click(function (e) {
        // console.log(window.hello);

        // When the link is clicked, load data via AJAX and populate the modal
        $.ajax({
            url: window.ajaxUrl,
            type: 'GET',
            dataType: 'json', // Expect JSON response
            success: function (data) {
                console.log(data);
                // Handle the success response and populate the modal
                // Employees to assign
                const employeesToAssign = data.employees_to_assign;
                const employeeSelect = $('#formAssignEmployee');
                            
                employeesToAssign.forEach(function (employee) {
                    employeeSelect.append($('<option>', {
                        value: employee.id,
                        text: employee.name
                    }));
                });
                
            },
            error: function (xhr, textStatus, errorThrown) {
                // Handle any errors that occur during the AJAX request
                console.log("AJAX request failed:", textStatus, errorThrown);
            }
        });            
    });


    // Add an event listener for the "Assign" button click
    $('#jobassignbtn').click(function (e) {
        e.preventDefault();
        // Get the selected employee and the job_id
        const selectedEmployee = $('#formAssignEmployee').val();
        const job_id = $('#jobId').val();;  // Get the current job_id from the page

        // Include the CSRF token in the headers
        const csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        const headers = {
            'X-CSRFToken': csrfToken,
            "Content-Type": 'application/json',
        };

        const data =  { 
            employee_id: selectedEmployee,
            job_id: job_id  // Automatically save the job_id
        }
      
        console.log({data})

        //return
        // Make an AJAX request to save the assignment
        console.log("hello")
        $.ajax({
            url: window.ajaxUrl,
            type: 'POST',
            data:JSON.stringify(data),
            headers: headers,
            success: function (response) {
                console.log(data)
                if (response.redirect_url) {
                    console.log("In POST")
                    // Redirect to the specified URL
                    window.location.href = response.redirect_url;
                } else {
                    // Handle any other response conditions
                    console.log("Error: " + response.error);
                }
            },
            error: function (xhr, textStatus, errorThrown) {
                console.log("AJAX request failed:", textStatus, errorThrown);
            }
        });
    });

    // Add click event listeners to each deleteQuotation link
    var unAssignJobModal = document.getElementById('unAssignModal');

    unAssignJobModal.addEventListener('click', function(event) {
        // Prevent the default behavior of the link
        event.preventDefault();

        // Set the href attribute of the "Delete" link
        var confirmUnAssignJob = document.getElementById('confirmUnAssign');
        var getTaskId = document.getElementById('jobTaskId').value;
        console.log(getTaskId);
        confirmUnAssignJob.href = `/job_unassign/${getTaskId}`;

        console.log(confirmUnAssignJob)
    });

});