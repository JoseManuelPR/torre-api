from fastapi import APIRouter
from resources.opportunity import OpportunityResource

router = APIRouter(
  prefix="/api",
  tags=["job"],
)

# Gets job information of $id
# GET https://torre.co/api/opportunities/$id
router.add_api_route("/opportunities/{id}",
  OpportunityResource.get_job_information,
  methods=['GET'],
  name="Gets job information of $id",
  description="<strong>Gets job information of $id</strong>",
  tags=["job"]
)

# Search for jobs in general
# POST https://search.torre.co/opportunities/_search/?[offset=$offset&size=$size&aggregate=$aggregate]
router.add_api_route("/opportunities/_search/{offset}/{size}/{aggregate}",
  OpportunityResource.search_opportunities_by_filters,
  methods=['POST'],
  name="Search for jobs in general",
  description="<strong>Search for jobs in general</strong>",
  tags=["job"]
)