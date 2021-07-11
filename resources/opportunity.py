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