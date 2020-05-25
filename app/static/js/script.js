
document.querySelector(".user-icon").addEventListener("click",function(){
     var profileOptions= document.getElementById("profile-options");
      if (profileOptions.style.visibility==="visible"){
      profileOptions.style.visibility="hidden";
      }
      else {
      profileOptions.style.visibility="visible";
      }
})

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
  if (query !==""){
  request.open('GET', 'http://localhost:5000/api/products/groceries/'+query)
  request.onload= function(){
  var data = JSON.parse(request.responseText)
  data.forEach(result => {
      appendElement(result.name)
})
   }
  request.send()
  } 

  
if (e.keyCode === 13 ){
  e.preventDefault()
  var query = document.querySelector("input").value;
 window.location.href="/search?keyword="+query.toLowerCase() 
  console.log(query)
}
})


