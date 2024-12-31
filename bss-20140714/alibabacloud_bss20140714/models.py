# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        param_str: str = None,
    ):
        # This parameter is required.
        self.param_str = param_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_str is not None:
            result['paramStr'] = self.param_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('paramStr') is not None:
            self.param_str = m.get('paramStr')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
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


class CreateOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOrderResponseBody = None,
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
            temp_model = CreateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCashDetailResponseBody(TeaModel):
    def __init__(
        self,
        amount_owed: str = None,
        available_credit: str = None,
        balance_amount: str = None,
        credit_card_amount: str = None,
        credit_limit: str = None,
        enable_threshold_alert: str = None,
        frozen_amount: str = None,
        mini_alert_threshold: int = None,
        remmitance_amount: str = None,
        request_id: str = None,
    ):
        self.amount_owed = amount_owed
        self.available_credit = available_credit
        self.balance_amount = balance_amount
        self.credit_card_amount = credit_card_amount
        self.credit_limit = credit_limit
        self.enable_threshold_alert = enable_threshold_alert
        self.frozen_amount = frozen_amount
        self.mini_alert_threshold = mini_alert_threshold
        self.remmitance_amount = remmitance_amount
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount_owed is not None:
            result['AmountOwed'] = self.amount_owed
        if self.available_credit is not None:
            result['AvailableCredit'] = self.available_credit
        if self.balance_amount is not None:
            result['BalanceAmount'] = self.balance_amount
        if self.credit_card_amount is not None:
            result['CreditCardAmount'] = self.credit_card_amount
        if self.credit_limit is not None:
            result['CreditLimit'] = self.credit_limit
        if self.enable_threshold_alert is not None:
            result['EnableThresholdAlert'] = self.enable_threshold_alert
        if self.frozen_amount is not None:
            result['FrozenAmount'] = self.frozen_amount
        if self.mini_alert_threshold is not None:
            result['MiniAlertThreshold'] = self.mini_alert_threshold
        if self.remmitance_amount is not None:
            result['RemmitanceAmount'] = self.remmitance_amount
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AmountOwed') is not None:
            self.amount_owed = m.get('AmountOwed')
        if m.get('AvailableCredit') is not None:
            self.available_credit = m.get('AvailableCredit')
        if m.get('BalanceAmount') is not None:
            self.balance_amount = m.get('BalanceAmount')
        if m.get('CreditCardAmount') is not None:
            self.credit_card_amount = m.get('CreditCardAmount')
        if m.get('CreditLimit') is not None:
            self.credit_limit = m.get('CreditLimit')
        if m.get('EnableThresholdAlert') is not None:
            self.enable_threshold_alert = m.get('EnableThresholdAlert')
        if m.get('FrozenAmount') is not None:
            self.frozen_amount = m.get('FrozenAmount')
        if m.get('MiniAlertThreshold') is not None:
            self.mini_alert_threshold = m.get('MiniAlertThreshold')
        if m.get('RemmitanceAmount') is not None:
            self.remmitance_amount = m.get('RemmitanceAmount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCashDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCashDetailResponseBody = None,
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
            temp_model = DescribeCashDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCouponListRequest(TeaModel):
    def __init__(
        self,
        end_delivery_time: str = None,
        page_num: int = None,
        page_size: int = None,
        start_delivery_time: str = None,
        status: str = None,
    ):
        self.end_delivery_time = end_delivery_time
        self.page_num = page_num
        self.page_size = page_size
        self.start_delivery_time = start_delivery_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_delivery_time is not None:
            result['EndDeliveryTime'] = self.end_delivery_time
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_delivery_time is not None:
            result['StartDeliveryTime'] = self.start_delivery_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDeliveryTime') is not None:
            self.end_delivery_time = m.get('EndDeliveryTime')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDeliveryTime') is not None:
            self.start_delivery_time = m.get('StartDeliveryTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCouponListResponseBodyCouponsCouponProductCodes(TeaModel):
    def __init__(
        self,
        product_code: List[str] = None,
    ):
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribeCouponListResponseBodyCouponsCouponTradeTypes(TeaModel):
    def __init__(
        self,
        trade_type: List[str] = None,
    ):
        self.trade_type = trade_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trade_type is not None:
            result['TradeType'] = self.trade_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TradeType') is not None:
            self.trade_type = m.get('TradeType')
        return self


class DescribeCouponListResponseBodyCouponsCoupon(TeaModel):
    def __init__(
        self,
        application: str = None,
        balance_amount: str = None,
        coupon_number: str = None,
        coupon_template_id: int = None,
        creation_time: str = None,
        delivery_time: str = None,
        description: str = None,
        expired_amount: str = None,
        expired_time: str = None,
        frozen_amount: str = None,
        modification_time: str = None,
        price_limit: str = None,
        product_codes: DescribeCouponListResponseBodyCouponsCouponProductCodes = None,
        status: str = None,
        total_amount: str = None,
        trade_types: DescribeCouponListResponseBodyCouponsCouponTradeTypes = None,
    ):
        self.application = application
        self.balance_amount = balance_amount
        self.coupon_number = coupon_number
        self.coupon_template_id = coupon_template_id
        self.creation_time = creation_time
        self.delivery_time = delivery_time
        self.description = description
        self.expired_amount = expired_amount
        self.expired_time = expired_time
        self.frozen_amount = frozen_amount
        self.modification_time = modification_time
        self.price_limit = price_limit
        self.product_codes = product_codes
        self.status = status
        self.total_amount = total_amount
        self.trade_types = trade_types

    def validate(self):
        if self.product_codes:
            self.product_codes.validate()
        if self.trade_types:
            self.trade_types.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application
        if self.balance_amount is not None:
            result['BalanceAmount'] = self.balance_amount
        if self.coupon_number is not None:
            result['CouponNumber'] = self.coupon_number
        if self.coupon_template_id is not None:
            result['CouponTemplateId'] = self.coupon_template_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_amount is not None:
            result['ExpiredAmount'] = self.expired_amount
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.frozen_amount is not None:
            result['FrozenAmount'] = self.frozen_amount
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        if self.product_codes is not None:
            result['ProductCodes'] = self.product_codes.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount
        if self.trade_types is not None:
            result['TradeTypes'] = self.trade_types.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            self.application = m.get('Application')
        if m.get('BalanceAmount') is not None:
            self.balance_amount = m.get('BalanceAmount')
        if m.get('CouponNumber') is not None:
            self.coupon_number = m.get('CouponNumber')
        if m.get('CouponTemplateId') is not None:
            self.coupon_template_id = m.get('CouponTemplateId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredAmount') is not None:
            self.expired_amount = m.get('ExpiredAmount')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FrozenAmount') is not None:
            self.frozen_amount = m.get('FrozenAmount')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        if m.get('ProductCodes') is not None:
            temp_model = DescribeCouponListResponseBodyCouponsCouponProductCodes()
            self.product_codes = temp_model.from_map(m['ProductCodes'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')
        if m.get('TradeTypes') is not None:
            temp_model = DescribeCouponListResponseBodyCouponsCouponTradeTypes()
            self.trade_types = temp_model.from_map(m['TradeTypes'])
        return self


class DescribeCouponListResponseBodyCoupons(TeaModel):
    def __init__(
        self,
        coupon: List[DescribeCouponListResponseBodyCouponsCoupon] = None,
    ):
        self.coupon = coupon

    def validate(self):
        if self.coupon:
            for k in self.coupon:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Coupon'] = []
        if self.coupon is not None:
            for k in self.coupon:
                result['Coupon'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.coupon = []
        if m.get('Coupon') is not None:
            for k in m.get('Coupon'):
                temp_model = DescribeCouponListResponseBodyCouponsCoupon()
                self.coupon.append(temp_model.from_map(k))
        return self


class DescribeCouponListResponseBody(TeaModel):
    def __init__(
        self,
        coupons: DescribeCouponListResponseBodyCoupons = None,
        request_id: str = None,
    ):
        self.coupons = coupons
        self.request_id = request_id

    def validate(self):
        if self.coupons:
            self.coupons.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupons is not None:
            result['Coupons'] = self.coupons.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coupons') is not None:
            temp_model = DescribeCouponListResponseBodyCoupons()
            self.coupons = temp_model.from_map(m['Coupons'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCouponListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCouponListResponseBody = None,
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
            temp_model = DescribeCouponListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenCallbackRequest(TeaModel):
    def __init__(
        self,
        param_str: str = None,
    ):
        # This parameter is required.
        self.param_str = param_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_str is not None:
            result['paramStr'] = self.param_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('paramStr') is not None:
            self.param_str = m.get('paramStr')
        return self


class OpenCallbackResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
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


class OpenCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenCallbackResponseBody = None,
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
            temp_model = OpenCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryForCssOrderRequest(TeaModel):
    def __init__(
        self,
        param_str: str = None,
    ):
        # This parameter is required.
        self.param_str = param_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_str is not None:
            result['paramStr'] = self.param_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('paramStr') is not None:
            self.param_str = m.get('paramStr')
        return self


class QueryForCssOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
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


class QueryForCssOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryForCssOrderResponseBody = None,
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
            temp_model = QueryForCssOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VnoBatchRefundOrderRequest(TeaModel):
    def __init__(
        self,
        param_str: str = None,
    ):
        # This parameter is required.
        self.param_str = param_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_str is not None:
            result['paramStr'] = self.param_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('paramStr') is not None:
            self.param_str = m.get('paramStr')
        return self


class VnoBatchRefundOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
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


class VnoBatchRefundOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VnoBatchRefundOrderResponseBody = None,
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
            temp_model = VnoBatchRefundOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


