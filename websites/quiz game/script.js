const nextBtn = document.getElementById('next');
const questionElement = document.getElementById('question');
const answersElement = document.getElementById('anwers'); // Correct the ID
let index = 0;
let score = 0;
let answered = false;

const questions = [
    {
        question: 'What is legal drinking age in Georgia?',
        answers: [ 
            { answer: 'It doesnt Exist', correct: true },
            { answer: '18', correct: false },
            { answer: '14', correct: false },
            { answer: '21', correct: false }
        ]
    },
    {
        question: 'When was titanic relised',
        answers: [
            { answer: '1997', correct: true },
            { answer: '2001', correct: false },
            { answer: '1978', correct: false },
            { answer: '2003', correct: false }
        ]
    },
    {
        question: 'Name worlds largest continent',
        answers: [
            { answer: 'Africa', correct: false },
            { answer: 'Europe', correct: false },
            { answer: 'Asia', correct: true },
            { answer: 'Australia', correct: false }
        ]
    },
    {
        question: 'When is damoukidebloba is Georgia',
        answers: [
            { answer: 'may 27', correct: false },
            { answer: 'january 12', correct: false },
            { answer: 'may 26', correct: true },
            { answer: 'april 18', correct: false }
        ]
    },
    {
        question: 'What does sigma mean',
        answers: [
            { answer: 'mate', correct: true },
            { answer: 'mate', correct: false },
            { answer: 'mate', correct: false },
            { answer: 'mate', correct: false }
        ]
    }

];

function startQuiz() {
    index = 0;
    score = 0;
    displayQuestion();
}

function displayQuestion() {
    answered = false;
    let question = questions[index].question;
    questionElement.innerHTML = `${index + 1}. ${question}`; 

    answersElement.innerHTML = ''; =

    questions[index].answers.forEach(element => { 
        const button = document.createElement("button");
        button.innerHTML = element.answer; 
        button.classList.add('btn');
        button.addEventListener('click', () => selectAnswer(button, element));
        answersElement.appendChild(button);
    });
    nextBtn.style.display = 'none';
}

function selectAnswer(button, answer) {
    if (answered) return;
    answered = true;
    if (answer.correct) {
        button.style.backgroundColor = 'rgba(0, 255, 0, 0.8)';
        score++;
    } else {
        button.style.backgroundColor = 'rgba(255, 0, 0, 0.8)';
    }
    nextBtn.style.display = 'block'
}

function showResults() {
    questionElement.innerHTML = `You scored ${score} out of ${questions.length}`;
    answersElement.innerHTML = '';
    nextBtn.style.display = 'none';
}

nextBtn.addEventListener('click', () => {
    if (index < questions.length - 1) {
        index++;
        displayQuestion();
    } else {
        showResults();
    }
});

startQuiz();
