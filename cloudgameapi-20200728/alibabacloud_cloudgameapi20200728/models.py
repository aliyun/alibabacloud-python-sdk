# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class BatchDispatchGameSlotRequest(TeaModel):
    def __init__(
        self,
        queue_user_list: str = None,
    ):
        self.queue_user_list = queue_user_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_user_list is not None:
            result['QueueUserList'] = self.queue_user_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueueUserList') is not None:
            self.queue_user_list = m.get('QueueUserList')
        return self


class BatchDispatchGameSlotResponseBodyQueueResultList(TeaModel):
    def __init__(
        self,
        region_name: str = None,
        game_session: str = None,
        user_id: str = None,
        queue_state: int = None,
        message: str = None,
        game_id: str = None,
        queue_code: int = None,
    ):
        self.region_name = region_name
        self.game_session = game_session
        self.user_id = user_id
        self.queue_state = queue_state
        self.message = message
        self.game_id = game_id
        self.queue_code = queue_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.queue_state is not None:
            result['QueueState'] = self.queue_state
        if self.message is not None:
            result['Message'] = self.message
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.queue_code is not None:
            result['QueueCode'] = self.queue_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('QueueState') is not None:
            self.queue_state = m.get('QueueState')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('QueueCode') is not None:
            self.queue_code = m.get('QueueCode')
        return self


class BatchDispatchGameSlotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        queue_result_list: List[BatchDispatchGameSlotResponseBodyQueueResultList] = None,
    ):
        self.request_id = request_id
        self.queue_result_list = queue_result_list

    def validate(self):
        if self.queue_result_list:
            for k in self.queue_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['QueueResultList'] = []
        if self.queue_result_list is not None:
            for k in self.queue_result_list:
                result['QueueResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.queue_result_list = []
        if m.get('QueueResultList') is not None:
            for k in m.get('QueueResultList'):
                temp_model = BatchDispatchGameSlotResponseBodyQueueResultList()
                self.queue_result_list.append(temp_model.from_map(k))
        return self


class BatchDispatchGameSlotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchDispatchGameSlotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = BatchDispatchGameSlotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopGameSessionsRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        game_id: str = None,
        token: str = None,
        reason: str = None,
        track_info: str = None,
        tags: str = None,
    ):
        self.project_id = project_id
        self.game_id = game_id
        self.token = token
        self.reason = reason
        self.track_info = track_info
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.token is not None:
            result['Token'] = self.token
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.track_info is not None:
            result['TrackInfo'] = self.track_info
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('TrackInfo') is not None:
            self.track_info = m.get('TrackInfo')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class BatchStopGameSessionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        project_id: str = None,
        queue_state: int = None,
        message: str = None,
        game_id: str = None,
        track_info: str = None,
    ):
        self.request_id = request_id
        self.success = success
        self.project_id = project_id
        self.queue_state = queue_state
        self.message = message
        self.game_id = game_id
        self.track_info = track_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.queue_state is not None:
            result['QueueState'] = self.queue_state
        if self.message is not None:
            result['Message'] = self.message
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.track_info is not None:
            result['TrackInfo'] = self.track_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('QueueState') is not None:
            self.queue_state = m.get('QueueState')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('TrackInfo') is not None:
            self.track_info = m.get('TrackInfo')
        return self


class BatchStopGameSessionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchStopGameSessionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = BatchStopGameSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseOrderRequest(TeaModel):
    def __init__(
        self,
        buyer_account_id: str = None,
        order_id: str = None,
        account_domain: str = None,
    ):
        self.buyer_account_id = buyer_account_id
        self.order_id = order_id
        self.account_domain = account_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class CloseOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloseOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloseOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CloseOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        buyer_account_id: str = None,
        item_id: str = None,
        sku_id: str = None,
        origin_price: int = None,
        settlement_price: int = None,
        amount: int = None,
        idempotent_code: str = None,
        account_domain: str = None,
    ):
        self.buyer_account_id = buyer_account_id
        self.item_id = item_id
        self.sku_id = sku_id
        self.origin_price = origin_price
        self.settlement_price = settlement_price
        self.amount = amount
        self.idempotent_code = idempotent_code
        self.account_domain = account_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.settlement_price is not None:
            result['SettlementPrice'] = self.settlement_price
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.idempotent_code is not None:
            result['IdempotentCode'] = self.idempotent_code
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('SettlementPrice') is not None:
            self.settlement_price = m.get('SettlementPrice')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('IdempotentCode') is not None:
            self.idempotent_code = m.get('IdempotentCode')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class CreateOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        finish_time: int = None,
        create_time: int = None,
        auto_unlock_time: int = None,
        apply_delivery_time: int = None,
        item_id: str = None,
        origin_price: int = None,
        buyer_account_id: str = None,
        amount: int = None,
        sku_id: str = None,
        settlement_price: int = None,
        order_id: str = None,
        account_domain: str = None,
    ):
        self.status = status
        self.finish_time = finish_time
        self.create_time = create_time
        self.auto_unlock_time = auto_unlock_time
        self.apply_delivery_time = apply_delivery_time
        self.item_id = item_id
        self.origin_price = origin_price
        self.buyer_account_id = buyer_account_id
        self.amount = amount
        self.sku_id = sku_id
        self.settlement_price = settlement_price
        self.order_id = order_id
        self.account_domain = account_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.auto_unlock_time is not None:
            result['AutoUnlockTime'] = self.auto_unlock_time
        if self.apply_delivery_time is not None:
            result['ApplyDeliveryTime'] = self.apply_delivery_time
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.settlement_price is not None:
            result['SettlementPrice'] = self.settlement_price
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AutoUnlockTime') is not None:
            self.auto_unlock_time = m.get('AutoUnlockTime')
        if m.get('ApplyDeliveryTime') is not None:
            self.apply_delivery_time = m.get('ApplyDeliveryTime')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SettlementPrice') is not None:
            self.settlement_price = m.get('SettlementPrice')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: CreateOrderResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTokenRequest(TeaModel):
    def __init__(
        self,
        session: str = None,
        current_token: str = None,
        client_token: str = None,
    ):
        self.session = session
        self.current_token = current_token
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session is not None:
            result['Session'] = self.session
        if self.current_token is not None:
            result['CurrentToken'] = self.current_token
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Session') is not None:
            self.session = m.get('Session')
        if m.get('CurrentToken') is not None:
            self.current_token = m.get('CurrentToken')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        token: str = None,
    ):
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class CreateTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: CreateTokenResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTokenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreateTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeliveryOrderRequest(TeaModel):
    def __init__(
        self,
        buyer_account_id: str = None,
        order_id: str = None,
        account_domain: str = None,
    ):
        self.buyer_account_id = buyer_account_id
        self.order_id = order_id
        self.account_domain = account_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class DeliveryOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        delivery_status: str = None,
    ):
        self.delivery_status = delivery_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_status is not None:
            result['DeliveryStatus'] = self.delivery_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryStatus') is not None:
            self.delivery_status = m.get('DeliveryStatus')
        return self


class DeliveryOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DeliveryOrderResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DeliveryOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DeliveryOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeliveryOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DeliveryOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DispatchGameSlotRequest(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        access_key: str = None,
        region_name: str = None,
        user_id: str = None,
        biz_param: str = None,
        cancel: bool = None,
        game_session: str = None,
        game_start_param: str = None,
        game_command: str = None,
        system_info: str = None,
        client_ip: str = None,
        reconnect: bool = None,
        tags: str = None,
    ):
        self.game_id = game_id
        self.access_key = access_key
        self.region_name = region_name
        self.user_id = user_id
        self.biz_param = biz_param
        self.cancel = cancel
        self.game_session = game_session
        self.game_start_param = game_start_param
        self.game_command = game_command
        self.system_info = system_info
        self.client_ip = client_ip
        self.reconnect = reconnect
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_param is not None:
            result['BizParam'] = self.biz_param
        if self.cancel is not None:
            result['Cancel'] = self.cancel
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.game_start_param is not None:
            result['GameStartParam'] = self.game_start_param
        if self.game_command is not None:
            result['GameCommand'] = self.game_command
        if self.system_info is not None:
            result['SystemInfo'] = self.system_info
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.reconnect is not None:
            result['Reconnect'] = self.reconnect
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizParam') is not None:
            self.biz_param = m.get('BizParam')
        if m.get('Cancel') is not None:
            self.cancel = m.get('Cancel')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('GameStartParam') is not None:
            self.game_start_param = m.get('GameStartParam')
        if m.get('GameCommand') is not None:
            self.game_command = m.get('GameCommand')
        if m.get('SystemInfo') is not None:
            self.system_info = m.get('SystemInfo')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Reconnect') is not None:
            self.reconnect = m.get('Reconnect')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DispatchGameSlotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        region_name: str = None,
        game_session: str = None,
        user_id: str = None,
        queue_state: int = None,
        message: str = None,
        game_id: str = None,
        queue_code: int = None,
    ):
        self.request_id = request_id
        self.region_name = region_name
        self.game_session = game_session
        self.user_id = user_id
        self.queue_state = queue_state
        self.message = message
        self.game_id = game_id
        self.queue_code = queue_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.queue_state is not None:
            result['QueueState'] = self.queue_state
        if self.message is not None:
            result['Message'] = self.message
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.queue_code is not None:
            result['QueueCode'] = self.queue_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('QueueState') is not None:
            self.queue_state = m.get('QueueState')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('QueueCode') is not None:
            self.queue_code = m.get('QueueCode')
        return self


class DispatchGameSlotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DispatchGameSlotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = DispatchGameSlotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGameCcuRequest(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        region_name: str = None,
        access_key: str = None,
    ):
        self.game_id = game_id
        self.region_name = region_name
        self.access_key = access_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        return self


class GetGameCcuResponseBodyDataList(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        ccu: int = None,
        region_id: str = None,
    ):
        self.game_id = game_id
        self.ccu = ccu
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.ccu is not None:
            result['Ccu'] = self.ccu
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('Ccu') is not None:
            self.ccu = m.get('Ccu')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetGameCcuResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data_list: List[GetGameCcuResponseBodyDataList] = None,
    ):
        self.request_id = request_id
        self.data_list = data_list

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = GetGameCcuResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        return self


class GetGameCcuResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGameCcuResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetGameCcuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGameStockRequest(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        access_key: str = None,
        user_level: int = None,
    ):
        self.game_id = game_id
        self.access_key = access_key
        self.user_level = user_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.user_level is not None:
            result['UserLevel'] = self.user_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('UserLevel') is not None:
            self.user_level = m.get('UserLevel')
        return self


class GetGameStockResponseBodyInstanceStockList(TeaModel):
    def __init__(
        self,
        available_slots: int = None,
        regin_name: str = None,
        instance_id: str = None,
        user_level: int = None,
        instance_spec: str = None,
    ):
        self.available_slots = available_slots
        self.regin_name = regin_name
        self.instance_id = instance_id
        self.user_level = user_level
        self.instance_spec = instance_spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_slots is not None:
            result['AvailableSlots'] = self.available_slots
        if self.regin_name is not None:
            result['ReginName'] = self.regin_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_level is not None:
            result['UserLevel'] = self.user_level
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableSlots') is not None:
            self.available_slots = m.get('AvailableSlots')
        if m.get('ReginName') is not None:
            self.regin_name = m.get('ReginName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserLevel') is not None:
            self.user_level = m.get('UserLevel')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        return self


class GetGameStockResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        game_id: str = None,
        request_id: str = None,
        instance_stock_list: List[GetGameStockResponseBodyInstanceStockList] = None,
    ):
        self.message = message
        self.game_id = game_id
        self.request_id = request_id
        self.instance_stock_list = instance_stock_list

    def validate(self):
        if self.instance_stock_list:
            for k in self.instance_stock_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceStockList'] = []
        if self.instance_stock_list is not None:
            for k in self.instance_stock_list:
                result['InstanceStockList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_stock_list = []
        if m.get('InstanceStockList') is not None:
            for k in m.get('InstanceStockList'):
                temp_model = GetGameStockResponseBodyInstanceStockList()
                self.instance_stock_list.append(temp_model.from_map(k))
        return self


class GetGameStockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGameStockResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetGameStockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetItemRequest(TeaModel):
    def __init__(
        self,
        item_id: str = None,
    ):
        self.item_id = item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class GetItemResponseBodyDataGames(TeaModel):
    def __init__(
        self,
        name: str = None,
        game_id: str = None,
    ):
        self.name = name
        self.game_id = game_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.game_id is not None:
            result['GameId'] = self.game_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        return self


class GetItemResponseBodyDataSkusSaleProps(TeaModel):
    def __init__(
        self,
        value: str = None,
        value_id: int = None,
        property_id: int = None,
        property_name: str = None,
    ):
        self.value = value
        self.value_id = value_id
        self.property_id = property_id
        self.property_name = property_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.value_id is not None:
            result['ValueId'] = self.value_id
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueId') is not None:
            self.value_id = m.get('ValueId')
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        return self


class GetItemResponseBodyDataSkus(TeaModel):
    def __init__(
        self,
        status: int = None,
        create_time: int = None,
        sku_id: str = None,
        item_id: str = None,
        sale_price: int = None,
        origin_price: int = None,
        modify_time: int = None,
        sale_props: List[GetItemResponseBodyDataSkusSaleProps] = None,
    ):
        self.status = status
        self.create_time = create_time
        self.sku_id = sku_id
        self.item_id = item_id
        self.sale_price = sale_price
        self.origin_price = origin_price
        self.modify_time = modify_time
        self.sale_props = sale_props

    def validate(self):
        if self.sale_props:
            for k in self.sale_props:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sale_price is not None:
            result['SalePrice'] = self.sale_price
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        result['SaleProps'] = []
        if self.sale_props is not None:
            for k in self.sale_props:
                result['SaleProps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SalePrice') is not None:
            self.sale_price = m.get('SalePrice')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        self.sale_props = []
        if m.get('SaleProps') is not None:
            for k in m.get('SaleProps'):
                temp_model = GetItemResponseBodyDataSkusSaleProps()
                self.sale_props.append(temp_model.from_map(k))
        return self


class GetItemResponseBodyData(TeaModel):
    def __init__(
        self,
        status: int = None,
        supplier: str = None,
        description: str = None,
        create_time: int = None,
        seller_id: str = None,
        category_id: int = None,
        title: str = None,
        item_id: str = None,
        sale_price: int = None,
        origin_price: int = None,
        modify_time: int = None,
        games: List[GetItemResponseBodyDataGames] = None,
        skus: List[GetItemResponseBodyDataSkus] = None,
    ):
        self.status = status
        self.supplier = supplier
        self.description = description
        self.create_time = create_time
        self.seller_id = seller_id
        self.category_id = category_id
        self.title = title
        self.item_id = item_id
        self.sale_price = sale_price
        self.origin_price = origin_price
        self.modify_time = modify_time
        self.games = games
        self.skus = skus

    def validate(self):
        if self.games:
            for k in self.games:
                if k:
                    k.validate()
        if self.skus:
            for k in self.skus:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier is not None:
            result['Supplier'] = self.supplier
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.title is not None:
            result['Title'] = self.title
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sale_price is not None:
            result['SalePrice'] = self.sale_price
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        result['Games'] = []
        if self.games is not None:
            for k in self.games:
                result['Games'].append(k.to_map() if k else None)
        result['Skus'] = []
        if self.skus is not None:
            for k in self.skus:
                result['Skus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Supplier') is not None:
            self.supplier = m.get('Supplier')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SalePrice') is not None:
            self.sale_price = m.get('SalePrice')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        self.games = []
        if m.get('Games') is not None:
            for k in m.get('Games'):
                temp_model = GetItemResponseBodyDataGames()
                self.games.append(temp_model.from_map(k))
        self.skus = []
        if m.get('Skus') is not None:
            for k in m.get('Skus'):
                temp_model = GetItemResponseBodyDataSkus()
                self.skus.append(temp_model.from_map(k))
        return self


class GetItemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetItemResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetItemResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetItemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOutAccountBindDetailRequest(TeaModel):
    def __init__(
        self,
        out_account_type: str = None,
        account_id: str = None,
        account_domain: str = None,
    ):
        self.out_account_type = out_account_type
        self.account_id = account_id
        self.account_domain = account_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_account_type is not None:
            result['OutAccountType'] = self.out_account_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutAccountType') is not None:
            self.out_account_type = m.get('OutAccountType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class GetOutAccountBindDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        out_account_id: str = None,
        token: str = None,
        bind_status: int = None,
        token_expire_time: int = None,
        out_account_type: str = None,
    ):
        self.out_account_id = out_account_id
        self.token = token
        self.bind_status = bind_status
        self.token_expire_time = token_expire_time
        self.out_account_type = out_account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_account_id is not None:
            result['OutAccountId'] = self.out_account_id
        if self.token is not None:
            result['Token'] = self.token
        if self.bind_status is not None:
            result['BindStatus'] = self.bind_status
        if self.token_expire_time is not None:
            result['TokenExpireTime'] = self.token_expire_time
        if self.out_account_type is not None:
            result['OutAccountType'] = self.out_account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutAccountId') is not None:
            self.out_account_id = m.get('OutAccountId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('BindStatus') is not None:
            self.bind_status = m.get('BindStatus')
        if m.get('TokenExpireTime') is not None:
            self.token_expire_time = m.get('TokenExpireTime')
        if m.get('OutAccountType') is not None:
            self.out_account_type = m.get('OutAccountType')
        return self


class GetOutAccountBindDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetOutAccountBindDetailResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetOutAccountBindDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetOutAccountBindDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOutAccountBindDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetOutAccountBindDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionRequest(TeaModel):
    def __init__(
        self,
        token: str = None,
    ):
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetSessionResponseBodyData(TeaModel):
    def __init__(
        self,
        session: str = None,
    ):
        self.session = session

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session is not None:
            result['Session'] = self.session
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Session') is not None:
            self.session = m.get('Session')
        return self


class GetSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetSessionResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetSessionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSessionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStopGameTokenRequest(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        access_key: str = None,
    ):
        self.game_id = game_id
        self.access_key = access_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        return self


class GetStopGameTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        token: str = None,
        expire_time: int = None,
    ):
        self.request_id = request_id
        self.token = token
        self.expire_time = expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class GetStopGameTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetStopGameTokenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetStopGameTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBoughtGamesRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_domain: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.account_id = account_id
        self.account_domain = account_domain
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListBoughtGamesResponseBodyItems(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        game_id: str = None,
        game_name: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.game_id = game_id
        self.game_name = game_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.game_name is not None:
            result['GameName'] = self.game_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('GameName') is not None:
            self.game_name = m.get('GameName')
        return self


class ListBoughtGamesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        items: List[ListBoughtGamesResponseBodyItems] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListBoughtGamesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListBoughtGamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBoughtGamesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListBoughtGamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGameRequest(TeaModel):
    def __init__(
        self,
        project_id: int = None,
        page_no: int = None,
        page_size: int = None,
        tenant_id: int = None,
    ):
        self.project_id = project_id
        self.page_no = page_no
        self.page_size = page_size
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryGameResponseBodyData(TeaModel):
    def __init__(
        self,
        version: str = None,
        project_id: int = None,
        gmt_create: str = None,
        game_id: int = None,
        name: str = None,
        tenant_id: int = None,
    ):
        self.version = version
        self.project_id = project_id
        self.gmt_create = gmt_create
        self.game_id = game_id
        self.name = name
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryGameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        data: List[QueryGameResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.data = data

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryGameResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryGameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryGameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = QueryGameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryItemsResponseBodyDataItemsSkusSaleProps(TeaModel):
    def __init__(
        self,
        value: str = None,
        value_id: int = None,
        property_name: str = None,
        property_id: int = None,
    ):
        self.value = value
        self.value_id = value_id
        self.property_name = property_name
        self.property_id = property_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.value_id is not None:
            result['ValueId'] = self.value_id
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueId') is not None:
            self.value_id = m.get('ValueId')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        return self


class QueryItemsResponseBodyDataItemsSkus(TeaModel):
    def __init__(
        self,
        status: int = None,
        create_time: int = None,
        sku_id: str = None,
        item_id: str = None,
        sale_price: int = None,
        origin_price: int = None,
        modify_time: int = None,
        sale_props: List[QueryItemsResponseBodyDataItemsSkusSaleProps] = None,
    ):
        self.status = status
        self.create_time = create_time
        self.sku_id = sku_id
        self.item_id = item_id
        self.sale_price = sale_price
        self.origin_price = origin_price
        self.modify_time = modify_time
        self.sale_props = sale_props

    def validate(self):
        if self.sale_props:
            for k in self.sale_props:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sale_price is not None:
            result['SalePrice'] = self.sale_price
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        result['SaleProps'] = []
        if self.sale_props is not None:
            for k in self.sale_props:
                result['SaleProps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SalePrice') is not None:
            self.sale_price = m.get('SalePrice')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        self.sale_props = []
        if m.get('SaleProps') is not None:
            for k in m.get('SaleProps'):
                temp_model = QueryItemsResponseBodyDataItemsSkusSaleProps()
                self.sale_props.append(temp_model.from_map(k))
        return self


class QueryItemsResponseBodyDataItemsGames(TeaModel):
    def __init__(
        self,
        name: str = None,
        game_id: str = None,
    ):
        self.name = name
        self.game_id = game_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.game_id is not None:
            result['GameId'] = self.game_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        return self


class QueryItemsResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        status: int = None,
        supplier: str = None,
        description: str = None,
        create_time: int = None,
        seller_id: str = None,
        category_id: int = None,
        item_id: str = None,
        title: str = None,
        sale_price: int = None,
        origin_price: int = None,
        modify_time: int = None,
        skus: List[QueryItemsResponseBodyDataItemsSkus] = None,
        games: List[QueryItemsResponseBodyDataItemsGames] = None,
    ):
        self.status = status
        self.supplier = supplier
        self.description = description
        self.create_time = create_time
        self.seller_id = seller_id
        self.category_id = category_id
        self.item_id = item_id
        self.title = title
        self.sale_price = sale_price
        self.origin_price = origin_price
        self.modify_time = modify_time
        self.skus = skus
        self.games = games

    def validate(self):
        if self.skus:
            for k in self.skus:
                if k:
                    k.validate()
        if self.games:
            for k in self.games:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier is not None:
            result['Supplier'] = self.supplier
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.title is not None:
            result['Title'] = self.title
        if self.sale_price is not None:
            result['SalePrice'] = self.sale_price
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        result['Skus'] = []
        if self.skus is not None:
            for k in self.skus:
                result['Skus'].append(k.to_map() if k else None)
        result['Games'] = []
        if self.games is not None:
            for k in self.games:
                result['Games'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Supplier') is not None:
            self.supplier = m.get('Supplier')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('SalePrice') is not None:
            self.sale_price = m.get('SalePrice')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        self.skus = []
        if m.get('Skus') is not None:
            for k in m.get('Skus'):
                temp_model = QueryItemsResponseBodyDataItemsSkus()
                self.skus.append(temp_model.from_map(k))
        self.games = []
        if m.get('Games') is not None:
            for k in m.get('Games'):
                temp_model = QueryItemsResponseBodyDataItemsGames()
                self.games.append(temp_model.from_map(k))
        return self


class QueryItemsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        items: List[QueryItemsResponseBodyDataItems] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = QueryItemsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class QueryItemsResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        data: QueryItemsResponseBodyData = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = QueryItemsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryItemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = QueryItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderRequest(TeaModel):
    def __init__(
        self,
        buyer_account_id: str = None,
        order_id: str = None,
        account_domain: str = None,
    ):
        self.buyer_account_id = buyer_account_id
        self.order_id = order_id
        self.account_domain = account_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class QueryOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        finish_time: int = None,
        create_time: int = None,
        auto_unlock_time: int = None,
        apply_delivery_time: int = None,
        item_id: str = None,
        origin_price: int = None,
        buyer_account_id: str = None,
        amount: int = None,
        sku_id: str = None,
        settlement_price: int = None,
        order_id: str = None,
        account_domain: str = None,
    ):
        self.status = status
        self.finish_time = finish_time
        self.create_time = create_time
        self.auto_unlock_time = auto_unlock_time
        self.apply_delivery_time = apply_delivery_time
        self.item_id = item_id
        self.origin_price = origin_price
        self.buyer_account_id = buyer_account_id
        self.amount = amount
        self.sku_id = sku_id
        self.settlement_price = settlement_price
        self.order_id = order_id
        self.account_domain = account_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.auto_unlock_time is not None:
            result['AutoUnlockTime'] = self.auto_unlock_time
        if self.apply_delivery_time is not None:
            result['ApplyDeliveryTime'] = self.apply_delivery_time
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.buyer_account_id is not None:
            result['BuyerAccountId'] = self.buyer_account_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.settlement_price is not None:
            result['SettlementPrice'] = self.settlement_price
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AutoUnlockTime') is not None:
            self.auto_unlock_time = m.get('AutoUnlockTime')
        if m.get('ApplyDeliveryTime') is not None:
            self.apply_delivery_time = m.get('ApplyDeliveryTime')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('BuyerAccountId') is not None:
            self.buyer_account_id = m.get('BuyerAccountId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SettlementPrice') is not None:
            self.settlement_price = m.get('SettlementPrice')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class QueryOrderResponseBody(TeaModel):
    def __init__(
        self,
        delivery_status: str = None,
        request_id: str = None,
        refund_status: str = None,
        data: QueryOrderResponseBodyData = None,
    ):
        self.delivery_status = delivery_status
        self.request_id = request_id
        self.refund_status = refund_status
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_status is not None:
            result['DeliveryStatus'] = self.delivery_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.refund_status is not None:
            result['RefundStatus'] = self.refund_status
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryStatus') is not None:
            self.delivery_status = m.get('DeliveryStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RefundStatus') is not None:
            self.refund_status = m.get('RefundStatus')
        if m.get('Data') is not None:
            temp_model = QueryOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = QueryOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOutAccountBindStatusRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        game_id: str = None,
        account_domain: str = None,
    ):
        self.account_id = account_id
        self.game_id = game_id
        self.account_domain = account_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.account_domain is not None:
            result['AccountDomain'] = self.account_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('AccountDomain') is not None:
            self.account_domain = m.get('AccountDomain')
        return self


class QueryOutAccountBindStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        bind_status: int = None,
    ):
        self.bind_status = bind_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_status is not None:
            result['BindStatus'] = self.bind_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindStatus') is not None:
            self.bind_status = m.get('BindStatus')
        return self


class QueryOutAccountBindStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryOutAccountBindStatusResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryOutAccountBindStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryOutAccountBindStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOutAccountBindStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = QueryOutAccountBindStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProjectRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        project_id: int = None,
        tenant_id: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.project_id = project_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: int = None,
        tenant_id: int = None,
    ):
        self.name = name
        self.id = id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        data: List[QueryProjectResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.data = data

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryProjectResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = QueryProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTenantRequest(TeaModel):
    def __init__(
        self,
        param: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.param = param
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param is not None:
            result['Param'] = self.param
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTenantResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        name: str = None,
        tenant_id: int = None,
    ):
        self.gmt_create = gmt_create
        self.name = name
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryTenantResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        data: List[QueryTenantResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.data = data

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTenantResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryTenantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTenantResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = QueryTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SkipTrialPolicyRequest(TeaModel):
    def __init__(
        self,
        game_session_id: str = None,
    ):
        self.game_session_id = game_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_session_id is not None:
            result['GameSessionId'] = self.game_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameSessionId') is not None:
            self.game_session_id = m.get('GameSessionId')
        return self


class SkipTrialPolicyResponseBodyData(TeaModel):
    def __init__(
        self,
        skip_result: int = None,
    ):
        self.skip_result = skip_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skip_result is not None:
            result['SkipResult'] = self.skip_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkipResult') is not None:
            self.skip_result = m.get('SkipResult')
        return self


class SkipTrialPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SkipTrialPolicyResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SkipTrialPolicyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SkipTrialPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SkipTrialPolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = SkipTrialPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopGameSessionRequest(TeaModel):
    def __init__(
        self,
        game_id: str = None,
        access_key: str = None,
        user_id: str = None,
        biz_param: str = None,
        game_session: str = None,
        reason: str = None,
    ):
        self.game_id = game_id
        self.access_key = access_key
        self.user_id = user_id
        self.biz_param = biz_param
        self.game_session = game_session
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_param is not None:
            result['BizParam'] = self.biz_param
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizParam') is not None:
            self.biz_param = m.get('BizParam')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class StopGameSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        game_session: str = None,
        queue_state: int = None,
        message: str = None,
        game_id: str = None,
        queue_code: int = None,
    ):
        self.request_id = request_id
        self.success = success
        self.game_session = game_session
        self.queue_state = queue_state
        self.message = message
        self.game_id = game_id
        self.queue_code = queue_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.game_session is not None:
            result['GameSession'] = self.game_session
        if self.queue_state is not None:
            result['QueueState'] = self.queue_state
        if self.message is not None:
            result['Message'] = self.message
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.queue_code is not None:
            result['QueueCode'] = self.queue_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('GameSession') is not None:
            self.game_session = m.get('GameSession')
        if m.get('QueueState') is not None:
            self.queue_state = m.get('QueueState')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('QueueCode') is not None:
            self.queue_code = m.get('QueueCode')
        return self


class StopGameSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopGameSessionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = StopGameSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitInternalPurchaseChargeDataRequest(TeaModel):
    def __init__(
        self,
        user_activation_rate: int = None,
        new_user_retention_rate_one_day: int = None,
        active_user_retention_rate_one_day: int = None,
        new_user_retention_rate_seven_day: int = None,
        active_user_retention_rate_seven_day: int = None,
        payment_conversion_rate: int = None,
        dau: int = None,
        mau: int = None,
        play_time_range_one_day: str = None,
        play_time_range_thirty_day: str = None,
        arpu: int = None,
        game_id: str = None,
        charge_date: str = None,
        new_user_retention_rate_thirty_day: int = None,
        active_user_retention_rate_thirty_day: int = None,
        play_time_average_one_day: int = None,
        play_time_average_thirty_day: int = None,
        play_time_ninety_points_one_day: int = None,
        play_time_ninety_points_thirty_day: int = None,
    ):
        self.user_activation_rate = user_activation_rate
        self.new_user_retention_rate_one_day = new_user_retention_rate_one_day
        self.active_user_retention_rate_one_day = active_user_retention_rate_one_day
        self.new_user_retention_rate_seven_day = new_user_retention_rate_seven_day
        self.active_user_retention_rate_seven_day = active_user_retention_rate_seven_day
        self.payment_conversion_rate = payment_conversion_rate
        self.dau = dau
        self.mau = mau
        self.play_time_range_one_day = play_time_range_one_day
        self.play_time_range_thirty_day = play_time_range_thirty_day
        self.arpu = arpu
        self.game_id = game_id
        self.charge_date = charge_date
        self.new_user_retention_rate_thirty_day = new_user_retention_rate_thirty_day
        self.active_user_retention_rate_thirty_day = active_user_retention_rate_thirty_day
        self.play_time_average_one_day = play_time_average_one_day
        self.play_time_average_thirty_day = play_time_average_thirty_day
        self.play_time_ninety_points_one_day = play_time_ninety_points_one_day
        self.play_time_ninety_points_thirty_day = play_time_ninety_points_thirty_day

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_activation_rate is not None:
            result['UserActivationRate'] = self.user_activation_rate
        if self.new_user_retention_rate_one_day is not None:
            result['NewUserRetentionRateOneDay'] = self.new_user_retention_rate_one_day
        if self.active_user_retention_rate_one_day is not None:
            result['ActiveUserRetentionRateOneDay'] = self.active_user_retention_rate_one_day
        if self.new_user_retention_rate_seven_day is not None:
            result['NewUserRetentionRateSevenDay'] = self.new_user_retention_rate_seven_day
        if self.active_user_retention_rate_seven_day is not None:
            result['ActiveUserRetentionRateSevenDay'] = self.active_user_retention_rate_seven_day
        if self.payment_conversion_rate is not None:
            result['PaymentConversionRate'] = self.payment_conversion_rate
        if self.dau is not None:
            result['Dau'] = self.dau
        if self.mau is not None:
            result['Mau'] = self.mau
        if self.play_time_range_one_day is not None:
            result['PlayTimeRangeOneDay'] = self.play_time_range_one_day
        if self.play_time_range_thirty_day is not None:
            result['PlayTimeRangeThirtyDay'] = self.play_time_range_thirty_day
        if self.arpu is not None:
            result['Arpu'] = self.arpu
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.charge_date is not None:
            result['ChargeDate'] = self.charge_date
        if self.new_user_retention_rate_thirty_day is not None:
            result['NewUserRetentionRateThirtyDay'] = self.new_user_retention_rate_thirty_day
        if self.active_user_retention_rate_thirty_day is not None:
            result['ActiveUserRetentionRateThirtyDay'] = self.active_user_retention_rate_thirty_day
        if self.play_time_average_one_day is not None:
            result['PlayTimeAverageOneDay'] = self.play_time_average_one_day
        if self.play_time_average_thirty_day is not None:
            result['PlayTimeAverageThirtyDay'] = self.play_time_average_thirty_day
        if self.play_time_ninety_points_one_day is not None:
            result['PlayTimeNinetyPointsOneDay'] = self.play_time_ninety_points_one_day
        if self.play_time_ninety_points_thirty_day is not None:
            result['PlayTimeNinetyPointsThirtyDay'] = self.play_time_ninety_points_thirty_day
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserActivationRate') is not None:
            self.user_activation_rate = m.get('UserActivationRate')
        if m.get('NewUserRetentionRateOneDay') is not None:
            self.new_user_retention_rate_one_day = m.get('NewUserRetentionRateOneDay')
        if m.get('ActiveUserRetentionRateOneDay') is not None:
            self.active_user_retention_rate_one_day = m.get('ActiveUserRetentionRateOneDay')
        if m.get('NewUserRetentionRateSevenDay') is not None:
            self.new_user_retention_rate_seven_day = m.get('NewUserRetentionRateSevenDay')
        if m.get('ActiveUserRetentionRateSevenDay') is not None:
            self.active_user_retention_rate_seven_day = m.get('ActiveUserRetentionRateSevenDay')
        if m.get('PaymentConversionRate') is not None:
            self.payment_conversion_rate = m.get('PaymentConversionRate')
        if m.get('Dau') is not None:
            self.dau = m.get('Dau')
        if m.get('Mau') is not None:
            self.mau = m.get('Mau')
        if m.get('PlayTimeRangeOneDay') is not None:
            self.play_time_range_one_day = m.get('PlayTimeRangeOneDay')
        if m.get('PlayTimeRangeThirtyDay') is not None:
            self.play_time_range_thirty_day = m.get('PlayTimeRangeThirtyDay')
        if m.get('Arpu') is not None:
            self.arpu = m.get('Arpu')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('ChargeDate') is not None:
            self.charge_date = m.get('ChargeDate')
        if m.get('NewUserRetentionRateThirtyDay') is not None:
            self.new_user_retention_rate_thirty_day = m.get('NewUserRetentionRateThirtyDay')
        if m.get('ActiveUserRetentionRateThirtyDay') is not None:
            self.active_user_retention_rate_thirty_day = m.get('ActiveUserRetentionRateThirtyDay')
        if m.get('PlayTimeAverageOneDay') is not None:
            self.play_time_average_one_day = m.get('PlayTimeAverageOneDay')
        if m.get('PlayTimeAverageThirtyDay') is not None:
            self.play_time_average_thirty_day = m.get('PlayTimeAverageThirtyDay')
        if m.get('PlayTimeNinetyPointsOneDay') is not None:
            self.play_time_ninety_points_one_day = m.get('PlayTimeNinetyPointsOneDay')
        if m.get('PlayTimeNinetyPointsThirtyDay') is not None:
            self.play_time_ninety_points_thirty_day = m.get('PlayTimeNinetyPointsThirtyDay')
        return self


class SubmitInternalPurchaseChargeDataResponseBodyData(TeaModel):
    def __init__(
        self,
        status: int = None,
        message: str = None,
    ):
        self.status = status
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SubmitInternalPurchaseChargeDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SubmitInternalPurchaseChargeDataResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SubmitInternalPurchaseChargeDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SubmitInternalPurchaseChargeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitInternalPurchaseChargeDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = SubmitInternalPurchaseChargeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitInternalPurchaseOrdersRequestOrderList(TeaModel):
    def __init__(
        self,
        finish_time: int = None,
        final_price: int = None,
        user_id: str = None,
        game_id: str = None,
        batch_number: str = None,
        role_id: str = None,
        order_id: str = None,
    ):
        self.finish_time = finish_time
        self.final_price = final_price
        self.user_id = user_id
        self.game_id = game_id
        self.batch_number = batch_number
        self.role_id = role_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.final_price is not None:
            result['FinalPrice'] = self.final_price
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.batch_number is not None:
            result['BatchNumber'] = self.batch_number
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('FinalPrice') is not None:
            self.final_price = m.get('FinalPrice')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('BatchNumber') is not None:
            self.batch_number = m.get('BatchNumber')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class SubmitInternalPurchaseOrdersRequest(TeaModel):
    def __init__(
        self,
        order_list: List[SubmitInternalPurchaseOrdersRequestOrderList] = None,
    ):
        self.order_list = order_list

    def validate(self):
        if self.order_list:
            for k in self.order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrderList'] = []
        if self.order_list is not None:
            for k in self.order_list:
                result['OrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_list = []
        if m.get('OrderList') is not None:
            for k in m.get('OrderList'):
                temp_model = SubmitInternalPurchaseOrdersRequestOrderList()
                self.order_list.append(temp_model.from_map(k))
        return self


class SubmitInternalPurchaseOrdersResponseBodyData(TeaModel):
    def __init__(
        self,
        status: int = None,
        message: str = None,
    ):
        self.status = status
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SubmitInternalPurchaseOrdersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SubmitInternalPurchaseOrdersResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SubmitInternalPurchaseOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SubmitInternalPurchaseOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitInternalPurchaseOrdersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = SubmitInternalPurchaseOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitInternalPurchaseReadyFlagRequestBatchInfoList(TeaModel):
    def __init__(
        self,
        batch_size: int = None,
        batch_numbers: str = None,
    ):
        self.batch_size = batch_size
        self.batch_numbers = batch_numbers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.batch_numbers is not None:
            result['BatchNumbers'] = self.batch_numbers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('BatchNumbers') is not None:
            self.batch_numbers = m.get('BatchNumbers')
        return self


class SubmitInternalPurchaseReadyFlagRequest(TeaModel):
    def __init__(
        self,
        status: int = None,
        game_id: str = None,
        charge_date: str = None,
        order_total_count: int = None,
        batch_info_list: List[SubmitInternalPurchaseReadyFlagRequestBatchInfoList] = None,
    ):
        self.status = status
        self.game_id = game_id
        self.charge_date = charge_date
        self.order_total_count = order_total_count
        self.batch_info_list = batch_info_list

    def validate(self):
        if self.batch_info_list:
            for k in self.batch_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.game_id is not None:
            result['GameId'] = self.game_id
        if self.charge_date is not None:
            result['ChargeDate'] = self.charge_date
        if self.order_total_count is not None:
            result['OrderTotalCount'] = self.order_total_count
        result['BatchInfoList'] = []
        if self.batch_info_list is not None:
            for k in self.batch_info_list:
                result['BatchInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GameId') is not None:
            self.game_id = m.get('GameId')
        if m.get('ChargeDate') is not None:
            self.charge_date = m.get('ChargeDate')
        if m.get('OrderTotalCount') is not None:
            self.order_total_count = m.get('OrderTotalCount')
        self.batch_info_list = []
        if m.get('BatchInfoList') is not None:
            for k in m.get('BatchInfoList'):
                temp_model = SubmitInternalPurchaseReadyFlagRequestBatchInfoList()
                self.batch_info_list.append(temp_model.from_map(k))
        return self


class SubmitInternalPurchaseReadyFlagResponseBodyData(TeaModel):
    def __init__(
        self,
        status: int = None,
        missing_batch_numbers: str = None,
        message: str = None,
    ):
        self.status = status
        self.missing_batch_numbers = missing_batch_numbers
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.missing_batch_numbers is not None:
            result['MissingBatchNumbers'] = self.missing_batch_numbers
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MissingBatchNumbers') is not None:
            self.missing_batch_numbers = m.get('MissingBatchNumbers')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SubmitInternalPurchaseReadyFlagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SubmitInternalPurchaseReadyFlagResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SubmitInternalPurchaseReadyFlagResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SubmitInternalPurchaseReadyFlagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitInternalPurchaseReadyFlagResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = SubmitInternalPurchaseReadyFlagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


