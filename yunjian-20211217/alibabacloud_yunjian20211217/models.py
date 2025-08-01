# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CreateDemandPlanHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        yun_user_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.yun_user_id = yun_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.yun_user_id is not None:
            result['Yun-User-Id'] = self.yun_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Yun-User-Id') is not None:
            self.yun_user_id = m.get('Yun-User-Id')
        return self


class CreateDemandPlanRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        demand_type: str = None,
        description: str = None,
        name: str = None,
        period: str = None,
        source: str = None,
        target_cid: int = None,
        type: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        self.demand_type = demand_type
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.period = period
        self.source = source
        self.target_cid = target_cid
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.demand_type is not None:
            result['demandType'] = self.demand_type
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.period is not None:
            result['period'] = self.period
        if self.source is not None:
            result['source'] = self.source
        if self.target_cid is not None:
            result['targetCid'] = self.target_cid
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('demandType') is not None:
            self.demand_type = m.get('demandType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('targetCid') is not None:
            self.target_cid = m.get('targetCid')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateDemandPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        message: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # code
        self.code = code
        self.data = data
        self.message = message
        # success
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CreateDemandPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDemandPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDemandPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDemandPlanV2Headers(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        yun_user_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.yun_user_id = yun_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.yun_user_id is not None:
            result['Yun-User-Id'] = self.yun_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Yun-User-Id') is not None:
            self.yun_user_id = m.get('Yun-User-Id')
        return self


class CreateDemandPlanV2Request(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        demand_type: str = None,
        description: str = None,
        name: str = None,
        product_type: str = None,
        target_cid: int = None,
        type: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        self.demand_type = demand_type
        self.description = description
        # This parameter is required.
        self.name = name
        self.product_type = product_type
        self.target_cid = target_cid
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.demand_type is not None:
            result['demandType'] = self.demand_type
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.product_type is not None:
            result['productType'] = self.product_type
        if self.target_cid is not None:
            result['targetCid'] = self.target_cid
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('demandType') is not None:
            self.demand_type = m.get('demandType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('targetCid') is not None:
            self.target_cid = m.get('targetCid')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateDemandPlanV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        message: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CreateDemandPlanV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDemandPlanV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDemandPlanV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUrgentDemandItemHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        yun_user_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.yun_user_id = yun_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.yun_user_id is not None:
            result['Yun-User-Id'] = self.yun_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Yun-User-Id') is not None:
            self.yun_user_id = m.get('Yun-User-Id')
        return self


class DeleteUrgentDemandItemRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        modifier: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.modifier = modifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.modifier is not None:
            result['modifier'] = self.modifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        return self


class DeleteUrgentDemandItemResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        message: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class DeleteUrgentDemandItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUrgentDemandItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUrgentDemandItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUrgentDemandPlanHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        yun_user_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.yun_user_id = yun_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.yun_user_id is not None:
            result['Yun-User-Id'] = self.yun_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Yun-User-Id') is not None:
            self.yun_user_id = m.get('Yun-User-Id')
        return self


class DeleteUrgentDemandPlanRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        modifier: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.modifier = modifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.modifier is not None:
            result['modifier'] = self.modifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        return self


class DeleteUrgentDemandPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        message: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class DeleteUrgentDemandPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUrgentDemandPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUrgentDemandPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeliveryItemDetailSynHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        yun_user_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.yun_user_id = yun_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.yun_user_id is not None:
            result['Yun-User-Id'] = self.yun_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Yun-User-Id') is not None:
            self.yun_user_id = m.get('Yun-User-Id')
        return self


class DeliveryItemDetailSynRequestDeliveryItemDetailDTOS(TeaModel):
    def __init__(
        self,
        actual_supply_time: str = None,
        amount: int = None,
        comment: str = None,
        delivered_amount: int = None,
        delivery_item_id: str = None,
        delivery_plan_id: str = None,
        last_supply_time: str = None,
        status: str = None,
        sub_demand_supply_performer_name: str = None,
        sub_demand_supply_performer_uid: str = None,
        sub_demand_supply_pm_name: str = None,
        sub_demand_supply_pm_uid: str = None,
        sub_order_id: int = None,
        supply_status: str = None,
        total_order_id: int = None,
    ):
        self.actual_supply_time = actual_supply_time
        self.amount = amount
        self.comment = comment
        self.delivered_amount = delivered_amount
        self.delivery_item_id = delivery_item_id
        self.delivery_plan_id = delivery_plan_id
        self.last_supply_time = last_supply_time
        self.status = status
        self.sub_demand_supply_performer_name = sub_demand_supply_performer_name
        self.sub_demand_supply_performer_uid = sub_demand_supply_performer_uid
        self.sub_demand_supply_pm_name = sub_demand_supply_pm_name
        self.sub_demand_supply_pm_uid = sub_demand_supply_pm_uid
        self.sub_order_id = sub_order_id
        self.supply_status = supply_status
        self.total_order_id = total_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_supply_time is not None:
            result['actualSupplyTime'] = self.actual_supply_time
        if self.amount is not None:
            result['amount'] = self.amount
        if self.comment is not None:
            result['comment'] = self.comment
        if self.delivered_amount is not None:
            result['deliveredAmount'] = self.delivered_amount
        if self.delivery_item_id is not None:
            result['deliveryItemId'] = self.delivery_item_id
        if self.delivery_plan_id is not None:
            result['deliveryPlanId'] = self.delivery_plan_id
        if self.last_supply_time is not None:
            result['lastSupplyTime'] = self.last_supply_time
        if self.status is not None:
            result['status'] = self.status
        if self.sub_demand_supply_performer_name is not None:
            result['subDemandSupplyPerformerName'] = self.sub_demand_supply_performer_name
        if self.sub_demand_supply_performer_uid is not None:
            result['subDemandSupplyPerformerUid'] = self.sub_demand_supply_performer_uid
        if self.sub_demand_supply_pm_name is not None:
            result['subDemandSupplyPmName'] = self.sub_demand_supply_pm_name
        if self.sub_demand_supply_pm_uid is not None:
            result['subDemandSupplyPmUid'] = self.sub_demand_supply_pm_uid
        if self.sub_order_id is not None:
            result['subOrderId'] = self.sub_order_id
        if self.supply_status is not None:
            result['supplyStatus'] = self.supply_status
        if self.total_order_id is not None:
            result['totalOrderId'] = self.total_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actualSupplyTime') is not None:
            self.actual_supply_time = m.get('actualSupplyTime')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('deliveredAmount') is not None:
            self.delivered_amount = m.get('deliveredAmount')
        if m.get('deliveryItemId') is not None:
            self.delivery_item_id = m.get('deliveryItemId')
        if m.get('deliveryPlanId') is not None:
            self.delivery_plan_id = m.get('deliveryPlanId')
        if m.get('lastSupplyTime') is not None:
            self.last_supply_time = m.get('lastSupplyTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subDemandSupplyPerformerName') is not None:
            self.sub_demand_supply_performer_name = m.get('subDemandSupplyPerformerName')
        if m.get('subDemandSupplyPerformerUid') is not None:
            self.sub_demand_supply_performer_uid = m.get('subDemandSupplyPerformerUid')
        if m.get('subDemandSupplyPmName') is not None:
            self.sub_demand_supply_pm_name = m.get('subDemandSupplyPmName')
        if m.get('subDemandSupplyPmUid') is not None:
            self.sub_demand_supply_pm_uid = m.get('subDemandSupplyPmUid')
        if m.get('subOrderId') is not None:
            self.sub_order_id = m.get('subOrderId')
        if m.get('supplyStatus') is not None:
            self.supply_status = m.get('supplyStatus')
        if m.get('totalOrderId') is not None:
            self.total_order_id = m.get('totalOrderId')
        return self


class DeliveryItemDetailSynRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        delivery_item_detail_dtos: List[DeliveryItemDetailSynRequestDeliveryItemDetailDTOS] = None,
        delivery_item_id: str = None,
        delivery_plan_id: str = None,
    ):
        self.channel = channel
        self.delivery_item_detail_dtos = delivery_item_detail_dtos
        self.delivery_item_id = delivery_item_id
        self.delivery_plan_id = delivery_plan_id

    def validate(self):
        if self.delivery_item_detail_dtos:
            for k in self.delivery_item_detail_dtos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        result['deliveryItemDetailDTOS'] = []
        if self.delivery_item_detail_dtos is not None:
            for k in self.delivery_item_detail_dtos:
                result['deliveryItemDetailDTOS'].append(k.to_map() if k else None)
        if self.delivery_item_id is not None:
            result['deliveryItemId'] = self.delivery_item_id
        if self.delivery_plan_id is not None:
            result['deliveryPlanId'] = self.delivery_plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        self.delivery_item_detail_dtos = []
        if m.get('deliveryItemDetailDTOS') is not None:
            for k in m.get('deliveryItemDetailDTOS'):
                temp_model = DeliveryItemDetailSynRequestDeliveryItemDetailDTOS()
                self.delivery_item_detail_dtos.append(temp_model.from_map(k))
        if m.get('deliveryItemId') is not None:
            self.delivery_item_id = m.get('deliveryItemId')
        if m.get('deliveryPlanId') is not None:
            self.delivery_plan_id = m.get('deliveryPlanId')
        return self


class DeliveryItemDetailSynResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        message: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class DeliveryItemDetailSynResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeliveryItemDetailSynResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeliveryItemDetailSynResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUrgentDemandItemListHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        yun_user_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.yun_user_id = yun_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.yun_user_id is not None:
            result['Yun-User-Id'] = self.yun_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Yun-User-Id') is not None:
            self.yun_user_id = m.get('Yun-User-Id')
        return self


class GetUrgentDemandItemListRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_type_code: str = None,
        current: int = None,
        plan_id: int = None,
        region: str = None,
        size: int = None,
        zone: str = None,
    ):
        self.commodity_code = commodity_code
        self.commodity_type_code = commodity_type_code
        self.current = current
        self.plan_id = plan_id
        self.region = region
        self.size = size
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.commodity_type_code is not None:
            result['commodityTypeCode'] = self.commodity_type_code
        if self.current is not None:
            result['current'] = self.current
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        if self.region is not None:
            result['region'] = self.region
        if self.size is not None:
            result['size'] = self.size
        if self.zone is not None:
            result['zone'] = self.zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('commodityTypeCode') is not None:
            self.commodity_type_code = m.get('commodityTypeCode')
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        return self


class GetUrgentDemandItemListResponseBodyDataRecordsUrgentDemandEbsRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_num: int = None,
        commodity_type_code: str = None,
        data_disk_size: int = None,
        item_id: int = None,
        performance_level: int = None,
    ):
        self.commodity_code = commodity_code
        self.commodity_num = commodity_num
        self.commodity_type_code = commodity_type_code
        self.data_disk_size = data_disk_size
        self.item_id = item_id
        self.performance_level = performance_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.commodity_num is not None:
            result['commodityNum'] = self.commodity_num
        if self.commodity_type_code is not None:
            result['commodityTypeCode'] = self.commodity_type_code
        if self.data_disk_size is not None:
            result['dataDiskSize'] = self.data_disk_size
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('commodityNum') is not None:
            self.commodity_num = m.get('commodityNum')
        if m.get('commodityTypeCode') is not None:
            self.commodity_type_code = m.get('commodityTypeCode')
        if m.get('dataDiskSize') is not None:
            self.data_disk_size = m.get('dataDiskSize')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')
        return self


class GetUrgentDemandItemListResponseBodyDataRecordsUrgentDemandEcsRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_num: int = None,
        commodity_type_code: str = None,
        item_id: int = None,
        vcpu_count: int = None,
    ):
        self.commodity_code = commodity_code
        self.commodity_num = commodity_num
        self.commodity_type_code = commodity_type_code
        self.item_id = item_id
        self.vcpu_count = vcpu_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.commodity_num is not None:
            result['commodityNum'] = self.commodity_num
        if self.commodity_type_code is not None:
            result['commodityTypeCode'] = self.commodity_type_code
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.vcpu_count is not None:
            result['vcpuCount'] = self.vcpu_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('commodityNum') is not None:
            self.commodity_num = m.get('commodityNum')
        if m.get('commodityTypeCode') is not None:
            self.commodity_type_code = m.get('commodityTypeCode')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('vcpuCount') is not None:
            self.vcpu_count = m.get('vcpuCount')
        return self


class GetUrgentDemandItemListResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        zone: str = None,
        account_id: str = None,
        commodity_code: str = None,
        commodity_num: int = None,
        commodity_type_code: str = None,
        creator: str = None,
        creator_name: str = None,
        effect_time: str = None,
        gmt_modified: str = None,
        id: int = None,
        modifier: str = None,
        modifier_name: str = None,
        network_type: str = None,
        pay_duration: int = None,
        pay_duration_unit: str = None,
        pay_type: str = None,
        plan_id: int = None,
        region: str = None,
        urgent_demand_ebs_request: GetUrgentDemandItemListResponseBodyDataRecordsUrgentDemandEbsRequest = None,
        urgent_demand_ecs_request: GetUrgentDemandItemListResponseBodyDataRecordsUrgentDemandEcsRequest = None,
    ):
        self.zone = zone
        self.account_id = account_id
        self.commodity_code = commodity_code
        self.commodity_num = commodity_num
        self.commodity_type_code = commodity_type_code
        self.creator = creator
        self.creator_name = creator_name
        self.effect_time = effect_time
        self.gmt_modified = gmt_modified
        self.id = id
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.network_type = network_type
        self.pay_duration = pay_duration
        self.pay_duration_unit = pay_duration_unit
        self.pay_type = pay_type
        self.plan_id = plan_id
        self.region = region
        self.urgent_demand_ebs_request = urgent_demand_ebs_request
        self.urgent_demand_ecs_request = urgent_demand_ecs_request

    def validate(self):
        if self.urgent_demand_ebs_request:
            self.urgent_demand_ebs_request.validate()
        if self.urgent_demand_ecs_request:
            self.urgent_demand_ecs_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone is not None:
            result['Zone'] = self.zone
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.commodity_num is not None:
            result['commodityNum'] = self.commodity_num
        if self.commodity_type_code is not None:
            result['commodityTypeCode'] = self.commodity_type_code
        if self.creator is not None:
            result['creator'] = self.creator
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.effect_time is not None:
            result['effectTime'] = self.effect_time
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.pay_duration is not None:
            result['payDuration'] = self.pay_duration
        if self.pay_duration_unit is not None:
            result['payDurationUnit'] = self.pay_duration_unit
        if self.pay_type is not None:
            result['payType'] = self.pay_type
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        if self.region is not None:
            result['region'] = self.region
        if self.urgent_demand_ebs_request is not None:
            result['urgentDemandEbsRequest'] = self.urgent_demand_ebs_request.to_map()
        if self.urgent_demand_ecs_request is not None:
            result['urgentDemandEcsRequest'] = self.urgent_demand_ecs_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('commodityNum') is not None:
            self.commodity_num = m.get('commodityNum')
        if m.get('commodityTypeCode') is not None:
            self.commodity_type_code = m.get('commodityTypeCode')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('effectTime') is not None:
            self.effect_time = m.get('effectTime')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('payDuration') is not None:
            self.pay_duration = m.get('payDuration')
        if m.get('payDurationUnit') is not None:
            self.pay_duration_unit = m.get('payDurationUnit')
        if m.get('payType') is not None:
            self.pay_type = m.get('payType')
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('urgentDemandEbsRequest') is not None:
            temp_model = GetUrgentDemandItemListResponseBodyDataRecordsUrgentDemandEbsRequest()
            self.urgent_demand_ebs_request = temp_model.from_map(m['urgentDemandEbsRequest'])
        if m.get('urgentDemandEcsRequest') is not None:
            temp_model = GetUrgentDemandItemListResponseBodyDataRecordsUrgentDemandEcsRequest()
            self.urgent_demand_ecs_request = temp_model.from_map(m['urgentDemandEcsRequest'])
        return self


class GetUrgentDemandItemListResponseBodyData(TeaModel):
    def __init__(
        self,
        current: int = None,
        pages: int = None,
        records: List[GetUrgentDemandItemListResponseBodyDataRecords] = None,
        size: int = None,
        total: int = None,
    ):
        self.current = current
        self.pages = pages
        self.records = records
        self.size = size
        self.total = total

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['current'] = self.current
        if self.pages is not None:
            result['pages'] = self.pages
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.size is not None:
            result['size'] = self.size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('pages') is not None:
            self.pages = m.get('pages')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = GetUrgentDemandItemListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetUrgentDemandItemListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetUrgentDemandItemListResponseBodyData = None,
        message: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetUrgentDemandItemListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class GetUrgentDemandItemListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUrgentDemandItemListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUrgentDemandItemListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUrgentDemandPlanDetailHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        yun_user_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.yun_user_id = yun_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.yun_user_id is not None:
            result['Yun-User-Id'] = self.yun_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Yun-User-Id') is not None:
            self.yun_user_id = m.get('Yun-User-Id')
        return self


class GetUrgentDemandPlanDetailRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
    ):
        # This parameter is required.
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        return self


class GetUrgentDemandPlanDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        account_dept: str = None,
        account_id: str = None,
        account_name: str = None,
        approval_url: str = None,
        bpm_substate: Dict[str, Any] = None,
        commodity_type_code_list: List[str] = None,
        creator: str = None,
        creator_name: str = None,
        description: str = None,
        detail_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        modifier: str = None,
        modifier_name: str = None,
        plan_id: int = None,
        plan_name: str = None,
        status: int = None,
        yunzhi_product_name: str = None,
    ):
        self.account_dept = account_dept
        self.account_id = account_id
        self.account_name = account_name
        self.approval_url = approval_url
        self.bpm_substate = bpm_substate
        self.commodity_type_code_list = commodity_type_code_list
        self.creator = creator
        self.creator_name = creator_name
        self.description = description
        self.detail_type = detail_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.plan_id = plan_id
        self.plan_name = plan_name
        self.status = status
        self.yunzhi_product_name = yunzhi_product_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_dept is not None:
            result['accountDept'] = self.account_dept
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.approval_url is not None:
            result['approvalUrl'] = self.approval_url
        if self.bpm_substate is not None:
            result['bpmSubstate'] = self.bpm_substate
        if self.commodity_type_code_list is not None:
            result['commodityTypeCodeList'] = self.commodity_type_code_list
        if self.creator is not None:
            result['creator'] = self.creator
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.description is not None:
            result['description'] = self.description
        if self.detail_type is not None:
            result['detailType'] = self.detail_type
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        if self.plan_name is not None:
            result['planName'] = self.plan_name
        if self.status is not None:
            result['status'] = self.status
        if self.yunzhi_product_name is not None:
            result['yunzhiProductName'] = self.yunzhi_product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountDept') is not None:
            self.account_dept = m.get('accountDept')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('approvalUrl') is not None:
            self.approval_url = m.get('approvalUrl')
        if m.get('bpmSubstate') is not None:
            self.bpm_substate = m.get('bpmSubstate')
        if m.get('commodityTypeCodeList') is not None:
            self.commodity_type_code_list = m.get('commodityTypeCodeList')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('detailType') is not None:
            self.detail_type = m.get('detailType')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        if m.get('planName') is not None:
            self.plan_name = m.get('planName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('yunzhiProductName') is not None:
            self.yunzhi_product_name = m.get('yunzhiProductName')
        return self


class GetUrgentDemandPlanDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetUrgentDemandPlanDetailResponseBodyData = None,
        message: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # code
        self.code = code
        # body
        self.data = data
        self.message = message
        # success
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetUrgentDemandPlanDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class GetUrgentDemandPlanDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUrgentDemandPlanDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUrgentDemandPlanDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUrgentDemandPlanListHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        yun_user_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.yun_user_id = yun_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.yun_user_id is not None:
            result['Yun-User-Id'] = self.yun_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Yun-User-Id') is not None:
            self.yun_user_id = m.get('Yun-User-Id')
        return self


class GetUrgentDemandPlanListRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        period: str = None,
        plan_type: int = None,
        size: int = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.current = current
        # This parameter is required.
        self.period = period
        # This parameter is required.
        self.plan_type = plan_type
        # This parameter is required.
        self.size = size
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['current'] = self.current
        if self.period is not None:
            result['period'] = self.period
        if self.plan_type is not None:
            result['planType'] = self.plan_type
        if self.size is not None:
            result['size'] = self.size
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('planType') is not None:
            self.plan_type = m.get('planType')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetUrgentDemandPlanListResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        account_type: str = None,
        approval_url: str = None,
        creator: str = None,
        creator_name: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        modifier: str = None,
        modifier_name: str = None,
        plan_id: int = None,
        plan_name: str = None,
        status: int = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.account_type = account_type
        self.approval_url = approval_url
        self.creator = creator
        self.creator_name = creator_name
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.plan_id = plan_id
        self.plan_name = plan_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.approval_url is not None:
            result['approvalUrl'] = self.approval_url
        if self.creator is not None:
            result['creator'] = self.creator
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.description is not None:
            result['description'] = self.description
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        if self.plan_name is not None:
            result['planName'] = self.plan_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('approvalUrl') is not None:
            self.approval_url = m.get('approvalUrl')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        if m.get('planName') is not None:
            self.plan_name = m.get('planName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetUrgentDemandPlanListResponseBodyData(TeaModel):
    def __init__(
        self,
        current: int = None,
        pages: int = None,
        records: List[GetUrgentDemandPlanListResponseBodyDataRecords] = None,
        size: int = None,
        total: int = None,
    ):
        self.current = current
        self.pages = pages
        self.records = records
        self.size = size
        self.total = total

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['current'] = self.current
        if self.pages is not None:
            result['pages'] = self.pages
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        if self.size is not None:
            result['size'] = self.size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('pages') is not None:
            self.pages = m.get('pages')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = GetUrgentDemandPlanListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetUrgentDemandPlanListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetUrgentDemandPlanListResponseBodyData = None,
        message: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetUrgentDemandPlanListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class GetUrgentDemandPlanListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUrgentDemandPlanListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUrgentDemandPlanListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageDemandPlanWithDemandInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        yun_user_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.yun_user_id = yun_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.yun_user_id is not None:
            result['Yun-User-Id'] = self.yun_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Yun-User-Id') is not None:
            self.yun_user_id = m.get('Yun-User-Id')
        return self


class PageDemandPlanWithDemandInfoRequest(TeaModel):
    def __init__(
        self,
        approval_status: str = None,
        create_time_end: str = None,
        create_time_start: str = None,
        creator_staff_id: str = None,
        demand_delivery_status: str = None,
        demand_id: List[int] = None,
        demand_plan_id: List[int] = None,
        demand_plan_status: str = None,
        operator: str = None,
        page_num: int = None,
        page_size: int = None,
        ro_code: str = None,
    ):
        self.approval_status = approval_status
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.creator_staff_id = creator_staff_id
        self.demand_delivery_status = demand_delivery_status
        self.demand_id = demand_id
        self.demand_plan_id = demand_plan_id
        self.demand_plan_status = demand_plan_status
        # This parameter is required.
        self.operator = operator
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size
        self.ro_code = ro_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_status is not None:
            result['approvalStatus'] = self.approval_status
        if self.create_time_end is not None:
            result['createTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['createTimeStart'] = self.create_time_start
        if self.creator_staff_id is not None:
            result['creatorStaffId'] = self.creator_staff_id
        if self.demand_delivery_status is not None:
            result['demandDeliveryStatus'] = self.demand_delivery_status
        if self.demand_id is not None:
            result['demandId'] = self.demand_id
        if self.demand_plan_id is not None:
            result['demandPlanId'] = self.demand_plan_id
        if self.demand_plan_status is not None:
            result['demandPlanStatus'] = self.demand_plan_status
        if self.operator is not None:
            result['operator'] = self.operator
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.ro_code is not None:
            result['roCode'] = self.ro_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approvalStatus') is not None:
            self.approval_status = m.get('approvalStatus')
        if m.get('createTimeEnd') is not None:
            self.create_time_end = m.get('createTimeEnd')
        if m.get('createTimeStart') is not None:
            self.create_time_start = m.get('createTimeStart')
        if m.get('creatorStaffId') is not None:
            self.creator_staff_id = m.get('creatorStaffId')
        if m.get('demandDeliveryStatus') is not None:
            self.demand_delivery_status = m.get('demandDeliveryStatus')
        if m.get('demandId') is not None:
            self.demand_id = m.get('demandId')
        if m.get('demandPlanId') is not None:
            self.demand_plan_id = m.get('demandPlanId')
        if m.get('demandPlanStatus') is not None:
            self.demand_plan_status = m.get('demandPlanStatus')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('roCode') is not None:
            self.ro_code = m.get('roCode')
        return self


class PageDemandPlanWithDemandInfoResponseBodyDataData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        approval_node_status: str = None,
        approval_status: str = None,
        creator: str = None,
        delivery_plan_id: str = None,
        delivery_status: str = None,
        demand_desc: str = None,
        demand_id: int = None,
        demand_name: str = None,
        demand_plan_id: float = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        modifier: str = None,
        requirement_object_code: str = None,
        uid: int = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.approval_node_status = approval_node_status
        self.approval_status = approval_status
        self.creator = creator
        self.delivery_plan_id = delivery_plan_id
        self.delivery_status = delivery_status
        self.demand_desc = demand_desc
        self.demand_id = demand_id
        self.demand_name = demand_name
        self.demand_plan_id = demand_plan_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.modifier = modifier
        self.requirement_object_code = requirement_object_code
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.approval_node_status is not None:
            result['approvalNodeStatus'] = self.approval_node_status
        if self.approval_status is not None:
            result['approvalStatus'] = self.approval_status
        if self.creator is not None:
            result['creator'] = self.creator
        if self.delivery_plan_id is not None:
            result['deliveryPlanId'] = self.delivery_plan_id
        if self.delivery_status is not None:
            result['deliveryStatus'] = self.delivery_status
        if self.demand_desc is not None:
            result['demandDesc'] = self.demand_desc
        if self.demand_id is not None:
            result['demandId'] = self.demand_id
        if self.demand_name is not None:
            result['demandName'] = self.demand_name
        if self.demand_plan_id is not None:
            result['demandPlanId'] = self.demand_plan_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.requirement_object_code is not None:
            result['requirementObjectCode'] = self.requirement_object_code
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('approvalNodeStatus') is not None:
            self.approval_node_status = m.get('approvalNodeStatus')
        if m.get('approvalStatus') is not None:
            self.approval_status = m.get('approvalStatus')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('deliveryPlanId') is not None:
            self.delivery_plan_id = m.get('deliveryPlanId')
        if m.get('deliveryStatus') is not None:
            self.delivery_status = m.get('deliveryStatus')
        if m.get('demandDesc') is not None:
            self.demand_desc = m.get('demandDesc')
        if m.get('demandId') is not None:
            self.demand_id = m.get('demandId')
        if m.get('demandName') is not None:
            self.demand_name = m.get('demandName')
        if m.get('demandPlanId') is not None:
            self.demand_plan_id = m.get('demandPlanId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('requirementObjectCode') is not None:
            self.requirement_object_code = m.get('requirementObjectCode')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class PageDemandPlanWithDemandInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[PageDemandPlanWithDemandInfoResponseBodyDataData] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.data = data
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = PageDemandPlanWithDemandInfoResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class PageDemandPlanWithDemandInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: PageDemandPlanWithDemandInfoResponseBodyData = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = PageDemandPlanWithDemandInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class PageDemandPlanWithDemandInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PageDemandPlanWithDemandInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PageDemandPlanWithDemandInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushResourcePlanHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        yun_user_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.yun_user_id = yun_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.yun_user_id is not None:
            result['Yun-User-Id'] = self.yun_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Yun-User-Id') is not None:
            self.yun_user_id = m.get('Yun-User-Id')
        return self


class PushResourcePlanRequestMethodListDataList(TeaModel):
    def __init__(
        self,
        class_zone: str = None,
        convert_host_type: str = None,
        logic_zone: str = None,
        net_arch: str = None,
        nic: str = None,
        product_3: str = None,
        safe_zone: str = None,
        scenario: str = None,
        supply_amount: int = None,
        supply_date: str = None,
        supply_type: int = None,
        supply_vm_amount: int = None,
    ):
        self.class_zone = class_zone
        self.convert_host_type = convert_host_type
        self.logic_zone = logic_zone
        self.net_arch = net_arch
        self.nic = nic
        self.product_3 = product_3
        self.safe_zone = safe_zone
        self.scenario = scenario
        self.supply_amount = supply_amount
        # This parameter is required.
        self.supply_date = supply_date
        self.supply_type = supply_type
        self.supply_vm_amount = supply_vm_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_zone is not None:
            result['classZone'] = self.class_zone
        if self.convert_host_type is not None:
            result['convertHostType'] = self.convert_host_type
        if self.logic_zone is not None:
            result['logicZone'] = self.logic_zone
        if self.net_arch is not None:
            result['netArch'] = self.net_arch
        if self.nic is not None:
            result['nic'] = self.nic
        if self.product_3 is not None:
            result['product3'] = self.product_3
        if self.safe_zone is not None:
            result['safeZone'] = self.safe_zone
        if self.scenario is not None:
            result['scenario'] = self.scenario
        if self.supply_amount is not None:
            result['supplyAmount'] = self.supply_amount
        if self.supply_date is not None:
            result['supplyDate'] = self.supply_date
        if self.supply_type is not None:
            result['supplyType'] = self.supply_type
        if self.supply_vm_amount is not None:
            result['supplyVmAmount'] = self.supply_vm_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('classZone') is not None:
            self.class_zone = m.get('classZone')
        if m.get('convertHostType') is not None:
            self.convert_host_type = m.get('convertHostType')
        if m.get('logicZone') is not None:
            self.logic_zone = m.get('logicZone')
        if m.get('netArch') is not None:
            self.net_arch = m.get('netArch')
        if m.get('nic') is not None:
            self.nic = m.get('nic')
        if m.get('product3') is not None:
            self.product_3 = m.get('product3')
        if m.get('safeZone') is not None:
            self.safe_zone = m.get('safeZone')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        if m.get('supplyAmount') is not None:
            self.supply_amount = m.get('supplyAmount')
        if m.get('supplyDate') is not None:
            self.supply_date = m.get('supplyDate')
        if m.get('supplyType') is not None:
            self.supply_type = m.get('supplyType')
        if m.get('supplyVmAmount') is not None:
            self.supply_vm_amount = m.get('supplyVmAmount')
        return self


class PushResourcePlanRequestMethodList(TeaModel):
    def __init__(
        self,
        azone: str = None,
        buffer_cnt: int = None,
        cluster: str = None,
        comment: str = None,
        convert_host_cnt: int = None,
        convert_host_type: str = None,
        data_list: List[PushResourcePlanRequestMethodListDataList] = None,
        denamd_count: int = None,
        gap_cnt: int = None,
        promise_date: str = None,
        region: str = None,
        resource_method_id: int = None,
        room_code: str = None,
    ):
        self.azone = azone
        self.buffer_cnt = buffer_cnt
        self.cluster = cluster
        self.comment = comment
        self.convert_host_cnt = convert_host_cnt
        self.convert_host_type = convert_host_type
        self.data_list = data_list
        self.denamd_count = denamd_count
        self.gap_cnt = gap_cnt
        self.promise_date = promise_date
        self.region = region
        self.resource_method_id = resource_method_id
        self.room_code = room_code

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.azone is not None:
            result['azone'] = self.azone
        if self.buffer_cnt is not None:
            result['bufferCnt'] = self.buffer_cnt
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.comment is not None:
            result['comment'] = self.comment
        if self.convert_host_cnt is not None:
            result['convertHostCnt'] = self.convert_host_cnt
        if self.convert_host_type is not None:
            result['convertHostType'] = self.convert_host_type
        result['dataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['dataList'].append(k.to_map() if k else None)
        if self.denamd_count is not None:
            result['denamdCount'] = self.denamd_count
        if self.gap_cnt is not None:
            result['gapCnt'] = self.gap_cnt
        if self.promise_date is not None:
            result['promiseDate'] = self.promise_date
        if self.region is not None:
            result['region'] = self.region
        if self.resource_method_id is not None:
            result['resourceMethodId'] = self.resource_method_id
        if self.room_code is not None:
            result['roomCode'] = self.room_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('azone') is not None:
            self.azone = m.get('azone')
        if m.get('bufferCnt') is not None:
            self.buffer_cnt = m.get('bufferCnt')
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('convertHostCnt') is not None:
            self.convert_host_cnt = m.get('convertHostCnt')
        if m.get('convertHostType') is not None:
            self.convert_host_type = m.get('convertHostType')
        self.data_list = []
        if m.get('dataList') is not None:
            for k in m.get('dataList'):
                temp_model = PushResourcePlanRequestMethodListDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('denamdCount') is not None:
            self.denamd_count = m.get('denamdCount')
        if m.get('gapCnt') is not None:
            self.gap_cnt = m.get('gapCnt')
        if m.get('promiseDate') is not None:
            self.promise_date = m.get('promiseDate')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('resourceMethodId') is not None:
            self.resource_method_id = m.get('resourceMethodId')
        if m.get('roomCode') is not None:
            self.room_code = m.get('roomCode')
        return self


class PushResourcePlanRequest(TeaModel):
    def __init__(
        self,
        buffer_cnt: int = None,
        demand_count: int = None,
        demand_id: str = None,
        method_list: List[PushResourcePlanRequestMethodList] = None,
        request_id: str = None,
        require_cnt: int = None,
        sub_demand_id: str = None,
    ):
        self.buffer_cnt = buffer_cnt
        self.demand_count = demand_count
        self.demand_id = demand_id
        self.method_list = method_list
        self.request_id = request_id
        self.require_cnt = require_cnt
        self.sub_demand_id = sub_demand_id

    def validate(self):
        if self.method_list:
            for k in self.method_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buffer_cnt is not None:
            result['bufferCnt'] = self.buffer_cnt
        if self.demand_count is not None:
            result['demandCount'] = self.demand_count
        if self.demand_id is not None:
            result['demandId'] = self.demand_id
        result['methodList'] = []
        if self.method_list is not None:
            for k in self.method_list:
                result['methodList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.require_cnt is not None:
            result['requireCnt'] = self.require_cnt
        if self.sub_demand_id is not None:
            result['subDemandId'] = self.sub_demand_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bufferCnt') is not None:
            self.buffer_cnt = m.get('bufferCnt')
        if m.get('demandCount') is not None:
            self.demand_count = m.get('demandCount')
        if m.get('demandId') is not None:
            self.demand_id = m.get('demandId')
        self.method_list = []
        if m.get('methodList') is not None:
            for k in m.get('methodList'):
                temp_model = PushResourcePlanRequestMethodList()
                self.method_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('requireCnt') is not None:
            self.require_cnt = m.get('requireCnt')
        if m.get('subDemandId') is not None:
            self.sub_demand_id = m.get('subDemandId')
        return self


class PushResourcePlanResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        message: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class PushResourcePlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushResourcePlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PushResourcePlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeliveredSupplyItemsRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        commodity_type_code: str = None,
    ):
        self.account_id = account_id
        self.commodity_type_code = commodity_type_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.commodity_type_code is not None:
            result['commodityTypeCode'] = self.commodity_type_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('commodityTypeCode') is not None:
            self.commodity_type_code = m.get('commodityTypeCode')
        return self


class QueryDeliveredSupplyItemsResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        commodity_type_code: str = None,
        demand_plan_id: int = None,
        plan_title: str = None,
        region: str = None,
        zone: str = None,
        commodity_code: str = None,
        demand_count: int = None,
        delivered_amount: int = None,
        open_count: int = None,
    ):
        self.account_id = account_id
        self.commodity_type_code = commodity_type_code
        self.demand_plan_id = demand_plan_id
        self.plan_title = plan_title
        self.region = region
        self.zone = zone
        self.commodity_code = commodity_code
        self.demand_count = demand_count
        self.delivered_amount = delivered_amount
        self.open_count = open_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.commodity_type_code is not None:
            result['commodityTypeCode'] = self.commodity_type_code
        if self.demand_plan_id is not None:
            result['demandPlanId'] = self.demand_plan_id
        if self.plan_title is not None:
            result['planTitle'] = self.plan_title
        if self.region is not None:
            result['region'] = self.region
        if self.zone is not None:
            result['zone'] = self.zone
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.demand_count is not None:
            result['demandCount'] = self.demand_count
        if self.delivered_amount is not None:
            result['deliveredAmount'] = self.delivered_amount
        if self.open_count is not None:
            result['openCount'] = self.open_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('commodityTypeCode') is not None:
            self.commodity_type_code = m.get('commodityTypeCode')
        if m.get('demandPlanId') is not None:
            self.demand_plan_id = m.get('demandPlanId')
        if m.get('planTitle') is not None:
            self.plan_title = m.get('planTitle')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('demandCount') is not None:
            self.demand_count = m.get('demandCount')
        if m.get('deliveredAmount') is not None:
            self.delivered_amount = m.get('deliveredAmount')
        if m.get('openCount') is not None:
            self.open_count = m.get('openCount')
        return self


class QueryDeliveredSupplyItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[QueryDeliveredSupplyItemsResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = QueryDeliveredSupplyItemsResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class QueryPeriodBudgetBillRequest(TeaModel):
    def __init__(
        self,
        object_ids: str = None,
        object_type: str = None,
        period: str = None,
    ):
        self.object_ids = object_ids
        self.object_type = object_type
        self.period = period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_ids is not None:
            result['objectIds'] = self.object_ids
        if self.object_type is not None:
            result['objectType'] = self.object_type
        if self.period is not None:
            result['period'] = self.period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectIds') is not None:
            self.object_ids = m.get('objectIds')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        if m.get('period') is not None:
            self.period = m.get('period')
        return self


class QueryPeriodBudgetBillResponseBodyPeriodBudgetBillDTOS(TeaModel):
    def __init__(
        self,
        bill: float = None,
        budget: float = None,
        last_year_bill: float = None,
        month: str = None,
    ):
        self.bill = bill
        self.budget = budget
        self.last_year_bill = last_year_bill
        self.month = month

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill is not None:
            result['bill'] = self.bill
        if self.budget is not None:
            result['budget'] = self.budget
        if self.last_year_bill is not None:
            result['lastYearBill'] = self.last_year_bill
        if self.month is not None:
            result['month'] = self.month
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bill') is not None:
            self.bill = m.get('bill')
        if m.get('budget') is not None:
            self.budget = m.get('budget')
        if m.get('lastYearBill') is not None:
            self.last_year_bill = m.get('lastYearBill')
        if m.get('month') is not None:
            self.month = m.get('month')
        return self


class QueryPeriodBudgetBillResponseBody(TeaModel):
    def __init__(
        self,
        period_budget_bill_dtos: List[QueryPeriodBudgetBillResponseBodyPeriodBudgetBillDTOS] = None,
    ):
        self.period_budget_bill_dtos = period_budget_bill_dtos

    def validate(self):
        if self.period_budget_bill_dtos:
            for k in self.period_budget_bill_dtos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['periodBudgetBillDTOS'] = []
        if self.period_budget_bill_dtos is not None:
            for k in self.period_budget_bill_dtos:
                result['periodBudgetBillDTOS'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.period_budget_bill_dtos = []
        if m.get('periodBudgetBillDTOS') is not None:
            for k in m.get('periodBudgetBillDTOS'):
                temp_model = QueryPeriodBudgetBillResponseBodyPeriodBudgetBillDTOS()
                self.period_budget_bill_dtos.append(temp_model.from_map(k))
        return self


class QueryPeriodBudgetBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPeriodBudgetBillResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPeriodBudgetBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveUrgentDemandItemHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        yun_user_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.yun_user_id = yun_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.yun_user_id is not None:
            result['Yun-User-Id'] = self.yun_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Yun-User-Id') is not None:
            self.yun_user_id = m.get('Yun-User-Id')
        return self


class SaveUrgentDemandItemRequestUrgentDemandEbsRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_num: int = None,
        commodity_type_code: str = None,
        item_id: int = None,
        performance_level: int = None,
    ):
        self.commodity_code = commodity_code
        self.commodity_num = commodity_num
        self.commodity_type_code = commodity_type_code
        self.item_id = item_id
        self.performance_level = performance_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.commodity_num is not None:
            result['commodityNum'] = self.commodity_num
        if self.commodity_type_code is not None:
            result['commodityTypeCode'] = self.commodity_type_code
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('commodityNum') is not None:
            self.commodity_num = m.get('commodityNum')
        if m.get('commodityTypeCode') is not None:
            self.commodity_type_code = m.get('commodityTypeCode')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')
        return self


class SaveUrgentDemandItemRequestUrgentDemandEcsRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_num: int = None,
        commodity_type_code: str = None,
        item_id: int = None,
        v_cpu_count: int = None,
    ):
        self.commodity_code = commodity_code
        self.commodity_num = commodity_num
        self.commodity_type_code = commodity_type_code
        self.item_id = item_id
        self.v_cpu_count = v_cpu_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.commodity_num is not None:
            result['commodityNum'] = self.commodity_num
        if self.commodity_type_code is not None:
            result['commodityTypeCode'] = self.commodity_type_code
        if self.item_id is not None:
            result['itemId'] = self.item_id
        if self.v_cpu_count is not None:
            result['vCpuCount'] = self.v_cpu_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('commodityNum') is not None:
            self.commodity_num = m.get('commodityNum')
        if m.get('commodityTypeCode') is not None:
            self.commodity_type_code = m.get('commodityTypeCode')
        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')
        if m.get('vCpuCount') is not None:
            self.v_cpu_count = m.get('vCpuCount')
        return self


class SaveUrgentDemandItemRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        creator: str = None,
        effect_time: str = None,
        modifier: str = None,
        network_type: str = None,
        pay_duration: str = None,
        pay_duration_unit: str = None,
        pay_type: str = None,
        plan_id: int = None,
        region: str = None,
        urgent_demand_ebs_request: SaveUrgentDemandItemRequestUrgentDemandEbsRequest = None,
        urgent_demand_ecs_request: SaveUrgentDemandItemRequestUrgentDemandEcsRequest = None,
        zone: str = None,
    ):
        self.account_id = account_id
        self.creator = creator
        self.effect_time = effect_time
        self.modifier = modifier
        self.network_type = network_type
        self.pay_duration = pay_duration
        self.pay_duration_unit = pay_duration_unit
        self.pay_type = pay_type
        self.plan_id = plan_id
        self.region = region
        self.urgent_demand_ebs_request = urgent_demand_ebs_request
        self.urgent_demand_ecs_request = urgent_demand_ecs_request
        self.zone = zone

    def validate(self):
        if self.urgent_demand_ebs_request:
            self.urgent_demand_ebs_request.validate()
        if self.urgent_demand_ecs_request:
            self.urgent_demand_ecs_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.creator is not None:
            result['creator'] = self.creator
        if self.effect_time is not None:
            result['effectTime'] = self.effect_time
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.pay_duration is not None:
            result['payDuration'] = self.pay_duration
        if self.pay_duration_unit is not None:
            result['payDurationUnit'] = self.pay_duration_unit
        if self.pay_type is not None:
            result['payType'] = self.pay_type
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        if self.region is not None:
            result['region'] = self.region
        if self.urgent_demand_ebs_request is not None:
            result['urgentDemandEbsRequest'] = self.urgent_demand_ebs_request.to_map()
        if self.urgent_demand_ecs_request is not None:
            result['urgentDemandEcsRequest'] = self.urgent_demand_ecs_request.to_map()
        if self.zone is not None:
            result['zone'] = self.zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('effectTime') is not None:
            self.effect_time = m.get('effectTime')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('payDuration') is not None:
            self.pay_duration = m.get('payDuration')
        if m.get('payDurationUnit') is not None:
            self.pay_duration_unit = m.get('payDurationUnit')
        if m.get('payType') is not None:
            self.pay_type = m.get('payType')
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('urgentDemandEbsRequest') is not None:
            temp_model = SaveUrgentDemandItemRequestUrgentDemandEbsRequest()
            self.urgent_demand_ebs_request = temp_model.from_map(m['urgentDemandEbsRequest'])
        if m.get('urgentDemandEcsRequest') is not None:
            temp_model = SaveUrgentDemandItemRequestUrgentDemandEcsRequest()
            self.urgent_demand_ecs_request = temp_model.from_map(m['urgentDemandEcsRequest'])
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        return self


class SaveUrgentDemandItemResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[int] = None,
        message: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class SaveUrgentDemandItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveUrgentDemandItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveUrgentDemandItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitUrgentDemandPlanHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        yun_user_id: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.yun_user_id = yun_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.yun_user_id is not None:
            result['Yun-User-Id'] = self.yun_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Yun-User-Id') is not None:
            self.yun_user_id = m.get('Yun-User-Id')
        return self


class SubmitUrgentDemandPlanRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.plan_id = plan_id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SubmitUrgentDemandPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        message: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # code
        self.code = code
        self.data = data
        self.message = message
        # success
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class SubmitUrgentDemandPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitUrgentDemandPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitUrgentDemandPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AcceptFulfillmentDecisionRequest(TeaModel):
    def __init__(
        self,
        decision_conclusion: str = None,
        decision_type: str = None,
        order_id: str = None,
    ):
        self.decision_conclusion = decision_conclusion
        self.decision_type = decision_type
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decision_conclusion is not None:
            result['DecisionConclusion'] = self.decision_conclusion
        if self.decision_type is not None:
            result['DecisionType'] = self.decision_type
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DecisionConclusion') is not None:
            self.decision_conclusion = m.get('DecisionConclusion')
        if m.get('DecisionType') is not None:
            self.decision_type = m.get('DecisionType')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class AcceptFulfillmentDecisionResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AcceptFulfillmentDecisionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AcceptFulfillmentDecisionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AcceptFulfillmentDecisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


