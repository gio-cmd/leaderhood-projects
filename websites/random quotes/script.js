const author = document.getElementById('author')
const quote = document.getElementById('quote')

async function getQuote(){
    const response = await fetch("https://api.quotable.io/random")
    const data = await response.json()
    console.log(data)
    author.innerHTML = data.author
    quote.innerHTML = data.content
}

getQuote()