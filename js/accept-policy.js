const btnDecline = document.querySelector(".btn__decline");
const btnGo = document.querySelector(".btn__go");
const acceptPolicy = document.querySelector(".accept__policy");

if(btnGo) {
  btnGo.addEventListener("click", (e) => {
    e.preventDefault();
    acceptPolicy.style.display = "none";
  });
};

if(btnDecline) {
  btnDecline.addEventListener("click", (e) => {
    location.assign("https://m.facebook.com/Escrowme-2387271738222517/");
  });
}


window.addEventListener("load", (e) => console.log("hello"));