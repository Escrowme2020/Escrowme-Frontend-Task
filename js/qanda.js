const questionAnswerTab = document.querySelectorAll(".question__answer__tab");

const questionAnswerTabArray = Array.from(questionAnswerTab);

const answerContent = document.querySelectorAll(".answer__content");

const answerContentArray = Array.from(answerContent);

const plus = document.querySelectorAll(".plus");

const plusArray = Array.from(plus);




if(questionAnswerTab) {
  const changePlus = (i) => {
    if(plusArray[i].textContent === "+") {
      plusArray[i].textContent = "-";
    } else {
      plusArray[i].textContent = "+";
    }
  }
  
  const questionAnswerTabFunction = (e, i) => {
    if(e.target.className === "plus") {
      answerContentArray[i].classList.toggle("answer__content__active");
      changePlus(i);
    }
  };
  
  plusArray.map((el, i) => {
    el.addEventListener("click", (e) => questionAnswerTabFunction(e, i));
  });
}
  /*
  .addEventListener("click", (e) => {
    if(e.target.className === "question__answer__tab") {
      console.log(e.target);
    }
  });*/