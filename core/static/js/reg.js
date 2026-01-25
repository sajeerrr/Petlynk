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
    document.querySelectorAll('.forms-container input, .reset-card input').forEach(input => {
        let placeholderText = "";
        const name = input.name.toLowerCase();

        if (name.includes('username')) placeholderText = "Username (e.g. Fluffy)";
        else if (name.includes('email')) placeholderText = "Email (e.g. pet@love.com)";
        else if (name.includes('password')) placeholderText = "Password";
        else if (input.placeholder) placeholderText = input.placeholder;
        else placeholderText = input.name.charAt(0).toUpperCase() + input.name.slice(1);

        input.placeholder = ""; // Clear existing to prevent ghosting
        input.placeholder = placeholderText;
        input.style.background = 'transparent';
        input.style.border = 'none';
        input.style.width = '100%';

        // Remove error state on input
        input.addEventListener('input', () => {
            const field = input.closest('.input-field');
            if (field) field.classList.remove('error-state');
        });
    });

    // Handle Professional Form Validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            let isValid = true;
            const requiredInputs = form.querySelectorAll('input[required]');

            requiredInputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    const field = input.closest('.input-field');
                    if (field) {
                        field.classList.add('error-state');
                        // Trigger shake
                        field.classList.add('shake');
                        setTimeout(() => field.classList.remove('shake'), 500);
                    }
                }
            });

            if (!isValid) {
                e.preventDefault();
                console.log("Form check: Missing required fields.");
            }
        });
    });
});
