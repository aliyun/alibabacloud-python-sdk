# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterPriceResponseBody(DaraModel):
    def __init__(
        self,
        order_type: str = None,
        price_info: main_models.DescribeDBClusterPriceResponseBodyPriceInfo = None,
        request_id: str = None,
        rules: main_models.DescribeDBClusterPriceResponseBodyRules = None,
        show_discount: bool = None,
    ):
        # The order type. Valid values:
        # * BUY: new purchase.
        # * UPGRADE: specification change.
        # * RENEW: renewal.
        # * CONVERT: billing method conversion.
        self.order_type = order_type
        # The price details.
        self.price_info = price_info
        # The request ID.
        self.request_id = request_id
        self.rules = rules
        # Indicates whether discounts are allowed.
        self.show_discount = show_discount

    def validate(self):
        if self.price_info:
            self.price_info.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        if self.show_discount is not None:
            result['ShowDiscount'] = self.show_discount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PriceInfo') is not None:
            temp_model = main_models.DescribeDBClusterPriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m.get('PriceInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rules') is not None:
            temp_model = main_models.DescribeDBClusterPriceResponseBodyRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        if m.get('ShowDiscount') is not None:
            self.show_discount = m.get('ShowDiscount')

        return self

class DescribeDBClusterPriceResponseBodyRules(DaraModel):
    def __init__(
        self,
        rule: List[main_models.DescribeDBClusterPriceResponseBodyRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for v1 in self.rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Rule'] = []
        if self.rule is not None:
            for k1 in self.rule:
                result['Rule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k1 in m.get('Rule'):
                temp_model = main_models.DescribeDBClusterPriceResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterPriceResponseBodyRulesRule(DaraModel):
    def __init__(
        self,
        name: str = None,
        rule_id: int = None,
    ):
        self.name = name
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

class DescribeDBClusterPriceResponseBodyPriceInfo(DaraModel):
    def __init__(
        self,
        coupons: main_models.DescribeDBClusterPriceResponseBodyPriceInfoCoupons = None,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        rule_ids: main_models.DescribeDBClusterPriceResponseBodyPriceInfoRuleIds = None,
        trade_price: float = None,
    ):
        self.coupons = coupons
        # The currency unit.
        self.currency = currency
        # The discount amount.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        self.rule_ids = rule_ids
        # The final price, which is the original price minus the discount.
        self.trade_price = trade_price

    def validate(self):
        if self.coupons:
            self.coupons.validate()
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coupons is not None:
            result['Coupons'] = self.coupons.to_map()

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coupons') is not None:
            temp_model = main_models.DescribeDBClusterPriceResponseBodyPriceInfoCoupons()
            self.coupons = temp_model.from_map(m.get('Coupons'))

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('RuleIds') is not None:
            temp_model = main_models.DescribeDBClusterPriceResponseBodyPriceInfoRuleIds()
            self.rule_ids = temp_model.from_map(m.get('RuleIds'))

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribeDBClusterPriceResponseBodyPriceInfoRuleIds(DaraModel):
    def __init__(
        self,
        rule_id: List[str] = None,
    ):
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

class DescribeDBClusterPriceResponseBodyPriceInfoCoupons(DaraModel):
    def __init__(
        self,
        coupon: List[main_models.DescribeDBClusterPriceResponseBodyPriceInfoCouponsCoupon] = None,
    ):
        self.coupon = coupon

    def validate(self):
        if self.coupon:
            for v1 in self.coupon:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Coupon'] = []
        if self.coupon is not None:
            for k1 in self.coupon:
                result['Coupon'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.coupon = []
        if m.get('Coupon') is not None:
            for k1 in m.get('Coupon'):
                temp_model = main_models.DescribeDBClusterPriceResponseBodyPriceInfoCouponsCoupon()
                self.coupon.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterPriceResponseBodyPriceInfoCouponsCoupon(DaraModel):
    def __init__(
        self,
        coupon_no: str = None,
        is_selected: str = None,
        name: str = None,
    ):
        self.coupon_no = coupon_no
        self.is_selected = is_selected
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

