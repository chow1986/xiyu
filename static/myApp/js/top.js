// JavaScript Document
$(function(){
	$(".tab ul li").hover(function(){
		$(this).addClass("tab_hover");
		$(".tab ul li:first").removeClass(" tab_lia");
		},function(){
			$(this).removeClass(" tab_hover");
			$(".tab ul li:first").addClass(" tab_lia");})})
	