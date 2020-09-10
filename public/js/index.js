// DOM
const userDropdown = document.querySelector(".user__username");

const profileSidebar = document.querySelector(".profile__sidebar");



// User drop down Handler Function
userDropdown.addEventListener("click", () => {
  const el = document.querySelector(".drop__down");
  const down = document.getElementById('down');
  
  if(el.style.display === "") {
    el.style.display = "grid";
    down.className = "fas fa-angle-up";
  } else if (el.style.display === "grid") {
    el.style.display = "";
    down.className = "fas fa-angle-down";
  };
});


// User profile Handler function
profileSidebar.addEventListener("click", e => {
  const el = Array.from(document.querySelectorAll(".profile__sidebar--text"));
  
    if(e.target.id !== "") {
      const tar = e.target;
      el.forEach(arr => arr.classList.remove("profile__active"));
    
      if(tar.id === "0") {
        el[0].classList.add("profile__active");
      } else if (tar.id === "1") {
        el[1].classList.add("profile__active");
      } else if (tar.id === "2") {
        el[2].classList.add("profile__active");
      } else if (tar.id === "3") {
        el[3].classList.add("profile__active");
      }
    }
});