window.onload = function () {
alert('hi');
const namesto = localStorage.getItem("fullname");
document.getElementById('fullNames').innerHTML = namesto;
};


