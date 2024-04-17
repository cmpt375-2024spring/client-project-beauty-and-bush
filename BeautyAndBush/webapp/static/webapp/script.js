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
    var email = $('#email').val();
    if (email) {

        Email.send({

            })
    }
}

function sendEmail() {
    var name = $('#name').val();
    var email = $('#email').val();
    var phone = $('#phone').val();
    var question = $('#question').val();

    // Check if all fields are filled
    if (name && email && phone && question) {
        var body = 'Name: ' + name + '<br>Email: ' + email + '<br>Phone: ' + phone + '<br>Question: ' + question;

        Email.send({
            SecureToken: "3f405439-2429-4ee3-8d35-d1488b532739",
            To: 'shreeyamaskey.1@gmail.com', //will have to change it to slc@empirebodywaxing.com
            From: "shreeyamaskey.1@gmail.com", //change email
            Subject: "New Inquiry Contact Form From " + name,
            Body: body
        }).then(
            message => {
                if (message === 'OK' || message === 'Sent') {
                    console.log(message);
                    console.log(body);
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
