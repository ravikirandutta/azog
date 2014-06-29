$(document).ready(function(){
$("#new_user").click(function(){
  
  $('#sync').addClass('registerMode');
  var speed=220;
   $(' .email').animate({top:'13px'},speed);
  $('#sync .new_user').animate({top:'70px'},speed); 
  $('#sync .password').animate({top:'43px'},speed);
  $('#sync .spinner').animate({top:'370px'},speed);
  $('#sync > span').animate({top:'125px'},speed);
  $('#new_user').val ("Register") ;
});
});


