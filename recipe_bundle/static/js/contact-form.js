/* jshint esversion: 6 */

/* Adapted from https://jsfiddle.net/13atu8e5/ */
/* Send email using emailJS */
var resultbox = document.getElementById("submitResult");

window.onload = function () {
  document.getElementById('contactForm').addEventListener('submit', function (event) {
      event.preventDefault();
      emailjs.sendForm('MS3-RecipeBundle', 'RecipeBundle', this)
          .then(function () {
              console.log('SUCCESS!');
              resultbox.innerHTML = `<p>Message sent successfully.</p>`;
          }, function (error) {
              console.log('FAILED...', error);
              resultbox.innerHTML = `<p>Message sending failed. Please try again later.</p>`;
          });
  });
};
