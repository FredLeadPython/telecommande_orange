from django.shortcuts import render
from django.http import JsonResponse
import requests
import json


DECODER_IP = "192.168.1.16"
BASE_URL = f"http://{DECODER_IP}:8080/remoteControl/cmd"

def remote_control_view(request):
    """Affiche la page HTML de la télécommande."""
    return render(request, 'telecommande/remote.html')

def send_command_view(request):
    """Reçoit une requête AJAX et envoie la commande au décodeur."""
    if request.method == 'POST':
        try:
            # Récupérer le code de la touche depuis le corps de la requête POST
            data = json.loads(request.body)
            key_code = data.get('key')

            if not key_code:
                return JsonResponse({'status': 'error', 'message': 'Code de touche manquant'}, status=400)

            # Construction des paramètres de la requête GET [cite: 17]
            params = {
                'operation': '01', # Simule un appui sur une touche [cite: 21]
                'key': key_code,
                'mode': '0' # Simule un appui court [cite: 27]
            }

            # Envoi de la requête HTTP au décodeur [cite: 10]
            response = requests.get(BASE_URL, params=params, timeout=2)
            response.raise_for_status() # Lève une exception si la requête échoue

            return JsonResponse({'status': 'success', 'message': f'Commande {key_code} envoyée'})

        except requests.exceptions.RequestException as e:
            return JsonResponse({'status': 'error', 'message': f"Erreur de communication avec le décodeur : {e}"}, status=500)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"Erreur inattendue : {e}"}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'}, status=405)