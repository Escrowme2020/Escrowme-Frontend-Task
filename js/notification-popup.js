const popup = document.querySelector(".popup");
const rejectModal = document.querySelector(".reject__modal");
const verificationDetail  = document.querySelector(".verification__filter--form");

const closePopup = document.querySelector(".close__popup");
const btnCancel = document.querySelector(".btn__cancel");
const btnReject = document.querySelector(".btn__reject");
const btnFilter = document.querySelector(".btn__filter");

const notificationBox = document.querySelectorAll(".notification__box");

const notificationBoxArray = Array.from(notificationBox);

const overlay = document.querySelector(".overlay");



if(notificationBoxArray) {
  const closeDropDown = (e) => {
    if(popup.style.display === "") {
      popup.style.display = "block";
      overlay.style.display = "block";
    } else {
      popup.style.animation = "zoomOut .4s linear";
      popup.style.display = "";
      overlay.style.display = "";
    }
    /*if(e.target.id === "buy") {
    }*/
  };
  
  notificationBoxArray.map((el) => {
    el.addEventListener("click", (e) => closeDropDown(e));
  });
};

if(closePopup) {
  closePopup.addEventListener("click", (e) => {
    popup.style.display = "";
    overlay.style.display = "";
  });
}


// Reject Modal
if(btnReject) {
  const showModal = (e) => {
    e.preventDefault();
    console.log("h");
    if(rejectModal.style.display === "") {
      rejectModal.style.display = "block";
      overlay.style.display = "block";
    } else {
      rejectModal.style.animation = "zoomOut .4s linear";
      rejectModal.style.display = "";
      overlay.style.display = "";
    }
  }
  
  btnReject.addEventListener("click", (e) => showModal(e));
}

if(btnCancel) {
  btnCancel.addEventListener("click", (e) => {
    e.preventDefault();
  rejectModal.style.display = "";
  overlay.style.display = "";
});
}


// Filter btn
if(btnFilter) {
  const showFilter = (e) => {
    e.preventDefault();
    if(verificationDetail.style.display === "") {
      verificationDetail.style.display = "block";
    } else {
      verificationDetail.style.display = "";
    }
  };
  
  btnFilter.addEventListener("click", (e) => showFilter(e))
}