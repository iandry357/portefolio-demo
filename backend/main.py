from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À restreindre plus tard
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel('gemini-2.0-flash-exp')
model = genai.GenerativeModel('gemini-2.5-flash')

CV_CONTEXT = """

ALTIM
CDI · 3 ans 11 mois
Computer Vision Engineer
Computer Vision Engineer
janv. 2026 - aujourd’hui · 2 moisDe janv. 2026 à aujourd’hui · 2 mois
Boulogne-Billancourt, Île-de-France, FranceBoulogne-Billancourt, Île-de-France, France
Mission SIBELIANTHE | Projet SPRING 
Supervision déchets sauvages

Objectif :
Démontrer l'intégration de modèle de détection dans une solution développée avec la stack C++,QT, OpenCV 4 et évaluer des alternatives offrant une meilleure explicabilité concernant les résultats.

Problème :
Modèles YOLOv8 entraînés non compatibles (formats .pt/.pb vs .onnx requis) avec une manque d'explicabilité (classes fixes opaques, faux positifs incontrôlables).

Réalisations :
Audit exhaustif + tests compatibilité → sélection modèles viables
Pipeline conversion PyTorch/TensorFlow → ONNX optimisé OpenCV 4 + validation inférence C++
Proposition alternative Grounding DINO (open-vocabulary detection) : détection par prompting textuel → taxonomie déchets customisable sans réentraînement
Intégration ONNX dans application QT C++ + benchmark comparatif YOLOv8 vs Grounding DINO
Animation des daily meeting de l'équipe

Résultat :
Déblocage immédiat projet après une période d'impasse. 
Nouvelle voie R&D proposée : explicabilité accrue, adaptabilité métier instantanée (ajout types déchets sans collecte ni réentraînement). 

Stack :
Computer Vision, OpenCV 4, YOLOv8, Grounding DINO, Open-Vocabulary Detection, ONNX Runtime, QT (C++), Python, Object Detection, Conversion/optimisation modèles ML, google Colab, git

Acquis :
Industrialisation CV contexte contraint, Open-vocabulary & zero-shot detection, Contraintes Soft C++/embedded, Vision environnementale
Mission SIBELIANTHE | Projet SPRING Supervision déchets sauvages Objectif : Démontrer l'intégration de modèle de détection dans une solution développée avec la stack C++,QT, OpenCV 4 et évaluer des alternatives offrant une meilleure explicabilité concernant les résultats. Problème : Modèles YOLOv8 entraînés non compatibles (formats .pt/.pb vs .onnx requis) avec une manque d'explicabilité (classes fixes opaques, faux positifs incontrôlables). Réalisations : Audit exhaustif + tests compatibilité → sélection modèles viables Pipeline conversion PyTorch/TensorFlow → ONNX optimisé OpenCV 4 + validation inférence C++ Proposition alternative Grounding DINO (open-vocabulary detection) : détection par prompting textuel → taxonomie déchets customisable sans réentraînement Intégration ONNX dans application QT C++ + benchmark comparatif YOLOv8 vs Grounding DINO Animation des daily meeting de l'équipe Résultat : Déblocage immédiat projet après une période d'impasse. Nouvelle voie R&D proposée : explicabilité accrue, adaptabilité métier instantanée (ajout types déchets sans collecte ni réentraînement). Stack : Computer Vision, OpenCV 4, YOLOv8, Grounding DINO, Open-Vocabulary Detection, ONNX Runtime, QT (C++), Python, Object Detection, Conversion/optimisation modèles ML, google Colab, git Acquis : Industrialisation CV contexte contraint, Open-vocabulary & zero-shot detection, Contraintes Soft C++/embedded, Vision environnementale
Data Scientist / ML Engineer
Data Scientist / ML Engineer
avr. 2022 - déc. 2025 · 3 ans 9 moisDu avr. 2022 au déc. 2025 · 3 ans 9 mois
Boulogne-Billancourt, Île-de-France, FranceBoulogne-Billancourt, Île-de-France, France
Mission GE Healthcare
Suivi de la fiabilité des systèmes imagerie médicale 

Objectif :
Automatiser progressivement l'analyse de logs issus des tests automatiques (0-150 occurrences/jour, 1k-100k lignes logs/occurrence).

Problème :
Volume massif de logs à analyser manuellement pour identifier les spécialistes concernés et clôturer les incidents remontés. 
Process initial : extraction manuelle lignes pertinentes via Notepad.

Réalisations :
. Base MySQL retaçant l'historique des occurrences → traitement de 1-20 occ/jour → 0 fin semaine
. POC Classification ML : TF-IDF + Random Forest avec stratégie segmentation innovante → 97% précision (vs 80% outil existant) pour la prédiction des Problem Reports (PR)
. Immersion en Test Automation : compréhension architecture système tests auto (cycling → logs → occurrences)
. Pipeline extraction automatique : SGDClassifier + apprentissage incrémental sur dataset 43M+ lignes → 150 occurrences traitées à la fin de la journée

Résultat :
Gain temps ×10-20 pour les analyses de premier niveau 
Suite de POC R&D validant faisabilité automatisation ML/NLP en environnement industriel dynamique (multi-releases) 
Prototypes opérationnels pour l'équipe d'analyse Level 1

Stack :
Python, Polars, scikit-learn (TF-IDF, Random Forest, SGDClassifier), Flask, Docker, MySQL, SQL, ETL pipelines, NLP, Apprentissage incrémental, Machine Learning industriel, TCL, Java, Git, Excel

Acquis :
ML industriel contexte contraint, Data Engineering, Data Analysis, Data Science, Analyse logs massifs, Collaboration métier/tech, Architecture systèmes complexes
Mission GE Healthcare Suivi de la fiabilité des systèmes imagerie médicale Objectif : Automatiser progressivement l'analyse de logs issus des tests automatiques (0-150 occurrences/jour, 1k-100k lignes logs/occurrence). Problème : Volume massif de logs à analyser manuellement pour identifier les spécialistes concernés et clôturer les incidents remontés. Process initial : extraction manuelle lignes pertinentes via Notepad. Réalisations : . Base MySQL retaçant l'historique des occurrences → traitement de 1-20 occ/jour → 0 fin semaine . POC Classification ML : TF-IDF + Random Forest avec stratégie segmentation innovante → 97% précision (vs 80% outil existant) pour la prédiction des Problem Reports (PR) . Immersion en Test Automation : compréhension architecture système tests auto (cycling → logs → occurrences) . Pipeline extraction automatique : SGDClassifier + apprentissage incrémental sur dataset 43M+ lignes → 150 occurrences traitées à la fin de la journée Résultat : Gain temps ×10-20 pour les analyses de premier niveau Suite de POC R&D validant faisabilité automatisation ML/NLP en environnement industriel dynamique (multi-releases) Prototypes opérationnels pour l'équipe d'analyse Level 1 Stack : Python, Polars, scikit-learn (TF-IDF, Random Forest, SGDClassifier), Flask, Docker, MySQL, SQL, ETL pipelines, NLP, Apprentissage incrémental, Machine Learning industriel, TCL, Java, Git, Excel Acquis : ML industriel contexte contraint, Data Engineering, Data Analysis, Data Science, Analyse logs massifs, Collaboration métier/tech, Architecture systèmes complexes



Muséum national d'Histoire naturelle
CDD · 2 ans 11 moisCDD · 2 ans 11 mois
Ville de Paris, Île-de-France, France · Sur siteVille de Paris, Île-de-France, France · Sur site
Data Scientist – Applied ML & Crowdsourcing
Data Scientist – Applied ML & Crowdsourcing
déc. 2019 - juil. 2021 · 1 an 8 moisDu déc. 2019 au juil. 2021 · 1 an 8 mois
Collaboration DRUID (IRISA Rennes) + CESCO (MNHN) | Projet HEADWORK 

Réalisations : 
. Optimisé la validation des images provenant du SPIPOLL (milliers de photos pollinisateurs) via une plateforme de crowdsourcing : 
+10% taux validation, +7% précision identifications (expérimentation terrain 2 semaines, ~10 
participants). 

. Expérimenté des modèles Predictive pour prédire la justesse des identifications :
SVM, Random Forest, MLP, Régression Linéaire ; features historique utilisateur + qualité/rareté photo → publication scientifique (Ecological Informatics, 2020).
Lien : https://www.sciencedirect.com/science/article/abs/pii/S1574954120301266 

. Conception et implémentation d'un algorithme Recommender Systems / task assignment : 
Scoring des compétences utilisateurs × difficulté tâches (rareté espèce, état validations, similarité) → listes personnalisées priorisant photos à 1-2 validations (règle 3 indépendantes). 
Matching skill-difficulty 
Lien : https://inria.hal.science/hal-04162652 

Impact : 
Amélioration significative apporté par le crowdsourcing concernant la participation ; approche IA réplicable pour les observatoires citoyens / citizen science.

Stack : 
Machine Learning (scikit-learn : SVM, Random Forest), Deep Learning (MLP), Recommender Systems, A/B Testing, Predictive Modeling, PHP, JavaScript, MySQL, Algorithmes scoring/ranking/task assignment optimization.
Collaboration DRUID (IRISA Rennes) + CESCO (MNHN) | Projet HEADWORK Réalisations : . Optimisé la validation des images provenant du SPIPOLL (milliers de photos pollinisateurs) via une plateforme de crowdsourcing : +10% taux validation, +7% précision identifications (expérimentation terrain 2 semaines, ~10 participants). . Expérimenté des modèles Predictive pour prédire la justesse des identifications : SVM, Random Forest, MLP, Régression Linéaire ; features historique utilisateur + qualité/rareté photo → publication scientifique (Ecological Informatics, 2020). Lien : https://www.sciencedirect.com/science/article/abs/pii/S1574954120301266 . Conception et implémentation d'un algorithme Recommender Systems / task assignment : Scoring des compétences utilisateurs × difficulté tâches (rareté espèce, état validations, similarité) → listes personnalisées priorisant photos à 1-2 validations (règle 3 indépendantes). Matching skill-difficulty Lien : https://inria.hal.science/hal-04162652 Impact : Amélioration significative apporté par le crowdsourcing concernant la participation ; approche IA réplicable pour les observatoires citoyens / citizen science. Stack : Machine Learning (scikit-learn : SVM, Random Forest), Deep Learning (MLP), Recommender Systems, A/B Testing, Predictive Modeling, PHP, JavaScript, MySQL, Algorithmes scoring/ranking/task assignment optimization.
Back-end Developer
Back-end Developer
juin 2019 - nov. 2019 · 6 moisDu juin 2019 au nov. 2019 · 6 mois
Équipes 64MO - VigieNature | Sciences Participatives

Objectif :
Développement backends complets pour deux observatoires citoyens : Plage Vivante (biodiversité marine) et Vigie Terre (géologie).

Réalisations :
Architecture Node.js + LoopBack 3 + MySQL avec API REST
Gestion utilisateurs, observations géolocalisées (GPS + photos), formulaires protocoles scientifiques
Système validation collaborative par pairs
Carte interactive observations + module actualités

Résultat : 
structuration données terrain, autonomie scientifiques MNHN, qualité données améliorée via validation collaborative.

Plateforme web : 
https://www.plages-vivantes.fr
https://www.vigie-terre.org

Stack : 
Node.js, LoopBack 3, MySQL, API REST, Géolocalisation GPS | Outils : JIRA, Confluence, Git

Acquis : 
Backend développement, API REST, Sciences participatives, Systèmes de validation collaborative, Data export scientifique
Équipes 64MO - VigieNature | Sciences Participatives Objectif : Développement backends complets pour deux observatoires citoyens : Plage Vivante (biodiversité marine) et Vigie Terre (géologie). Réalisations : Architecture Node.js + LoopBack 3 + MySQL avec API REST Gestion utilisateurs, observations géolocalisées (GPS + photos), formulaires protocoles scientifiques Système validation collaborative par pairs Carte interactive observations + module actualités Résultat : structuration données terrain, autonomie scientifiques MNHN, qualité données améliorée via validation collaborative. Plateforme web : https://www.plages-vivantes.fr https://www.vigie-terre.org Stack : Node.js, LoopBack 3, MySQL, API REST, Géolocalisation GPS | Outils : JIRA, Confluence, Git Acquis : Backend développement, API REST, Sciences participatives, Systèmes de validation collaborative, Data export scientifique
Data Engineer / Spatial OLAP Developer
Data Engineer / Spatial OLAP Developer
sept. 2018 - mai 2019 · 9 moisDu sept. 2018 au mai 2019 · 9 mois
Collaboration IRSTEA (INRAE Clermont-Ferrand) - OAB-VigieNature (MNHN) | Projet VGI4BIO

Objectif : 
Conception solution Spatial OLAP pour analyser 500k observations de l'Observatoire Agricole de la Biodiversité. 

Problème : 
chercheurs utilisent R/Excel/QGIS, impossible d'explorer dynamiquement les corrélations pratiques agricoles ↔ biodiversité pollinisateurs.

Réalisations :
Data Warehouse spatial : PostgreSQL/PostGIS
Cube OLAP multidimensionnel : Mondrian + Saiku (dimensions : région, année, pratiques, espèces)
Pipeline ETL : Talend pour nettoyage et agrégations spatiales (observation → commune → région)
Visualisations : intégration Saiku → Feature Analyzer (cartes interactives, filtres dynamiques, drill-down spatial)

Résultat : 
autonomie chercheurs, analyses multidimensionnelles en quelques secondes, publication scientifique validant l'approche.

Publication : https://www.researchgate.net/publication/336686141_Analyse_en_ligne_des_donnees_de_biodiversite_en_milieu_agricole

Stack : 
PostgreSQL, PostGIS, Mondrian, Saiku, Talend, Java, SQL, Python, Data Visualization

Acquis : 
Business Intelligence, Spatial OLAP, Data Engineering, Bases de données spatiales, Collaboration interdisciplinaire recherche appliquée, Recherche & Développement

----------------------------
Mes hobbies : 
Choriste dans différent ensemble comme le choeur de l'Oratoire du Louvre, SQUILLO, MELANGE
Apprenti Chanteur lyrique, prend des cours de chants avec Sophie Hérvé
Apprenti chef de choeur au conservatoire du 18e arrondissement de paris dans la classe d'Ariel Alonzo
joue de la guitare/piano

Concert en cours de préparation : 
Concert SQUILLO le 06 fevrier 2026
Preparation SQUILLO BACH le 14 fevrier 2026
"""

SYSTEM_PROMPT = f"""Tu es l'assistant personnel d'Ian'ch, un data consultant basé à Paris.

Contexte professionnel :
{CV_CONTEXT}

Règles strictes :
1. Réponds UNIQUEMENT en français
2. Base-toi UNIQUEMENT sur les informations du contexte
3. Sois factuel et précis
4. Si une info n'est pas dans le contexte : "Je n'ai pas cette information dans le profil d'Ian'ch"
5. Ton conversationnel mais professionnel
6. Ne jamais inventer de données

Tu peux discuter de :
- Son parcours professionnel
- Ses compétences techniques
- Ses projets en cours
- Sa transition vers l'indépendant
- Sa passion pour la musique chorale
"""

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]

@app.get("/")
def read_root():
    return {"status": "API Portfolio Chat - Online"}

# @app.post("/chat")
# async def chat(request: ChatRequest):
#     try:
#         # Construire l'historique pour Gemini
#         chat_history = []
#         for msg in request.messages[:-1]:  # Tous sauf le dernier
#             chat_history.append({
#                 "role": "user" if msg.role == "user" else "model",
#                 "parts": [msg.content]
#             })
        
#         # Créer le chat avec historique
#         chat = model.start_chat(
#             history=chat_history
#         )
        
#         # Envoyer le message avec le system prompt inclus
#         user_message = request.messages[-1].content
#         full_prompt = f"{SYSTEM_PROMPT}\n\nQuestion: {user_message}"
        
#         response = chat.send_message(full_prompt)
        
#         return {
#             "response": response.text,
#             "model": "gemini-2.0-flash-exp"
#         }
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        print("=== Début du traitement ===")
        print(f"Messages reçus: {len(request.messages)}")
        
        # Construire l'historique pour Gemini
        chat_history = []
        for msg in request.messages[:-1]:
            print(f"Ajout message: {msg.role}")
            chat_history.append({
                "role": "user" if msg.role == "user" else "model",
                "parts": [msg.content]
            })
        
        print("=== Création du chat ===")
        chat = model.start_chat(history=chat_history)
        
        print("=== Envoi du message ===")
        user_message = request.messages[-1].content
        full_prompt = f"{SYSTEM_PROMPT}\n\nQuestion: {user_message}"
        
        response = chat.send_message(full_prompt)
        
        print("=== Succès ===")
        return {
            "response": response.text,
            "model": "gemini-2.0-flash-exp"
        }
        
    except Exception as e:
        print(f"❌ ERREUR: {e}")
        print(f"Type: {type(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "healthy"}

