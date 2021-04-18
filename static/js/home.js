
let a = $('.latest')
a[1].removeChild(a[1].firstElementChild)

let interval = setInterval(changeImage, 6000);

let index = 0;
function changeImage() {
  let imgContainer = $('#home-image-container').children('li');
  imgContainer[index].classList.remove('active');
  if (index < imgContainer.length - 1) {
    index++;
  } else index = 0;
  imgContainer[index].classList.add('active');
}

$(document).ready(function () {

  $("a").on('click', function (event) {


    if (this.hash !== "") {

      event.preventDefault();

      let hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function () {
        window.location.hash = hash;
      });
    }
  });
});