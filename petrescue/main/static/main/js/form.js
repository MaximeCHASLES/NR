const especes = [
    "Chat",
    "Chien",
    "Furet"
]

const inputPosition = document.querySelector('input#position');
const inputCode = document.querySelector('input#code');
const inputEspece = document.querySelector('input#espece');
const divMenu = document.querySelector('.position__menu');
const ulMenuPosition = document.querySelector('.position__menu > ul');
const ulMenuEspece = document.querySelector('.espece__menu > ul');
const liFindMe = document.querySelector('#find-me');


liFindMe.addEventListener('click', geoLocation)
inputPosition.addEventListener('focus', affichageMenu);
inputPosition.addEventListener('blur', masquageMenu);
inputPosition.addEventListener('input', autoCompletion);
inputEspece.addEventListener('focus', affichageMenu);
inputEspece.addEventListener('blur', masquageMenu);


// 
function affichageMenu(event) {
    // divMenu.classList.add('active');
    const nextElement = event.target.nextElementSibling;
    nextElement.classList.add('active');
    if (nextElement.classList.contains('espece')) {
        ulMenuEspece.innerHTML = "";
        especes.forEach(espece => {
            const li = document.createElement('li');
            li.className = "menu__choix";
            li.textContent = espece;
            li.addEventListener('click', updateInputEspece);
            ulMenuEspece.appendChild(li);
        })
    }
} // affichageMenu

//
function masquageMenu(event) {
    setTimeout(() => {
        // divMenu.classList.remove('active');
        const nextElement = event.target.nextElementSibling;
        nextElement.classList.remove('active');
    }, 100)
    ;
} // masquageMenu


function updateInputPosition(event) {
    inputPosition.value = event.currentTarget.dataset.ville;
    inputCode.value = event.currentTarget.dataset.code;
} // updateInputPosition

function updateInputEspece(event) {
    inputEspece.value = event.currentTarget.textContent;
} // updateInputEspece


function geoLocation(event) {
    if (!navigator.geolocation) {
        console.log("La géolocalisation n'est pas supportée par votre navigateur.");
    } else {
        console.log("Localisation…");
        navigator.geolocation.getCurrentPosition(geoSuccess, geoError);
    }
} // geoLocation


function geoSuccess(position) {
    console.log("Localisé à (coordonnées) : ");
    console.log([position.coords.latitude,position.coords.longitude]);

    const lat = position.coords.latitude;
    const lng = position.coords.longitude;

    const promise = axios.get(`https://geo.api.gouv.fr/communes?lat=${lat}&lon=${lng}&fields=code,nom,codesPostaux,surface,population,centre,contour`);

    promise.then((response) => {
        console.log("Localisé à (ville) : ");
        const data = response.data[0];
        inputPosition.value = data.nom;
        console.log(data.nom + " (code : " + data.code + ")");
        inputCode.value = data.code;
    })
} // geoSuccess


function geoError() {
    console.log("Impossible de déterminer votre position.");
} // geoError


function autoCompletion(event) {
    const input = event.target.value;
    const promise = axios.get(`https://geo.api.gouv.fr/communes?nom=${input}&fields=departement&boost=population&limit=5`);
    
    promise.then((response) => {
        ulMenuPosition.innerHTML = "";
        const datas = response.data;

        if (datas.length > 0) {
            datas.forEach(data => {
                const li = document.createElement('li');
                li.textContent = `${data.nom} (${data.departement.code})`;
                li.className = "menu__choix";
                li.dataset.ville = data.nom;
                li.dataset.code = data.code;
                li.addEventListener('click', updateInputPosition);
                ulMenuPosition.appendChild(li);   
            })
        } else {
            if (input == "") {
                const li = document.createElement('li');
                li.textContent = "Utiliser ma position";
                li.id = "find-me";
                li.className = "menu__choix";
                li.addEventListener('click', geoLocation);
                ulMenuPosition.appendChild(li)
            } else {
                const li = document.createElement('li');
                li.textContent = "Aucun résultat";
                li.className = "menu__no-result";
                ulMenuPosition.appendChild(li)
            }  
        } 
    })
} // autoCompletion