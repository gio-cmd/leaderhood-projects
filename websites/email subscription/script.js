const scriptURL = 'https://script.google.com/macros/s/AKfycbwbsH1_p10jPxkxuoDavlM4Z981q8tzphQAuGE3BSs-mtn8fZUI8QH-1hTKgPX1KNySbA/exec'
const form = document.forms['contact-form']



form.addEventListener('submit', e => {
    let input = document.getElementById('input')

    let text = document.querySelector('p.p')
    text.id = 'appear' 
    input.value = ''

    e.preventDefault()

    fetch(scriptURL, {method: 'POST', body: new FormData(form)})
        .then(response => console.log('Success!', response))
        .catch(error => console.error('Error!', error.message))
})