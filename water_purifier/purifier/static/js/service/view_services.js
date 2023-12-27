var deleteServiceLinks = document.querySelectorAll('.delete-service-btn');

deleteServiceLinks.forEach(function(link) {
    link.addEventListener('click', function(event) {
        // Prevent the default behavior of the link
        event.preventDefault();

        // Get the 'data-bs-id'
        var id = link.getAttribute('data-bs-id');
        console.log(id);

        // Set the href attribute of the "Delete" link
        var confirmDeleteLink = document.getElementById('deleteServiceButton');
        confirmDeleteLink.href = 'delete_service/' + id;
        console.log(confirmDeleteLink);

        
    });
});