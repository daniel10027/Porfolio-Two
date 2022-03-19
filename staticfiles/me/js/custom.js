/*global $, window, WOW*/

$(function () {
    
    "use strict";
    
    var win = $(window),
        htmlBody = $("html, body"),
        nav = $(".vertical-nav"),
        progressCheck = false;
		
    /*========== Loading  ==========*/
    $('.preloader').delay(200).fadeOut(700, function () {
        $(this).remove();
    });
	
	/*========== Color Switcher  ==========*/
    $(".switch-button").on("click", function () {
        $(this).addClass("hide");
        $(".switched-styles").addClass("show");
    });
    
    $(".switched-styles .hide-button").on("click", function () {
        $(this).parent().removeClass("show");
        $(".switch-button").removeClass("hide");
    });
    
    $(".switched-styles ul li").on("click", function () {
        $("link[href*='color']").attr("href", "css/colors/" + $(this).data('color') + "_color.css");
    });
    
    /*========== Active Menu  ==========*/
    $(".vertical-nav .toggle-menu").on("click", function () {
        nav.toggleClass("menu-active");
    });
    
    /*========== Smooth Scroll  ==========*/
    $(".vertical-nav .mini-menu > ul li a").on("click", function (e) {
        e.preventDefault();
		var selector = $(this);
        $(".vertical-nav").removeClass('menu-active');
		$(selector.attr('href')).addClass('active').siblings("section").removeClass('active');
    });
	
	/*========== Skills Progress ==========*/
	function skillsPogress() {
        $(".progress-container").each(function () {
            var progressBar = $(this).find(".progress-bar");
            progressBar.css("width", progressBar.attr("aria-valuenow") + "%");
        });
    }
    
    if (!progressCheck && $('#about').scrollTop() >= $(".skills").offset().top) {
        skillsPogress();
        progressCheck = true;
    }
    
    $('#about').on("scroll", function () {
		
		console.log($('#about').scrollTop());
        
        if (!progressCheck && $('#about').scrollTop() >= $(".skills").offset().top) {
            skillsPogress();
            progressCheck = true;
        }
        
    });
    
    /*========== Start Portfolio Trigger Filterizr Js  ==========*/
    $("#control li").on('click', function () {
        $(this).addClass('active').siblings("li").removeClass('active');
    });
    // The Filterizr
    $('#filtr-container').filterizr({
        animationDuration: 0.4
    });
    
    /*========== Start Magnigic Popup Js ==========*/
    if ($('.portfolio-content .item')[0]) {

        $('.portfolio-content .item').magnificPopup({
            delegate: '.icon-img',
            type: 'image',
            gallery: {
                enabled: true
            }
        });
    }
	
	/*========== Ajax Contact Form  ==========*/
	$('.contact-form').on("submit", function () {
		
		var myForm = $(this),
			data = {};
		
		myForm.find('[name]').each(function() {
			
			var that = $(this),
				name = that.attr('name'),
				value = that.val();
			
			data[name] = value;
			
		});
		
		$.ajax({
			
			url: myForm.attr('action'),
			type: myForm.attr('method'),
			data: data,
			success: function (response) {
				
				if (response == "success") {
								
					$(".contact-form").find(".form-message").addClass("success");
					$(".form-message span").text("Message Sent!");
					
				} else {
					
					$(".contact-form").find(".form-message").addClass("error");
					$(".form-message span").text("Error Sending!");
					
				}
			}
			
		});
		
		return false;
		
	});
});