function onSignIn(googleUser) {
    "use strict";
    var profile = googleUser.getBasicProfile();
    $(".g-signin2").css("display", "none");//hide sign in buttton
    $(".data").css("display", "block");//diplay profile data
    $("#profile_picture").attr('src',profile.getImageUrl());//display profile picture
    $("#email").text(profile.getEmail());//display email text information
}