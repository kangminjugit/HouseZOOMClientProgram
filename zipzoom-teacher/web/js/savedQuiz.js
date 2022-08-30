window.onload = async function(){
    var data = await eel.get_problemTable(JSON.parse(localStorage.getItem('classId')), JSON.parse(localStorage.getItem('accessToken')))();
    if(data['status'] === 'success'){
        problemTable = data['data']['quizArr'];
        console.log(problemTable);

        localStorage.setItem('problemTable', JSON.stringify(problemTable));

        dataTable = [];
        problemTable.map((problem, index) => {
            dataTable.push({
                isOX: problem['isOX'],
                problem: problem['problem'],
                btn: `<button type="button" class="btn btn-primary submitBtn" id=${index} onClick="handleClick(this.id)">제출</button>`
            })
        });

        $('#problemTable').DataTable( {        
            // 표시 건수기능 숨기기
            lengthChange: false,
            // 검색 기능 숨기기
            searching: false,
            // 정렬 기능 숨기기
            ordering: false,
            // 정보 표시 숨기기
            info: false,
            // 페이징 기능 숨기기
            paging: false, 
            data: dataTable,
            columns: [
                {data: 'isOX'},
                { data: 'problem' },
                {data:'btn'}
            ]});
    }

}

function handleClick(clicked_id){
    const elt = JSON.parse(localStorage.getItem('problemTable'));

    if(elt[clicked_id]['isOX']){
        var {classId, teacherID, accessToken, problem, answer, timeLimitMin, timeLimitSec, point, badgeSubject, badgeDescription} = elt[clicked_id];
        eel.giveOXQuiz(classId, teacherID, accessToken, problem, answer, timeLimitMin, timeLimitSec, point, badgeSubject, badgeDescription);
    }else{
        var {classId, teacherID, accessToken, problem,choice, answer, timeLimitMin, timeLimitSec, point, badgeSubject, badgeDescription} = elt[clicked_id];
        eel.giveChoiceQuiz(classId, teacherID, accessToken, problem, choice, answer, timeLimitMin, timeLimitSec, point, badgeSubject, badgeDescription);
    }
        
}