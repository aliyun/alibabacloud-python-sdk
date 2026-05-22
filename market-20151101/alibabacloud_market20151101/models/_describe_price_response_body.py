# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribePriceResponseBody(DaraModel):
    def __init__(
        self,
        coupons: main_models.DescribePriceResponseBodyCoupons = None,
        currency: str = None,
        cuxiao: bool = None,
        cycle: str = None,
        discount_price: float = None,
        duration: int = None,
        expression_code: str = None,
        expression_message: str = None,
        info_title: str = None,
        original_price: float = None,
        product_code: str = None,
        promotion_rules: main_models.DescribePriceResponseBodyPromotionRules = None,
        trade_price: float = None,
    ):
        self.coupons = coupons
        self.currency = currency
        self.cuxiao = cuxiao
        self.cycle = cycle
        self.discount_price = discount_price
        self.duration = duration
        self.expression_code = expression_code
        self.expression_message = expression_message
        self.info_title = info_title
        self.original_price = original_price
        self.product_code = product_code
        self.promotion_rules = promotion_rules
        self.trade_price = trade_price

    def validate(self):
        if self.coupons:
            self.coupons.validate()
        if self.promotion_rules:
            self.promotion_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coupons is not None:
            result['Coupons'] = self.coupons.to_map()

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

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.promotion_rules is not None:
            result['PromotionRules'] = self.promotion_rules.to_map()

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coupons') is not None:
            temp_model = main_models.DescribePriceResponseBodyCoupons()
            self.coupons = temp_model.from_map(m.get('Coupons'))

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

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('PromotionRules') is not None:
            temp_model = main_models.DescribePriceResponseBodyPromotionRules()
            self.promotion_rules = temp_model.from_map(m.get('PromotionRules'))

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribePriceResponseBodyPromotionRules(DaraModel):
    def __init__(
        self,
        promotion_rule: List[main_models.DescribePriceResponseBodyPromotionRulesPromotionRule] = None,
    ):
        self.promotion_rule = promotion_rule

    def validate(self):
        if self.promotion_rule:
            for v1 in self.promotion_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PromotionRule'] = []
        if self.promotion_rule is not None:
            for k1 in self.promotion_rule:
                result['PromotionRule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.promotion_rule = []
        if m.get('PromotionRule') is not None:
            for k1 in m.get('PromotionRule'):
                temp_model = main_models.DescribePriceResponseBodyPromotionRulesPromotionRule()
                self.promotion_rule.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodyPromotionRulesPromotionRule(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribePriceResponseBodyCoupons(DaraModel):
    def __init__(
        self,
        coupon: List[main_models.DescribePriceResponseBodyCouponsCoupon] = None,
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
                temp_model = main_models.DescribePriceResponseBodyCouponsCoupon()
                self.coupon.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodyCouponsCoupon(DaraModel):
    def __init__(
        self,
        can_prom_fee: float = None,
        coupon_desc: str = None,
        coupon_name: str = None,
        coupon_option_code: str = None,
        coupon_option_no: str = None,
        is_selected: bool = None,
    ):
        self.can_prom_fee = can_prom_fee
        self.coupon_desc = coupon_desc
        self.coupon_name = coupon_name
        self.coupon_option_code = coupon_option_code
        self.coupon_option_no = coupon_option_no
        self.is_selected = is_selected

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        return self

