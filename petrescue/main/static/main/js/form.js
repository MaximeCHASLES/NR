const inputLocation = document.querySelector('input#location')
const inputMask = document.querySelector('.input-mask')
const inputList = document.querySelector('.search-list')

inputMask.addEventListener('click', displayList)
inputLocation.addEventListener('input', diplaySuggests)

function displayList(event) {
    event.currentTarget.classList.add("inactive");
    inputList.classList.add('active')

}

function diplaySuggests(event) {
    const suggestList = document.querySelector('.search-list__locate');
    const input = event.target.value;
    suggestList.innerHTML= "";

    url = `https://geo.api.gouv.fr/communes?nom=${input}&fields=departement&boost=population&limit=5`;
    
    // Requête http GET
    axios.get(url)
    .then(function (response) {
        // en cas de réussite de la requête
    console.log(response);
    const datas = response.data

    display(datas)
    

    })
    .catch(function (error) {
    // en cas d’échec de la requête
    console.log(error);
    })
    .finally(function () {
    // dans tous les cas
    });
    
}

function display(datas) {
    datas.forEach(data => {
        const ul = document.querySelector('.search-list__locate');

        const nom = data.nom;
        const dpt = data.departement.code;

        const li = document.createElement('li');
        li.className = "suggestion";
        li.textContent = nom + " (" + dpt + ")"
        
        ul.appendChild(li)

    })
}