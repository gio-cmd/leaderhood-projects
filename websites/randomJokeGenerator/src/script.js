let webJoke = document.getElementById('joke')
let button = document.getElementById('btn')


button.addEventListener('click', ()=>{
    fetch('https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit')
    
        .then(data => data.json())
        .then(data => {
            webJoke.textContent = `${data.setup} ${data.delivery}`
        })
})
