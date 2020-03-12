$(document).ready(function () {
    $(".header h1").click(function () {
        alert("Hello World!");
        console.log("Hello World!");
    })
    $("button1").click(function () {
        $("p1").before("<p>Hello world!</p>");
    })
    $("button2").click(function () {
        $(".after p2").after("<p>Hello world!</p>");
    })
    $("button5").click(function () {
        $(".html p2").html("<p><b>This is an image of the jQuery Logo!!<b><p>");
        $(".html p2").addClass("red");
    })
    $("button4").click(function () {
        $(".attr img").attr("width", "700");
    })

    $("button3").click(function () {
        $("input:text").val("Mary Jones");
    })

    $("button6").click(function () {
        $(".text p4").text("Hello Coding Dojo!");
        $(".text p4").addClass("red");
    })
    $("button7").click(function () {
        $(".data").data("greeting", "Hello Mary!");
    })
    $("button8").click(function () {
        alert($(".data").data("greeting"));
    })
})