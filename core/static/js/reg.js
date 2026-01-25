document.addEventListener('DOMContentLoaded', () => {
    const sign_in_btn = document.querySelector("#sign-in-btn");
    const sign_up_btn = document.querySelector("#sign-up-btn");
    const container = document.querySelector(".auth-container");

    if (sign_up_btn && sign_in_btn && container) {
        sign_up_btn.addEventListener("click", () => {
            container.classList.add("sign-up-mode");
        });

        sign_in_btn.addEventListener("click", () => {
            container.classList.remove("sign-up-mode");
        });
    }

    // Customize input fields from Django form to match design
    document.querySelectorAll('.sign-up-form input').forEach(input => {
        let placeholderText = "";
        const name = input.name.toLowerCase();

        if (name.includes('username')) placeholderText = "Username (e.g. Fluffy)";
        else if (name.includes('email')) placeholderText = "Email (e.g. pet@love.com)";
        else if (name.includes('password')) placeholderText = "Password";
        else placeholderText = input.name.charAt(0).toUpperCase() + input.name.slice(1);

        input.placeholder = placeholderText;
        input.style.background = 'transparent';
        input.style.border = 'none';
        input.style.width = '100%';
    });
});
