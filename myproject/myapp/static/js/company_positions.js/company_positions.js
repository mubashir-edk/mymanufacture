$(document).ready(function() {
    // Load content from 'second_url' and insert it into the modal body
    $(document).on('click', '[data-target="#createModal"]', function(e) {
        e.preventDefault();
        var modalBody = $('#createModal .modal-body');
        
        $.get("{% url 'create_company_position' %}", function(data) {
            modalBody.html(data);
        });
    });
});