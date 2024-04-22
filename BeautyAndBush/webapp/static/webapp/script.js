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
//function for FAQ clickable
function toggleAnswer(question) {
  var answers = document.querySelectorAll('.answer');
  var questions = document.querySelectorAll('.question');

  // Remove bold class from all questions
  questions.forEach(function(q) {
    q.classList.remove('bold');
  });

  // Add bold class to clicked question
  question.classList.add('bold');

  // Hide all answers
  answers.forEach(function(answer) {
    answer.classList.remove('active');
  });

  // Show answer corresponding to clicked question
  question.nextElementSibling.classList.toggle('active');
}


function sendReset() {
    var email = $('#email').val();
    if (email) {
        // Check if email exists in the backend
        checkEmailExistence(email)
            .then(function(response) {
                if (response.exists) {
                    // Email exists, proceed with password reset
                    initiatePasswordReset(email);
                } else {
                    // Email does not exist, show error message
                    alert("No account found with this email. Please try again.");
                }
            })
            .catch(function(error) {
                // Handle error
                console.error("Error checking email existence:", error);
                // Show error message to user
                alert("An error occurred. Please try again later.");
            });
    }
}

function checkEmailExistence(email) {
    // Send an AJAX request to backend to check email existence
    return new Promise(function(resolve, reject) {
        $.ajax({
            url: '/api/check_email_existence/', // Replace with your backend API endpoint
            method: 'GET',
            data: { email: email },
            success: function(response) {
                resolve(response);
            },
            error: function(xhr, status, error) {
                reject(error);
            }
        });
    });
}

function initiatePasswordReset(email) {
    // Generate reset token and URL
    var resetToken = generateRandomToken(16);
    var resetUrl = "https://127.0.0.1:8000/reset_password/?token=" + resetToken;

    // Construct email body
    var body = "You're receiving this email because you requested a password reset for your user account. \nPlease go to the following page and choose a new password: " + resetUrl;

    // Send email
    Email.send({
        SecureToken: "3f405439-2429-4ee3-8d35-d1488b532739",
        To: email,
        From: "tca0103@westminsteru.edu",
        Subject: "Empire Body Waxing Password Reset",
        Body: body
    }).then(
        function() {
            // Redirect to the confirmation page after sending the email
            window.location.href = "/password_reset_confirmation/";
        }
    );
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

function generateRandomToken(length) {
    var charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    var token = '';
    var crypto = window.crypto || window.msCrypto; // Get crypto object for generating random values

    if (crypto && crypto.getRandomValues) {
        var values = new Uint32Array(length);
        crypto.getRandomValues(values);

        for (var i = 0; i < length; i++) {
            token += charset[values[i] % charset.length];
        }
    } else {
        // Fallback to Math.random for browsers not supporting crypto.getRandomValues
        for (var i = 0; i < length; i++) {
            token += charset.charAt(Math.floor(Math.random() * charset.length));
        }
    }

    return token;
}
