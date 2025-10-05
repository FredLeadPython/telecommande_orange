# Télécommande TV Orange

Ce projet est une télécommande virtuelle pour les décodeurs TV Orange, développée avec Django.

## Configuration

Avant de lancer l'application, vous devez configurer l'adresse IP de votre décodeur Orange TV.

1.  Ouvrez le fichier `telecommande/views.py`.
2.  Trouvez la ligne `DECODER_IP = "192.168.1.16"`.
3.  Remplacez `"192.168.1.50"` par l'adresse IP de votre décodeur.

## Installation

1.  Clonez le dépôt.
2.  Installez les dépendances : `pip install -r requirements.txt`
3.  Lancez les migrations : `python orange_tv/manage.py migrate`
4.  Démarrez le serveur : `python orange_tv/manage.py runserver`

## Utilisation

Ouvrez votre navigateur à l'adresse `http://127.0.0.1:8000/` pour accéder à la télécommande.

---

# Orange TV Remote Control

This project is a virtual remote control for Orange TV decoders, developed with Django.

## Configuration

Before running the application, you must configure the IP address of your Orange TV decoder.

1.  Open the file `telecommande/views.py`.
2.  Find the line `DECODER_IP = "192.168.1.16"`.
3.  Replace `"192.168.1.50"` with the IP address of your decoder.

## Installation

1.  Clone the repository.
2.  Install the dependencies: `pip install -r requirements.txt`
3.  Run migrations: `python orange_tv/manage.py migrate`
4.  Start the server: `python orange_tv/manage.py runserver`

## Usage

Open your browser to `http://127.0.0.1:8000/` to access the remote control.

---
