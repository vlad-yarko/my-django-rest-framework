import logging

from django.dispatch import receiver, Signal
from django.db.models.signals import post_save
from .models import CustomUser

from google import genai


vasya_signal = Signal()


@receiver(vasya_signal)
def vasya_signal_llm(sender, **kwargs):
    client = genai.Client(api_key="AIzaSyDcSjAhFNfgg06LD7qFSPrwTYe8pB7kWj0")
    
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Vasya"
    )
    
    logging.info(resp.text)
    


# @receiver(post_save, sender=CustomUser)
# def user_post_save_signal(sender, instance, created, **kwargs):
#     if created:
#         CustomUser.objects.create(**kwargs)
#     else:
#         print("Vasya")
        
        
# vasya_signal = Signal()


# @receiver(vasya_signal)
# def vasya_signal_receiver(sender, user, **kwargs):
#     print("VASYA")


# from django.dispatch import Signal, receiver
# from django.db.models.signals import post_save
# from .models import CustomUser, Profile


# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# # Створення власних сигналів
# user_logged_in_first_time = Signal()
# order_status_changed = Signal()
# payment_completed = Signal()


# # Відправка власного сигналу
# def mark_first_login(user):
#     # Логіка перевірки першого входу
#     if not hasattr(user, 'profile') or not user.profile.first_login_completed:
#         user_logged_in_first_time.send(sender=user.__class__, user=user)


# # Обробка власного сигналу
# @receiver(user_logged_in_first_time)
# def handle_first_login(sender, user, **kwargs):
#     """Обробка першого входу користувача"""
#     profile = Profile.objects.create(user=user)
#     print(f"Користувач {user.username} зайшов вперше!")
#     print("AAAAAAAAAAAAAAaa")
#     print("AAAAAAAAAAAAA")
    
#     # Тепер можна відразу оновити поле
#     profile.first_login_completed = True
#     profile.save()

















# # # from django.db.models.signals import post_save, post_delete
# # # from django.dispatch import receiver, Signal
# # # from django.core.mail import send_mail
# # # from django.conf import settings

# # # from .models import Profile, CustomUser

# # # @receiver(post_save, sender=CustomUser)
# # # def create_user_profile(sender, instance, created, **kwargs):
# # #     """
# # #         Автоматично створює профіль для нового користувача
# # #         """
# # #     if created:
# # #         profile = Profile.objects.create(user=instance)
# # #         print(f"Створено профіль для користувача {instance.username}")

# # #         # Відправка welcome email (опціонально)
# # #         try:
# # #             send_mail(
# # #                 'Ласкаво просимо!',
# # #                 f'Привіт {instance.first_name or instance.username}, ласкаво просимо на наш сайт!',
# # #                 settings.DEFAULT_FROM_EMAIL,
# # #                 [instance.email],
# # #                 fail_silently=True,
# # #             )
# # #             print(f"Welcome email відправлено для {instance.email}")
# # #         except Exception as e:
# # #             print(f"Помилка відправки email: {e}")


# # # @receiver(post_save, sender=CustomUser)
# # # def save_user_profile(sender, instance, **kwargs):
# # #     """
# # #     Зберігає профіль при оновленні користувача
# # #     """
# # #     try:
# # #         # Перевіряємо, чи існує профіль
# # #         if hasattr(instance, 'profile'):
# # #             instance.profile.save()
# # #             print(f"Профіль збережено для користувача {instance.username}")
# # #         else:
# # #             # Якщо з якихось причин профіль не існує, створюємо його
# # #             Profile.objects.create(user=instance)
# # #             print(f"Профіль не існував для {instance.username}, створено новий")
# # #     except Exception as e:
# # #         print(f"Помилка збереження профілю для {instance.username}: {e}")


# # from django.db.models.signals import pre_delete, pre_save, post_delete, post_save
# # from django.dispatcher import receiver

# # from models import CustomUser



# # @receiver(pre_save, sender=CustomUser)
# # def prepare_data_for_user(sender, instance, **kwargs):
# #     """Підготовка даних перед збереженням користувача"""
# #     # Нормалізація email
# #     if instance.email:
# #         instance.email = instance.email.lower().strip()

# #     # Логування змін
# #     if instance.pk:  # Якщо це оновлення існуючого користувача
# #         print(f"Оновлення користувача: {instance.username}")
# #     else:  # Якщо це новий користувач
# #         print(f"Створення нового користувача: {instance.username}")


# # @receiver(post_save, sender=CustomUser)
# # def user_saved_handler(sender, instance, created, **kwargs):
# #     """Обробка після збереження користувача"""
# #     if created:
# #         print(f"Новий користувач створений: {instance.username}")
# #         # Тут можна додати логіку створення профілю, надсилання welcome email тощо
# #     else:
# #         print(f"Користувач оновлений: {instance.username}")


# # @receiver(pre_delete, sender=CustomUser)
# # def backup_user_data(sender, instance, **kwargs):
# #     """Резервне копіювання даних перед видаленням"""
# #     print(f"Створюємо резервну копію для користувача: {instance.username}")
# #     # Логіка резервного копіювання

# # @receiver(post_delete, sender=CustomUser)
# # def cleanup_user_files(sender, instance, **kwargs):
# #     """Очищення файлів після видалення користувача"""
# #     print(f"Очищаємо файли користувача: {instance.username}")
# #     # Видалення аватарок, завантажених файлів тощо
