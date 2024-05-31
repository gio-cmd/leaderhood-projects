const number = Math.ceil(Math.random() * 100)
const p = document.getElementById('p')
const userInput = document.getElementById('input')
const myBtn = document.getElementById('my-btn')

myBtn.addEventListener('click', () =>{
    if(Number(userInput.value) === number){
        p.innerHTML = "You guessed the number"
    }
    else if(userInput.value < number){
        p.innerHTML = "your guess is lower than the number"
    }else{
        p.innerHTML = "your guess is higher than the number"
    }
})