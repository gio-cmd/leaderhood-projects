let milliseconds = 0;
let seconds = 0;
let minutes = 0;
let hours = 0;

let timer = document.querySelector('.timerDisplay');
let interval = null;

document.getElementById('startTimer').addEventListener('click', function() {
    if (interval !== null) {
        clearInterval(interval);
    }
    interval = setInterval(function() {
        displayTimer();
    }, 10);
});

document.getElementById('pauseTimer').addEventListener('click', function() {
    clearInterval(interval);
});

document.getElementById('resetTimer').addEventListener('click', function() {
    clearInterval(interval);
    milliseconds = 0;
    seconds = 0;
    minutes = 0;
    hours = 0;
    timer.innerHTML = '00 : 00 : 00 : 000';
});

function displayTimer() {
    milliseconds = milliseconds + 10;
    if (milliseconds == 1000) {
        milliseconds = 0;
        seconds = seconds + 1;
    }
    if (seconds == 60) {
        seconds = 0;
        minutes = minutes + 1;
    }
    if (minutes == 60) {
        minutes = 0;
        hours = hours + 1;
    }

    let h = hours;
    if (hours < 10) {
        h = "0" + hours;
    }

    let m = minutes;
    if (minutes < 10) {
        m = "0" + minutes;
    }

    let s = seconds;
    if (seconds < 10) {
        s = "0" + seconds;
    }

    let ms = milliseconds;
    if (milliseconds < 10) {
        ms = "00" + milliseconds;
    } else if (milliseconds < 100) {
        ms = "0" + milliseconds;
    }

    timerRef.innerHTML = h + " : " + m + " : " + s + " : " + ms;
}

