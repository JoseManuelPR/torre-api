from starlette.endpoints import HTTPEndpoint
import requests
from fastapi import Depends
from schemas import filters

class OpportunityResource(HTTPEndpoint):
  @staticmethod
  async def get_job_information(id: str):
    """
      *Description: Gets job information of $id
      *Method: GET
      *Headers:
        Accept: application/json
        ContentType-response:  application/json
      *QueryString
      *Return:
        sttus, 200, Consulta exitosa
      *Errors:
        sttus 500, Error en el servidor
    """
    try:
      response = requests.get("https://torre.co/api/opportunities/{}".format(id), timeout=30)
      response = response.json()
      return response
    except:
      print("An exception occurred")

  @staticmethod
  async def search_opportunities_by_filters(params: filters.FiltersValidate = Depends()):
    """
      *Description: Search for jobs in general
      *Method: POST
      *Headers:
        Accept: application/json
        ContentType-response:  application/json
      *QueryString
      *Return:
        sttus, 200, Consulta exitosa
      *Errors:
        sttus 500, Error en el servidor
    """
    try:
      offset = params.offset
      size = params.size
      aggregate = params.aggregate
      
      headers= {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      }
      response = requests.post("https://search.torre.co/opportunities/_search/?offset={}&size={}&aggregate={}"
                          .format(offset, size, aggregate), headers=headers, timeout=30)
      response = response.json()
      return response
      return
    except:
      print("An exception occurred")

  @staticmethod
  async def search_opportunities_by_skills(username: str):
    """
      *Description: Search for jobs in general
      *Method: POST
      *Headers:
        Accept: application/json
        ContentType-response:  application/json
      *QueryString
      *Return:
        sttus, 200, Consulta exitosa
      *Errors:
        sttus 500, Error en el servidor
    """
    try:
      responseBio = requests.get("https://torre.bio/api/bios/{}".format(username), timeout=30)
      responseBio = responseBio.json()
      
      headers= {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      }
      responseJobs = requests.post("https://search.torre.co/opportunities/_search/?offset={}&size={}&aggregate={}"
                          .format('200', '100', 'false'), headers=headers, timeout=30)
      responseJobs = responseJobs.json()

      bioStrengths = []
      if(responseBio["strengths"]):
          strengths = responseBio["strengths"]
          if(strengths):
            for strength in strengths:
              if(strength["name"]):
                bioStrengths.append(strength["name"])

      jobsFounded = []
      founded = False
      
      if(bioStrengths):
        if(responseJobs["results"]):
            # Saving jobs in a variable
            jobs = responseJobs["results"]
            # Verify skills in each job (limit to 20 probably jobs)
            for job in jobs:
              if len(jobsFounded) >= 20:
                break
              if(job["skills"]):
                # Saving skills in a variable
                skills = job["skills"]
                # Verify skills name with skills of the bio
                for skill in skills:
                  if(skill["name"]):
                    # Load skillsbio to compare
                    if any(skill["name"] in s for s in bioStrengths):
                      # A probably job was founded
                      founded = True
                      jobsFounded.append(job)
                  if(founded):
                    break
      probablyOpportunities = {}
      probablyOpportunities["probablyOpportunities"] = jobsFounded
      return probablyOpportunities
    except:
      print("An exception occurred")