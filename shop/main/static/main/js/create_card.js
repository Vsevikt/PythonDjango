document.getElementById("createForm").addEventListener("submit", async function(e) {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
     const data = Object.fromEntries(formData.entries());

    const csrfToken = form.querySelector('[name="csrfmiddlewaretoken"]').value;
    const json = JSON.stringify(data)
    try {

const response = await fetch("create", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken
    },
    body: json
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