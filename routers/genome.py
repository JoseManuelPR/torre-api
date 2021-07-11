from fastapi import APIRouter
from resources.genome import GenomeResource

router = APIRouter(
  prefix="/api",
  tags=["genome"],
)

# Gets bio information of $username
# GET https://torre.bio/api/bios/$username
router.add_api_route("/bios/{username}",
  GenomeResource.get_bio_information,
  methods=['GET'],
  name="Gets bio information of $username",
  description="<strong>Gets bio information of $username</strong>",
  tags=["genome"]
)


# Search for people in general
# POST https://search.torre.co/people/_search/?[offset=$offset&size=$size&aggregate=$aggregate]
router.add_api_route("/bios/_search/",
  GenomeResource.search_bios_by_filters,
  methods=['POST'],
  name="Search for people in general",
  description="<strong>Search for people in general</strong>",
  tags=["genome"]
)