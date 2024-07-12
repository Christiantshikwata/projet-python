import json
import os
articles=[]
numArticle=0    

# creation de la fonction pour la validation du nom de l'article
def validationNomArticle(nomArt):
    while not nomArt.isalpha():
        nomArt=input("""saisissez le nom de l'article : \n
                     => """)
    return nomArt


#implementation de la fonction de la validation du prix de l'article
def validationPrixArticle(prix):
    while not prix.isdecimal() and prix.isalpha() and prix==0:
        prix=input("""erreur saisissez prix existant \n
                   => """)
    return prix


#definition de la fonction de validation de la quantité d'article
def validationQteArticle(qteArticle):
    while not qteArticle.isnumeric() and qteArticle.isalpha():
        qteArticle=input("""saisissez la quantite de l'article : \n
                         => """)
    return qteArticle


# implementation de la fonction ajout article
def ajouter_articles():
    
    prix = input("""Veuillez entrer le prix :\n
                 => """)
    prix = validationPrixArticle(prix)
    qteArticle = input("""Veuillez indiquer la quantité de produit :\n
                       => """)
    qteArticle = validationQteArticle(qteArticle)
    nomArt = input("""Saisissez le nom de l'article :\n
                   => """)
    nomArt = validationNomArticle(nomArt)
    with open('stockProduit.json', 'r') as notre_stock:
            articles = json.load(notre_stock)
            if len(articles) <= 0:
                 numArticle=1
            else:    
                numArticle= len(articles) + 1
    article = {'NumArticle': numArticle,'prix': prix,'qteArticle': qteArticle,'nomArt': nomArt}
    # ici nous recuperons les données de notre fichier Json pour y ajouter des nouveaux element après try:
    try:    
        with open('stockProduit.json', 'r') as notre_stock:
            articles = json.load(notre_stock)
    except FileNotFoundError:
        articles = []
    articles.append(article)
     
    with open('stockProduit.json', 'w') as notre_stock:
        json.dump(articles, notre_stock,indent=1)

# implementation de la fonction de recherche d'article par son nom
def rechercherArticleNom_par_NOM():
    with open('stockProduit.json', 'r') as notre_stock:
            articles = json.load(notre_stock)
    verification = input("""saisissez le nom de l'article que vous rechercher : \n
                         => """)
    i=0
    while (i <= len(articles)-1):
        if verification == articles[i] ["nomArt"]:
              print(" Quantité d'article : ", articles[i]['qteArticle'],"\n nom de l'article : ", articles[i]['nomArt'],"\n le prix de l'article : ", articles[i]['prix'])
              return i
        elif (i != len(articles)-1):
             i += 1
        else:    
            print("cette article n'y est pas ")
            break


#fonction qui permet d'afficher les articles en stock
def afficher_produit():
     
        with open('stockProduit.json', 'r') as notre_stock:
            articles = json.load(notre_stock)
        for article in articles:
            print(article)

# implementation de la fonction de recherche d'article par son ID
def rechercherArticleNom_par_ID():
    with open('stockProduit.json', 'r') as notre_stock:
            articles = json.load(notre_stock)
    verification = input("""saisissez la valeur de l'id  : \n
                         => """)
    verification= validationQteArticle(verification)
    verification=int(verification)
    i=0
    while (i <= len(articles)-1):
        if verification == articles[i] ['NumArticle']:
              print(" Quantité d'article : ", articles[i]['qteArticle'],"\n nom de l'article : ", articles[i]['nomArt'],"\n le prix de l'article : ", articles[i]['prix'])
              return i - 1
        elif (i != len(articles)-1):
             i += 1
        else:    
            print("le numéro de l'article n'y est pas ")
            break


#implementation de la fonction de suppression d'article
def supprimerArticleDuStock():
    with open('stockProduit.json', 'r') as notre_stock:
            articles = json.load(notre_stock)
    suprimer=rechercherArticleNom_par_NOM()
    del articles[suprimer]
    with open('stockProduit.json', 'w') as notre_stock:
        json.dump(articles, notre_stock,indent=1)



# implementation de la fonction rechercher produit qui fait appel à trois fonctions 
def Rechercher_Produit():
    select = int(input("""quelle option voulez-vous effectuer: \n
                       1. rechercher un article\n
                       2. supprimer un article\n
                       => """))
    if select == 1:
        choice = int(input("""par quoi voulez-vous rechercher le produit : \n
                        1. par le nom \n
                        2. par son id\n
                        => """))
          
        if choice == 1:
            rechercherArticleNom_par_NOM()
        elif choice == 2:
            rechercherArticleNom_par_ID ()   
        else:    
            print("erreur de choix")
    elif select ==2:
         supprimerArticleDuStock()
    else:
         print("erreur de selection ")   
