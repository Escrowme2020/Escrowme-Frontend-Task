let showPassword = document.querySelectorAll('.showP')
showPassword.forEach(i=>{
	i.addEventListener('click', toggleShow)
})
function toggleShow(e) {
	let x = e.target.parentElement.children.length
	let value = e.target.parentElement.children[x-2]
	if(value.getAttribute('type') == 'password'){
		value.setAttribute('type', 'text')
		e.target.innerText = 'hide'
	} else {
		value.setAttribute('type', 'password')
		e.target.innerText = 'show'
	}
}