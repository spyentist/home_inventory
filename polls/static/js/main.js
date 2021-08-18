let date = new Date();
let weekDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"];
let weekDay = weekDays[date.getDay()];
let dayNum = date.getDate();
let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
let month = months[date.getMonth()];
let year = date.getUTCFullYear();
let today = weekDay;

let display = weekDay + ", " + dayNum + " " + month + " " + year;


    document.getElementById("curdate").innerHTML = display;
    document.getElementById("year").innerHTML = year;
