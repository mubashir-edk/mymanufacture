const imageInput = document.getElementById('formEmployee_Profile');
    const imagePreview = document.getElementById('image-preview');

    imageInput.addEventListener('change', function () {
        const file = imageInput.files[0];
        if (file) {
            const reader = new FileReader();

            reader.onload = function (e) {
                imagePreview.src = e.target.result;
                imagePreview.style.display = 'block';
            };

            reader.readAsDataURL(file);
            
            // Hide the existing/default image
            const existingImage = document.querySelector('.col.mb-4.d-flex.justify-content-center img:not(#image-preview)');
            existingImage.style.display = 'none';
        } else {
            imagePreview.src = '';
            imagePreview.style.display = 'none';
            
            // Show the existing/default image again
            const existingImage = document.querySelector('.col.mb-4.d-flex.justify-content-center img:not(#image-preview)');
            existingImage.style.display = 'block';
        }
    });