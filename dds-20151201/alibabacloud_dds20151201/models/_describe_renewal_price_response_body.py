# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeRenewalPriceResponseBody(DaraModel):
    def __init__(
        self,
        order: main_models.DescribeRenewalPriceResponseBodyOrder = None,
        request_id: str = None,
        rules: main_models.DescribeRenewalPriceResponseBodyRules = None,
        sub_orders: main_models.DescribeRenewalPriceResponseBodySubOrders = None,
    ):
        # The list of orders.
        self.order = order
        # The ID of the request.
        self.request_id = request_id
        # Details about the promotion rules.
        self.rules = rules
        # The rules matching the coupons.
        self.sub_orders = sub_orders

    def validate(self):
        if self.order:
            self.order.validate()
        if self.rules:
            self.rules.validate()
        if self.sub_orders:
            self.sub_orders.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        if self.sub_orders is not None:
            result['SubOrders'] = self.sub_orders.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodyOrder()
            self.order = temp_model.from_map(m.get('Order'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rules') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodyRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        if m.get('SubOrders') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodySubOrders()
            self.sub_orders = temp_model.from_map(m.get('SubOrders'))

        return self

class DescribeRenewalPriceResponseBodySubOrders(DaraModel):
    def __init__(
        self,
        sub_order: List[main_models.DescribeRenewalPriceResponseBodySubOrdersSubOrder] = None,
    ):
        self.sub_order = sub_order

    def validate(self):
        if self.sub_order:
            for v1 in self.sub_order:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubOrder'] = []
        if self.sub_order is not None:
            for k1 in self.sub_order:
                result['SubOrder'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_order = []
        if m.get('SubOrder') is not None:
            for k1 in m.get('SubOrder'):
                temp_model = main_models.DescribeRenewalPriceResponseBodySubOrdersSubOrder()
                self.sub_order.append(temp_model.from_map(k1))

        return self

class DescribeRenewalPriceResponseBodySubOrdersSubOrder(DaraModel):
    def __init__(
        self,
        discount_amount: float = None,
        instance_id: str = None,
        original_amount: float = None,
        rule_ids: main_models.DescribeRenewalPriceResponseBodySubOrdersSubOrderRuleIds = None,
        trade_amount: float = None,
    ):
        # The discount amount of the order.
        self.discount_amount = discount_amount
        # The ID of the instance.
        self.instance_id = instance_id
        # The original price of the order.
        self.original_amount = original_amount
        # The IDs of the matched rules.
        self.rule_ids = rule_ids
        # The actual price of the order.
        self.trade_amount = trade_amount

    def validate(self):
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        if m.get('RuleIds') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodySubOrdersSubOrderRuleIds()
            self.rule_ids = temp_model.from_map(m.get('RuleIds'))

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

class DescribeRenewalPriceResponseBodySubOrdersSubOrderRuleIds(DaraModel):
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
        name: str = None,
        rule_desc_id: int = None,
        title: str = None,
    ):
        # The name of the rule.
        self.name = name
        # The ID of the rule.
        self.rule_desc_id = rule_desc_id
        # The title of the rule.
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

        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class DescribeRenewalPriceResponseBodyOrder(DaraModel):
    def __init__(
        self,
        coupons: main_models.DescribeRenewalPriceResponseBodyOrderCoupons = None,
        currency: str = None,
        discount_amount: float = None,
        original_amount: float = None,
        rule_ids: main_models.DescribeRenewalPriceResponseBodyOrderRuleIds = None,
        trade_amount: float = None,
    ):
        # Details about the coupons.
        self.coupons = coupons
        # The type of the currency. Valid values:
        # 
        # *   USD: United States dollar
        # *   JPY: Japanese Yen
        self.currency = currency
        # The discount amount of the order.
        self.discount_amount = discount_amount
        # The original price of the order.
        self.original_amount = original_amount
        # The IDs of the matched rules.
        self.rule_ids = rule_ids
        # The actual price of the order.
        self.trade_amount = trade_amount

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

        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coupons') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodyOrderCoupons()
            self.coupons = temp_model.from_map(m.get('Coupons'))

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        if m.get('RuleIds') is not None:
            temp_model = main_models.DescribeRenewalPriceResponseBodyOrderRuleIds()
            self.rule_ids = temp_model.from_map(m.get('RuleIds'))

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

class DescribeRenewalPriceResponseBodyOrderRuleIds(DaraModel):
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

class DescribeRenewalPriceResponseBodyOrderCoupons(DaraModel):
    def __init__(
        self,
        coupon: List[main_models.DescribeRenewalPriceResponseBodyOrderCouponsCoupon] = None,
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
                temp_model = main_models.DescribeRenewalPriceResponseBodyOrderCouponsCoupon()
                self.coupon.append(temp_model.from_map(k1))

        return self

class DescribeRenewalPriceResponseBodyOrderCouponsCoupon(DaraModel):
    def __init__(
        self,
        coupon_no: str = None,
        description: str = None,
        is_selected: str = None,
        name: str = None,
    ):
        # The coupon number.
        self.coupon_no = coupon_no
        # The description of the coupon.
        self.description = description
        # Indicates whether the coupon was selected.
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

