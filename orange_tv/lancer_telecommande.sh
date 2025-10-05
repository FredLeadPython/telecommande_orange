#!/bin/bash

# Chemin vers le dossier du projet
PROJECT_DIR="$HOME/orange/orange_tv"
cd "$PROJECT_DIR"

# --- MODIFICATION IMPORTANTE ---
# Active l'environnement virtuel.
# VEUILLEZ VÉRIFIER QUE CE CHEMIN EST CORRECT.
# Il pourrait être par exemple $HOME/env/bin/activate ou autre.
VENV_ACTIVATE="$HOME/env/orange/bin/activate"

if [ -f "$VENV_ACTIVATE" ]; then
    source "$VENV_ACTIVATE"
else
    echo "Erreur : Environnement virtuel non trouvé à $VENV_ACTIVATE" > "$PROJECT_DIR/telecommande_server.log"
    exit 1
fi

# Vérifie si le serveur est déjà en cours
if ! pgrep -f "manage.py runserver" > /dev/null
then
    echo "Le serveur n'est pas lancé. Démarrage en arrière-plan..."
    # Lance le serveur avec le python de l'environnement virtuel
    # Les logs sont maintenant dans le dossier du projet
    python manage.py runserver 0.0.0.0:8000 > "$PROJECT_DIR/telecommande_server.log" 2>&1 &
    sleep 2
else
    echo "Le serveur est déjà en cours d'exécution."
fi

# Ouvre le navigateur
echo "Ouverture du navigateur..."
xdg-open http://127.0.0.1:8000