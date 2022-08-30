document.getElementById('submitBtn').addEventListener('click', () => {
    var classId = JSON.parse(localStorage.getItem('classId'));
    var teacherID = JSON.parse(localStorage.getItem('teacherID'));
    var accessToken = JSON.parse(localStorage.getItem('accessToken'));
    var problem = document.getElementById('quiz').value;
    var answer = document.getElementById('gridRadios1').checked;
    var timeLimitMin = document.getElementById('time-limit-min').value;
    var timeLimitSec = document.getElementById('time-limit-sec').value;
    var point = document.getElementById('point').value;
    var badgeSubject =document.getElementById('badge_input1').value;
    var badgeDescription = document.getElementById('badge_input2').value;

    eel.giveOXQuiz(classId,teacherID,accessToken, problem, answer, timeLimitMin, timeLimitSec, point, badgeSubject, badgeDescription);
  });
  
document.getElementById('saveBtn').addEventListener('click', () => {
  var classId = JSON.parse(localStorage.getItem('classId'));
  var teacherID = JSON.parse(localStorage.getItem('teacherID'));
  var accessToken = JSON.parse(localStorage.getItem('accessToken'));
  var problem = document.getElementById('quiz').value;
  var answer = document.getElementById('gridRadios1').checked;
  var timeLimitMin = document.getElementById('time-limit-min').value;
  var timeLimitSec = document.getElementById('time-limit-sec').value;
  var point = document.getElementById('point').value;
  var badgeSubject =document.getElementById('badge_input1').value;
  var badgeDescription = document.getElementById('badge_input2').value;

  eel.saveOXQuiz(classId,teacherID,accessToken, problem, answer, timeLimitMin, timeLimitSec, point, badgeSubject, badgeDescription);
});