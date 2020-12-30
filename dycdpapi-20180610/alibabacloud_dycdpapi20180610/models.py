# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class QueryCdpOfferRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vendor: str = None,
        channel_type: str = None,
        province: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.vendor = vendor
        self.channel_type = channel_type
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class QueryCdpOfferResponseBodyFlowOffersFlowOffer(TeaModel):
    def __init__(
        self,
        right: str = None,
        use_eff: str = None,
        channel_type: str = None,
        use_limit: str = None,
        use_scene: str = None,
        vendor: str = None,
        grade: str = None,
        offer_id: int = None,
        price: int = None,
        flow_type: str = None,
        discount: str = None,
        province: str = None,
    ):
        self.right = right
        self.use_eff = use_eff
        self.channel_type = channel_type
        self.use_limit = use_limit
        self.use_scene = use_scene
        self.vendor = vendor
        self.grade = grade
        self.offer_id = offer_id
        self.price = price
        self.flow_type = flow_type
        self.discount = discount
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.right is not None:
            result['Right'] = self.right
        if self.use_eff is not None:
            result['UseEff'] = self.use_eff
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.use_limit is not None:
            result['UseLimit'] = self.use_limit
        if self.use_scene is not None:
            result['UseScene'] = self.use_scene
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.grade is not None:
            result['Grade'] = self.grade
        if self.offer_id is not None:
            result['OfferId'] = self.offer_id
        if self.price is not None:
            result['Price'] = self.price
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.discount is not None:
            result['Discount'] = self.discount
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Right') is not None:
            self.right = m.get('Right')
        if m.get('UseEff') is not None:
            self.use_eff = m.get('UseEff')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('UseLimit') is not None:
            self.use_limit = m.get('UseLimit')
        if m.get('UseScene') is not None:
            self.use_scene = m.get('UseScene')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Grade') is not None:
            self.grade = m.get('Grade')
        if m.get('OfferId') is not None:
            self.offer_id = m.get('OfferId')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('Discount') is not None:
            self.discount = m.get('Discount')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class QueryCdpOfferResponseBodyFlowOffers(TeaModel):
    def __init__(
        self,
        flow_offer: List[QueryCdpOfferResponseBodyFlowOffersFlowOffer] = None,
    ):
        self.flow_offer = flow_offer

    def validate(self):
        if self.flow_offer:
            for k in self.flow_offer:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FlowOffer'] = []
        if self.flow_offer is not None:
            for k in self.flow_offer:
                result['FlowOffer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_offer = []
        if m.get('FlowOffer') is not None:
            for k in m.get('FlowOffer'):
                temp_model = QueryCdpOfferResponseBodyFlowOffersFlowOffer()
                self.flow_offer.append(temp_model.from_map(k))
        return self


class QueryCdpOfferResponseBody(TeaModel):
    def __init__(
        self,
        flow_offers: QueryCdpOfferResponseBodyFlowOffers = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.flow_offers = flow_offers
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.flow_offers:
            self.flow_offers.validate()

    def to_map(self):
        result = dict()
        if self.flow_offers is not None:
            result['FlowOffers'] = self.flow_offers.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowOffers') is not None:
            temp_model = QueryCdpOfferResponseBodyFlowOffers()
            self.flow_offers = temp_model.from_map(m['FlowOffers'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryCdpOfferResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCdpOfferResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryCdpOfferResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCdpOfferByIdRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        offer_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.offer_id = offer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.offer_id is not None:
            result['OfferId'] = self.offer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OfferId') is not None:
            self.offer_id = m.get('OfferId')
        return self


class QueryCdpOfferByIdResponseBodyFlowOffersFlowOffer(TeaModel):
    def __init__(
        self,
        right: str = None,
        use_eff: str = None,
        channel_type: str = None,
        use_limit: str = None,
        use_scene: str = None,
        vendor: str = None,
        grade: str = None,
        offer_id: int = None,
        price: int = None,
        flow_type: str = None,
        discount: str = None,
        province: str = None,
    ):
        self.right = right
        self.use_eff = use_eff
        self.channel_type = channel_type
        self.use_limit = use_limit
        self.use_scene = use_scene
        self.vendor = vendor
        self.grade = grade
        self.offer_id = offer_id
        self.price = price
        self.flow_type = flow_type
        self.discount = discount
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.right is not None:
            result['Right'] = self.right
        if self.use_eff is not None:
            result['UseEff'] = self.use_eff
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.use_limit is not None:
            result['UseLimit'] = self.use_limit
        if self.use_scene is not None:
            result['UseScene'] = self.use_scene
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.grade is not None:
            result['Grade'] = self.grade
        if self.offer_id is not None:
            result['OfferId'] = self.offer_id
        if self.price is not None:
            result['Price'] = self.price
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.discount is not None:
            result['Discount'] = self.discount
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Right') is not None:
            self.right = m.get('Right')
        if m.get('UseEff') is not None:
            self.use_eff = m.get('UseEff')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('UseLimit') is not None:
            self.use_limit = m.get('UseLimit')
        if m.get('UseScene') is not None:
            self.use_scene = m.get('UseScene')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Grade') is not None:
            self.grade = m.get('Grade')
        if m.get('OfferId') is not None:
            self.offer_id = m.get('OfferId')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('Discount') is not None:
            self.discount = m.get('Discount')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class QueryCdpOfferByIdResponseBodyFlowOffers(TeaModel):
    def __init__(
        self,
        flow_offer: List[QueryCdpOfferByIdResponseBodyFlowOffersFlowOffer] = None,
    ):
        self.flow_offer = flow_offer

    def validate(self):
        if self.flow_offer:
            for k in self.flow_offer:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FlowOffer'] = []
        if self.flow_offer is not None:
            for k in self.flow_offer:
                result['FlowOffer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_offer = []
        if m.get('FlowOffer') is not None:
            for k in m.get('FlowOffer'):
                temp_model = QueryCdpOfferByIdResponseBodyFlowOffersFlowOffer()
                self.flow_offer.append(temp_model.from_map(k))
        return self


class QueryCdpOfferByIdResponseBody(TeaModel):
    def __init__(
        self,
        flow_offers: QueryCdpOfferByIdResponseBodyFlowOffers = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.flow_offers = flow_offers
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.flow_offers:
            self.flow_offers.validate()

    def to_map(self):
        result = dict()
        if self.flow_offers is not None:
            result['FlowOffers'] = self.flow_offers.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowOffers') is not None:
            temp_model = QueryCdpOfferByIdResponseBodyFlowOffers()
            self.flow_offers = temp_model.from_map(m['FlowOffers'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryCdpOfferByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCdpOfferByIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryCdpOfferByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCdpOrderRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        out_order_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.out_order_id = out_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.out_order_id is not None:
            result['OutOrderId'] = self.out_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OutOrderId') is not None:
            self.out_order_id = m.get('OutOrderId')
        return self


class QueryCdpOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        extend_param: str = None,
        result_code: str = None,
        result_msg: str = None,
    ):
        self.extend_param = extend_param
        self.result_code = result_code
        self.result_msg = result_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extend_param is not None:
            result['ExtendParam'] = self.extend_param
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendParam') is not None:
            self.extend_param = m.get('ExtendParam')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        return self


class QueryCdpOrderResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: QueryCdpOrderResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryCdpOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryCdpOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCdpOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryCdpOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


