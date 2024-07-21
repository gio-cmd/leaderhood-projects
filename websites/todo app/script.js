const input = document.getElementById('input');
const lists = document.getElementById('ul');

function addTask() {
    if (input.value === '') {
        window.alert('You have to fill in the input');
    } else {
        let li = document.createElement('li');
        li.innerHTML = input.value;

        let x = document.createElement('span');
        x.innerHTML = 'x';
        x.className = 'close';

        x.addEventListener('click', function() {
            this.parentElement.remove();
        });

        li.appendChild(x); 

        li.addEventListener('click', function() {
            this.classList.toggle('checked');
        });

        lists.appendChild(li);
        input.value = '';
    }
}
