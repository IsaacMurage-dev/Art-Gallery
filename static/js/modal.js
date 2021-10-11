$(document).ready(function(){
$('.my_Img').click(function(){
    $('#Modal_pic').css('display',"block")
    $("#img1").attr('src',$(this).attr('src'));
    $("#caption").html() = $(this).attr('alt');
})

// When the user clicks on <span> (x), close the modal
$(".close").click(function() {
  $('#Modal_pic').css('display',"none");
  })

})
