function previewImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById('avatar-preview').src = e.target.result;
        }
        reader.readAsDataURL(input.files[0]);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.profile-form');
    const fieldsWithOther = ['habitat', 'territory', 'personality', 'diet', 'favorite_activity', 'preference'];
    const chipGroups = ['gender', 'energy_level', 'social_style', 'bonding_style', 'activity_cycle', ...fieldsWithOther];

    if (form) {
        // Remove error state on input
        form.querySelectorAll('input, select, textarea').forEach(input => {
            input.addEventListener('input', () => {
                input.classList.remove('error-state');
                const group = input.closest('.mb-4');
                if (group) group.classList.remove('error-state');
            });
        });

        form.addEventListener('submit', (e) => {
            let isValid = true;

            // 1. Check Standard Inputs (Name, Species, Age)
            const textInputs = ['name', 'species', 'age'];
            textInputs.forEach(name => {
                const input = form.querySelector(`[name="${name}"]`);
                if (input && !input.value.trim()) {
                    isValid = false;
                    input.classList.add('error-state');
                    input.classList.add('shake');
                    setTimeout(() => input.classList.remove('shake'), 500);
                }
            });

            // 2. Check Photo Upload
            const imageInput = document.getElementById('id_image');
            const preview = document.querySelector('.profile-pic-wrapper');
            if (imageInput && !imageInput.files[0]) {
                isValid = false;
                preview.classList.add('error-state');
                preview.classList.add('shake');
                setTimeout(() => preview.classList.remove('shake'), 500);
            }

            // 3. Check Chip Groups (Radios)
            chipGroups.forEach(field => {
                const radios = document.querySelectorAll(`input[name="${field}"]`);
                const checked = document.querySelector(`input[name="${field}"]:checked`);
                const groupContainer = radios[0]?.closest('.mb-4');

                if (radios.length > 0 && !checked) {
                    isValid = false;
                    if (groupContainer) {
                        groupContainer.classList.add('error-state');
                        groupContainer.classList.add('shake');
                        setTimeout(() => groupContainer.classList.remove('shake'), 500);
                    }
                }

                // 4. Handle "Other" synchronization and validation
                if (fieldsWithOther.includes(field) && checked && checked.value === "Other") {
                    const customInput = document.getElementById(`custom-${field}-input`);
                    const val = customInput ? customInput.value.trim() : "";
                    if (!val) {
                        isValid = false;
                        if (customInput) {
                            customInput.classList.add('error-state');
                            customInput.classList.add('shake');
                            setTimeout(() => customInput.classList.remove('shake'), 500);
                        }
                    } else {
                        // Crucial: Create a temporary hidden input or update the value for submission
                        // We modify the checked radio's value so it gets sent to Django
                        checked.value = val;
                    }
                }
            });

            if (!isValid) {
                e.preventDefault();
                // Scroll to the first error
                const firstError = document.querySelector('.error-state');
                if (firstError) {
                    firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }
        });

        // Show/Hide Custom Input Boxes for all fields with "Other"
        fieldsWithOther.forEach(field => {
            const radios = document.querySelectorAll(`input[name="${field}"]`);
            const otherContainer = document.getElementById(`other-${field}-container`);
            const customInput = document.getElementById(`custom-${field}-input`);

            if (radios.length > 0 && otherContainer && customInput) {
                radios.forEach(radio => {
                    radio.addEventListener('change', () => {
                        if (radio.value === "Other") {
                            otherContainer.style.display = 'block';
                            customInput.focus();
                        } else {
                            otherContainer.style.display = 'none';
                        }
                    });
                });
            }
        });
    }
});
