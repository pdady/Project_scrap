Installation: 
pip3 install requests
pip3 install lxml
pip3 install fake-useragent



Le script marche de 2 façons, soit en mode console ou directement depuis le main en utilisant la fonction info_from_url,
pour utiliser la fonction il suffit de commenter la fonction get_argument dans le main et de décommanter les deux lignes suivantes.

Tous les articles récupérés depuis l’URL de départ seront stocké dans la liste all_products sous forme de dictionnaires.

Ex:
	info_products [
			{
			 ‘Seller name’ :  ‘リヴェラール’
			 ‘Seller URL’ :  ‘https://www.rakuten.co.jp/riverall/‘
			 ‘Price’ :  ‘380’
			 ‘Item URL’ :  ‘https://item.rakuten.co.jp/riverall/riverall-wrap/’
			 ‘Image URL’ :  ‘https://thumbnail.image.rakuten.co.jp/@0_mall/riverall/cabinet/wrapping/riv-shopper.jpg?_ex=112x112’
			 ‘Description :  ‘オリジナルショッパー ギフト ラッピング 財布やキーケースなどの小物からバッグま で対応♪ あす楽対応’
			 ‘Writed’ :  ‘0’
			}
		      ]

La clé ‘Writed’ a pour valeur ‘1’ si les produits de all_products ont déjà été écrits
dans le fichier results.txt depuis la session courante du mode console, voir (II).

A chaque itération de info_from_url, une vérification est faite avant de remplir all_products pour éviter les duplications.




(I) get_info_from_url

La fonction info_from_url prend 4 paramètres : 	- Une URL de départ

						- Une liste qui contiendra les données stockées sous forme de dictionnaires 
						  pour chacun des produits.

						- Nombre maximum d’items voulu. (-1 pour tous les items possibles, mais très long temp d’attente dû aux requetes)

						- Mode (Pour le mode console) ‘1’ pour afficher sur la sortie standard,
						  ‘2’ pour écrire les données dans le fichier results.txt, à mettre à ‘0’ par défaut.


 
(ex: 	
	import get
	
	url = ‘https://search.rakuten.co.jp/search/mall/-/565210/tg1000741/’   	<—- URL de sac à main Hermes
	all_products = []							<—- Liste où tous les produits seront stockés
	get.info_from_url(url, all_products, 50, 0)				<—- 50 produits max, tous les articles récupérés sont stocké dans all_products, mode 0
	debug_aff(all_products)							<—- Fonction pour afficher le contenu de all_products 
)

						     



(II) Mode console

$ python3 scraper.py -n [nb]	<—- Où [nb] le nombre maximum d’articles à récupérer

Simple affichage des données de [nb] articles récupérer depuis toutes les marques en même temps (Hermes, Louis Vuitton, Gucci, Chanel, Prada)
(+ Utilisé pour le débug)



$ python3 scraper.py -c

(1) Hermes
(2) Louis Vuitton
(3) Gucci
(4) Chanel
(5) Prada
(6) All

—>> Choisir une marque en entrant un chiffre (ex: 4 	<—- Pour la marque Chanel
						  6) 	<—- Pour toutes les marques

(1) Display mode
(2) Write in the result.txt

1 -> Le mode display permet de remplir la data tous en affichant les donnée reçues.

2 -> Permets d’écrire toutes les données accumulées dans la data dans un fichier texte sous un format spécial.
     (Chaque produit est séparé par 2 ‘\n’, et chaque données du produit est séparée par 1 ‘\n’, les donnés
      sont sous forme de dictionnaire)

Pour quittez, tapez ‘exit’

A noter que quand on quitte le mode console, les données accumulées sont effacées, la clé ‘Writed’ aussi,
il peut donc y avoir des duplications dans le fichier results.txt si une deuxième écriture est faite dessus en rouvrant un mode console avec l’argument ’-c’.
La vérification pour les duplications est faite sur la data (all_products) et non pas sur le fichier results.txt (à faire).