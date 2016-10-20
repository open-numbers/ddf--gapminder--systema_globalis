
window.onload = function() {
	var lists = document.getElementsByTagName('li');
	for (i = 0; i < lists.length; i++) {
		listItem = lists[i];
		listItem.addEventListener('click', handleClick)
	}
}

function handleClick() {
	var tableDiv = this.getElementsByTagName("div")[0];
	if (tableDiv)
		tableDiv.parentNode.removeChild(tableDiv);
	else {
		var div = document.createElement('div');
		this.appendChild(div);
		fetch(this.textContent + '.html')
			.then((response) => response.text())
			.then((text) => div.innerHTML = text)
	}
}