
document.body.addEventListener("click", function(){
  document.querySelector(".search_results").style.display = "none"
})


function appendElement(text){
  var div = document.createElement("div");
  var a = document.createElement("a");
  a.href= `/products/groceries/${text.toLowerCase()}`
  var textNode = document.createTextNode(text);
  a.appendChild(textNode)

 
  div.appendChild(a)
  div.classList = "results"
  document.querySelector(".search_results").appendChild(div);
}

function removeElement(){
    var element = document.querySelectorAll(".results")
    for (i=0; i<element.length;i++){
    element[i].parentNode.removeChild(element[i])
    }
  
}

document.getElementsByTagName("input")[0].addEventListener("keypress", function(e){
  var query = e.target.value.toLowerCase();
  if (query === ""){
    removeElement()
    document.querySelector(".search_results").style.display ="none"
  }
  document.querySelector(".search_results").style.display = "block"
  request = new XMLHttpRequest();
  request.open('GET', '/api/products/groceries/'+query)
  request.onload= function(){
  var data = JSON.parse(request.responseText)
  data.forEach(result => {
    removeElement()
      appendElement(result.name, result.img_url)
})

   }
  request.send()

  

})

document.querySelector(".search-button").addEventListener("click", function(){
  var query = document.querySelector("input").value;
window.location.href=`/search?keyword=${query.toLowerCase()}`;

})


