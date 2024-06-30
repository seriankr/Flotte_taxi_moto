from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Modèle Utilisateur
class Utilisateur(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='utilisateur_groups',  # Nom unique pour éviter les conflits
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='utilisateur_permissions',  # Nom unique pour éviter les conflits
        blank=True
    )
    
    TYPES_UTILISATEUR = (
         ('admin','Admin'),
         ('manager','Manager'),
         ('chauffeur','Chauffeur'),
    )
    type_utilisateur = models.CharField(max_length=10, choices=TYPES_UTILISATEUR)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True) 
    date_embauche = models.DateField(null=True, blank=True)
    

    
    def __str__(self):
        return self.username
    
  