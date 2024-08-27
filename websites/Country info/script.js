let input = document.getElementById('country-inp')
let searchBtn = document.getElementById('search-btn')
let infoContainer = document.getElementById('result')


function countryInfo(){
    if (input.value.trim() === "") {
        infoContainer.innerHTML = `<h3>Input field shouldn't be empty</h3>`;
        return;
    }


    fetch(`https://restcountries.com/v3.1/name/${input.value}?fullText=true`)
        .then(data => data.json())
        .then(data => {
            console.log(data)
            infoContainer.innerHTML = `
            <img src=${data[0].flags.png} class="flag-img">
            <h2>${data[0].name.common}</h2>

            <div>
                <div class="wrapper">
            <div class="data-wrapper">
                <h4>Capital:</h4>
                <span>${data[0].capital[0]}</span>
            </div>
        </div>
        <div class="wrapper">
            <div class="data-wrapper">
                <h4>Continent:</h4>
                <span>${data[0].continents[0]}</span>
            </div>
        </div>
         <div class="wrapper">
            <div class="data-wrapper">
                <h4>Population:</h4>
                <span>${data[0].population}</span>
            </div>
        </div>
        <div class="wrapper">
            <div class="data-wrapper">
                <h4>Currency:</h4>
                <span>${
                  data[0].currencies[Object.keys(data[0].currencies)].name
                } - ${Object.keys(data[0].currencies)[0]}</span>
            </div>
        </div>
         <div class="wrapper">
            <div class="data-wrapper">
                <h4>Common Languages:</h4>
                <span>${Object.values(data[0].languages)
                  .toString()
                  .split(",")
                  .join(", ")}</span>
            </div>
        </div>
      `;
    })
}