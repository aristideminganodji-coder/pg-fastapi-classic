# 🚀 FastAPI Classic API

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Une API RESTful complète construite avec **FastAPI** et **PostgreSQL**, implémentant un système d'authentification et des opérations CRUD.

## ✨ Fonctionnalités

- ✅ **Authentification sécurisée** (bcrypt)
  - Inscription (`/auth/register`)
  - Connexion (`/auth/login-simple`)
- ✅ **CRUD Utilisateurs** complet
- ✅ **CRUD Tâches** (liées aux utilisateurs)
- ✅ **Documentation automatique** (Swagger/ReDoc)
- ✅ **Validation des données** avec Pydantic

## 🛠 Stack Technique

| Technologie | Utilisation |
|------------|-------------|
| **FastAPI** | Framework web |
| **PostgreSQL** | Base de données |
| **SQLAlchemy** | ORM |
| **Pydantic** | Validation |
| **bcrypt** | Hachage des mots de passe |
| **python-dotenv** | Gestion des variables d'environnement |

## 📋 Prérequis

- Python 3.11 ou supérieur
- PostgreSQL 15 ou supérieur
- Git

## 🚀 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/aristideminganodji-coder/pg-fastapi-classic.git
cd pg-fastapi-classic
```

### 2. Créer l'environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données
```bash
# Se connecter à PostgreSQL
sudo -u postgres psql

# Exécuter ces commandes SQL
CREATE DATABASE tfastapi_classic;
CREATE USER fastapi_user WITH PASSWORD 'votre_mot_de_passe';
GRANT ALL PRIVILEGES ON DATABASE tfastapi_classic TO fastapi_user;
\q
```

### 5. Configurer les variables d'environnement
```bash
# Copier le fichier d'exemple
cp .env.example .env

# Éditer avec vos informations
nano .env
```

**Configurez ces variables dans `.env` :**
```env
DATABASE_URL=postgresql://fastapi_user:votre_mdp@localhost/tfastapi_classic
SECRET_KEY=votre_cle_secrete_ici
DEBUG=True
```

### 6. Lancer l'application
```bash
uvicorn app.main:app --reload
```

L'API sera accessible à : http://localhost:8000

## 📚 Documentation API

Une fois le serveur lancé, deux interfaces interactives sont disponibles :

| Interface | URL | Description |
|-----------|-----|-------------|
| **Swagger UI** | http://localhost:8000/docs | Interface de test interactive |
| **ReDoc** | http://localhost:8000/redoc | Documentation détaillée |

## 🔌 Points d'entrée de l'API

### 🔐 Authentification
| Méthode | Endpoint | Description |
|---------|----------|-------------|
| POST | `/auth/register` | Créer un compte |
| POST | `/auth/login-simple` | Se connecter |

### 👥 Utilisateurs
| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/users/` | Liste des utilisateurs |
| GET | `/users/{id}` | Détail d'un utilisateur |
| PUT | `/users/{id}` | Modifier un utilisateur |
| DELETE | `/users/{id}` | Supprimer un utilisateur |

### ✅ Tâches
| Méthode | Endpoint | Description |
|---------|----------|-------------|
| POST | `/tasks/` | Créer une tâche |
| GET | `/tasks/` | Liste des tâches |
| GET | `/tasks/{id}` | Détail d'une tâche |
| PUT | `/tasks/{id}` | Modifier une tâche |
| DELETE | `/tasks/{id}` | Supprimer une tâche |

## 🧪 Exemples de requêtes

### Inscription
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "secret123"}'
```

### Connexion
```bash
curl -X POST http://localhost:8000/auth/login-simple \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "secret123"}'
```

### Créer une tâche
```bash
curl -X POST http://localhost:8000/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Apprendre FastAPI", "user_id": 1}'
```

### Lister les tâches
```bash
curl http://localhost:8000/tasks/ | python -m json.tool
```

## 📁 Structure du projet

```
pg-fastapi-classic/
├── 📂 app/
│   ├── 📄 __init__.py
│   ├── 📄 main.py              # Point d'entrée
│   ├── 📄 database.py          # Configuration DB
│   ├── 📂 models/               # Modèles SQLAlchemy
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── task.py
│   ├── 📂 schemas/              # Schémas Pydantic
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── task.py
│   └── 📂 routers/              # Routes de l'API
│       ├── __init__.py
│       ├── auth.py
│       ├── users.py
│       └── tasks.py
├── 📄 .env                      # Variables d'environnement (ignoré)
├── 📄 .env.example              # Exemple de configuration
├── 📄 .gitignore                # Fichiers ignorés
├── 📄 requirements.txt          # Dépendances
└── 📄 README.md                  # Documentation
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit les changements (`git commit -m 'Ajout d'une fonctionnalité'`)
4. Push (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👤 Auteur

**Aristide** - [@aristideminganodji-coder](https://github.com/aristideminganodji-coder)

---

⭐ **Si ce projet vous a aidé, n'hésitez pas à lui donner une étoile !**