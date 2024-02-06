$(document).ready(function (e) {

    // Assign
    var assignServiceWorkLinks = document.querySelectorAll('#assignWorkBtn');

    assignServiceWorkLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();

            var servicework_id = link.getAttribute('data-bs-servicework');
            console.log("asdasd: " + servicework_id);

            // Set the href attribute of the "Delete" link
            var confirmAssignLink = document.getElementById('confirmWorkAssign');
            assignUrl = `/assign_servicer/${servicework_id}`;

            confirmAssignLink.setAttribute('action', assignUrl);
        });
    });


    // UnAssign
    var unAssignServiceWorkLinks = document.querySelectorAll('#confirmWorkUnAssign');

    unAssignServiceWorkLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();

            var serviceworkId = link.getAttribute('data-bs-service');
            var servicework_service = link.getAttribute('data-bs-serviceName');
            var servicework_servicer = link.getAttribute('data-bs-servicer');

            console.log(serviceworkId);
            console.log(servicework_service);
            console.log(servicework_servicer);

            // Set the href attribute of the "Delete" link
            var confirmUnAssignLink = document.getElementById('confirmUnAssign');
            var unAssignModalBody = document.getElementById('unAssignModalBody');
            unAssignUrl = `/unassign_servicer/${serviceworkId}`;

            confirmUnAssignLink.href = unAssignUrl;
            console.log(confirmUnAssignLink);
            unAssignModalBody.innerHTML = 'you want to unAssign <b>' + servicework_servicer + '</b> from <b>' + servicework_service + '</b>.';
        });
    });

});