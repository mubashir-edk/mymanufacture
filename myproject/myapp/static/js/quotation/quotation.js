// document.addEventListener("DOMContentLoaded", function () {
//     const addJobButton = document.getElementById("addJobButton");
//     const jobTableBody = document.querySelector("#jobTable tbody");
//     let jobRowCounter = {{ job_formset|length }};
    
//     addJobButton.addEventListener("click", function () {
//         const newRow = document.createElement("tr");
//         newRow.innerHTML = `
//             <th scope="col">${jobRowCounter + 1}</th>
//             <th scope="col"><input type="text" class="form-control" name="form-${jobRowCounter}-length" /></th>
//             <th scope="col"><input type="text" class="form-control" name="form-${jobRowCounter}-width" /></th>
//             <th scope="col"><input type="text" class="form-control" name="form-${jobRowCounter}-height" /></th>
//             <th scope="col"><input type="text" class="form-control" name="form-${jobRowCounter}-remarks" /></th>
//             <th scope="col"><input type="number" class="form-control" name="form-${jobRowCounter}-quantity" /></th>
//             <th scope="col"><input type="file" name="form-${jobRowCounter}-attachment" /></th>
//         `;
//         jobTableBody.appendChild(newRow);
//         jobRowCounter++;
//     });
// });