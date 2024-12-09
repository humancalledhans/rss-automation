from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any

router = APIRouter()


class PurchaseInfo(BaseModel):
    id: str
    offer: Dict[str, Any]
    price: float
    currency: str


class CustomerInfo(BaseModel):
    id: str
    name: str
    email: str


class KajabiWebhookPayload(BaseModel):
    purchase: PurchaseInfo
    customer: CustomerInfo


@router.post('/kajabi')
async def create_custom_campaign(
    req_body: Any,
    # files: Optional[List[UploadFile]] = File([])
):

    print("req bdoy 3920993", req_body)

    fb_access_token = req_body.fb_access_token
    campaign_name = req_body.campaign_name

    env = req_body.env

    print("kajabi testing. anything printed out?")

    return
