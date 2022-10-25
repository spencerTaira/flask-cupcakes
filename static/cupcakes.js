"use strict";

const BASE_API_URL = "http://localhost:5000/api";
const $cupcakesContainer = $('#cupcakes-container');
const $addCupcakeForm = $('#cupcake-add-form');


/**
 * Main controller function
 */

async function main() {
  const cupcakes = await getCupcakes();
  showCupcakes(cupcakes);
}

/**
 * Makes axios get request to BASE_API_URL
 * Inputs: None
 * Outputs: Array of cupcake objects
 */

async function getCupcakes() {
  const response = await axios.get(BASE_API_URL + '/cupcakes');
  return response.data.cupcakes;
}

/**
 * Creates jQuery Object for a single cupcake
 * Input: cupcake object
 * Output: jQuery object of cupcake with HTML.
 */
function generateCupcake(cupcake) {
  return $("<div>")
    .attr('id', `${cupcake.id}`)
    .addClass('cupcake')
    .append($(`<img src = "${cupcake.image}">`))
    .append(`<p>Flavor: ${cupcake.flavor},
    Size: ${cupcake.size},
    Rating: ${cupcake.rating}</p>`);
}

/**
 * Generate jQuery objects for list of cupcakes, and appends HTML to the DOM.
 * Inputs: None
 * Output: None
 */

function showCupcakes(cupcakes) {

  for (let cupcake of cupcakes) {
    $cupcakesContainer.append(generateCupcake(cupcake));
  }

}

/**
 * Handle form submission to add a new cupcake to the database.
 * Refreshes page with new cupcake.
 * Inputs: None
 * Outputs: None
 */
async function addCupcake(evt) {

  evt.preventDefault();

  const flavor = $('#flavor').val();
  const rating = $('#rating').val();
  const size = $('#size').val();
  const image = $('#image').val();

  const response = await axios.post(
    BASE_API_URL + '/cupcakes',
    {
      flavor,
      rating,
      size,
      image
    }
  );

  const $cupcake = generateCupcake(response.data.cupcake)
  $cupcakesContainer.append($cupcake)
  $addCupcakeForm[0].reset();
}

main();
$addCupcakeForm.on('submit', addCupcake);
