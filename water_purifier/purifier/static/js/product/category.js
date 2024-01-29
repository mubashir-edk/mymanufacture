const imageInputCategory = document.getElementById('formCategoryImage');
const imagePreviewCategory = document.getElementById('image-preview-category');
const existingImageCategory = document.getElementById('categoryDefaultImage');

imageInputCategory.style.display = 'none';

imageInputCategory.addEventListener('change', function () {
    const file = imageInputCategory.files[0];
    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            imagePreviewCategory.src = e.target.result;
            imagePreviewCategory.style.display = 'block';
            existingImageCategory.style.display = 'none'; // Hide the existing/default image
        };

        reader.readAsDataURL(file);
    } else {
        imagePreviewCategory.src = '';
        imagePreviewCategory.style.display = 'none';
        existingImageCategory.style.display = 'block'; // Show the existing/default image
    }
});


var updateCategoryLinks = document.querySelectorAll('.update-category-btn');

    updateCategoryLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            // Prevent the default behavior of the link
            event.preventDefault();

            // Get the 'data-bs-id' and 'data-bs-name' and 'data-bs-chalan' attributes for the clicked link
            var id = link.getAttribute('data-bs-id');
            console.log(id);

            // Set the href attribute of the "Delete" link
            updateUrl = `/update_category/${id}`;
        });
    });


$(document).ready(function() {
    $(".update-category-btn").click(function(e) {
        e.preventDefault();
        
        console.log(updateUrl);
        // Make an AJAX request to the update_category view
        $.ajax({
            url: updateUrl,
            type: 'GET',
            success: function(data) {
                // Update the content of updateCategoryModal with the received HTML

                if (data.category.image){
                    $('#updateCategoryModal #image-preview-category').attr('src', data.category.image);
                } else {
                    console.log("No Image");
                }
                
                $('#updateCategoryModal #formCategoryName').val(data.category.name);
                
                
                // Show the modal
                // $('#updateCategoryModal').modal('show');
            },
            error: function(error) {
                console.error('Error fetching update_category view:', error);
            }
        });
    });
    
    $("#categoryUpdateButton").click(function(e) {
        $('#updateCategoryForm').attr('action', updateUrl);
    });
    
});