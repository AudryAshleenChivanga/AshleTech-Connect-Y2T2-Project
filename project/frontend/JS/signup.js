document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm-password').value;
    var agree = document.getElementById('agree').checked;

    if (!agree) {
        alert('You must agree to the terms and conditions to continue.');
        return;
    }

    if (password !== confirmPassword) {
        alert('Passwords do not match.');
        return;
    }

    console.log('Email:', email, 'Password:', password);
    // Implement your API call for sign up here
});
