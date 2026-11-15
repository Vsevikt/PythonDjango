document.addEventListener('DOMContentLoaded', () => {
    const avatarInput = document.querySelector('input[name="avatar"]');
    const avatarImage = document.getElementById('avatarPreview');

    if (avatarInput && avatarImage) {
        avatarInput.addEventListener('change', (event) => {
            const file = event.target.files && event.target.files[0];
            if (!file) return;
            if (avatarImage.dataset.previewUrl) URL.revokeObjectURL(avatarImage.dataset.previewUrl);
            const previewUrl = URL.createObjectURL(file);
            avatarImage.dataset.previewUrl = previewUrl;
            avatarImage.src = previewUrl;
            avatarImage.classList.remove('d-none');
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('createForm');
    const cardsList = document.getElementById('cardsList');
    if (!form || !cardsList) return;

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const submitButton = form.querySelector('button[type="submit"]');
        const originalText = submitButton.textContent;
        submitButton.disabled = true;
        submitButton.textContent = 'Збереження...';

        try {
            const response = await fetch(form.action, {
                method: 'POST',
                headers: { 'X-CSRFToken': form.querySelector('[name="csrfmiddlewaretoken"]').value },
                body: new FormData(form),
            });
            const result = await response.json();
            if (!response.ok) throw new Error(result.error || 'Не вдалося створити картку.');

            document.querySelector('.empty-cards-message')?.remove();
            const column = document.createElement('div');
            column.className = 'col d-flex';
            const article = document.createElement('article');
            article.className = 'card listing-card w-100 h-100';

            if (result.image_url) {
                const image = document.createElement('img');
                image.src = result.image_url;
                image.alt = result.title;
                image.className = 'card-img-top';
                article.appendChild(image);
            }

            const body = document.createElement('div');
            body.className = 'card-body d-flex flex-column p-4';
            const heading = document.createElement('h3');
            heading.className = 'card-title h5 fw-semibold';
            heading.textContent = result.title;
            const description = document.createElement('p');
            description.className = 'card-text text-secondary';
            description.textContent = result.description;
            const link = document.createElement('a');
            link.href = result.detail_url;
            link.className = 'btn btn-outline-primary mt-auto align-self-start';
            link.textContent = 'Детальніше';
            body.append(heading, description, link);
            article.appendChild(body);
            column.appendChild(article);
            cardsList.prepend(column);
            form.reset();
            document.getElementById('cards').scrollIntoView({ behavior: 'smooth', block: 'start' });
        } catch (error) {
            let message = form.querySelector('.create-error');
            if (!message) {
                message = document.createElement('p');
                message.className = 'create-error text-danger mb-0';
                form.appendChild(message);
            }
            message.textContent = error.message;
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = originalText;
        }
    });
});
