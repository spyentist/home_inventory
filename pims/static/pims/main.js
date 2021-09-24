function doInputOutput() {
    let date = new Date();
    let weekDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"];
    let weekDay = weekDays[date.getDay()];
    let dayNum = date.getDate();
    let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    let month = months[date.getMonth()];
    let year = date.getUTCFullYear();
    
    let display = weekDay + ", " + dayNum + " " + month + ", " + year;

    

    document.getElementById("curdate").innerHTML = display;
    document.getElementById("year").innerHTML = year;


    // month = 'January';
    // month = 'December';
    // month = 'October';
    // month = 'February';
    month = 'November';

    // Holiday variables
    let icons = document.querySelectorAll('.sub_icons');
    // Holiday Styling

    for (i in icons) {
        switch (month) {
            case 'December':
                icons[i].classList.add("christmas");
                break;
            case 'October':
                icons[i].classList.add('halloween');
                break;
            case 'February':
                icons[i].classList.add('valentines');
                break;
            case 'November':
                icons[i].classList.add('thanksgiving');
                break;
            case 'January':
                icons[i].classList.add('wedding');
        
        }
    }

}


function listSearch() {
    // Declare variables
    let input, filter, ul, li, a, i, txtValue;
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

function listSearchTableTEST() {
    // Declare variables
    let input, filter, ul, li, a, i, txtValue;
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