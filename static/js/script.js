function openModal(imageSrc) {
  // Update the modal image source and show the modal
  var modalImage = document.getElementById("modalImage");
  modalImage.src = imageSrc;
  $("#exampleModal").modal("show");
}
