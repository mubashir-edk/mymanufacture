const imageInputProduct = document.getElementById('formProductImage');
const imageInputCategory = document.getElementById('formCategoryImage');
const imagePreviewProduct = document.getElementById('image-preview-product');
const existingImageProduct = document.getElementById('productDefaultImage');

const imagePreviewCategory = document.getElementById('image-preview-category');
const existingImageCategory = document.getElementById('categoryDefaultImage');

imageInputCategory.style.display = 'none';
imageInputProduct.style.display = 'none';

imageInputProduct.addEventListener('change', function () {
    const file = imageInputProduct.files[0];
    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            imagePreviewProduct.src = e.target.result;
            imagePreviewProduct.style.display = 'block';
            existingImageProduct.style.display = 'none'; // Hide the existing/default image
        };

        reader.readAsDataURL(file);
    } else {
        imagePreviewProduct.src = '';
        imagePreviewProduct.style.display = 'none';
        existingImageProduct.style.display = 'block'; // Show the existing/default image
    }
});

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
