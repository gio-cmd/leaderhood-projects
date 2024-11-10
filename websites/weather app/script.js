let apiKey = "8b3c2188b1fe57f318bdcd6231e30d94";
let apiUrl = "https://api.openweathermap.org/data/2.5/weather?units=metric&lang=en";

let search = document.querySelector(".search-container input");
let searchButton = document.querySelector(".search-btn");
let weatherIcon = document.querySelector(".weather-icon");


async function weather(city) {
  try {
    const response = await fetch(`${apiUrl}&q=${city}&appid=${apiKey}`);
    const data = await response.json();
    console.log(data);

    document.querySelector(".city-name").innerHTML = data.name;
    const temperature = Math.round(data.main.temp);
    document.querySelector(".temperature").innerHTML = temperature + "°C";
    document.querySelector(".humidity-value").innerHTML = data.main.humidity + "%";
    document.querySelector(".visibility-value").innerHTML = data.visibility;

    if (data.weather[0].main === "Clouds") {
      weatherIcon.src = "./images/1.png";
    } else if (data.weather[0].main === "Clear") {
      weatherIcon.src = "./images/2.png";
    } else if (data.weather[0].main === "Rain") {
      weatherIcon.src = "./images/3.png";
    } else if (data.weather[0].main === "Drizzle") {
      weatherIcon.src = "./images/4.png";
    } else if (data.weather[0].main === "Mist") {
      weatherIcon.src = "./images/5.png";
    } else{
        weatherIcon.src = './images/6.png'
    }

    document.querySelector(".weather-info").style.display = "block";

  } catch (error) {
    document.querySelector(".weather-info").style.display = "none";
  }
}

searchButton.addEventListener("click", () => {
  const city = search.value;
  if (city !== "") {
    weather(city);
  }
});
