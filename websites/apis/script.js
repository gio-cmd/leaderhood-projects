const apiKey = '95da03f5bd59f14f34ca3e257b952f8f';
const city = 'london'
const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

fetch("http://api.quotable.io/random")
    .then(res => res.json())
    .catch(error => console.log('Error'))
        
    
    