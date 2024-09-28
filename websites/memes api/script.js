let meme = document.getElementById("meme");
let title = document.getElementById("quote");
let getMemeBtn = document.getElementById("get-meme-btn");



getMemeBtn.addEventListener('click', ()=>{
    let meme1 = Math.round(Math.random() * 100)
    fetch("https://api.imgflip.com/get_memes")
        .then(data => data.json())
        .then(data => {
            console.log(data.data.memes[meme1])
            title.innerHTML = data.data.memes[meme1].name
            meme.src = data.data.memes[meme1].url
    })
})

