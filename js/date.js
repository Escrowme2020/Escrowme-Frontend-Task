const textNodeList = document.querySelectorAll(".count__down__value");
const textArrayList = Array.from(textNodeList);


const time = setInterval(() => {
  // Current Date
  const now = new Date().getTime();
  
  // Future Date
  const countDownDate = new Date("December 20, 2020 11:00:00").getTime();
  
  // Difference of the date
  const difference = countDownDate - now;
  
  // Days
  const days = Math.floor(difference / (1000 * 60 * 60 * 24));
  
  // Hours
  const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  
  // Minutes
  const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
  
  // Second
  const seconds = Math.floor((difference % (1000 * 60)) / 1000);
  
  console.log(days, hours, minutes, seconds);
  
  textArrayList[0].textContent = days;
  textArrayList[1].textContent = hours;
  textArrayList[2].textContent = minutes;
  textArrayList[3].textContent = seconds;
  
  if (difference < 0) {
    clearInterval(x);
  };
}, 1000);