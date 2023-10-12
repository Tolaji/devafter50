/* disable right click and context menu*/
window.addEventListener("contextmenu", function (e) {
  e.preventDefault();
});

window.addEventListener("mousedown", function (e) {
  if (e.button === 2) {
    e.preventDefault();
  }
});

/* disable viewing page source (ctrl+U)*/
window.addEventListener("keydown", function (e) {
  if (e.ctrlKey && e.keyCode === 85) {
    e.preventDefault();
  }
});

/* Disable developer tools (f12*/
window.addEventListener("keydown", function (e) {
  if (e.keyCode === 123) {
    e.preventDefault();
  }
});

/* Disable right click on images*/
document.addEventListener("contextmenu", function (e) {
  if (e.target.tagName === "IMG") {
    e.preventDefault();
  }
});

/* Disable copy paste*/
document.addEventListener("keydown", function (e) {
  if (e.ctrlKey && (e.keyCode === 67 || e.keyCode === 86)) {
    e.preventDefault();
  }
});

/* Disable selecting text*/
document.addEventListener("selectstart", function (e) {
  e.preventDefault();
});

/* Disable drag and drop*/
document.addEventListener("dragstart", function (e) {
  e.preventDefault();
});

/* Disable url bar editing*/
window.addEventListener("keydown", function (e) {
  if (e.ctrlKey && e.keyCode === 82) {
    e.preventDefault();
  }
});

/* Disable console (f12)*/
Object.defineProperty(window, "console", {
  value: {
    log: function () {},
    warn: function () {},
    error: function () {},
  },
});

/* Disable right click on links*/
document.addEventListener("contextmenu", function (e) {
  if (e.target.tagName === "A") {
    e.preventDefault();
  }
});
