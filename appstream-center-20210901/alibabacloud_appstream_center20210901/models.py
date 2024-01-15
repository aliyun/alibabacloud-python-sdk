# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AccessPageGetAclRequest(TeaModel):
    def __init__(
        self,
        access_page_id: str = None,
    ):
        self.access_page_id = access_page_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        return self


class AccessPageGetAclResponseBodyData(TeaModel):
    def __init__(
        self,
        access_mode: str = None,
        access_url: str = None,
        effect_time: int = None,
        unit: str = None,
        url_expire_time: str = None,
    ):
        self.access_mode = access_mode
        self.access_url = access_url
        self.effect_time = effect_time
        self.unit = unit
        self.url_expire_time = url_expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        if self.access_url is not None:
            result['AccessUrl'] = self.access_url
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.url_expire_time is not None:
            result['UrlExpireTime'] = self.url_expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        if m.get('AccessUrl') is not None:
            self.access_url = m.get('AccessUrl')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('UrlExpireTime') is not None:
            self.url_expire_time = m.get('UrlExpireTime')
        return self


class AccessPageGetAclResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[AccessPageGetAclResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AccessPageGetAclResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AccessPageGetAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AccessPageGetAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AccessPageGetAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AccessPageSetAclRequest(TeaModel):
    def __init__(
        self,
        access_mode: str = None,
        access_page_id: str = None,
        access_page_name: str = None,
        effect_time: int = None,
        unit: str = None,
    ):
        self.access_mode = access_mode
        self.access_page_id = access_page_id
        self.access_page_name = access_page_name
        self.effect_time = effect_time
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        if self.access_page_name is not None:
            result['AccessPageName'] = self.access_page_name
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        if m.get('AccessPageName') is not None:
            self.access_page_name = m.get('AccessPageName')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class AccessPageSetAclResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AccessPageSetAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AccessPageSetAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AccessPageSetAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveOtaTaskRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        ota_type: str = None,
        start_time: str = None,
        task_id: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.biz_region_id = biz_region_id
        self.ota_type = ota_type
        self.start_time = start_time
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.ota_type is not None:
            result['OtaType'] = self.ota_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('OtaType') is not None:
            self.ota_type = m.get('OtaType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ApproveOtaTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApproveOtaTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApproveOtaTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ApproveOtaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AskSessionPackagePriceRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        max_sessions: int = None,
        period: int = None,
        period_unit: str = None,
        region: str = None,
        session_package_type: str = None,
        session_spec: str = None,
        session_type: str = None,
    ):
        self.charge_type = charge_type
        self.max_sessions = max_sessions
        self.period = period
        self.period_unit = period_unit
        self.region = region
        self.session_package_type = session_package_type
        self.session_spec = session_spec
        self.session_type = session_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.max_sessions is not None:
            result['MaxSessions'] = self.max_sessions
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region is not None:
            result['Region'] = self.region
        if self.session_package_type is not None:
            result['SessionPackageType'] = self.session_package_type
        if self.session_spec is not None:
            result['SessionSpec'] = self.session_spec
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('MaxSessions') is not None:
            self.max_sessions = m.get('MaxSessions')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SessionPackageType') is not None:
            self.session_package_type = m.get('SessionPackageType')
        if m.get('SessionSpec') is not None:
            self.session_spec = m.get('SessionSpec')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        return self


class AskSessionPackagePriceResponseBodyDataPrice(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class AskSessionPackagePriceResponseBodyData(TeaModel):
    def __init__(
        self,
        price: AskSessionPackagePriceResponseBodyDataPrice = None,
    ):
        self.price = price

    def validate(self):
        if self.price:
            self.price.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = AskSessionPackagePriceResponseBodyDataPrice()
            self.price = temp_model.from_map(m['Price'])
        return self


class AskSessionPackagePriceResponseBody(TeaModel):
    def __init__(
        self,
        data: List[AskSessionPackagePriceResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AskSessionPackagePriceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AskSessionPackagePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AskSessionPackagePriceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AskSessionPackagePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AskSessionPackageRenewPriceRequest(TeaModel):
    def __init__(
        self,
        period: int = None,
        period_unit: str = None,
        session_package_id: str = None,
    ):
        self.period = period
        self.period_unit = period_unit
        self.session_package_id = session_package_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        return self


class AskSessionPackageRenewPriceResponseBodyDataPrice(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class AskSessionPackageRenewPriceResponseBodyData(TeaModel):
    def __init__(
        self,
        price: AskSessionPackageRenewPriceResponseBodyDataPrice = None,
    ):
        self.price = price

    def validate(self):
        if self.price:
            self.price.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = AskSessionPackageRenewPriceResponseBodyDataPrice()
            self.price = temp_model.from_map(m['Price'])
        return self


class AskSessionPackageRenewPriceResponseBody(TeaModel):
    def __init__(
        self,
        data: List[AskSessionPackageRenewPriceResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AskSessionPackageRenewPriceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AskSessionPackageRenewPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AskSessionPackageRenewPriceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AskSessionPackageRenewPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        authorize_user_ids: List[str] = None,
        product_type: str = None,
        un_authorize_user_ids: List[str] = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.authorize_user_ids = authorize_user_ids
        self.product_type = product_type
        self.un_authorize_user_ids = un_authorize_user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.authorize_user_ids is not None:
            result['AuthorizeUserIds'] = self.authorize_user_ids
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.un_authorize_user_ids is not None:
            result['UnAuthorizeUserIds'] = self.un_authorize_user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AuthorizeUserIds') is not None:
            self.authorize_user_ids = m.get('AuthorizeUserIds')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('UnAuthorizeUserIds') is not None:
            self.un_authorize_user_ids = m.get('UnAuthorizeUserIds')
        return self


class AuthorizeInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AuthorizeInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthorizeInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AuthorizeInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BuySessionPackageRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        max_sessions: int = None,
        period: int = None,
        period_unit: str = None,
        project_id: str = None,
        region: str = None,
        session_package_name: str = None,
        session_package_type: str = None,
        session_spec: str = None,
        session_type: str = None,
    ):
        self.charge_type = charge_type
        self.max_sessions = max_sessions
        self.period = period
        self.period_unit = period_unit
        self.project_id = project_id
        self.region = region
        self.session_package_name = session_package_name
        self.session_package_type = session_package_type
        self.session_spec = session_spec
        self.session_type = session_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.max_sessions is not None:
            result['MaxSessions'] = self.max_sessions
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region is not None:
            result['Region'] = self.region
        if self.session_package_name is not None:
            result['SessionPackageName'] = self.session_package_name
        if self.session_package_type is not None:
            result['SessionPackageType'] = self.session_package_type
        if self.session_spec is not None:
            result['SessionSpec'] = self.session_spec
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('MaxSessions') is not None:
            self.max_sessions = m.get('MaxSessions')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SessionPackageName') is not None:
            self.session_package_name = m.get('SessionPackageName')
        if m.get('SessionPackageType') is not None:
            self.session_package_type = m.get('SessionPackageType')
        if m.get('SessionSpec') is not None:
            self.session_spec = m.get('SessionSpec')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        return self


class BuySessionPackageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        session_package_id: int = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.session_package_id = session_package_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BuySessionPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BuySessionPackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = BuySessionPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelOtaTaskRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        task_id: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelOtaTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelOtaTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelOtaTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CancelOtaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessPageRequest(TeaModel):
    def __init__(
        self,
        access_page_name: str = None,
        cloud_env_id: str = None,
        effect_time: int = None,
        project_id: str = None,
        project_name: str = None,
        unit: str = None,
    ):
        self.access_page_name = access_page_name
        self.cloud_env_id = cloud_env_id
        self.effect_time = effect_time
        self.project_id = project_id
        self.project_name = project_name
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_name is not None:
            result['AccessPageName'] = self.access_page_name
        if self.cloud_env_id is not None:
            result['CloudEnvId'] = self.cloud_env_id
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPageName') is not None:
            self.access_page_name = m.get('AccessPageName')
        if m.get('CloudEnvId') is not None:
            self.cloud_env_id = m.get('CloudEnvId')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class CreateAccessPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAccessPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccessPageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateAccessPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppInstanceGroupRequestNetworkDomainRules(TeaModel):
    def __init__(
        self,
        domain: str = None,
        policy: str = None,
    ):
        self.domain = domain
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.policy is not None:
            result['Policy'] = self.policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        return self


class CreateAppInstanceGroupRequestNetworkRoutes(TeaModel):
    def __init__(
        self,
        destination: str = None,
        mode: str = None,
    ):
        self.destination = destination
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class CreateAppInstanceGroupRequestNetwork(TeaModel):
    def __init__(
        self,
        domain_rules: List[CreateAppInstanceGroupRequestNetworkDomainRules] = None,
        ip_expire_minutes: int = None,
        routes: List[CreateAppInstanceGroupRequestNetworkRoutes] = None,
        strategy_type: str = None,
    ):
        self.domain_rules = domain_rules
        self.ip_expire_minutes = ip_expire_minutes
        self.routes = routes
        self.strategy_type = strategy_type

    def validate(self):
        if self.domain_rules:
            for k in self.domain_rules:
                if k:
                    k.validate()
        if self.routes:
            for k in self.routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainRules'] = []
        if self.domain_rules is not None:
            for k in self.domain_rules:
                result['DomainRules'].append(k.to_map() if k else None)
        if self.ip_expire_minutes is not None:
            result['IpExpireMinutes'] = self.ip_expire_minutes
        result['Routes'] = []
        if self.routes is not None:
            for k in self.routes:
                result['Routes'].append(k.to_map() if k else None)
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_rules = []
        if m.get('DomainRules') is not None:
            for k in m.get('DomainRules'):
                temp_model = CreateAppInstanceGroupRequestNetworkDomainRules()
                self.domain_rules.append(temp_model.from_map(k))
        if m.get('IpExpireMinutes') is not None:
            self.ip_expire_minutes = m.get('IpExpireMinutes')
        self.routes = []
        if m.get('Routes') is not None:
            for k in m.get('Routes'):
                temp_model = CreateAppInstanceGroupRequestNetworkRoutes()
                self.routes.append(temp_model.from_map(k))
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        return self


class CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(
        self,
        amount: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.amount = amount
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules(TeaModel):
    def __init__(
        self,
        recurrence_type: str = None,
        recurrence_values: List[int] = None,
        timer_periods: List[CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods] = None,
    ):
        self.recurrence_type = recurrence_type
        self.recurrence_values = recurrence_values
        self.timer_periods = timer_periods

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class CreateAppInstanceGroupRequestNodePool(TeaModel):
    def __init__(
        self,
        max_scaling_amount: int = None,
        node_amount: int = None,
        node_capacity: int = None,
        node_instance_type: str = None,
        recurrence_schedules: List[CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules] = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        strategy_disable_date: str = None,
        strategy_enable_date: str = None,
        strategy_type: str = None,
        warm_up: bool = None,
    ):
        self.max_scaling_amount = max_scaling_amount
        self.node_amount = node_amount
        self.node_capacity = node_capacity
        self.node_instance_type = node_instance_type
        self.recurrence_schedules = recurrence_schedules
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        self.scaling_step = scaling_step
        self.scaling_usage_threshold = scaling_usage_threshold
        self.strategy_disable_date = strategy_disable_date
        self.strategy_enable_date = strategy_enable_date
        self.strategy_type = strategy_type
        self.warm_up = warm_up

    def validate(self):
        if self.recurrence_schedules:
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.strategy_disable_date is not None:
            result['StrategyDisableDate'] = self.strategy_disable_date
        if self.strategy_enable_date is not None:
            result['StrategyEnableDate'] = self.strategy_enable_date
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.warm_up is not None:
            result['WarmUp'] = self.warm_up
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k in m.get('RecurrenceSchedules'):
                temp_model = CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('StrategyDisableDate') is not None:
            self.strategy_disable_date = m.get('StrategyDisableDate')
        if m.get('StrategyEnableDate') is not None:
            self.strategy_enable_date = m.get('StrategyEnableDate')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('WarmUp') is not None:
            self.warm_up = m.get('WarmUp')
        return self


class CreateAppInstanceGroupRequestRuntimePolicy(TeaModel):
    def __init__(
        self,
        debug_mode: str = None,
        session_type: str = None,
    ):
        self.debug_mode = debug_mode
        # 会话类型。
        self.session_type = session_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_mode is not None:
            result['DebugMode'] = self.debug_mode
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugMode') is not None:
            self.debug_mode = m.get('DebugMode')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        return self


class CreateAppInstanceGroupRequestSecurityPolicy(TeaModel):
    def __init__(
        self,
        reset_after_unbind: bool = None,
        skip_user_auth_check: bool = None,
    ):
        self.reset_after_unbind = reset_after_unbind
        self.skip_user_auth_check = skip_user_auth_check

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reset_after_unbind is not None:
            result['ResetAfterUnbind'] = self.reset_after_unbind
        if self.skip_user_auth_check is not None:
            result['SkipUserAuthCheck'] = self.skip_user_auth_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResetAfterUnbind') is not None:
            self.reset_after_unbind = m.get('ResetAfterUnbind')
        if m.get('SkipUserAuthCheck') is not None:
            self.skip_user_auth_check = m.get('SkipUserAuthCheck')
        return self


class CreateAppInstanceGroupRequestStoragePolicy(TeaModel):
    def __init__(
        self,
        storage_type_list: List[str] = None,
    ):
        self.storage_type_list = storage_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_type_list is not None:
            result['StorageTypeList'] = self.storage_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageTypeList') is not None:
            self.storage_type_list = m.get('StorageTypeList')
        return self


class CreateAppInstanceGroupRequestUserInfo(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_name: str = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        network: CreateAppInstanceGroupRequestNetwork = None,
        node_pool: CreateAppInstanceGroupRequestNodePool = None,
        period: int = None,
        period_unit: str = None,
        pre_open_app_id: str = None,
        product_type: str = None,
        promotion_id: str = None,
        runtime_policy: CreateAppInstanceGroupRequestRuntimePolicy = None,
        security_policy: CreateAppInstanceGroupRequestSecurityPolicy = None,
        session_timeout: int = None,
        storage_policy: CreateAppInstanceGroupRequestStoragePolicy = None,
        user_info: CreateAppInstanceGroupRequestUserInfo = None,
        users: List[str] = None,
    ):
        self.app_center_image_id = app_center_image_id
        self.app_instance_group_name = app_instance_group_name
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.biz_region_id = biz_region_id
        self.charge_resource_mode = charge_resource_mode
        self.charge_type = charge_type
        self.network = network
        self.node_pool = node_pool
        self.period = period
        self.period_unit = period_unit
        self.pre_open_app_id = pre_open_app_id
        self.product_type = product_type
        self.promotion_id = promotion_id
        self.runtime_policy = runtime_policy
        self.security_policy = security_policy
        self.session_timeout = session_timeout
        self.storage_policy = storage_policy
        self.user_info = user_info
        self.users = users

    def validate(self):
        if self.network:
            self.network.validate()
        if self.node_pool:
            self.node_pool.validate()
        if self.runtime_policy:
            self.runtime_policy.validate()
        if self.security_policy:
            self.security_policy.validate()
        if self.storage_policy:
            self.storage_policy.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.node_pool is not None:
            result['NodePool'] = self.node_pool.to_map()
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.runtime_policy is not None:
            result['RuntimePolicy'] = self.runtime_policy.to_map()
        if self.security_policy is not None:
            result['SecurityPolicy'] = self.security_policy.to_map()
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.storage_policy is not None:
            result['StoragePolicy'] = self.storage_policy.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Network') is not None:
            temp_model = CreateAppInstanceGroupRequestNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('NodePool') is not None:
            temp_model = CreateAppInstanceGroupRequestNodePool()
            self.node_pool = temp_model.from_map(m['NodePool'])
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RuntimePolicy') is not None:
            temp_model = CreateAppInstanceGroupRequestRuntimePolicy()
            self.runtime_policy = temp_model.from_map(m['RuntimePolicy'])
        if m.get('SecurityPolicy') is not None:
            temp_model = CreateAppInstanceGroupRequestSecurityPolicy()
            self.security_policy = temp_model.from_map(m['SecurityPolicy'])
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('StoragePolicy') is not None:
            temp_model = CreateAppInstanceGroupRequestStoragePolicy()
            self.storage_policy = temp_model.from_map(m['StoragePolicy'])
        if m.get('UserInfo') is not None:
            temp_model = CreateAppInstanceGroupRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateAppInstanceGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_name: str = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        network_shrink: str = None,
        node_pool_shrink: str = None,
        period: int = None,
        period_unit: str = None,
        pre_open_app_id: str = None,
        product_type: str = None,
        promotion_id: str = None,
        runtime_policy_shrink: str = None,
        security_policy_shrink: str = None,
        session_timeout: int = None,
        storage_policy_shrink: str = None,
        user_info_shrink: str = None,
        users: List[str] = None,
    ):
        self.app_center_image_id = app_center_image_id
        self.app_instance_group_name = app_instance_group_name
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.biz_region_id = biz_region_id
        self.charge_resource_mode = charge_resource_mode
        self.charge_type = charge_type
        self.network_shrink = network_shrink
        self.node_pool_shrink = node_pool_shrink
        self.period = period
        self.period_unit = period_unit
        self.pre_open_app_id = pre_open_app_id
        self.product_type = product_type
        self.promotion_id = promotion_id
        self.runtime_policy_shrink = runtime_policy_shrink
        self.security_policy_shrink = security_policy_shrink
        self.session_timeout = session_timeout
        self.storage_policy_shrink = storage_policy_shrink
        self.user_info_shrink = user_info_shrink
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.network_shrink is not None:
            result['Network'] = self.network_shrink
        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.runtime_policy_shrink is not None:
            result['RuntimePolicy'] = self.runtime_policy_shrink
        if self.security_policy_shrink is not None:
            result['SecurityPolicy'] = self.security_policy_shrink
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.storage_policy_shrink is not None:
            result['StoragePolicy'] = self.storage_policy_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Network') is not None:
            self.network_shrink = m.get('Network')
        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RuntimePolicy') is not None:
            self.runtime_policy_shrink = m.get('RuntimePolicy')
        if m.get('SecurityPolicy') is not None:
            self.security_policy_shrink = m.get('SecurityPolicy')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('StoragePolicy') is not None:
            self.storage_policy_shrink = m.get('StoragePolicy')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateAppInstanceGroupResponseBodyAppInstanceGroupModel(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        node_pool_id: str = None,
        order_id: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.node_pool_id = node_pool_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        app_instance_group_model: CreateAppInstanceGroupResponseBodyAppInstanceGroupModel = None,
        request_id: str = None,
    ):
        self.app_instance_group_model = app_instance_group_model
        self.request_id = request_id

    def validate(self):
        if self.app_instance_group_model:
            self.app_instance_group_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_model is not None:
            result['AppInstanceGroupModel'] = self.app_instance_group_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupModel') is not None:
            temp_model = CreateAppInstanceGroupResponseBodyAppInstanceGroupModel()
            self.app_instance_group_model = temp_model.from_map(m['AppInstanceGroupModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageFromAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_center_image_name: str = None,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        self.app_center_image_name = app_center_image_name
        self.app_instance_group_id = app_instance_group_id
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_name is not None:
            result['AppCenterImageName'] = self.app_center_image_name
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageName') is not None:
            self.app_center_image_name = m.get('AppCenterImageName')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class CreateImageFromAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        self.image_id = image_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageFromAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageFromAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateImageFromAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        clipboard: int = None,
        cloud_env_id: str = None,
        content_id: str = None,
        description: str = None,
        file_transfer: int = None,
        frame_rate: int = None,
        keep_alive_duration: int = None,
        project_name: str = None,
        session_resolution_height: int = None,
        session_resolution_width: int = None,
        session_spec: str = None,
        streaming_mode: str = None,
        terminal_resolution_adaptation: bool = None,
    ):
        self.clipboard = clipboard
        self.cloud_env_id = cloud_env_id
        self.content_id = content_id
        self.description = description
        self.file_transfer = file_transfer
        self.frame_rate = frame_rate
        self.keep_alive_duration = keep_alive_duration
        self.project_name = project_name
        self.session_resolution_height = session_resolution_height
        self.session_resolution_width = session_resolution_width
        self.session_spec = session_spec
        self.streaming_mode = streaming_mode
        self.terminal_resolution_adaptation = terminal_resolution_adaptation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.cloud_env_id is not None:
            result['CloudEnvId'] = self.cloud_env_id
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        if self.description is not None:
            result['Description'] = self.description
        if self.file_transfer is not None:
            result['FileTransfer'] = self.file_transfer
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.keep_alive_duration is not None:
            result['KeepAliveDuration'] = self.keep_alive_duration
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.session_resolution_height is not None:
            result['SessionResolutionHeight'] = self.session_resolution_height
        if self.session_resolution_width is not None:
            result['SessionResolutionWidth'] = self.session_resolution_width
        if self.session_spec is not None:
            result['SessionSpec'] = self.session_spec
        if self.streaming_mode is not None:
            result['StreamingMode'] = self.streaming_mode
        if self.terminal_resolution_adaptation is not None:
            result['TerminalResolutionAdaptation'] = self.terminal_resolution_adaptation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('CloudEnvId') is not None:
            self.cloud_env_id = m.get('CloudEnvId')
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileTransfer') is not None:
            self.file_transfer = m.get('FileTransfer')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('KeepAliveDuration') is not None:
            self.keep_alive_duration = m.get('KeepAliveDuration')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SessionResolutionHeight') is not None:
            self.session_resolution_height = m.get('SessionResolutionHeight')
        if m.get('SessionResolutionWidth') is not None:
            self.session_resolution_width = m.get('SessionResolutionWidth')
        if m.get('SessionSpec') is not None:
            self.session_spec = m.get('SessionSpec')
        if m.get('StreamingMode') is not None:
            self.streaming_mode = m.get('StreamingMode')
        if m.get('TerminalResolutionAdaptation') is not None:
            self.terminal_resolution_adaptation = m.get('TerminalResolutionAdaptation')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessPageRequest(TeaModel):
    def __init__(
        self,
        access_page_id: str = None,
    ):
        self.access_page_id = access_page_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        return self


class DeleteAccessPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAccessPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccessPageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteAccessPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DeleteAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppInstancesRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_ids: List[str] = None,
        product_type: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_ids = app_instance_ids
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_ids is not None:
            result['AppInstanceIds'] = self.app_instance_ids
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceIds') is not None:
            self.app_instance_ids = m.get('AppInstanceIds')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DeleteAppInstancesResponseBodyDeleteAppInstanceModels(TeaModel):
    def __init__(
        self,
        app_instance_id: str = None,
        code: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.app_instance_id = app_instance_id
        self.code = code
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAppInstancesResponseBody(TeaModel):
    def __init__(
        self,
        delete_app_instance_models: List[DeleteAppInstancesResponseBodyDeleteAppInstanceModels] = None,
        request_id: str = None,
    ):
        self.delete_app_instance_models = delete_app_instance_models
        self.request_id = request_id

    def validate(self):
        if self.delete_app_instance_models:
            for k in self.delete_app_instance_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeleteAppInstanceModels'] = []
        if self.delete_app_instance_models is not None:
            for k in self.delete_app_instance_models:
                result['DeleteAppInstanceModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delete_app_instance_models = []
        if m.get('DeleteAppInstanceModels') is not None:
            for k in m.get('DeleteAppInstanceModels'):
                temp_model = DeleteAppInstancesResponseBodyDeleteAppInstanceModels()
                self.delete_app_instance_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteAppInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessPageSessionRequest(TeaModel):
    def __init__(
        self,
        access_page_id: str = None,
        access_page_token: str = None,
        external_user_id: str = None,
    ):
        self.access_page_id = access_page_id
        self.access_page_token = access_page_token
        self.external_user_id = external_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        if self.access_page_token is not None:
            result['AccessPageToken'] = self.access_page_token
        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        if m.get('AccessPageToken') is not None:
            self.access_page_token = m.get('AccessPageToken')
        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')
        return self


class GetAccessPageSessionResponseBodyData(TeaModel):
    def __init__(
        self,
        connect_ticket: str = None,
        flow_id: str = None,
    ):
        self.connect_ticket = connect_ticket
        # flow ID
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_ticket is not None:
            result['ConnectTicket'] = self.connect_ticket
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectTicket') is not None:
            self.connect_ticket = m.get('ConnectTicket')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class GetAccessPageSessionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAccessPageSessionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAccessPageSessionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAccessPageSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccessPageSessionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetAccessPageSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsApps(TeaModel):
    def __init__(
        self,
        app_icon: str = None,
        app_id: str = None,
        app_name: str = None,
        app_version: str = None,
        app_version_name: str = None,
    ):
        self.app_icon = app_icon
        self.app_id = app_id
        self.app_name = app_name
        self.app_version = app_version
        self.app_version_name = app_version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_icon is not None:
            result['AppIcon'] = self.app_icon
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIcon') is not None:
            self.app_icon = m.get('AppIcon')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(
        self,
        amount: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.amount = amount
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules(TeaModel):
    def __init__(
        self,
        recurrence_type: str = None,
        recurrence_values: List[int] = None,
        timer_periods: List[GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods] = None,
    ):
        self.recurrence_type = recurrence_type
        self.recurrence_values = recurrence_values
        self.timer_periods = timer_periods

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool(TeaModel):
    def __init__(
        self,
        amount: int = None,
        max_scaling_amount: int = None,
        node_amount: int = None,
        node_capacity: int = None,
        node_instance_type: str = None,
        node_pool_id: str = None,
        node_type_name: str = None,
        node_used: int = None,
        recurrence_schedules: List[GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules] = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_node_amount: int = None,
        scaling_node_used: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        strategy_disable_date: str = None,
        strategy_enable_date: str = None,
        strategy_type: str = None,
        warm_up: bool = None,
    ):
        self.amount = amount
        self.max_scaling_amount = max_scaling_amount
        self.node_amount = node_amount
        self.node_capacity = node_capacity
        self.node_instance_type = node_instance_type
        self.node_pool_id = node_pool_id
        self.node_type_name = node_type_name
        self.node_used = node_used
        self.recurrence_schedules = recurrence_schedules
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        self.scaling_node_amount = scaling_node_amount
        self.scaling_node_used = scaling_node_used
        self.scaling_step = scaling_step
        self.scaling_usage_threshold = scaling_usage_threshold
        self.strategy_disable_date = strategy_disable_date
        self.strategy_enable_date = strategy_enable_date
        self.strategy_type = strategy_type
        self.warm_up = warm_up

    def validate(self):
        if self.recurrence_schedules:
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        if self.node_type_name is not None:
            result['NodeTypeName'] = self.node_type_name
        if self.node_used is not None:
            result['NodeUsed'] = self.node_used
        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_node_amount is not None:
            result['ScalingNodeAmount'] = self.scaling_node_amount
        if self.scaling_node_used is not None:
            result['ScalingNodeUsed'] = self.scaling_node_used
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.strategy_disable_date is not None:
            result['StrategyDisableDate'] = self.strategy_disable_date
        if self.strategy_enable_date is not None:
            result['StrategyEnableDate'] = self.strategy_enable_date
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.warm_up is not None:
            result['WarmUp'] = self.warm_up
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        if m.get('NodeTypeName') is not None:
            self.node_type_name = m.get('NodeTypeName')
        if m.get('NodeUsed') is not None:
            self.node_used = m.get('NodeUsed')
        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k in m.get('RecurrenceSchedules'):
                temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingNodeAmount') is not None:
            self.scaling_node_amount = m.get('ScalingNodeAmount')
        if m.get('ScalingNodeUsed') is not None:
            self.scaling_node_used = m.get('ScalingNodeUsed')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('StrategyDisableDate') is not None:
            self.strategy_disable_date = m.get('StrategyDisableDate')
        if m.get('StrategyEnableDate') is not None:
            self.strategy_enable_date = m.get('StrategyEnableDate')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('WarmUp') is not None:
            self.warm_up = m.get('WarmUp')
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo(TeaModel):
    def __init__(
        self,
        new_ota_version: str = None,
        ota_version: str = None,
        task_id: str = None,
    ):
        self.new_ota_version = new_ota_version
        self.ota_version = ota_version
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_ota_version is not None:
            result['NewOtaVersion'] = self.new_ota_version
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewOtaVersion') is not None:
            self.new_ota_version = m.get('NewOtaVersion')
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModels(TeaModel):
    def __init__(
        self,
        amount: int = None,
        app_center_image_id: str = None,
        app_center_image_name: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        app_instance_type: str = None,
        app_instance_type_name: str = None,
        app_policy_id: str = None,
        apps: List[GetAppInstanceGroupResponseBodyAppInstanceGroupModelsApps] = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        expired_time: str = None,
        gmt_create: str = None,
        max_amount: int = None,
        min_amount: int = None,
        node_pool: List[GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool] = None,
        os_type: str = None,
        ota_info: GetAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo = None,
        product_type: str = None,
        region_id: str = None,
        reserve_amount_ratio: str = None,
        reserve_max_amount: int = None,
        reserve_min_amount: int = None,
        resource_status: str = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        session_timeout: str = None,
        skip_user_auth_check: bool = None,
        spec_id: str = None,
        status: str = None,
    ):
        self.amount = amount
        self.app_center_image_id = app_center_image_id
        self.app_center_image_name = app_center_image_name
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_group_name = app_instance_group_name
        self.app_instance_type = app_instance_type
        self.app_instance_type_name = app_instance_type_name
        self.app_policy_id = app_policy_id
        self.apps = apps
        self.charge_resource_mode = charge_resource_mode
        self.charge_type = charge_type
        self.expired_time = expired_time
        self.gmt_create = gmt_create
        self.max_amount = max_amount
        self.min_amount = min_amount
        self.node_pool = node_pool
        self.os_type = os_type
        self.ota_info = ota_info
        self.product_type = product_type
        self.region_id = region_id
        self.reserve_amount_ratio = reserve_amount_ratio
        self.reserve_max_amount = reserve_max_amount
        self.reserve_min_amount = reserve_min_amount
        self.resource_status = resource_status
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        self.scaling_step = scaling_step
        self.scaling_usage_threshold = scaling_usage_threshold
        self.session_timeout = session_timeout
        self.skip_user_auth_check = skip_user_auth_check
        self.spec_id = spec_id
        self.status = status

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()
        if self.node_pool:
            for k in self.node_pool:
                if k:
                    k.validate()
        if self.ota_info:
            self.ota_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_center_image_name is not None:
            result['AppCenterImageName'] = self.app_center_image_name
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type
        if self.app_instance_type_name is not None:
            result['AppInstanceTypeName'] = self.app_instance_type_name
        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.max_amount is not None:
            result['MaxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['MinAmount'] = self.min_amount
        result['NodePool'] = []
        if self.node_pool is not None:
            for k in self.node_pool:
                result['NodePool'].append(k.to_map() if k else None)
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.ota_info is not None:
            result['OtaInfo'] = self.ota_info.to_map()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reserve_amount_ratio is not None:
            result['ReserveAmountRatio'] = self.reserve_amount_ratio
        if self.reserve_max_amount is not None:
            result['ReserveMaxAmount'] = self.reserve_max_amount
        if self.reserve_min_amount is not None:
            result['ReserveMinAmount'] = self.reserve_min_amount
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.skip_user_auth_check is not None:
            result['SkipUserAuthCheck'] = self.skip_user_auth_check
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppCenterImageName') is not None:
            self.app_center_image_name = m.get('AppCenterImageName')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')
        if m.get('AppInstanceTypeName') is not None:
            self.app_instance_type_name = m.get('AppInstanceTypeName')
        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('MaxAmount') is not None:
            self.max_amount = m.get('MaxAmount')
        if m.get('MinAmount') is not None:
            self.min_amount = m.get('MinAmount')
        self.node_pool = []
        if m.get('NodePool') is not None:
            for k in m.get('NodePool'):
                temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool()
                self.node_pool.append(temp_model.from_map(k))
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OtaInfo') is not None:
            temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo()
            self.ota_info = temp_model.from_map(m['OtaInfo'])
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReserveAmountRatio') is not None:
            self.reserve_amount_ratio = m.get('ReserveAmountRatio')
        if m.get('ReserveMaxAmount') is not None:
            self.reserve_max_amount = m.get('ReserveMaxAmount')
        if m.get('ReserveMinAmount') is not None:
            self.reserve_min_amount = m.get('ReserveMinAmount')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('SkipUserAuthCheck') is not None:
            self.skip_user_auth_check = m.get('SkipUserAuthCheck')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        app_instance_group_models: GetAppInstanceGroupResponseBodyAppInstanceGroupModels = None,
        request_id: str = None,
    ):
        # AppInstanceGroupModels
        self.app_instance_group_models = app_instance_group_models
        self.request_id = request_id

    def validate(self):
        if self.app_instance_group_models:
            self.app_instance_group_models.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_models is not None:
            result['AppInstanceGroupModels'] = self.app_instance_group_models.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupModels') is not None:
            temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModels()
            self.app_instance_group_models = temp_model.from_map(m['AppInstanceGroupModels'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionTicketRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id_list: List[str] = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        app_start_param: str = None,
        app_version: str = None,
        biz_region_id: str = None,
        end_user_id: str = None,
        product_type: str = None,
        task_id: str = None,
    ):
        self.app_id = app_id
        self.app_instance_group_id_list = app_instance_group_id_list
        self.app_instance_id = app_instance_id
        self.app_instance_persistent_id = app_instance_persistent_id
        self.app_start_param = app_start_param
        self.app_version = app_version
        self.biz_region_id = biz_region_id
        self.end_user_id = end_user_id
        self.product_type = product_type
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_instance_group_id_list is not None:
            result['AppInstanceGroupIdList'] = self.app_instance_group_id_list
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id
        if self.app_start_param is not None:
            result['AppStartParam'] = self.app_start_param
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInstanceGroupIdList') is not None:
            self.app_instance_group_id_list = m.get('AppInstanceGroupIdList')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')
        if m.get('AppStartParam') is not None:
            self.app_start_param = m.get('AppStartParam')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetConnectionTicketResponseBody(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        biz_region_id: str = None,
        os_type: str = None,
        request_id: str = None,
        task_id: str = None,
        task_status: str = None,
        tenant_id: int = None,
        ticket: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.app_instance_persistent_id = app_instance_persistent_id
        self.biz_region_id = biz_region_id
        self.os_type = os_type
        self.request_id = request_id
        self.task_id = task_id
        self.task_status = task_status
        self.tenant_id = tenant_id
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class GetConnectionTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConnectionTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetConnectionTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDebugAppInstanceRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetDebugAppInstanceResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_version: str = None,
        auth_code: str = None,
        request_id: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.app_version = app_version
        self.auth_code = auth_code
        self.request_id = request_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetDebugAppInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDebugAppInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetDebugAppInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOtaTaskByTaskIdRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetOtaTaskByTaskIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        ota_version: str = None,
        release_note: str = None,
        request_id: str = None,
        task_start_time: str = None,
    ):
        self.code = code
        self.message = message
        self.ota_version = ota_version
        self.release_note = release_note
        self.request_id = request_id
        self.task_start_time = task_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')
        return self


class GetOtaTaskByTaskIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOtaTaskByTaskIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetOtaTaskByTaskIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectPoliciesRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetProjectPoliciesResponseBodyData(TeaModel):
    def __init__(
        self,
        clipboard: int = None,
        file_transfer: int = None,
        frame_rate: str = None,
        keep_alive_duration: int = None,
        max_hours: int = None,
        max_sessions: int = None,
        project_id: str = None,
        session_resolution_height: int = None,
        session_resolution_width: int = None,
        session_spec: str = None,
        streaming_mode: str = None,
        terminal_resolution_adaptation: bool = None,
    ):
        self.clipboard = clipboard
        self.file_transfer = file_transfer
        self.frame_rate = frame_rate
        self.keep_alive_duration = keep_alive_duration
        self.max_hours = max_hours
        self.max_sessions = max_sessions
        self.project_id = project_id
        self.session_resolution_height = session_resolution_height
        self.session_resolution_width = session_resolution_width
        self.session_spec = session_spec
        self.streaming_mode = streaming_mode
        self.terminal_resolution_adaptation = terminal_resolution_adaptation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.file_transfer is not None:
            result['FileTransfer'] = self.file_transfer
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.keep_alive_duration is not None:
            result['KeepAliveDuration'] = self.keep_alive_duration
        if self.max_hours is not None:
            result['MaxHours'] = self.max_hours
        if self.max_sessions is not None:
            result['MaxSessions'] = self.max_sessions
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.session_resolution_height is not None:
            result['SessionResolutionHeight'] = self.session_resolution_height
        if self.session_resolution_width is not None:
            result['SessionResolutionWidth'] = self.session_resolution_width
        if self.session_spec is not None:
            result['SessionSpec'] = self.session_spec
        if self.streaming_mode is not None:
            result['StreamingMode'] = self.streaming_mode
        if self.terminal_resolution_adaptation is not None:
            result['TerminalResolutionAdaptation'] = self.terminal_resolution_adaptation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('FileTransfer') is not None:
            self.file_transfer = m.get('FileTransfer')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('KeepAliveDuration') is not None:
            self.keep_alive_duration = m.get('KeepAliveDuration')
        if m.get('MaxHours') is not None:
            self.max_hours = m.get('MaxHours')
        if m.get('MaxSessions') is not None:
            self.max_sessions = m.get('MaxSessions')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SessionResolutionHeight') is not None:
            self.session_resolution_height = m.get('SessionResolutionHeight')
        if m.get('SessionResolutionWidth') is not None:
            self.session_resolution_width = m.get('SessionResolutionWidth')
        if m.get('SessionSpec') is not None:
            self.session_spec = m.get('SessionSpec')
        if m.get('StreamingMode') is not None:
            self.streaming_mode = m.get('StreamingMode')
        if m.get('TerminalResolutionAdaptation') is not None:
            self.terminal_resolution_adaptation = m.get('TerminalResolutionAdaptation')
        return self


class GetProjectPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetProjectPoliciesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetProjectPoliciesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetProjectPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectPoliciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetProjectPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourcePriceRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        app_instance_type: str = None,
        biz_region_id: str = None,
        charge_type: str = None,
        node_instance_type: str = None,
        period: int = None,
        period_unit: str = None,
        product_type: str = None,
    ):
        self.amount = amount
        self.app_instance_type = app_instance_type
        self.biz_region_id = biz_region_id
        self.charge_type = charge_type
        self.node_instance_type = node_instance_type
        self.period = period
        self.period_unit = period_unit
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetResourcePriceResponseBodyPriceListPricePromotions(TeaModel):
    def __init__(
        self,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        selected: bool = None,
    ):
        self.option_code = option_code
        self.promotion_desc = promotion_desc
        self.promotion_id = promotion_id
        self.promotion_name = promotion_name
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class GetResourcePriceResponseBodyPriceListPrice(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: str = None,
        original_price: str = None,
        promotions: List[GetResourcePriceResponseBodyPriceListPricePromotions] = None,
        trade_price: str = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.promotions = promotions
        self.trade_price = trade_price

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = GetResourcePriceResponseBodyPriceListPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class GetResourcePriceResponseBodyPriceListRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        self.description = description
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetResourcePriceResponseBodyPriceList(TeaModel):
    def __init__(
        self,
        price: GetResourcePriceResponseBodyPriceListPrice = None,
        price_type: str = None,
        rules: List[GetResourcePriceResponseBodyPriceListRules] = None,
    ):
        self.price = price
        self.price_type = price_type
        self.rules = rules

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        if self.price_type is not None:
            result['PriceType'] = self.price_type
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = GetResourcePriceResponseBodyPriceListPrice()
            self.price = temp_model.from_map(m['Price'])
        if m.get('PriceType') is not None:
            self.price_type = m.get('PriceType')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetResourcePriceResponseBodyPriceListRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetResourcePriceResponseBodyPriceModelPricePromotions(TeaModel):
    def __init__(
        self,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        selected: bool = None,
    ):
        self.option_code = option_code
        self.promotion_desc = promotion_desc
        self.promotion_id = promotion_id
        self.promotion_name = promotion_name
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class GetResourcePriceResponseBodyPriceModelPrice(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: str = None,
        original_price: str = None,
        promotions: List[GetResourcePriceResponseBodyPriceModelPricePromotions] = None,
        trade_price: str = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.promotions = promotions
        self.trade_price = trade_price

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = GetResourcePriceResponseBodyPriceModelPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class GetResourcePriceResponseBodyPriceModelRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        self.description = description
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetResourcePriceResponseBodyPriceModel(TeaModel):
    def __init__(
        self,
        price: GetResourcePriceResponseBodyPriceModelPrice = None,
        rules: List[GetResourcePriceResponseBodyPriceModelRules] = None,
    ):
        self.price = price
        self.rules = rules

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = GetResourcePriceResponseBodyPriceModelPrice()
            self.price = temp_model.from_map(m['Price'])
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetResourcePriceResponseBodyPriceModelRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetResourcePriceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        price_list: List[GetResourcePriceResponseBodyPriceList] = None,
        price_model: GetResourcePriceResponseBodyPriceModel = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.price_list = price_list
        self.price_model = price_model
        self.request_id = request_id

    def validate(self):
        if self.price_list:
            for k in self.price_list:
                if k:
                    k.validate()
        if self.price_model:
            self.price_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PriceList'] = []
        if self.price_list is not None:
            for k in self.price_list:
                result['PriceList'].append(k.to_map() if k else None)
        if self.price_model is not None:
            result['PriceModel'] = self.price_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.price_list = []
        if m.get('PriceList') is not None:
            for k in m.get('PriceList'):
                temp_model = GetResourcePriceResponseBodyPriceList()
                self.price_list.append(temp_model.from_map(k))
        if m.get('PriceModel') is not None:
            temp_model = GetResourcePriceResponseBodyPriceModel()
            self.price_model = temp_model.from_map(m['PriceModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourcePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourcePriceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetResourcePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceRenewPriceRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        period: int = None,
        period_unit: str = None,
        product_type: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.period = period
        self.period_unit = period_unit
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetResourceRenewPriceResponseBodyDataPricePromotions(TeaModel):
    def __init__(
        self,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        selected: bool = None,
    ):
        self.option_code = option_code
        self.promotion_desc = promotion_desc
        self.promotion_id = promotion_id
        self.promotion_name = promotion_name
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class GetResourceRenewPriceResponseBodyDataPrice(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: str = None,
        original_price: str = None,
        promotions: List[GetResourceRenewPriceResponseBodyDataPricePromotions] = None,
        trade_price: str = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.promotions = promotions
        self.trade_price = trade_price

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = GetResourceRenewPriceResponseBodyDataPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class GetResourceRenewPriceResponseBodyDataRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        self.description = description
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetResourceRenewPriceResponseBodyData(TeaModel):
    def __init__(
        self,
        price: GetResourceRenewPriceResponseBodyDataPrice = None,
        rules: List[GetResourceRenewPriceResponseBodyDataRules] = None,
    ):
        self.price = price
        self.rules = rules

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = GetResourceRenewPriceResponseBodyDataPrice()
            self.price = temp_model.from_map(m['Price'])
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetResourceRenewPriceResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetResourceRenewPriceResponseBody(TeaModel):
    def __init__(
        self,
        data: GetResourceRenewPriceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetResourceRenewPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceRenewPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceRenewPriceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetResourceRenewPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessPagesRequest(TeaModel):
    def __init__(
        self,
        access_page_id: str = None,
        access_page_name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        sort_type: str = None,
    ):
        self.access_page_id = access_page_id
        self.access_page_name = access_page_name
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.sort_type = sort_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        if self.access_page_name is not None:
            result['AccessPageName'] = self.access_page_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        if m.get('AccessPageName') is not None:
            self.access_page_name = m.get('AccessPageName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        return self


class ListAccessPagesResponseBodyData(TeaModel):
    def __init__(
        self,
        access_mode: str = None,
        access_page_id: str = None,
        access_page_name: str = None,
        access_page_state: str = None,
        access_url: str = None,
        content_id: str = None,
        content_name: str = None,
        effect_time: int = None,
        gmt_create: str = None,
        project_id: str = None,
        project_name: str = None,
        unit: str = None,
        url_expire_time: str = None,
    ):
        self.access_mode = access_mode
        self.access_page_id = access_page_id
        self.access_page_name = access_page_name
        self.access_page_state = access_page_state
        self.access_url = access_url
        self.content_id = content_id
        self.content_name = content_name
        self.effect_time = effect_time
        self.gmt_create = gmt_create
        self.project_id = project_id
        self.project_name = project_name
        self.unit = unit
        self.url_expire_time = url_expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        if self.access_page_name is not None:
            result['AccessPageName'] = self.access_page_name
        if self.access_page_state is not None:
            result['AccessPageState'] = self.access_page_state
        if self.access_url is not None:
            result['AccessUrl'] = self.access_url
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        if self.content_name is not None:
            result['ContentName'] = self.content_name
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.url_expire_time is not None:
            result['UrlExpireTime'] = self.url_expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        if m.get('AccessPageName') is not None:
            self.access_page_name = m.get('AccessPageName')
        if m.get('AccessPageState') is not None:
            self.access_page_state = m.get('AccessPageState')
        if m.get('AccessUrl') is not None:
            self.access_url = m.get('AccessUrl')
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        if m.get('ContentName') is not None:
            self.content_name = m.get('ContentName')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('UrlExpireTime') is not None:
            self.url_expire_time = m.get('UrlExpireTime')
        return self


class ListAccessPagesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: str = None,
        data: List[ListAccessPagesResponseBodyData] = None,
        message: str = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAccessPagesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAccessPagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccessPagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListAccessPagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        biz_region_id: str = None,
        node_instance_type: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        status: List[str] = None,
    ):
        self.app_center_image_id = app_center_image_id
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_group_name = app_instance_group_name
        self.biz_region_id = biz_region_id
        self.node_instance_type = node_instance_type
        self.page_number = page_number
        self.page_size = page_size
        self.product_type = product_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps(TeaModel):
    def __init__(
        self,
        app_icon: str = None,
        app_id: str = None,
        app_name: str = None,
        app_version: str = None,
        app_version_name: str = None,
    ):
        # 应用图标。
        self.app_icon = app_icon
        self.app_id = app_id
        self.app_name = app_name
        # 应用版本。
        self.app_version = app_version
        # 应用版本名称。
        self.app_version_name = app_version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_icon is not None:
            result['AppIcon'] = self.app_icon
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIcon') is not None:
            self.app_icon = m.get('AppIcon')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(
        self,
        amount: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.amount = amount
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules(TeaModel):
    def __init__(
        self,
        recurrence_type: str = None,
        recurrence_values: List[int] = None,
        timer_periods: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods] = None,
    ):
        self.recurrence_type = recurrence_type
        self.recurrence_values = recurrence_values
        self.timer_periods = timer_periods

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool(TeaModel):
    def __init__(
        self,
        amount: int = None,
        max_scaling_amount: int = None,
        node_amount: int = None,
        node_capacity: int = None,
        node_instance_type: str = None,
        node_pool_id: str = None,
        node_type_name: str = None,
        node_used: int = None,
        recurrence_schedules: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules] = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_node_amount: int = None,
        scaling_node_used: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        strategy_disable_date: str = None,
        strategy_enable_date: str = None,
        strategy_type: str = None,
        warm_up: bool = None,
    ):
        self.amount = amount
        self.max_scaling_amount = max_scaling_amount
        self.node_amount = node_amount
        self.node_capacity = node_capacity
        self.node_instance_type = node_instance_type
        self.node_pool_id = node_pool_id
        self.node_type_name = node_type_name
        self.node_used = node_used
        self.recurrence_schedules = recurrence_schedules
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        self.scaling_node_amount = scaling_node_amount
        self.scaling_node_used = scaling_node_used
        self.scaling_step = scaling_step
        self.scaling_usage_threshold = scaling_usage_threshold
        self.strategy_disable_date = strategy_disable_date
        self.strategy_enable_date = strategy_enable_date
        self.strategy_type = strategy_type
        self.warm_up = warm_up

    def validate(self):
        if self.recurrence_schedules:
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        if self.node_type_name is not None:
            result['NodeTypeName'] = self.node_type_name
        if self.node_used is not None:
            result['NodeUsed'] = self.node_used
        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_node_amount is not None:
            result['ScalingNodeAmount'] = self.scaling_node_amount
        if self.scaling_node_used is not None:
            result['ScalingNodeUsed'] = self.scaling_node_used
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.strategy_disable_date is not None:
            result['StrategyDisableDate'] = self.strategy_disable_date
        if self.strategy_enable_date is not None:
            result['StrategyEnableDate'] = self.strategy_enable_date
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.warm_up is not None:
            result['WarmUp'] = self.warm_up
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        if m.get('NodeTypeName') is not None:
            self.node_type_name = m.get('NodeTypeName')
        if m.get('NodeUsed') is not None:
            self.node_used = m.get('NodeUsed')
        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k in m.get('RecurrenceSchedules'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingNodeAmount') is not None:
            self.scaling_node_amount = m.get('ScalingNodeAmount')
        if m.get('ScalingNodeUsed') is not None:
            self.scaling_node_used = m.get('ScalingNodeUsed')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('StrategyDisableDate') is not None:
            self.strategy_disable_date = m.get('StrategyDisableDate')
        if m.get('StrategyEnableDate') is not None:
            self.strategy_enable_date = m.get('StrategyEnableDate')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('WarmUp') is not None:
            self.warm_up = m.get('WarmUp')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo(TeaModel):
    def __init__(
        self,
        new_ota_version: str = None,
        ota_version: str = None,
        task_id: str = None,
    ):
        self.new_ota_version = new_ota_version
        self.ota_version = ota_version
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_ota_version is not None:
            result['NewOtaVersion'] = self.new_ota_version
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewOtaVersion') is not None:
            self.new_ota_version = m.get('NewOtaVersion')
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModels(TeaModel):
    def __init__(
        self,
        amount: int = None,
        app_center_image_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        app_instance_type: str = None,
        app_policy_id: str = None,
        apps: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps] = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        expired_time: str = None,
        gmt_create: str = None,
        max_amount: int = None,
        min_amount: int = None,
        node_pool: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool] = None,
        os_type: str = None,
        ota_info: ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo = None,
        product_type: str = None,
        region_id: str = None,
        reserve_amount_ratio: str = None,
        reserve_max_amount: int = None,
        reserve_min_amount: int = None,
        resource_status: str = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        session_timeout: str = None,
        skip_user_auth_check: bool = None,
        spec_id: str = None,
        status: str = None,
    ):
        self.amount = amount
        self.app_center_image_id = app_center_image_id
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_group_name = app_instance_group_name
        self.app_instance_type = app_instance_type
        # 策略ID。
        self.app_policy_id = app_policy_id
        self.apps = apps
        # 售卖模式。
        self.charge_resource_mode = charge_resource_mode
        self.charge_type = charge_type
        self.expired_time = expired_time
        self.gmt_create = gmt_create
        self.max_amount = max_amount
        self.min_amount = min_amount
        self.node_pool = node_pool
        self.os_type = os_type
        self.ota_info = ota_info
        self.product_type = product_type
        self.region_id = region_id
        self.reserve_amount_ratio = reserve_amount_ratio
        self.reserve_max_amount = reserve_max_amount
        self.reserve_min_amount = reserve_min_amount
        self.resource_status = resource_status
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        self.scaling_step = scaling_step
        self.scaling_usage_threshold = scaling_usage_threshold
        self.session_timeout = session_timeout
        self.skip_user_auth_check = skip_user_auth_check
        self.spec_id = spec_id
        self.status = status

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()
        if self.node_pool:
            for k in self.node_pool:
                if k:
                    k.validate()
        if self.ota_info:
            self.ota_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type
        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.max_amount is not None:
            result['MaxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['MinAmount'] = self.min_amount
        result['NodePool'] = []
        if self.node_pool is not None:
            for k in self.node_pool:
                result['NodePool'].append(k.to_map() if k else None)
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.ota_info is not None:
            result['OtaInfo'] = self.ota_info.to_map()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reserve_amount_ratio is not None:
            result['ReserveAmountRatio'] = self.reserve_amount_ratio
        if self.reserve_max_amount is not None:
            result['ReserveMaxAmount'] = self.reserve_max_amount
        if self.reserve_min_amount is not None:
            result['ReserveMinAmount'] = self.reserve_min_amount
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.skip_user_auth_check is not None:
            result['SkipUserAuthCheck'] = self.skip_user_auth_check
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')
        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('MaxAmount') is not None:
            self.max_amount = m.get('MaxAmount')
        if m.get('MinAmount') is not None:
            self.min_amount = m.get('MinAmount')
        self.node_pool = []
        if m.get('NodePool') is not None:
            for k in m.get('NodePool'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool()
                self.node_pool.append(temp_model.from_map(k))
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OtaInfo') is not None:
            temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo()
            self.ota_info = temp_model.from_map(m['OtaInfo'])
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReserveAmountRatio') is not None:
            self.reserve_amount_ratio = m.get('ReserveAmountRatio')
        if m.get('ReserveMaxAmount') is not None:
            self.reserve_max_amount = m.get('ReserveMaxAmount')
        if m.get('ReserveMinAmount') is not None:
            self.reserve_min_amount = m.get('ReserveMinAmount')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('SkipUserAuthCheck') is not None:
            self.skip_user_auth_check = m.get('SkipUserAuthCheck')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        app_instance_group_models: List[ListAppInstanceGroupResponseBodyAppInstanceGroupModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.app_instance_group_models = app_instance_group_models
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.app_instance_group_models:
            for k in self.app_instance_group_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInstanceGroupModels'] = []
        if self.app_instance_group_models is not None:
            for k in self.app_instance_group_models:
                result['AppInstanceGroupModels'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_instance_group_models = []
        if m.get('AppInstanceGroupModels') is not None:
            for k in m.get('AppInstanceGroupModels'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModels()
                self.app_instance_group_models.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppInstancesRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_id_list: List[str] = None,
        include_deleted: bool = None,
        page_number: int = None,
        page_size: int = None,
        status: List[str] = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.app_instance_id_list = app_instance_id_list
        self.include_deleted = include_deleted
        self.page_number = page_number
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_id_list is not None:
            result['AppInstanceIdList'] = self.app_instance_id_list
        if self.include_deleted is not None:
            result['IncludeDeleted'] = self.include_deleted
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstanceIdList') is not None:
            self.app_instance_id_list = m.get('AppInstanceIdList')
        if m.get('IncludeDeleted') is not None:
            self.include_deleted = m.get('IncludeDeleted')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppInstancesResponseBodyAppInstanceModelsBindInfo(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        usage_duration: int = None,
    ):
        self.end_user_id = end_user_id
        self.usage_duration = usage_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.usage_duration is not None:
            result['UsageDuration'] = self.usage_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('UsageDuration') is not None:
            self.usage_duration = m.get('UsageDuration')
        return self


class ListAppInstancesResponseBodyAppInstanceModels(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        bind_info: ListAppInstancesResponseBodyAppInstanceModelsBindInfo = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        main_eth_public_ip: str = None,
        session_status: str = None,
        status: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.bind_info = bind_info
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.main_eth_public_ip = main_eth_public_ip
        self.session_status = session_status
        self.status = status

    def validate(self):
        if self.bind_info:
            self.bind_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.bind_info is not None:
            result['BindInfo'] = self.bind_info.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.main_eth_public_ip is not None:
            result['MainEthPublicIp'] = self.main_eth_public_ip
        if self.session_status is not None:
            result['SessionStatus'] = self.session_status
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('BindInfo') is not None:
            temp_model = ListAppInstancesResponseBodyAppInstanceModelsBindInfo()
            self.bind_info = temp_model.from_map(m['BindInfo'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MainEthPublicIp') is not None:
            self.main_eth_public_ip = m.get('MainEthPublicIp')
        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppInstancesResponseBody(TeaModel):
    def __init__(
        self,
        app_instance_models: List[ListAppInstancesResponseBodyAppInstanceModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.app_instance_models = app_instance_models
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.app_instance_models:
            for k in self.app_instance_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInstanceModels'] = []
        if self.app_instance_models is not None:
            for k in self.app_instance_models:
                result['AppInstanceModels'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_instance_models = []
        if m.get('AppInstanceModels') is not None:
            for k in m.get('AppInstanceModels'):
                temp_model = ListAppInstancesResponseBodyAppInstanceModels()
                self.app_instance_models.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListAppInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeInstanceTypeRequest(TeaModel):
    def __init__(
        self,
        biz_region_id: str = None,
        language: str = None,
        node_instance_type: str = None,
        os_type: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        # 资源所属的地域ID。关于支持的地域详情，请参见[使用限制](~~426036~~)。
        self.biz_region_id = biz_region_id
        # 语言类型。
        self.language = language
        self.node_instance_type = node_instance_type
        # 支持的操作系统类型。
        self.os_type = os_type
        self.page_number = page_number
        self.page_size = page_size
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.language is not None:
            result['Language'] = self.language
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels(TeaModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gpu_memory: int = None,
        max_capacity: int = None,
        memory: int = None,
        node_instance_type: str = None,
        node_instance_type_family: str = None,
        node_type_name: str = None,
    ):
        self.cpu = cpu
        self.gpu = gpu
        # 显卡内存大小，单位为MB。
        self.gpu_memory = gpu_memory
        # 最大并发会话数，即单个资源可同时连接的会话数。如果同时连接的会话数过多，可能导致应用的使用体验下降。取值范围因资源规格不同而不同。各资源规格对应的取值范围分别是：
        # 
        # - appstreaming.general.4c8g：1\~2；
        # - appstreaming.general.8c16g：1\~4；
        # - appstreaming.vgpu.8c16g.4g：1\~4；
        # - appstreaming.vgpu.8c31g.16g：1\~4；
        # - appstreaming.vgpu.14c93g.12g：1\~6；
        self.max_capacity = max_capacity
        self.memory = memory
        self.node_instance_type = node_instance_type
        self.node_instance_type_family = node_instance_type_family
        # 资源规格名称。
        self.node_type_name = node_type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory
        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.node_instance_type_family is not None:
            result['NodeInstanceTypeFamily'] = self.node_instance_type_family
        if self.node_type_name is not None:
            result['NodeTypeName'] = self.node_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')
        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('NodeInstanceTypeFamily') is not None:
            self.node_instance_type_family = m.get('NodeInstanceTypeFamily')
        if m.get('NodeTypeName') is not None:
            self.node_type_name = m.get('NodeTypeName')
        return self


class ListNodeInstanceTypeResponseBody(TeaModel):
    def __init__(
        self,
        node_instance_type_models: List[ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.node_instance_type_models = node_instance_type_models
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.node_instance_type_models:
            for k in self.node_instance_type_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInstanceTypeModels'] = []
        if self.node_instance_type_models is not None:
            for k in self.node_instance_type_models:
                result['NodeInstanceTypeModels'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_instance_type_models = []
        if m.get('NodeInstanceTypeModels') is not None:
            for k in m.get('NodeInstanceTypeModels'):
                temp_model = ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels()
                self.node_instance_type_models.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodeInstanceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodeInstanceTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListNodeInstanceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOtaTaskRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        ota_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.ota_type = ota_type
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.ota_type is not None:
            result['OtaType'] = self.ota_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('OtaType') is not None:
            self.ota_type = m.get('OtaType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOtaTaskResponseBodyTaskList(TeaModel):
    def __init__(
        self,
        ota_version: str = None,
        task_display_status: str = None,
        task_id: str = None,
        task_start_time: str = None,
    ):
        self.ota_version = ota_version
        self.task_display_status = task_display_status
        self.task_id = task_id
        self.task_start_time = task_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version
        if self.task_display_status is not None:
            result['TaskDisplayStatus'] = self.task_display_status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')
        if m.get('TaskDisplayStatus') is not None:
            self.task_display_status = m.get('TaskDisplayStatus')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')
        return self


class ListOtaTaskResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        task_list: List[ListOtaTaskResponseBodyTaskList] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.task_list = task_list
        self.total_count = total_count

    def validate(self):
        if self.task_list:
            for k in self.task_list:
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListOtaTaskResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOtaTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOtaTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListOtaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        project_name: str = None,
        sort_type: str = None,
        state_list: List[int] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.project_name = project_name
        self.sort_type = sort_type
        self.state_list = state_list

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
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.state_list is not None:
            result['StateList'] = self.state_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('StateList') is not None:
            self.state_list = m.get('StateList')
        return self


class ListProjectsResponseBodyData(TeaModel):
    def __init__(
        self,
        access_page_id: List[int] = None,
        available_hours: int = None,
        content_id: str = None,
        content_name: str = None,
        create_time: str = None,
        description: str = None,
        in_use_sessions: int = None,
        max_hours: int = None,
        max_sessions: int = None,
        project_id: str = None,
        project_name: str = None,
        project_state: str = None,
        session_spec: str = None,
    ):
        self.access_page_id = access_page_id
        self.available_hours = available_hours
        self.content_id = content_id
        self.content_name = content_name
        self.create_time = create_time
        self.description = description
        self.in_use_sessions = in_use_sessions
        self.max_hours = max_hours
        self.max_sessions = max_sessions
        self.project_id = project_id
        self.project_name = project_name
        self.project_state = project_state
        self.session_spec = session_spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        if self.available_hours is not None:
            result['AvailableHours'] = self.available_hours
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        if self.content_name is not None:
            result['ContentName'] = self.content_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.in_use_sessions is not None:
            result['InUseSessions'] = self.in_use_sessions
        if self.max_hours is not None:
            result['MaxHours'] = self.max_hours
        if self.max_sessions is not None:
            result['MaxSessions'] = self.max_sessions
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_state is not None:
            result['ProjectState'] = self.project_state
        if self.session_spec is not None:
            result['SessionSpec'] = self.session_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        if m.get('AvailableHours') is not None:
            self.available_hours = m.get('AvailableHours')
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        if m.get('ContentName') is not None:
            self.content_name = m.get('ContentName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InUseSessions') is not None:
            self.in_use_sessions = m.get('InUseSessions')
        if m.get('MaxHours') is not None:
            self.max_hours = m.get('MaxHours')
        if m.get('MaxSessions') is not None:
            self.max_sessions = m.get('MaxSessions')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectState') is not None:
            self.project_state = m.get('ProjectState')
        if m.get('SessionSpec') is not None:
            self.session_spec = m.get('SessionSpec')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListProjectsResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListProjectsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyRegionModels(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        region_models: List[ListRegionsResponseBodyRegionModels] = None,
        request_id: str = None,
    ):
        self.region_models = region_models
        self.request_id = request_id

    def validate(self):
        if self.region_models:
            for k in self.region_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionModels'] = []
        if self.region_models is not None:
            for k in self.region_models:
                result['RegionModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_models = []
        if m.get('RegionModels') is not None:
            for k in m.get('RegionModels'):
                temp_model = ListRegionsResponseBodyRegionModels()
                self.region_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSessionPackagesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        session_package_id: str = None,
        session_package_name: str = None,
        sort_type: str = None,
        state_list: List[int] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.session_package_id = session_package_id
        self.session_package_name = session_package_name
        self.sort_type = sort_type
        self.state_list = state_list

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
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
        if self.session_package_name is not None:
            result['SessionPackageName'] = self.session_package_name
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.state_list is not None:
            result['StateList'] = self.state_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        if m.get('SessionPackageName') is not None:
            self.session_package_name = m.get('SessionPackageName')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('StateList') is not None:
            self.state_list = m.get('StateList')
        return self


class ListSessionPackagesResponseBodyDataInstanceObject(TeaModel):
    def __init__(
        self,
        expired_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        resource_id: str = None,
        resource_type: str = None,
        start_time: str = None,
        total_time: int = None,
        used_time: int = None,
    ):
        self.expired_time = expired_time
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.start_time = start_time
        self.total_time = total_time
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        return self


class ListSessionPackagesResponseBodyData(TeaModel):
    def __init__(
        self,
        available_hours: int = None,
        charge_type: str = None,
        delete_status: int = None,
        gmt_create: str = None,
        gmt_modified_time: str = None,
        instance_object: ListSessionPackagesResponseBodyDataInstanceObject = None,
        max_hours: int = None,
        max_sessions: int = None,
        project_id: str = None,
        project_name: str = None,
        region: str = None,
        session_package_id: str = None,
        session_package_name: str = None,
        session_package_type_id: str = None,
        session_spec: str = None,
        session_usage_rate: int = None,
        state: int = None,
        user_identification: int = None,
    ):
        self.available_hours = available_hours
        self.charge_type = charge_type
        self.delete_status = delete_status
        self.gmt_create = gmt_create
        self.gmt_modified_time = gmt_modified_time
        self.instance_object = instance_object
        self.max_hours = max_hours
        self.max_sessions = max_sessions
        self.project_id = project_id
        self.project_name = project_name
        self.region = region
        self.session_package_id = session_package_id
        self.session_package_name = session_package_name
        self.session_package_type_id = session_package_type_id
        self.session_spec = session_spec
        self.session_usage_rate = session_usage_rate
        self.state = state
        self.user_identification = user_identification

    def validate(self):
        if self.instance_object:
            self.instance_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_hours is not None:
            result['AvailableHours'] = self.available_hours
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.delete_status is not None:
            result['DeleteStatus'] = self.delete_status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_object is not None:
            result['InstanceObject'] = self.instance_object.to_map()
        if self.max_hours is not None:
            result['MaxHours'] = self.max_hours
        if self.max_sessions is not None:
            result['MaxSessions'] = self.max_sessions
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region is not None:
            result['Region'] = self.region
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
        if self.session_package_name is not None:
            result['SessionPackageName'] = self.session_package_name
        if self.session_package_type_id is not None:
            result['SessionPackageTypeId'] = self.session_package_type_id
        if self.session_spec is not None:
            result['SessionSpec'] = self.session_spec
        if self.session_usage_rate is not None:
            result['SessionUsageRate'] = self.session_usage_rate
        if self.state is not None:
            result['State'] = self.state
        if self.user_identification is not None:
            result['UserIdentification'] = self.user_identification
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableHours') is not None:
            self.available_hours = m.get('AvailableHours')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DeleteStatus') is not None:
            self.delete_status = m.get('DeleteStatus')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceObject') is not None:
            temp_model = ListSessionPackagesResponseBodyDataInstanceObject()
            self.instance_object = temp_model.from_map(m['InstanceObject'])
        if m.get('MaxHours') is not None:
            self.max_hours = m.get('MaxHours')
        if m.get('MaxSessions') is not None:
            self.max_sessions = m.get('MaxSessions')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        if m.get('SessionPackageName') is not None:
            self.session_package_name = m.get('SessionPackageName')
        if m.get('SessionPackageTypeId') is not None:
            self.session_package_type_id = m.get('SessionPackageTypeId')
        if m.get('SessionSpec') is not None:
            self.session_spec = m.get('SessionSpec')
        if m.get('SessionUsageRate') is not None:
            self.session_usage_rate = m.get('SessionUsageRate')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserIdentification') is not None:
            self.user_identification = m.get('UserIdentification')
        return self


class ListSessionPackagesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListSessionPackagesResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSessionPackagesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSessionPackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSessionPackagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListSessionPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTenantConfigResponseBodyTenantConfigModel(TeaModel):
    def __init__(
        self,
        app_instance_group_expire_remind: bool = None,
    ):
        self.app_instance_group_expire_remind = app_instance_group_expire_remind

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_expire_remind is not None:
            result['AppInstanceGroupExpireRemind'] = self.app_instance_group_expire_remind
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupExpireRemind') is not None:
            self.app_instance_group_expire_remind = m.get('AppInstanceGroupExpireRemind')
        return self


class ListTenantConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_config_model: ListTenantConfigResponseBodyTenantConfigModel = None,
    ):
        self.request_id = request_id
        self.tenant_config_model = tenant_config_model

    def validate(self):
        if self.tenant_config_model:
            self.tenant_config_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_config_model is not None:
            result['TenantConfigModel'] = self.tenant_config_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantConfigModel') is not None:
            temp_model = ListTenantConfigResponseBodyTenantConfigModel()
            self.tenant_config_model = temp_model.from_map(m['TenantConfigModel'])
        return self


class ListTenantConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTenantConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListTenantConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LogOffAllSessionsInAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class LogOffAllSessionsInAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LogOffAllSessionsInAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LogOffAllSessionsInAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = LogOffAllSessionsInAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateSessionPackageRequest(TeaModel):
    def __init__(
        self,
        dest_project_id: str = None,
        session_package_id: str = None,
        source_project_id: str = None,
    ):
        self.dest_project_id = dest_project_id
        self.session_package_id = session_package_id
        self.source_project_id = source_project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_project_id is not None:
            result['DestProjectId'] = self.dest_project_id
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
        if self.source_project_id is not None:
            result['SourceProjectId'] = self.source_project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestProjectId') is not None:
            self.dest_project_id = m.get('DestProjectId')
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        if m.get('SourceProjectId') is not None:
            self.source_project_id = m.get('SourceProjectId')
        return self


class MigrateSessionPackageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MigrateSessionPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MigrateSessionPackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = MigrateSessionPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppInstanceGroupAttributeRequestNetworkDomainRules(TeaModel):
    def __init__(
        self,
        domain: str = None,
        policy: str = None,
    ):
        self.domain = domain
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.policy is not None:
            result['Policy'] = self.policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        return self


class ModifyAppInstanceGroupAttributeRequestNetwork(TeaModel):
    def __init__(
        self,
        domain_rules: List[ModifyAppInstanceGroupAttributeRequestNetworkDomainRules] = None,
    ):
        self.domain_rules = domain_rules

    def validate(self):
        if self.domain_rules:
            for k in self.domain_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainRules'] = []
        if self.domain_rules is not None:
            for k in self.domain_rules:
                result['DomainRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_rules = []
        if m.get('DomainRules') is not None:
            for k in m.get('DomainRules'):
                temp_model = ModifyAppInstanceGroupAttributeRequestNetworkDomainRules()
                self.domain_rules.append(temp_model.from_map(k))
        return self


class ModifyAppInstanceGroupAttributeRequestNodePool(TeaModel):
    def __init__(
        self,
        node_capacity: int = None,
        node_pool_id: str = None,
    ):
        self.node_capacity = node_capacity
        self.node_pool_id = node_pool_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        return self


class ModifyAppInstanceGroupAttributeRequestSecurityPolicy(TeaModel):
    def __init__(
        self,
        reset_after_unbind: bool = None,
        skip_user_auth_check: bool = None,
    ):
        self.reset_after_unbind = reset_after_unbind
        self.skip_user_auth_check = skip_user_auth_check

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reset_after_unbind is not None:
            result['ResetAfterUnbind'] = self.reset_after_unbind
        if self.skip_user_auth_check is not None:
            result['SkipUserAuthCheck'] = self.skip_user_auth_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResetAfterUnbind') is not None:
            self.reset_after_unbind = m.get('ResetAfterUnbind')
        if m.get('SkipUserAuthCheck') is not None:
            self.skip_user_auth_check = m.get('SkipUserAuthCheck')
        return self


class ModifyAppInstanceGroupAttributeRequestStoragePolicy(TeaModel):
    def __init__(
        self,
        storage_type_list: List[str] = None,
    ):
        self.storage_type_list = storage_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_type_list is not None:
            result['StorageTypeList'] = self.storage_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageTypeList') is not None:
            self.storage_type_list = m.get('StorageTypeList')
        return self


class ModifyAppInstanceGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        network: ModifyAppInstanceGroupAttributeRequestNetwork = None,
        node_pool: ModifyAppInstanceGroupAttributeRequestNodePool = None,
        pre_open_app_id: str = None,
        pre_open_mode: str = None,
        product_type: str = None,
        security_policy: ModifyAppInstanceGroupAttributeRequestSecurityPolicy = None,
        session_timeout: int = None,
        storage_policy: ModifyAppInstanceGroupAttributeRequestStoragePolicy = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_group_name = app_instance_group_name
        self.network = network
        self.node_pool = node_pool
        self.pre_open_app_id = pre_open_app_id
        self.pre_open_mode = pre_open_mode
        self.product_type = product_type
        self.security_policy = security_policy
        self.session_timeout = session_timeout
        self.storage_policy = storage_policy

    def validate(self):
        if self.network:
            self.network.validate()
        if self.node_pool:
            self.node_pool.validate()
        if self.security_policy:
            self.security_policy.validate()
        if self.storage_policy:
            self.storage_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.node_pool is not None:
            result['NodePool'] = self.node_pool.to_map()
        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id
        if self.pre_open_mode is not None:
            result['PreOpenMode'] = self.pre_open_mode
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.security_policy is not None:
            result['SecurityPolicy'] = self.security_policy.to_map()
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.storage_policy is not None:
            result['StoragePolicy'] = self.storage_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('Network') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('NodePool') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestNodePool()
            self.node_pool = temp_model.from_map(m['NodePool'])
        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')
        if m.get('PreOpenMode') is not None:
            self.pre_open_mode = m.get('PreOpenMode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SecurityPolicy') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestSecurityPolicy()
            self.security_policy = temp_model.from_map(m['SecurityPolicy'])
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('StoragePolicy') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestStoragePolicy()
            self.storage_policy = temp_model.from_map(m['StoragePolicy'])
        return self


class ModifyAppInstanceGroupAttributeShrinkRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        network_shrink: str = None,
        node_pool_shrink: str = None,
        pre_open_app_id: str = None,
        pre_open_mode: str = None,
        product_type: str = None,
        security_policy_shrink: str = None,
        session_timeout: int = None,
        storage_policy_shrink: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_group_name = app_instance_group_name
        self.network_shrink = network_shrink
        self.node_pool_shrink = node_pool_shrink
        self.pre_open_app_id = pre_open_app_id
        self.pre_open_mode = pre_open_mode
        self.product_type = product_type
        self.security_policy_shrink = security_policy_shrink
        self.session_timeout = session_timeout
        self.storage_policy_shrink = storage_policy_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.network_shrink is not None:
            result['Network'] = self.network_shrink
        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink
        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id
        if self.pre_open_mode is not None:
            result['PreOpenMode'] = self.pre_open_mode
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.security_policy_shrink is not None:
            result['SecurityPolicy'] = self.security_policy_shrink
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.storage_policy_shrink is not None:
            result['StoragePolicy'] = self.storage_policy_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('Network') is not None:
            self.network_shrink = m.get('Network')
        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')
        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')
        if m.get('PreOpenMode') is not None:
            self.pre_open_mode = m.get('PreOpenMode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SecurityPolicy') is not None:
            self.security_policy_shrink = m.get('SecurityPolicy')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('StoragePolicy') is not None:
            self.storage_policy_shrink = m.get('StoragePolicy')
        return self


class ModifyAppInstanceGroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppInstanceGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAppInstanceGroupAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyAppInstanceGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(
        self,
        amount: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # 资源数量。
        self.amount = amount
        # 结束时间。格式为HH:mm。
        self.end_time = end_time
        # 开始时间。格式为HH:mm。
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedules(TeaModel):
    def __init__(
        self,
        recurrence_type: str = None,
        recurrence_values: List[int] = None,
        timer_periods: List[ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedulesTimerPeriods] = None,
    ):
        # 策略执行周期的类型。必须同时指定`RecurrenceType`和`RecurrenceValues`。
        self.recurrence_type = recurrence_type
        # 策略执行周期的数值列表。
        self.recurrence_values = recurrence_values
        # 策略执行周期的时间段列表。时间段设置要求：
        # 
        # - 最多可添加3个时间段。
        # - 时间段之间不重叠。
        # - 时间段之间的间隔大于或等于5分钟。
        # - 单个时间段的时长大于或等于15分钟。
        # - 所有时间段累计不跨天。
        self.timer_periods = timer_periods

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class ModifyNodePoolAttributeRequestNodePoolStrategy(TeaModel):
    def __init__(
        self,
        max_scaling_amount: int = None,
        node_amount: int = None,
        recurrence_schedules: List[ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedules] = None,
        scaling_down_after_idle_minutes: int = None,
        scaling_step: int = None,
        scaling_usage_threshold: str = None,
        strategy_disable_date: str = None,
        strategy_enable_date: str = None,
        strategy_type: str = None,
        warm_up: bool = None,
    ):
        self.max_scaling_amount = max_scaling_amount
        # 购买资源的数量。取值范围：1~100。
        # 
        # > 
        # - 若为包年包月资源，则该参数不可修改。
        # - 若为按量付费资源，则当弹性模式（`StrategyType`）为固定数量（`NODE_FIXED`）或自动扩缩容（`NODE_SCALING_BY_USAGE`）时该参数可修改。
        self.node_amount = node_amount
        # 策略执行周期列表。`StrategyType`（弹性模式）设为`NODE_SCALING_BY_SCHEDULE`（定时扩缩容）时，该字段必填。
        self.recurrence_schedules = recurrence_schedules
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes
        self.scaling_step = scaling_step
        self.scaling_usage_threshold = scaling_usage_threshold
        # 策略失效日期。格式为：yyyy-MM-dd。失效日期与生效日期的间隔必须介于7天到1年之间（含7天和1年）。`StrategyType`（弹性模式）设为`NODE_SCALING_BY_SCHEDULE`（定时扩缩容）时，该字段必填。
        self.strategy_disable_date = strategy_disable_date
        # 策略生效日期。格式为：yyyy-MM-dd。该日期必须大于或等于当前日期。`StrategyType`（弹性模式）设为`NODE_SCALING_BY_SCHEDULE`（定时扩缩容）时，该字段必填。
        self.strategy_enable_date = strategy_enable_date
        self.strategy_type = strategy_type
        # 是否开启资源预热策略。`StrategyType`（弹性模式）设为`NODE_SCALING_BY_SCHEDULE`（定时扩缩容）时，该字段必填。
        self.warm_up = warm_up

    def validate(self):
        if self.recurrence_schedules:
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount
        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.strategy_disable_date is not None:
            result['StrategyDisableDate'] = self.strategy_disable_date
        if self.strategy_enable_date is not None:
            result['StrategyEnableDate'] = self.strategy_enable_date
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.warm_up is not None:
            result['WarmUp'] = self.warm_up
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')
        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k in m.get('RecurrenceSchedules'):
                temp_model = ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('StrategyDisableDate') is not None:
            self.strategy_disable_date = m.get('StrategyDisableDate')
        if m.get('StrategyEnableDate') is not None:
            self.strategy_enable_date = m.get('StrategyEnableDate')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('WarmUp') is not None:
            self.warm_up = m.get('WarmUp')
        return self


class ModifyNodePoolAttributeRequest(TeaModel):
    def __init__(
        self,
        biz_region_id: str = None,
        node_capacity: int = None,
        node_pool_strategy: ModifyNodePoolAttributeRequestNodePoolStrategy = None,
        pool_id: str = None,
        product_type: str = None,
    ):
        self.biz_region_id = biz_region_id
        self.node_capacity = node_capacity
        self.node_pool_strategy = node_pool_strategy
        self.pool_id = pool_id
        # 产品类型。
        self.product_type = product_type

    def validate(self):
        if self.node_pool_strategy:
            self.node_pool_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_pool_strategy is not None:
            result['NodePoolStrategy'] = self.node_pool_strategy.to_map()
        if self.pool_id is not None:
            result['PoolId'] = self.pool_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodePoolStrategy') is not None:
            temp_model = ModifyNodePoolAttributeRequestNodePoolStrategy()
            self.node_pool_strategy = temp_model.from_map(m['NodePoolStrategy'])
        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ModifyNodePoolAttributeShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_region_id: str = None,
        node_capacity: int = None,
        node_pool_strategy_shrink: str = None,
        pool_id: str = None,
        product_type: str = None,
    ):
        self.biz_region_id = biz_region_id
        self.node_capacity = node_capacity
        self.node_pool_strategy_shrink = node_pool_strategy_shrink
        self.pool_id = pool_id
        # 产品类型。
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_pool_strategy_shrink is not None:
            result['NodePoolStrategy'] = self.node_pool_strategy_shrink
        if self.pool_id is not None:
            result['PoolId'] = self.pool_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodePoolStrategy') is not None:
            self.node_pool_strategy_shrink = m.get('NodePoolStrategy')
        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ModifyNodePoolAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNodePoolAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNodePoolAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyNodePoolAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProjectPolicyRequest(TeaModel):
    def __init__(
        self,
        clipboard: int = None,
        file_transfer: int = None,
        frame_rate: int = None,
        keep_alive_duration: int = None,
        project_id: str = None,
        session_resolution_height: int = None,
        session_resolution_width: int = None,
        streaming_mode: str = None,
        terminal_resolution_adaptation: bool = None,
    ):
        self.clipboard = clipboard
        self.file_transfer = file_transfer
        self.frame_rate = frame_rate
        self.keep_alive_duration = keep_alive_duration
        self.project_id = project_id
        self.session_resolution_height = session_resolution_height
        self.session_resolution_width = session_resolution_width
        self.streaming_mode = streaming_mode
        self.terminal_resolution_adaptation = terminal_resolution_adaptation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.file_transfer is not None:
            result['FileTransfer'] = self.file_transfer
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.keep_alive_duration is not None:
            result['KeepAliveDuration'] = self.keep_alive_duration
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.session_resolution_height is not None:
            result['SessionResolutionHeight'] = self.session_resolution_height
        if self.session_resolution_width is not None:
            result['SessionResolutionWidth'] = self.session_resolution_width
        if self.streaming_mode is not None:
            result['StreamingMode'] = self.streaming_mode
        if self.terminal_resolution_adaptation is not None:
            result['TerminalResolutionAdaptation'] = self.terminal_resolution_adaptation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('FileTransfer') is not None:
            self.file_transfer = m.get('FileTransfer')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('KeepAliveDuration') is not None:
            self.keep_alive_duration = m.get('KeepAliveDuration')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SessionResolutionHeight') is not None:
            self.session_resolution_height = m.get('SessionResolutionHeight')
        if m.get('SessionResolutionWidth') is not None:
            self.session_resolution_width = m.get('SessionResolutionWidth')
        if m.get('StreamingMode') is not None:
            self.streaming_mode = m.get('StreamingMode')
        if m.get('TerminalResolutionAdaptation') is not None:
            self.terminal_resolution_adaptation = m.get('TerminalResolutionAdaptation')
        return self


class ModifyProjectPolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyProjectPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyProjectPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyProjectPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantConfigRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_expire_remind: bool = None,
    ):
        self.app_instance_group_expire_remind = app_instance_group_expire_remind

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_expire_remind is not None:
            result['AppInstanceGroupExpireRemind'] = self.app_instance_group_expire_remind
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupExpireRemind') is not None:
            self.app_instance_group_expire_remind = m.get('AppInstanceGroupExpireRemind')
        return self


class ModifyTenantConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyTenantConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTenantConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyTenantConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageListAppInstanceGroupUserRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.page_number = page_number
        self.page_size = page_size
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class PageListAppInstanceGroupUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        users: List[str] = None,
    ):
        self.request_id = request_id
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class PageListAppInstanceGroupUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PageListAppInstanceGroupUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = PageListAppInstanceGroupUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshAccessUrlRequest(TeaModel):
    def __init__(
        self,
        access_page_id: str = None,
    ):
        self.access_page_id = access_page_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        return self


class RefreshAccessUrlResponseBody(TeaModel):
    def __init__(
        self,
        access_url: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.access_url = access_url
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_url is not None:
            result['AccessUrl'] = self.access_url
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessUrl') is not None:
            self.access_url = m.get('AccessUrl')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefreshAccessUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshAccessUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RefreshAccessUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewAppInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        auto_pay: bool = None,
        period: int = None,
        period_unit: str = None,
        product_type: str = None,
        promotion_id: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.auto_pay = auto_pay
        self.period = period
        self.period_unit = period_unit
        self.product_type = product_type
        self.promotion_id = promotion_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        return self


class RenewAppInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewAppInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewAppInstanceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RenewAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewSessionPackageRequest(TeaModel):
    def __init__(
        self,
        period: int = None,
        period_unit: str = None,
        session_package_id: str = None,
    ):
        self.period = period
        self.period_unit = period_unit
        self.session_package_id = session_package_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        return self


class RenewSessionPackageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        session_package_id: int = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.session_package_id = session_package_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewSessionPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewSessionPackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RenewSessionPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindRequest(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        end_user_id: str = None,
        product_type: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.app_instance_persistent_id = app_instance_persistent_id
        self.end_user_id = end_user_id
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class UnbindResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UnbindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAccessPageStateRequest(TeaModel):
    def __init__(
        self,
        access_page_id: str = None,
        access_page_state: int = None,
    ):
        self.access_page_id = access_page_id
        self.access_page_state = access_page_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        if self.access_page_state is not None:
            result['AccessPageState'] = self.access_page_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        if m.get('AccessPageState') is not None:
            self.access_page_state = m.get('AccessPageState')
        return self


class UpdateAccessPageStateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAccessPageStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAccessPageStateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateAccessPageStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppInstanceGroupImageRequest(TeaModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        product_type: str = None,
    ):
        self.app_center_image_id = app_center_image_id
        self.app_instance_group_id = app_instance_group_id
        self.biz_region_id = biz_region_id
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class UpdateAppInstanceGroupImageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppInstanceGroupImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAppInstanceGroupImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateAppInstanceGroupImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


