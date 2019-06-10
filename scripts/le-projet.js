
console.log("--- le-projet.js / carousel ...")

const carouselDiv = document.querySelector('#carousel-home')
console.log("--- carouselDiv : ", carouselDiv)

console.log("--- le-projet.js / bulmaCarousel : ", bulmaCarousel)
const options = {
  slidesToScroll: 1,
  slidesToShow: 1,
  infinite: true,
  pagination: false,
}
console.log("--- le-projet.js / options : ", options)

let carouselHome = bulmaCarousel.attach('#carousel-project', options)

