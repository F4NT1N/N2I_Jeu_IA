// Récupère toutes les cellules
const cells = document.querySelectorAll('.cell');

let selectedImage = null; // Image actuellement sélectionnée
let selectedCellIndex = null; // Index de la cellule contenant l'image sélectionnée

// Fonction pour réinitialiser les couleurs et la sélection
function resetCellColors() {
  cells.forEach(cell => {
    cell.style.backgroundColor = ''; // Réinitialise la couleur
    cell.classList.remove('reachable'); // Retire la classe "atteignable"
  });
  selectedImage = null;
  selectedCellIndex = null;
}

// Fonction pour détecter les cases atteignables
function highlightReachableCells(index) {
  const rowSize = 6; // Nombre de colonnes dans la grille
  const reachableIndices = [
    index - rowSize, // Haut
    index + rowSize, // Bas
    index - 1,       // Gauche
    index + 1        // Droite
  ];

  reachableIndices.forEach(i => {
    if (i >= 0 && i < cells.length) { // Vérifie que l'indice est valide
      const isSameRow = Math.floor(index / rowSize) === Math.floor(i / rowSize);
      const isAdjacent = i === index - 1 || i === index + 1;

      // Vérifie les cases adjacentes et vides
      if ((isAdjacent && isSameRow) || !isAdjacent) {
        const cell = cells[i];
        if (!cell.querySelector('img')) { // Vérifie que la cellule est vide
          cell.style.backgroundColor = '#ffcccb'; // Couleur des cases atteignables
          cell.classList.add('reachable'); // Ajoute la classe "atteignable"
        }
      }
    }
  });
}

// Ajoute les événements sur les cellules
cells.forEach((cell, index) => {
  // Événement clic sur une cellule contenant une image
  const image = cell.querySelector('img');
  if (image) {
    cell.addEventListener('click', () => {
      if (!selectedImage) { // Si aucune image n'est encore sélectionnée
        resetCellColors(); // Réinitialise les couleurs
        selectedImage = image; // Définit l'image sélectionnée
        selectedCellIndex = index; // Définit l'index de la cellule
        highlightReachableCells(index); // Met en surbrillance les cases atteignables
      }
    });
  }

  // Événement clic sur une cellule vide
  cell.addEventListener('click', () => {
    if (selectedImage && cell.classList.contains('reachable')) {
      cell.appendChild(selectedImage); // Déplace l'image
      resetCellColors(); // Réinitialise tout
    }
  });
});
