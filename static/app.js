document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("data-form");
    const peopleList = document.getElementById("people-list");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const age = document.getElementById("age").value;

        const newPerson = {
            name,
            email,
            age: parseInt(age),
        };

        await fetch("/addPerson", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(newPerson),
        });

        await fetchPeople();
    });

    async function fetchPeople() {
        const response = await fetch("/getPeople");
        const data = await response.json();

        peopleList.innerHTML = "";

        data.forEach((person) => {
            const li = document.createElement("li");
            let text = `${person.name}`;

            if (person.age) {
                text += ` (${person.age} años)`;
            }

            if (person.email) {
                text += ` - ${person.email}`;
            }

            li.textContent = text;
            peopleList.appendChild(li);
        });
    }

    fetchPeople();
});
