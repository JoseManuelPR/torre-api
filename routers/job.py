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
router.add_api_route("/opportunities/_search/",
  OpportunityResource.search_opportunities_by_filters,
  methods=['POST'],
  name="Search for jobs in general",
  description="<strong>Search for jobs in general</strong>",
  tags=["job"]
)

# Search 20 jobs according to your skills
# GET https://torre.bio/api/bios/$username
# POST https://search.torre.co/opportunities/_search/?[offset=$offset&size=$size&aggregate=$aggregate]
router.add_api_route("/opportunities/_search/genome/{username}",
  OpportunityResource.search_opportunities_by_skills,
  methods=['GET'],
  name="Search for jobs in general",
  description="<strong>Search for jobs in general</strong>",
  tags=["job"]
)