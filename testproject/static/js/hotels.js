function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}



(function($) {

  // Menu filter
  $("#menu-flters li a").click(function() {
    $("#menu-flters li a").removeClass('active');
    $(this).addClass('active');

    var selectedFilter = $(this).data("filter");


    $(".menu-restaurant").fadeOut();

    setTimeout(function() {
      $(selectedFilter).slideDown();
    }, 300);
  });

  // scrolling to all links in navbar and footer link
  $(".sidenav a").on('click', function(event) {
    var hash = this.hash;
    if (hash) {
      event.preventDefault();
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function() {
        window.location.hash = hash;
      });
    }

  });

  $(".sidenav a").on('click', function() {
		closeNav();
	});

})(jQuery);
