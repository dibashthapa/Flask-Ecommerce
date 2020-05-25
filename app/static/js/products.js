let counter=0;

const quantity=10;

const url = window.location.href;

const product_table = url.split("/")[4]
window.addEventListener('load',load)
 window.onscroll = function(){
if (window.innerHeight+window.scrollY >= document.body.offsetHeight){
load()
}

}

function load(){
	const start = counter;
	const end = start+quantity-1;
	counter = end+1;
	getProducts(start, end);
}

function getProducts(start,end){
	 request = new XMLHttpRequest();
	 request.open('GET', `/api/products/${product_table}?start=${start}&end=${end}`)
	 request.onload = function(){

	 	var data = JSON.parse(request.responseText)
	 	data.forEach(result=>{
          add_contents(result.img_url, result.name)
	 	})
	 }
	 request.send()
}

function add_contents(img_url, name){
	var products_list = document.querySelector(".products-list");
	var firstDiv = document.createElement("div");
	firstDiv.classList = "images";

	var image = document.createElement("img");
	image.src=img_url;

	var secondDiv= document.createElement("div");
	secondDiv.classList="product-name";

	var thirdDiv = document.createElement("div");
	var a= document.createElement("a");
	a.href=`/products/groceries/${name.toLowerCase()}`;
	var textNode = document.createTextNode(name);
	a.appendChild(textNode);
	thirdDiv.appendChild(a);
	secondDiv.appendChild(thirdDiv);
	firstDiv.appendChild(image);
	firstDiv.appendChild(secondDiv);
	products_list.appendChild(firstDiv);

}