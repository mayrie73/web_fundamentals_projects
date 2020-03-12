$(document).ready(function () {
    $(".header h1").click(function () {
        alert("Hello World!");
        console.log("Hello World!");
    })
    $("button1").click(function () {
        $("p1").addClass("red");
    })
    $("button2").click(function () {
        $(".toggle p2").toggle("slow");
    })
    $("button5").click(function () {
        $(".slideToggle img").slideToggle("slow");
    })
    $("button4").click(function () {
        $(".slide img").slideUp("slow");
        $(".slide img").slideDown("slow");
    })
    $("button3").click(function () {
        $("p3").append("This is another paragraph");
    })
    $(".addClass h1").click(function () {
        $(".addClass h1").hide("slow");
        $(".addClass h1").show("slow");
    })
    $("button6").click(function () {
        $("p4").hide("slow");
        $("p4").fadeIn("slow");
    })
    $("button7").click(function () {
        $("p5").fadeOut("slow");
        $("p5").show("slow");
    })
})