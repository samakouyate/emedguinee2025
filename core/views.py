from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

def home_view(request):
    return render(request, 'core/home.html')

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    return render(request, 'core/contact.html')

def legal_view(request):
    return render(request, 'core/legal.html')



from .models import ContactMessage
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # 1. Envoi du message à l'admin
        send_mail(
            f'Nouveau message de {name}',
            f"Nom : {name}\nEmail : {email}\n\nMessage :\n{message}",
            email,
            ['kouyasam273@gmail.com'],
        )

        # 2. Enregistrement dans la base de données
        ContactMessage.objects.create(name=name, email=email, message=message)

        # 3. Envoi d'un email de confirmation personnalisé à l'utilisateur
        subject = "Votre message a bien été reçu - e_medGuinée"
        from_email = 'contact@emedguinee.com'
        to = [email]
        text_content = f"Bonjour {name},\n\nNous avons bien reçu votre message et vous remercions de nous avoir contactés.\n\nVotre message :\n{message}\n\nL’équipe e_medGuinée"
        html_content = f"""
            <div style="font-family:Arial,sans-serif;max-width:600px;margin:auto;">
                <h2 style="color:#2196F3;">Bonjour {name},</h2>
                <p>Nous avons bien reçu votre message :</p>
                <blockquote style="border-left:4px solid #2196F3;padding-left:12px;color:#333;background:#f6f8fa;">{message}</blockquote>
                <p style="margin-top:24px;">Notre équipe vous répondra dans les plus brefs délais.<br>
                <b style="color:#2196F3;">L’équipe e_medGuinée</b></p>
                <hr>
                <small style="color:#888;">Ceci est un message automatique, merci de ne pas y répondre.</small>
            </div>
        """
        email_msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        email_msg.attach_alternative(html_content, "text/html")
        email_msg.send()

        messages.success(request, "Votre message a bien été envoyé. Vous recevrez un email de confirmation.")
        return redirect('contact')
    return render(request, 'core/contact.html')