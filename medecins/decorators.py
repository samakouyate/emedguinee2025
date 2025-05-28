from django.contrib.auth.decorators import user_passes_test

def medecin_required(view_func):
    """
    Vérifie que l'utilisateur appartient au groupe 'Médecins'.
    """
    return user_passes_test(lambda u: u.is_authenticated and u.groups.filter(name='Médecins').exists())(view_func)
