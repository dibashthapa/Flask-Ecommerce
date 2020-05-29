
$(document).ready(function() {
    $(document).on('click', '.dropdown-menu', function (e) {
      e.stopPropagation();
    });
	if($('[data-toggle="tooltip"]').length>0) {  // check if element exists
		$('[data-toggle="tooltip"]').tooltip()
	} 

$(".search input").on("keyup", function(e){
    value = $(".search input").val();
    $.ajax({
        url:`/api/products/groceries/${value.toLowerCase()}`
    }).done(function(data){
      showResults(data)
    })

})


function showResults(data){
  var output="";
if(data.length === 0 ){
output = "No Search Results Found"
$(".search-results .container").html(output)
}
else if (data.length <=4 ){
  data.forEach(item => {
   output += `
    <div class="row">
    <div class="col p-2 ml-3">
      <a href="/products/groceries/${item.name}">${item.name}</a>

</div>
    </div>
    `

    $(".search-results").html(output)
  })

}


}

}); 

