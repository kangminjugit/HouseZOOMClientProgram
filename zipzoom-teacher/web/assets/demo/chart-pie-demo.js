// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';


window.onload = async function(){
  var ctx = document.getElementById("myPieChart");
  var classId = JSON.parse(localStorage.getItem('classId')); 
  var quizResult = await eel.get_quizResult(classId)();

  if(quizResult == null){
    var myPieChart = new Chart(ctx, {});
    return;
  }
  var quiz = quizResult[0][quizResult[0].length-1];

  var studentAnswerArr = [];
  var studentAnswer= {};
  quiz.choices.forEach(choice => studentAnswer[choice] = 0);

  quizResult[1].forEach(elem => {
    if(elem.quizId === quiz.id){
      if(quiz.isOX){
        studentAnswer[elem.answer == true? 'O':'X']++;
        studentAnswerArr.push({
          'id': elem.id,
          'answer': elem.answer == true? 'O':'X'
        });
      }else{
        studentAnswer[elem.answer]++;
        studentAnswerArr.push({
          'id': elem.id,
          'answer': elem.answer
        });
      }
      
    }
  });

  var chartData = [];
  for (var key in studentAnswer) {
    if (studentAnswer.hasOwnProperty(key)) {
      chartData.push( [ studentAnswer[key] ] );
    }
  }
  
  var myPieChart = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: quiz.choices,
      datasets: [{
        data: chartData,
        backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745', '#EC9B3B'],
      }],
    },
  });

  console.log(studentAnswerArr);
  
  
  // studentAnswerArr.sort((a,b) => a.id - b.id);
  // $('#answerTable').DataTable( {        
  //     // 표시 건수기능 숨기기
  //     lengthChange: false,
  //     // 검색 기능 숨기기
  //     searching: false,
  //     // 정렬 기능 숨기기
  //     ordering: false,
  //     // 정보 표시 숨기기
  //     info: false,
  //     // 페이징 기능 숨기기
  //     paging: false, 
  //     data: studentAnswerArr,
  //     columns: [
  //         { data: 'id'},
  //         { data: 'point' }
  //     ]});
}
