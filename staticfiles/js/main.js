(function($) {

    $(".toggle-password").click(function() {

        $(this).toggleClass("zmdi-eye zmdi-eye-off");
        var input = $($(this).attr("toggle"));
        if (input.attr("type") == "password") {
          input.attr("type", "text");
        } else {
          input.attr("type", "password");
        }
      });

})(jQuery);



// Show the popup after 5 seconds
window.onload = function () {
    setTimeout(function () {
        const popup = document.getElementById('popup');
        popup.style.display = 'flex'; // Show the popup
    }, 5000); // 5000ms = 5 seconds

    // Close the popup when the close button is clicked
    document.getElementById('closePopup').onclick = function () {
        const popup = document.getElementById('popup');
        popup.style.display = 'none'; // Hide the popup
    };
};

// Show the popup end