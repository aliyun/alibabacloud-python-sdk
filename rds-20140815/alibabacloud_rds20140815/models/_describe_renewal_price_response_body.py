# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRenewalPriceResponseBody(DaraModel):
    def __init__(
        self,
        price_info: main_models.DescribeRenewalPriceResponseBodyPriceInfo = None,
        request_id: str = None,
        rules: main_models.DescribeRenewalPriceResponseBodyRules = None,
    ):
        # Details of price information.
        self.price_info = price_info
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of the details of the promotion rule.
        self.rules = rules

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
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m.get('PriceInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rules') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodyRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        return self

class DescribeRenewalPriceResponseBodyRules(DaraModel):
    def __init__(
        self,
        rule: List[main_models.DescribeRenewalPriceResponseBodyRulesRule] = None,
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
                temp_model = main_models.DescribeRenewalPriceResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class DescribeRenewalPriceResponseBodyRulesRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        rule_id: int = None,
    ):
        # The description of the activity.
        self.description = description
        # The name of the rule.
        self.name = name
        # The ID of the promotion rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

class DescribeRenewalPriceResponseBodyPriceInfo(DaraModel):
    def __init__(
        self,
        activity_info: main_models.DescribeRenewalPriceResponseBodyPriceInfoActivityInfo = None,
        coupons: main_models.DescribeRenewalPriceResponseBodyPriceInfoCoupons = None,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        rule_ids: main_models.DescribeRenewalPriceResponseBodyPriceInfoRuleIds = None,
        trade_price: float = None,
    ):
        # The information about the promotion.
        self.activity_info = activity_info
        # An array that consists of information about the coupon.
        self.coupons = coupons
        # The currency unit.
        self.currency = currency
        # The discount.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # An array that consists of the ID of the promotion rule.
        self.rule_ids = rule_ids
        # The transaction price, which is equal to the original price minus the discount.
        self.trade_price = trade_price

    def validate(self):
        if self.activity_info:
            self.activity_info.validate()
        if self.coupons:
            self.coupons.validate()
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_info is not None:
            result['ActivityInfo'] = self.activity_info.to_map()

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
        if m.get('ActivityInfo') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodyPriceInfoActivityInfo()
            self.activity_info = temp_model.from_map(m.get('ActivityInfo'))

        if m.get('Coupons') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodyPriceInfoCoupons()
            self.coupons = temp_model.from_map(m.get('Coupons'))

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('RuleIds') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodyPriceInfoRuleIds()
            self.rule_ids = temp_model.from_map(m.get('RuleIds'))

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribeRenewalPriceResponseBodyPriceInfoRuleIds(DaraModel):
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

class DescribeRenewalPriceResponseBodyPriceInfoCoupons(DaraModel):
    def __init__(
        self,
        coupon: List[main_models.DescribeRenewalPriceResponseBodyPriceInfoCouponsCoupon] = None,
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
                temp_model = main_models.DescribeRenewalPriceResponseBodyPriceInfoCouponsCoupon()
                self.coupon.append(temp_model.from_map(k1))

        return self

class DescribeRenewalPriceResponseBodyPriceInfoCouponsCoupon(DaraModel):
    def __init__(
        self,
        coupon_no: str = None,
        description: str = None,
        is_selected: str = None,
        name: str = None,
    ):
        # The coupon ID.
        self.coupon_no = coupon_no
        # The description of the coupon.
        self.description = description
        # Indicates whether the coupon is selected.
        self.is_selected = is_selected
        # The name of the coupon.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeRenewalPriceResponseBodyPriceInfoActivityInfo(DaraModel):
    def __init__(
        self,
        check_err_msg: str = None,
        error_code: str = None,
        success: str = None,
    ):
        # The returned message.
        self.check_err_msg = check_err_msg
        # The error code that is returned.
        self.error_code = error_code
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_err_msg is not None:
            result['CheckErrMsg'] = self.check_err_msg

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckErrMsg') is not None:
            self.check_err_msg = m.get('CheckErrMsg')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

