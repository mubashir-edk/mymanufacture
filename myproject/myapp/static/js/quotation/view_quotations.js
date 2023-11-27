// Add click event listeners to each deleteQuotation link
var deleteQuotationLinks = document.querySelectorAll('.deleteQuotation');

deleteQuotationLinks.forEach(function(link) {
    link.addEventListener('click', function(event) {
        // Prevent the default behavior of the link
        event.preventDefault();

        // Get the 'data-bs-id' and 'data-bs-name' and 'data-bs-chalan' attributes for the clicked link
        var id = link.getAttribute('data-bs-id');
        var name = link.getAttribute('data-bs-name');
        var chalan = link.getAttribute('data-bs-chalan');

        // Set the values in the modal
        // var customerId = document.getElementById('customerId');
        var customerName = document.getElementById('customerName');
        var chalanNumber = document.getElementById('chalanNumber');

        //customerId.textContent = 'Customer Id: ' + id;
        customerName.textContent = 'Customer Name: ' + name;
        chalanNumber.textContent = 'Chalan Number: ' + chalan;

        console.log(id);

        // Set the href attribute of the "Delete" link
        var confirmDeleteLink = document.getElementById('confirmDelete');
        confirmDeleteLink.href = `delete_quotation/${id}`;
    });
});