# Pipeline CI/CD - Todo App

Ce document décrit le workflow CI/CD pour l'industrialisation de la Todo App.

## Pipeline GitHub Actions / GitLab CI imaginé

### 1. Stage: Lint & Test
- **Linting**: Vérification du style de code (flake8/black pour Python, eslint pour JS).
- **Unit Tests**: Exécution des tests pytest (backend) et npm test (frontend) dans des conteneurs éphémères.
- **Tools**: `docker build --target builder` pour isoler les outils de test.

### 2. Stage: Build & Scan
- **Build**: Construction des images multi-stage finales.
- **Security Scan**: Utilisation de `Trivy` pour scanner les images avant publication.
- **SBOM**: Génération d'un Software Bill of Materials (CycloneDX).

### 3. Stage: Publish
- **Registry**: Pousser les images vers un registre (Docker Hub, GitHub Packages, ou registre privé).
- **Tagging**: Utilisation de tags versionnés (ex: `1.0.0`) et de tags mobiles (ex: `latest`, `staging`).

### 4. Stage: Deploy
- **Promotion**: Déploiement automatique en environnement de staging.
- **Approval**: Validation manuelle pour la production.
- **Swarm/K8s**: Mise à jour de la stack via `docker stack deploy` ou `helm upgrade`.

## Gestion des Secrets
- Les secrets sont injectés via des variables d'environnement masquées dans l'outil de CI (ex: GitHub Secrets).
- En production, utilisation de Docker Secrets ou d'un Vault (Hashicorp Vault).

## Promotion des images
- `:staging`: Image construite à chaque commit sur `develop`.
- `:prod`: Image tagguée lors d'une release sur `main`.
