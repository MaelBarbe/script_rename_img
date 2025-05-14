import os
import shutil

def rename_img_safe(source_dossier, img_rename, prefixe="image_", extension_valide=(".jpg", ".jpeg", ".png")):
    # Crée le dossier de destination s'il n'existe pas
    os.makedirs(img_rename, exist_ok=True)

    fichiers = [f for f in os.listdir(source_dossier) if f.lower().endswith(extension_valide)]
    fichiers.sort()  # Tri pour un ordre stable

    for instance, nom_fichier in enumerate(fichiers, start=1):
        extension = os.path.splitext(nom_fichier)[1]
        nouveau_nom = f"{prefixe}{instance}{extension}"
        source_chemin = os.path.join(source_dossier, nom_fichier)
        destination_chemin = os.path.join(img_rename, nouveau_nom)

        shutil.copy2(source_chemin, destination_chemin)  # Copie avec métadonnées
        print(f"Copié et renommé : {nom_fichier} -> {nouveau_nom}")

# Changer le path "source" et "destination" avec les noms de dossier voulu
source = r"D:/img/img-opti-photoshop/opti-done"
destination = r"D:/img/img-opti-photoshop/img-rename"
rename_img_safe(source, destination, prefixe="img_")