document.getElementById("createForm").addEventListener("submit", async function(e) {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    const csrfToken = form.querySelector('[name="csrfmiddlewaretoken"]').value;

    try {


const response = await fetch("create", {
    method: "POST",
    headers: {
        "X-CSRFToken": csrfToken
    },
    body: formData
});

        const result = await response.json();
        console.log(result)
        if (response.ok) {
            console.log("Успішно створено:", result);
            form.reset();
        } else {
            console.error(result);
        }

    } catch (error) {
        console.error("Помилка:", error);
    }
});