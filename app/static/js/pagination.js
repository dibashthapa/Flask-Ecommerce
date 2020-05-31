
$(document).on("ready", function(){
	const url= window.location.href
	const params = url.split("?")
	if (params.length ==1){
		window.location.href="?page=1"
	}
	
	if (params[1] != undefined){
	 page = params[1].split("=")
	}
	else {
		page = 1
	}

	 if(page[1] !=1){
	 	 $(".prev-btn").attr("href", `?page=${page[1]-1}`);
	 }
	 else {
	 	$(".prev-btn").attr("href","")
	 }
	
	$(".next-btn").attr("href", `?page=${parseInt(page[1])+1}`)
})

