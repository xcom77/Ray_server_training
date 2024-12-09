import ray
from fastapi import FastAPI
from ray import serve

# Initialiser Ray et Ray Serve
ray.init(ignore_reinit_error=True)
serve.start()

# Créer une application FastAPI
app = FastAPI()

# Définir un déploiement Ray Serve
@serve.deployment(route_prefix="/process")
class ProcessService:
    def __init__(self):
        pass  # Initialisation si nécessaire

    async def __call__(self, request):
        # Traitement des requêtes
        data = await request.json()
        result = self.process_data(data["input"])
        return {"result": result}

    def process_data(self, data):
        # Simule un traitement intensif
        return f"Processed: {data}"

# Déployer le service sur Ray Serve
ProcessService.deploy()

# Connecter FastAPI à Ray Serve
@app.on_event("startup")
async def startup_event():
    client = serve.get_deployment("ProcessService")
    await client.get_handle().remote({"input": "startup_check"})

# Endpoint FastAPI standard
@app.get("/")
async def root():
    return {"message": "Ray Serve avec FastAPI est opérationnel"}

