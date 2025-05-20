from django.core.mail import send_mail, mail_managers, EmailMessage
from django.template.loader import render_to_string


def user_notification_claim_status_change(claim):
    """
    Notifies the user about the status change of their claim.
    """
    subject = f"Changement de statut de votre réclamation"
    message = f"Le statut de votre réclamation a été mis à jour.\n\nStatut: {claim.get_status_display()}" \
              f"\n\nDate de mise à jour: {claim.date_submitted}"
    send_mail(subject, message, from_email=None, recipient_list=[claim.user.email], fail_silently=True)


def manager_notification_new_claim(claim):
    """
    Notifies managers about a new claim.
    """
    subject = f"Nouvelle réclamation de {claim.user.username}"
    message = f"Une nouvelle réclamation a été soumise par {claim.user.username}.\n\nDescription: {claim.description}" \
              f"\n\nStatut: {claim.get_status_display()}\n\nDate de soumission: {claim.date_submitted}"
    mail_managers(subject, message, fail_silently=True)


def welcome_email(user):
    """
    Sends a welcome email to the user.
    """
    subject = "Bienvenue sur notre plateforme"
    html_body = render_to_string("email/email.html", {"user": user})
    email = EmailMessage(subject, body=html_body, to=[user.email])
    email.content_subtype = "html"
    email.attach_file("account/test_pdf.pdf")
    email.send(fail_silently=True)
