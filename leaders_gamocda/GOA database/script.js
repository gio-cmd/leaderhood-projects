const form = document.getElementById('form')
const registration = document.getElementById('registration')
const journal = document.getElementById('journal')
const viewer = document.getElementById('viewer')
const mod = document.getElementById('mod')
const jForm = document.getElementById('j-form')

form.addEventListener('submit', (e) => {
    e.preventDefault()
    registration.className = 'gone'
    journal.classList.remove('gone')

    if (mod.checked) {
        jForm.contentEditable = 'true'
    }
})