# Titre du Projet : Gestion des Contacts en Python (Version Basique)
### **Objectif du Projet : **
# Développer une application simplifiée de gestion de contacts en Python qui permet de manipuler les 
# données à l'aide de structures de données basiques telles que les listes et les dictionnaires, sans 
# utiliser de fonctions ni de boucles.

### **Fonctionnalités Requises : **
# 1. **Stockage des contacts :**
#  - Les contacts seront stockés dans une liste.
#  - Chaque contact sera représenté sous la forme d'un dictionnaire avec des clés telles que :
#  - Nom
#  - Prénom
#  - Numéro de téléphone
#  - Adresse email

Contact1 = {"nom": "fadli", "prenon": "nassim", "num_tel": "0671443222" , "add_email" : "n.fadli@gmail.com"}

# 2. **Ajout de contacts :**
# L'utilisateur pourra ajouter manuellement des contacts en créant un nouveau dictionnaire contenant les informations d'un contact, 
# qui sera ensuite ajouté à la liste des contacts.

Contact2 = {"nom": "daraoui", "prenon": "yassine", "num_tel": "0672477137" , "add_email" : " d.yassine90@yahoo.fr "}

# 3. **Affichage des contacts :**
# L'utilisateur pourra afficher les informations d'un ou plusieurs contacts en accédant directement aux données dans la liste.

print(contact2["nom"])  # Outputs: daraoui

# 4. **Modification d’un contact :**
# L'utilisateur pourra modifier les informations d'un contact spécifique en accédant
#  à son dictionnaire dans la liste et en mettant à jour les valeurs associées aux clés.

# Adding a new key-value pair
contact2["ville"] = "rabat"
print(contact2)  # Outputs: {"nom": "daraoui", "prenon": yassine, "num_tel": "0672477137" , "add_email" : " d.yassine90@yahoo.fr " , "ville" : " rabat " }

# **Suppression d’un contact :**
# L'utilisateur pourra supprimer un contact en retirant le dictionnaire correspondant de la liste.

# Removing a key-value pair
del contact2["ville"]
print(contact2)  # Outputs: {"nom": "daraoui", "prenon": yassine, "num_tel": "0672477137" , add_email : " d.yassine90@yahoo.fr " }

### **Contraintes Techniques :**

# **Pas de Fonctions :** Le code ne doit pas utiliser de fonctions pour encapsuler la logique du programme.
# **Pas de Boucles :** Aucune boucle (for ou while) ne doit être utilisée. 
# Toutes les opérations sur les données doivent se faire de manière manuelle et explicite.

# **Structures de Données Utilisées :** 

# **Liste** : pour stocker les différents contacts.

# **Dictionnaire** : pour organiser les informations relatives à chaque contact.

### **Livraison et Gestion avec GitHub :**

# 1. **Création d’un dépôt GitHub :**
#   - Créer un dépôt GitHub pour héberger le projet.
   
# 2. **Initialisation de Git :**
#   - Initialiser le projet avec Git en local, puis le lier au dépôt GitHub distant.
   
# 3. **Commit Initial :**
#   - Premier commit avec le squelette du projet (liste vide ou avec quelques exemples de contacts préremplis).

# 4. **Suivi des modifications :**
#   - Chaque modification (ajout de contacts, suppression, modification, etc.) doit être suivie d’un commit sur GitHub.

# 5. **Gestion des Versions :**
#   - Utiliser des tags pour marquer les différentes étapes de développement.
   
# 6. **Documentation :**
#   - Rédiger un fichier `README.md` qui décrit le projet, son objectif, et les étapes pour l’exécuter.
# ajouter le compte git hub avec cet email : abdessadeq.elmakkioui.20@gmail.com  comme collaborateur dans le répertoire du projet