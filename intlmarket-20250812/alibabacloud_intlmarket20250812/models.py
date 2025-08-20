# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity: str = None,
        order_souce: str = None,
        order_type: str = None,
        owner_id: str = None,
        payment_type: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.commodity = commodity
        self.order_souce = order_souce
        # This parameter is required.
        self.order_type = order_type
        self.owner_id = owner_id
        # This parameter is required.
        self.payment_type = payment_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity is not None:
            result['Commodity'] = self.commodity
        if self.order_souce is not None:
            result['OrderSouce'] = self.order_souce
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')
        if m.get('OrderSouce') is not None:
            self.order_souce = m.get('OrderSouce')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribePriceRequest(TeaModel):
    def __init__(
        self,
        commodity: str = None,
        order_type: str = None,
    ):
        self.commodity = commodity
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity is not None:
            result['Commodity'] = self.commodity
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class DescribePriceResponseBodyCoupons(TeaModel):
    def __init__(
        self,
        can_prom_fee: int = None,
        coupon_desc: str = None,
        coupon_name: str = None,
        coupon_option_code: str = None,
        coupon_option_no: str = None,
        is_selected: bool = None,
        promotion_desc: str = None,
    ):
        self.can_prom_fee = can_prom_fee
        self.coupon_desc = coupon_desc
        self.coupon_name = coupon_name
        self.coupon_option_code = coupon_option_code
        self.coupon_option_no = coupon_option_no
        self.is_selected = is_selected
        self.promotion_desc = promotion_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_prom_fee is not None:
            result['CanPromFee'] = self.can_prom_fee
        if self.coupon_desc is not None:
            result['CouponDesc'] = self.coupon_desc
        if self.coupon_name is not None:
            result['CouponName'] = self.coupon_name
        if self.coupon_option_code is not None:
            result['CouponOptionCode'] = self.coupon_option_code
        if self.coupon_option_no is not None:
            result['CouponOptionNo'] = self.coupon_option_no
        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanPromFee') is not None:
            self.can_prom_fee = m.get('CanPromFee')
        if m.get('CouponDesc') is not None:
            self.coupon_desc = m.get('CouponDesc')
        if m.get('CouponName') is not None:
            self.coupon_name = m.get('CouponName')
        if m.get('CouponOptionCode') is not None:
            self.coupon_option_code = m.get('CouponOptionCode')
        if m.get('CouponOptionNo') is not None:
            self.coupon_option_no = m.get('CouponOptionNo')
        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        return self


class DescribePriceResponseBodyPromotionRules(TeaModel):
    def __init__(
        self,
        name: str = None,
        rule_id: str = None,
        title: str = None,
    ):
        self.name = name
        self.rule_id = rule_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribePriceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        coupons: List[DescribePriceResponseBodyCoupons] = None,
        currency: str = None,
        cuxiao: bool = None,
        cycle: str = None,
        discount_price: float = None,
        duration: int = None,
        expression_code: str = None,
        expression_message: str = None,
        info_title: str = None,
        message: str = None,
        original_price: float = None,
        product_code: str = None,
        promotion_rules: List[DescribePriceResponseBodyPromotionRules] = None,
        request_id: str = None,
        trade_price: float = None,
    ):
        self.code = code
        self.coupons = coupons
        self.currency = currency
        self.cuxiao = cuxiao
        self.cycle = cycle
        self.discount_price = discount_price
        self.duration = duration
        self.expression_code = expression_code
        self.expression_message = expression_message
        self.info_title = info_title
        self.message = message
        self.original_price = original_price
        self.product_code = product_code
        self.promotion_rules = promotion_rules
        self.request_id = request_id
        self.trade_price = trade_price

    def validate(self):
        if self.coupons:
            for k in self.coupons:
                if k:
                    k.validate()
        if self.promotion_rules:
            for k in self.promotion_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Coupons'] = []
        if self.coupons is not None:
            for k in self.coupons:
                result['Coupons'].append(k.to_map() if k else None)
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.cuxiao is not None:
            result['Cuxiao'] = self.cuxiao
        if self.cycle is not None:
            result['Cycle'] = self.cycle
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression_code is not None:
            result['ExpressionCode'] = self.expression_code
        if self.expression_message is not None:
            result['ExpressionMessage'] = self.expression_message
        if self.info_title is not None:
            result['InfoTitle'] = self.info_title
        if self.message is not None:
            result['Message'] = self.message
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        result['PromotionRules'] = []
        if self.promotion_rules is not None:
            for k in self.promotion_rules:
                result['PromotionRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.coupons = []
        if m.get('Coupons') is not None:
            for k in m.get('Coupons'):
                temp_model = DescribePriceResponseBodyCoupons()
                self.coupons.append(temp_model.from_map(k))
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Cuxiao') is not None:
            self.cuxiao = m.get('Cuxiao')
        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpressionCode') is not None:
            self.expression_code = m.get('ExpressionCode')
        if m.get('ExpressionMessage') is not None:
            self.expression_message = m.get('ExpressionMessage')
        if m.get('InfoTitle') is not None:
            self.info_title = m.get('InfoTitle')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        self.promotion_rules = []
        if m.get('PromotionRules') is not None:
            for k in m.get('PromotionRules'):
                temp_model = DescribePriceResponseBodyPromotionRules()
                self.promotion_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePriceResponseBody = None,
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
            temp_model = DescribePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


