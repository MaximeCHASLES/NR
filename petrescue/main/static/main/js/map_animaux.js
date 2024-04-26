  /////////////
 // ANIMAUX //
/////////////

const divCarte = document.querySelector('div#carte');
const code = divCarte.dataset.code;
const divAnnonces = document.querySelectorAll(".annonce");


// Options de la carte.
const options = {
    scrollWheelZoom: false
}

// Création d'une instance de Map.
const map = L.map('carte', options);

// Positionnement de la carte.
positionnerCarte(code);

// Ajout du fond de carte.
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Positionnnement des marqueurs en fonction des annonces affichés à l'écran.
positionnerMarkers(divAnnonces)


// Pour adapter le positionnement selon la requête (POST ou GET).
function positionnerCarte(code) {
    if (code === "0") {
        const centre = [46.603354, 2.528991];
        map.setView(centre, 6);
    } else {
        setView(code).then((latlng) => {
            map.setView(latlng, 13);
        });
    }
} // positionnerCarte


// Positionnement de la carte en fonction du code ville renvoyé par le serveur.
function setView(code) {
    return new Promise((resolve, reject) => {
        const url = `https://geo.api.gouv.fr/communes?code=${code}&fields=centre`;

        axios.get(url)
            .then((response) => {
                const lat = response.data[0].centre.coordinates[1];
                const lng = response.data[0].centre.coordinates[0];
                resolve([lat, lng]);
            })
            .catch((error) => {
                reject(error);
            })
    })
} // setView


// Positionnement des markers en fonction des annonces renvoyés par le serveur.
function positionnerMarkers(annonces) {
    annonces.forEach(annonce => {
        const lat = annonce.dataset.lat;
        const lng = annonce.dataset.lng;
        const latlng = L.latLng(lat, lng)
        const m = L.marker(latlng)
        m.on('mouseover', highlightOn)
        m.on('mouseout', highlightOff)
        m.addTo(map);
    })
} // positionnerMarkers


// Mise en surbrillance de l'annonce correspondante au marqueur survolé par le curseur.
function highlightOn(event) {
    const lat = event['latlng'].lat
    const lng = event['latlng'].lng
    const annonce = document.querySelector(`.annonce[data-lat="${lat}"][data-lng="${lng}"]`)
    annonce.classList.add('highlight')
    
} // highlightOn


// Enlève la mise en surbrillance de l'annonce lorsque le curseur quitte le marqueur.
function highlightOff(event) {
    const lat = event['latlng'].lat
    const lng = event['latlng'].lng
    const annonce = document.querySelector(`.annonce[data-lat="${lat}"][data-lng="${lng}"]`)
    annonce.classList.remove('highlight')
} // highlightOff


