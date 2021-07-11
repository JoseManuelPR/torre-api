from starlette.endpoints import HTTPEndpoint
import requests
from fastapi import Depends
from schemas import filters

class GenomeResource(HTTPEndpoint):
  @staticmethod
  async def get_bio_information(username: str):
    """
      *Description: Gets bio information of $username
      *Method: GET
      *Headers:
        Accept: application/json
        ContentType-response:  application/json
      *QueryString
      *Return:
        sttus, 200, Response
      *Errors:
        sttus 500, Internal Server Error
    """
    try:
      response = requests.get("https://torre.bio/api/bios/{}".format(username), timeout=30)
      response = response.json()
      return response
    except:
      print("An exception occurred")

  @staticmethod
  async def search_bios_by_filters(params: filters.FiltersValidate = Depends()):
    """
      *Description: Search for people in general
      *Method: POST
      *Headers:
        Accept: application/json
        ContentType-response:  application/json
      *QueryString
      *Return:
        sttus, 200, Response
      *Errors:
        sttus 500, Internal Server Error
    """
    try:
      offset = params.offset
      size = params.size
      aggregate = params.aggregate

      headers= {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      }
      response = requests.post("https://search.torre.co/people/_search/?offset={}&size={}&aggregate={}"
                          .format(offset, size, aggregate), headers=headers, timeout=30)
      response = response.json()
      return response
      return
    except:
      print("An exception occurred")