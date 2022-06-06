
document.getElementById('class_start_btn').addEventListener('click', () => {
    var accessToken = JSON.parse(localStorage.getItem('accessToken'));
    var studentId = JSON.parse(localStorage.getItem('studentId'));
    var classId = JSON.parse(localStorage.getItem('classId'));
    var name = JSON.parse(localStorage.getItem('name'));
	eel.startClass(studentId, classId, accessToken, name);
});
