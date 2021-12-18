//Question bank
var questionBank = [{
        question: 'What are the key components of DevOps?',
        option: ['Continuous Integration', 'Continuous Testing', 'Continuous Delivery', 'Continuous Monitoring'],
        answer: 'Continuous Integration'
    },
    {
        question: 'Which of the following is an IAM Security Tool?',
        option: ['IAM Credentials Report', 'IAM Root Account Manager', 'IAM Service Report', 'IAM Security Advisor', ],
        answer: 'IAM Credentials Report'
    },
    {
        question: 'Which EC2 Purchasing Option can provide the biggest discount, but is not suitable for critical jobs or databases?',
        option: ['Scheduled Instances', 'Convertible Instances', 'Dedicated Hosts', 'Spot Instances'],
        answer: 'Spot Instances'
    },
    {
        question: 'Which AWS offered Load Balancer should you use to handle hundreds of thousands of connections with low latency?',
        option: ['Application Load Balancer', 'Network Load Balancer', 'Elastic Load Balancer ', 'N/A'],
        answer: 'Network Load Balancer'
    },
    {
        question: 'You want to create a decentralized blockchain on AWS. Which AWS service would you use?',
        option: ['DocumentDB', 'QLDB', 'Managed Blockchain', 'QuickSight'],
        answer: 'Managed Blockchain'
    }
]

var question = document.getElementById('question');
var quizContainer = document.getElementById('quiz-container');
var scorecard = document.getElementById('scorecard');
var option0 = document.getElementById('option0');
var option1 = document.getElementById('option1');
var option2 = document.getElementById('option2');
var option3 = document.getElementById('option3');
var next = document.querySelector('.next');
var points = document.getElementById('score');
var span = document.querySelectorAll('span');
var timer = document.getElementById("timer");
var i = 0;
var score = 0;

//function to display questions
function displayQuestion() {
    for (var a = 0; a < span.length; a++) {
        span[a].style.background = 'none';
    }
    question.innerHTML = 'Q.' + (i + 1) + ' ' + questionBank[i].question;
    option0.innerHTML = questionBank[i].option[0];
    option1.innerHTML = questionBank[i].option[1];
    option2.innerHTML = questionBank[i].option[2];
    option3.innerHTML = questionBank[i].option[3];
    stat.innerHTML = "Question" + ' ' + (i + 1) + ' ' + 'of' + ' ' + questionBank.length;
}

//function to calculate scores
function calcScore(e) {
    if (e.innerHTML === questionBank[i].answer && score < questionBank.length) {
        score = score + 1;
        document.getElementById(e.id).style.background = 'limegreen';
    } else {
        document.getElementById(e.id).style.background = 'tomato';
    }
    setTimeout(nextQuestion, 300);
}

//function to display next question
function nextQuestion() {
    if (i < questionBank.length - 1) {
        i = i + 1;
        displayQuestion();
    } else {
        points.innerHTML = score + '/' + questionBank.length;
        quizContainer.style.display = 'none';
        scoreboard.style.display = 'block'
        clearInterval(nxtqst);
        clearInterval(cgtm);
    }
}

//click events to next button
next.addEventListener('click', nextQuestion);
// setInterval(nextQuestion, 2000);
let timeOut = 3000;

function changeTime() {
    timer.innerText = "Time left: " + timeOut / 1000 + "s";
    timeOut -= 1000;
    if (timeOut == 0) {
        timeOut = 3000;
    }
    console.log("backgroundda ketomman");
    
}

// show the next question
var nxtqst = setInterval(nextQuestion, timeOut);
// change the html element
var cgtm = setInterval(changeTime, 1000);


//Back to Quiz button event
function backToQuiz() {
    location.reload();
}

//function to check Answers
function checkAnswer() {
    var answerBank = document.getElementById('answerBank');
    var answers = document.getElementById('answers');
    answerBank.style.display = 'block';
    scoreboard.style.display = 'none';
    for (var a = 0; a < questionBank.length; a++) {
        var list = document.createElement('li');
        list.innerHTML = questionBank[a].answer;
        answers.appendChild(list);
    }
}

displayQuestion();