function doInputOutput() {
let date = new Date();
let weekDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"];
let weekDay = weekDays[date.getDay()];
let dayNum = date.getDate();
let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
let month = months[date.getMonth()];
let year = date.getUTCFullYear();
let today = weekDay;

let display = weekDay + ", " + dayNum + " " + month + ", " + year;


    document.getElementById("curdate").innerHTML = display;
    document.getElementById("year").innerHTML = year;
}


function listSearch() {
  // Declare variables
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById("tableList");
  li = ul.getElementsByTagName('li');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName("a")[0];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}

function adaptiveMenu() {
  let links = document.getElementById("navigation");
  if (links.className === "navigation") {
      links.className += ".responsive";
  } else {
      links.className = "navigation";
  }
}