// DOM
const userDropdown = document.querySelector(".user__username");

const profileSidebar = document.querySelector(".profile__sidebar");

const headerMenu = document.querySelector(".header__menu");

const navigation = document.querySelector(".navigation");

const landingMenu = document.querySelector(".landing__menu");

const landingLinkContainer = document.querySelector(".landing__link__container");

const sendReceiveHeader = document.querySelector(".send__receive--header");



// User drop down Handler Function
if(userDropdown) {
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
    
}


// User profile Handler function
if(profileSidebar) {
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
}

// Left Drop Down
if(headerMenu) {
  headerMenu.addEventListener("click", e => {
    navigation.classList.toggle('active');
		headerMenu.classList.toggle('active');
	  if(headerMenu.classList.contains('active')){
				headerMenu.children[0].innerHTML = '<i id="bars" class="fas fa-times"></i>';
			} else {
				headerMenu.children[0].innerHTML = '<i id="bars" class="fas fa-bars"></i>';
			}
  });
}

// Landing Drop Down
if(landingMenu) {
  landingMenu.addEventListener("click", e => {
    landingLinkContainer.classList.toggle('active');
		landingMenu.classList.toggle('active');
	  if(landingMenu.classList.contains('active')){
				landingMenu.children[0].innerHTML = '<i id="bars" class="fas fa-times"></i>';
			} else {
				landingMenu.children[0].innerHTML = '<i id="bars" class="fas fa-bars"></i>';
			}
  });
}

// Send Receive Header
if(sendReceiveHeader) {
  sendReceiveHeader.addEventListener("click", (e) => {
    const classValue = e.target.className.split(" ");
    const sendContent = document.getElementById("send__content");
    const receiveContent = document.getElementById("receive__content");
    const sendTab = document.querySelector(".send__tab");
    const receiveTab = document.querySelector(".receive__tab");
    console.log(classValue);
    
    classValue[1] = "";
    // SEND TAB
    if(classValue[0] === "send__tab") {
      // Toggle the send__btc--active class
      
      receiveTab.classList.remove("send__btc--active");
      e.target.classList.add("send__btc--active");
      console.log("receiveTab", receiveTab.classList);
      // Display the tab
      if(sendContent.style.display === '' || sendContent.style.display === 'none') {
        receiveContent.style.display = 'none';
        sendContent.style.display = "grid";
      }
      console.log(e.target.className);
      
    // RECEIVE TAB  
    } else if(classValue[0] === "receive__tab") {
      // Toggle the send__btc--active class
      
      sendTab.classList.remove("send__btc--active");
      e.target.classList.add("send__btc--active");
      
      // Display the tab
      if(receiveContent.style.display === '' || receiveContent.style.display === 'none') {
        sendContent.style.display = "none";
        receiveContent.style.display = "grid";
      }
    
      console.log(e.target.className);
    }
    console.log(e);
  });
}