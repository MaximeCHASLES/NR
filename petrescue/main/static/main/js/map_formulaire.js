const inputVilleNom = document.getElementById('id_ville_nom');
const inputVilleCode = document.getElementById('id_ville_code');
const inputDeptNom = document.getElementById('id_departement_nom');
const inputDeptCode = document.getElementById('id_departement_code');
const inputLatitude = document.getElementById('id_latitude');
const inputLongitude = document.getElementById('id_longitude');


// Options de la carte.
const options = {
    scrollWheelZoom: false
}

// Création d'une instance de Map.
const map = L.map('carte_annonce', options);


// Ajout du fond de carte.
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Options du contrôleur
OPTIONS = {
    initialZoomLevel: 13
}

// Contôleur permettant la localisation.
L.control.locate(OPTIONS).addTo(map);

// Positionnement de la map en arrivant sur la page. Centré sur la France.
const centre = [46.603354, 2.528991];
map.setView(centre, 6);

// 
map.on('click', ajouterMarqueur)


// Ajoute un marqueur sur la carte et actualise les champs du formulaire.
function ajouterMarqueur(event) {
    // Supprimer tous les autres marqueurs de la carte
    map.eachLayer(function(layer) {
        if (layer instanceof L.Marker && layer.options.custom) {
            map.removeLayer(layer);
        }
    });

    const latlng = event.latlng;
    const lat = latlng.lat
    const lng = latlng.lng
    URL = `https://geo.api.gouv.fr/communes?lat=${lat}&lon=${lng}&fields=code,nom,departement,codesPostaux,centre,contour`
    axios.get(URL)
    .then((ville) => {
        const data = ville.data
        if (data.length > 0) {
            const m = L.marker(latlng, {custom: true});
            m.on('click', enleverMarqueur);
            m.addTo(map);
            actualiserFormulaire(data);
        } else {
            alert("Impossible de placer un marqueur ici.")
        }    
    })
    .catch((error) => {
        // Gérer les erreurs de requête vers l'API de géolocalisation
        console.error('Erreur lors de la requête vers l\'API de géolocalisation :', error);
        alert('Une erreur s\'est produite lors de la recherche de l\'emplacement. Veuillez réessayer.');
    });
} // ajouterMarqueur


//
function enleverMarqueur(event) {
    const m = event.target;
    map.removeLayer(m);
    inputLatitude.value = ""
    inputLongitude.value = ""
} // enleverMarqueur


function actualiserFormulaire(data) {
    const villeNom = data[0].nom
    const villeCode = data[0].code
    const deptNom = data[0].departement.nom
    const deptCode = data[0].departement.code
    const latitude = data[0].centre.coordinates[1]
    const longitude = data[0].centre.coordinates[0]
    
    inputVilleNom.value = villeNom
    inputVilleCode.value = villeCode
    inputDeptNom.value = deptNom
    inputDeptCode.value = deptCode
    inputLatitude.value = latitude
    inputLongitude.value = longitude
}


