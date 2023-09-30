function openPDF() {
  window.open(
    "Documents/UnofficialTranscript.pdf",
    "_blank",
    "width=600,height=400"
  );
}

window.addEventListener("scroll", function () {
  let offset = window.pageYOffset;
  document.querySelector(".parallax img").style.transform =
    "translateY(" + offset * 0.5 + "px)";
});
