# GraphOSINT

Outil d'analyse de liens pour l'OSINT. Interface graphique permettant de créer,
relier et organiser des entités (personnes, comptes, adresses, organisations,
etc.) sur un graphe interactif, directement dans le navigateur.

## Fonctionnalités

- Création d'entités et de liens entre entités, avec qualification des liens
- Recherche et mise en évidence dans le graphe
- Fusion d'entités dupliquées
- Annuler / rétablir
- Sauvegarde automatique locale (navigateur)
- Import et export au format JSON
- Export du graphe en PNG et en PDF

## Utilisation

Le fichier `index.html` est autonome et peut être ouvert directement dans un
navigateur.

Une interface Streamlit (`app.py`) est également fournie pour servir cette
page en plein écran :

```
pip install streamlit
streamlit run app.py
```

## Technologies

HTML, CSS et JavaScript, avec les bibliothèques vis-network (graphe),
jsPDF (export PDF) et Phosphor Icons.
