// OPEN MODAL SCRIPT
function openModal(imageSrc) {
  // Update the modal image source and show the modal
  var modalImage = document.getElementById("modalImage");
  modalImage.src = imageSrc;
  $("#exampleModal").modal("show");
}

// REPLACE CURRENCIES ON CLICK 
const exchangeIcon = document.querySelector("#replace-currencies");
const fromSelect = document.querySelector("#from");
const toSelect = document.querySelector("#to");

exchangeIcon.addEventListener("click", () => {
  const temp = fromSelect.value;
  fromSelect.value = toSelect.value;
  toSelect.value = temp;
});
