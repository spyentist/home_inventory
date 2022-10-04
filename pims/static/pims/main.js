function doInputOutput() {
    let date = new Date();
    let weekDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"];
    let weekDay = weekDays[date.getDay()];
    let dayNum = date.getDate();
    let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    let month = months[date.getMonth()];
    let year = date.getUTCFullYear();

    let display = weekDay + ", " + dayNum + " " + month + ", " + year;

    //Footer information
    document.getElementById("curdate").textContent = display;
    document.getElementById("year").innerHTML = year;
    
    // Holiday variables
    let icons = document.querySelectorAll('.sub_icons');
    // Holiday Styling
    if (icons.length != 0) {
        console.log(month);
        icons.forEach( function (icon) {
    switch (month) {
        case 'January':
            icon.classList.toggle('wedding');
            break;
        case 'February':
            icon.classList.toggle('valentines');
            break;    
        case 'October':
            icon.classList.toggle('halloween');
            break;
        case 'November':
            icon.classList.toggle('thanksgiving');
            break;
        case 'December':
            icon.classList.toggle("christmas");
            break;       
    }});}


    // Add event listeners for javascript fluidity.
    if(document.querySelector('#adaptiveMenu')){
    document.querySelector('#adaptiveMenu').addEventListener('click', adaptiveMenu);
    }
    if(document.querySelector('#adaptiveSubMenu')){
        document.querySelector('#adaptiveSubMenu').addEventListener('click', adaptiveSubMenu);
    }
        
}


function listSearch() {
    // Declare variables
    let input, filter, ul, li, a, txtValue;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("tableList");
    li = ul.getElementsByTagName('li');

    // Loop through all list items, and hide those who don't match the search query
    for (let i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function listSearchTable() {
    // Declare variables
    let input, filter, td, txtValue;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    td = document.getElementsByClassName('namecol');

    // Loop through all list items, and hide those who don't match the search query
    for (let i = 0; i < td.length; i++) {
        console.log(td);
        a = td[i].getElementsByTagName("a")[0];
        console.log(a);
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            td[i].parentElement.style.display = "";
        } else {
            td[i].parentElement.style.display = "none";
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



function adaptiveSubMenu() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// adaptiveSubMenu Undo
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    let dropdowns = document.getElementsByClassName("dropdown-content");
    for (let i = 0; i < dropdowns.length; i++) {
      let openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
};