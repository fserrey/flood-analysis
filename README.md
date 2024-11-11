# flood-analysis

### Test GCP Cloud Run
1. Asegúrate de tener el [Google Cloud SDK](https://cloud.google.com/sdk) instalado y configurado.
2. Inicia sesión en tu cuenta de Google Cloud:
   ```bash
   gcloud auth login
   ```
3. Configura tu proyecto de Google Cloud:
```bash
   gcloud config set project [YOUR_PROJECT_ID]
   ```
### Construir la Imagen Docker
En el directorio raíz (flood-analysis) ejecuta el siguiente comando para construir la imagen Docker:
```bash
docker build -t gcr.io/[YOUR_PROJECT_ID]/flood-analysis .
```
Subir la imagen Docker a Google Container Registry:
```bash
docker push gcr.io/[YOUR_PROJECT_ID]/flood-analysis
```
Desplegar la imagen en Google Cloud Run con:

```bash
gcloud run deploy flood-analysis \
    --image gcr.io/[YOUR_PROJECT_ID]/flood-analysis \
    --platform managed \
    --memory 2Gi \
    --cpu 1 \
    --max-instances 3 \
    --region [YOUR_REGION] \
    --allow-unauthenticated
```
