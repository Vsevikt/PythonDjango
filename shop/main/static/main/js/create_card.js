
document.getElementById("createForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);
    const csrfToken = form.querySelector('[name="csrfmiddlewaretoken"]').value;

    const fields = ["title", "image", "description", "tags"];

    // Очищаем ошибки предыдущей отправки
    fields.forEach(field => {
        const container = document.getElementById(`${field}-errors`);
        if (container) {
            container.textContent = "";
        }
    });

    document.getElementById("form-message").textContent = "";

    try {
        const response = await fetch(form.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken
            },
            body: formData
        });

        const result = await response.json();

        if (response.ok && result.success) {
            form.reset();
            location.reload();
            return;
        }

        // Выводим ошибки конкретных полей из Django forms.py
        if (result.errors) {
            Object.entries(result.errors).forEach(([field, messages]) => {
                const container = document.getElementById(`${field}-errors`);

                if (container) {
                    container.textContent = messages.join(" ");
                }
            });
        } else {
            document.getElementById("form-message").textContent =
                result.error || "Не вдалося створити картку.";
        }

    } catch (error) {
        console.error("Помилка:", error);

        document.getElementById("form-message").textContent =
            "Помилка з'єднання із сервером.";
    }
});

document.querySelectorAll('.tag-button').forEach(button => {
    button.addEventListener('click', () => {
        button.classList.toggle('active');
    });
});
