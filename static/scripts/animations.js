// The script below makes the page blur onload for 
// Cool loading effect when switching / loading pages
window.onload = () => { //Page blurring
    body = document.getElementsByTagName('BODY')[0]           // Asigning the BODY to the var body
    loadingDiv = document.getElementsByClassName('center')[0] // Loading div, This will be neccesery to remove it
    const anchors = document.querySelectorAll('a');           // When clicked on a tags it will run the blur function
  
    setTimeout(() => {
        body.classList.remove('blur-page'); 
        body.classList.remove('auto-blur-page'); 
        loadingDiv.classList.add('remove-object')
        body.classList.add('unBlur-page'); 
    }, 100);
    
    for (let i = 0; i < anchors.length; i++) {
      const anchor = anchors[i];
  
      anchor.addEventListener('click', e => {
        e.preventDefault();
        let target = e.target.href;
        
        body.classList.remove('unBlur-page'); 
        body.classList.add('blur-page'); 

  
        setTimeout(() => {
            window.location.href = target;
        }, 500);
      });
    }
}


function makeCross() //Change menu-toggler into a cross when clicked
{
  var line_1 = document.getElementById("menu-layer-1");   
  var line_2 = document.getElementById("menu-layer-2");   
  var header = document.getElementsByTagName("header");
  body = document.getElementsByTagName('BODY')[0]           // Asigning the BODY to the var body
    
  if ( line_1.style.transform == 'rotate(-45deg)' ) {
    var pos = 45;
    $( 'nav' ).hide();
    $( 'h2' ).hide();
    $( 'header' ).width('60px');
    body.classList.remove('auto-blur-page'); 
    body.classList.add('unBlur-page'); 

    turnToCross = true;
  } else {

    body.classList.remove('unBlur-page'); 
    body.classList.add('auto-blur-page'); 
    $( 'header' ).width("100%");
    $( 'nav' ).show();
    $( 'h2' ).show();
    var pos = 0;
    turnToCross = false;
  }
  
  var id = setInterval(frame, 0.1);
  function frame() 
  {
   
    if ( turnToCross )
    {

      if (pos == 0) 
      {
        clearInterval(id);
      } else {

        pos--;
        line_1.style.transform  = 'rotate(-' + pos + 'deg)'; 
        line_2.style.transform  = 'rotate(' + pos + 'deg)'; 
      }

    } else {
    
      if (pos == 45) 
      {
        clearInterval(id);
      } else {
      
        pos++;       
        line_1.style.transform  = 'rotate(-' + pos + 'deg)'; 
        line_2.style.transform  = 'rotate(' + pos + 'deg)'; 
      }

    }
  }

}

$(".code-blocks").click(function(){
  $(this).toggleClass("flip"); 
  $(this).toggleClass("show-code");

  if ( $(this).hasClass('show-code') ) {
    $(this).find(".front").hide();
    $(this).find(".back").show();
  } else {  
    $(this).find(".front").show();
    $(this).find(".back").hide();
  }


});

// The arrow animation script
$(window).scroll(function (event) 
{
  var scroll_client     = $(window).scrollTop();
  var catogorie_height  = $( ".homepage-banner" ).height();
  var button_change     = $( ".jump-btn" ).children('p').hasClass( "arrow-flip" )

  if ( button_change &&  scroll_client < catogorie_height ) 
  {
 
    $(".jump-btn").children('p').toggleClass('arrow-flip');
    
  } else
  if ( !button_change && scroll_client > catogorie_height )
  {
    
    $(".jump-btn").children('p').toggleClass('arrow-flip'); 

  }

});

// The back to categorie function
$(".jump-btn").click(function() {
  window.location.href = '#catogories';
});