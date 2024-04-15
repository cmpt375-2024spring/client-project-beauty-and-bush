$(document).ready(function() {
    $('.menu-toggle').click(function() {
        $('nav ul').toggleClass('nav-list-open'); // Add or remove class to trigger animation
    });
});

// Function to show the custom pop-up
function showPopupSent() {
    document.getElementById('sent-popup').style.display = 'block';
    setTimeout(hidePopupSent, 3000); // Hide popup after 3 seconds (3000 milliseconds)
}

// Function to hide the custom pop-up
function hidePopupSent() {
    document.getElementById('sent-popup').style.display = 'none';
}

function showPopupNotSent() {
    document.getElementById('not-sent-popup').style.display = 'block';
    setTimeout(hidePopupNotSent, 3000); // Hide popup after 3 seconds (3000 milliseconds)
}

// Function to hide the custom pop-up
function hidePopupNotSent() {
    document.getElementById('not-sent-popup').style.display = 'none';
}

// Ensure DOM is ready before accessing elements
$(document).ready(function() {
    $('#contact-form').submit(function(event) {
        event.preventDefault(); // Prevent form submission
        sendEmail();
    });
});

function sendEmail() {
    var name = $('#name').val();
    var email = $('#email').val();
    var phone = $('#phone').val();
    var question = $('#question').val();

    // Check if all fields are filled
    if (name && email && phone && question) {
        var body = 'Name: ' + name + '<br>Email: ' + email + '<br>Phone: ' + phone + '<br>Question: ' + question;

        Email.send({
            SecureToken: "625dfccc-8afe-4d13-848f-6969dcf976f9",
            // Host : "smtp.elasticemail.com",
            // Username : "shreeyamaskey.1@gmail.com",
            // Password : "6D5AD82E2A24EE0499D7FD418093F1F41EFA",
            To: 'shreeyamaskey.1@gmail.com',
            From: "shreeyamaskey.1@gmail.com",
            Subject: "New Inquiry Contact Form From " + name,
            Body: body
        }).then(
            message => {
                if (message === 'OK' || message === 'Sent') {
                    console.log(message);
                    // Show success message
                    showPopupSent();
                    $('#contact-form')[0].reset(); // Reset form after successful submission
                } else {
                    // Show error message
                    console.error(message);
                    showPopupNotSent();
                }
            }
        );
    }
}
