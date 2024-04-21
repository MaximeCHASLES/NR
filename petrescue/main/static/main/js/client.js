// const form = document.querySelector('form#filtres-resultats')

// form.addEventListener('submit', soumissionForm)

// const csrftoken = "B5l606N7jq4LjacmgSjGV2XG5bajicux"


// function soumissionForm(event) {
//     // Évite le rechargement de la page.
//     event.preventDefault()

//     // Création d'un objet FormData rattaché au formulaire.
//     const formData = new FormData(this)

//     // Convertir FormData en objet JavaScript.
//     const data = {};
//     for (const [name, value] of formData.entries()) {
//         data[name] = value;
//     }

//     // Affiche dans la console les données du formulaire.
//     console.log(data)

//     // 
//     axios({
//         method: 'post',
//         url: 'http://127.0.0.1:8000/petrescue/found',
//         data: formData,
//         headers: {
//             'X-CSRFToken': csrftoken
//           }
//       }).then(function(response) {
//         // Gérer la réponse si nécessaire
//         console.log(response.data)
//         document.body.innerHTML = response.data
//     })
//     .catch(function(error) {
//         // Gérer les erreurs si nécessaire
//         //console.error(error);
//     });
// }


