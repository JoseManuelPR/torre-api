from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from configs.environment import Config

app = FastAPI(
  title= getattr(Config, 'PROJECT_NAME', 'Torre'),
  version=getattr(Config, 'PROJECT_API_VERSION', '0.1.0'),
  debug=Config.DEBUG
)

app.add_middleware(
  CORSMiddleware,
  allow_origins="*",
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get('/health-check')
def root():
  """
    Root
  """
  return {
    'status': 'ok',
    'version': getattr(Config, 'PROJECT_API_VERSION', '0.1.0')
  }

# Add router
#pylint: disable=wrong-import-position
from routers.genome import router as genome_routers
from routers.job import router as job_routers

#pylint: enable=wrong-import-position

app.include_router(genome_routers)
app.include_router(job_routers)
