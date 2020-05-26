
document.querySelector(".user-icon").addEventListener("click",function(){
     var profileOptions= document.getElementById("profile-options");
      if (profileOptions.style.visibility==="visible"){
      profileOptions.style.visibility="hidden";
      }
      else {
      profileOptions.style.visibility="visible";
      }
})