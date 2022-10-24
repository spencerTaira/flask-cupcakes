"use strict";

const BASE_API_URL = "localhost:5000/api"
function main() {

}

/**
 * Makes axios get request to BASE_API_URL
 * Inputs: None
 * Outputs: Array of cupcake objects
 */

async function getCupcakes() {
  response = await axios.get(BASE_API_URL);
  return response.data.cupcakes;
}

/*
<ol>
for
  <li></li>
</ol>
*/
async function generateCupcakeHTML(cupcake) {
  return $("<div>")
    .attr('id', `${cupcake.id}`)
    .append($('<img>'))
    .append(`<p>${cupcake.flavor} Cupcake,
    Size: ${cupcake.size},
    Rating: ${cupcake.rating}</p>`)
}

// <image>
// <flavor> Cupcake
    // - size, rating


/*
  <div class="row"
    <div class="col">
      <img>
      <p> <Flavor>
    </div>
    <div class="col">
      <p>
    </div>
  </div>
*/