document.getElementById("card1").addEventListener("click", function () {
  alert("You clicked on Card 1");
});

document.getElementById("card2").addEventListener("click", function () {
  alert("You clicked on Card 2");
});

document.getElementById("card3").addEventListener("click", function () {
  alert("You clicked on Card 3");
});

document.getElementById("card4").addEventListener("click", function () {
  alert("You clicked on Card 4");
});

document.addEventListener("DOMContentLoaded", function () {
  var cards = document.querySelectorAll(".card");

  cards.forEach(function (card) {
    var img = card.querySelector("img");
    var textContent = card.querySelector(".text-content");

    card.addEventListener("mouseenter", function () {
      img.style.opacity = "0";
      textContent.style.opacity = "1";
    });

    card.addEventListener("mouseleave", function () {
      img.style.opacity = "1";
      textContent.style.opacity = "0";
    });
  });
});
