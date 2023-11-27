$(document).ready(function () {

    // Add an event listener for the "Assign" button click
    $('#sequencecreatebtn').click(function (e) {
        e.preventDefault();
        
        // Get Quotation Code Data
        const quotation_prefix = $('#sequenceFormOne #formCodePrefix').val();
        const quotation_size = $('#sequenceFormOne #formCodeSize').val();
        const quotation_suffix = $('#sequenceFormOne #formCodeSuffix').val();

        // Get QuotationJob Code Data
        const quotation_job_prefix = $('#sequenceFormTwo #formCodePrefix').val();
        const quotation_job_size = $('#sequenceFormTwo #formCodeSize').val();
        const quotation_job_suffix = $('#sequenceFormTwo #formCodeSuffix').val();
        
        // Get Quotation Code Data
        const task_prefix = $('#sequenceFormThree #formCodePrefix').val();
        const task_size = $('#sequenceFormThree #formCodeSize').val();
        const task_suffix = $('#sequenceFormThree #formCodeSuffix').val();

        // Include the CSRF token in the headers
        const csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        const headers = {
            'X-CSRFToken': csrfToken,
            "Content-Type": 'application/json',
        };

        const data =  {
            quotation_prefix: quotation_prefix,
            quotation_size: quotation_size,
            quotation_suffix: quotation_suffix,
            quotation_job_prefix: quotation_job_prefix,
            quotation_job_size: quotation_job_size,
            quotation_job_suffix: quotation_job_suffix,
            task_prefix: task_prefix,
            task_size: task_size,
            task_suffix: task_suffix,
        }
        
        console.log({data})

        //return
        // Make an AJAX request to save the assignment
        $.ajax({
            url: window.ajaxUrl,
            type: 'POST',
            data:JSON.stringify(data),
            headers: headers,
            success: function (response) {
                if (response.redirect_url) {
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
});