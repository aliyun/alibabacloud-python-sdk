# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribePriceResponseBody(DaraModel):
    def __init__(
        self,
        order_params: str = None,
        price_info: main_models.DescribePriceResponseBodyPriceInfo = None,
        request_id: str = None,
        rules: main_models.DescribePriceResponseBodyRules = None,
        serverless_price: main_models.DescribePriceResponseBodyServerlessPrice = None,
        show_discount: bool = None,
        trade_max_rcuamount: float = None,
        trade_min_rcuamount: float = None,
    ):
        # The order parameters.
        # 
        # >  If the **OrderParamOut** parameter is set to **true**, the value of the OrderParams parameter is returned.
        self.order_params = order_params
        # The price information.
        self.price_info = price_info
        # The ID of the request.
        self.request_id = request_id
        # The details of the promotion rule.
        self.rules = rules
        # The pricing information about a serverless RDS instance.
        self.serverless_price = serverless_price
        # Indicates whether discounts can be used.
        self.show_discount = show_discount
        # The estimated hourly fee that is calculated based on the maximum number of RCUs.
        self.trade_max_rcuamount = trade_max_rcuamount
        # The estimated hourly fee that is calculated based on the minimum number of RCUs.
        self.trade_min_rcuamount = trade_min_rcuamount

    def validate(self):
        if self.price_info:
            self.price_info.validate()
        if self.rules:
            self.rules.validate()
        if self.serverless_price:
            self.serverless_price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_params is not None:
            result['OrderParams'] = self.order_params

        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        if self.serverless_price is not None:
            result['ServerlessPrice'] = self.serverless_price.to_map()

        if self.show_discount is not None:
            result['ShowDiscount'] = self.show_discount

        if self.trade_max_rcuamount is not None:
            result['TradeMaxRCUAmount'] = self.trade_max_rcuamount

        if self.trade_min_rcuamount is not None:
            result['TradeMinRCUAmount'] = self.trade_min_rcuamount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderParams') is not None:
            self.order_params = m.get('OrderParams')

        if m.get('PriceInfo') is not None:
            temp_model = main_models.DescribePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m.get('PriceInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rules') is not None:
            temp_model = main_models.DescribePriceResponseBodyRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        if m.get('ServerlessPrice') is not None:
            temp_model = main_models.DescribePriceResponseBodyServerlessPrice()
            self.serverless_price = temp_model.from_map(m.get('ServerlessPrice'))

        if m.get('ShowDiscount') is not None:
            self.show_discount = m.get('ShowDiscount')

        if m.get('TradeMaxRCUAmount') is not None:
            self.trade_max_rcuamount = m.get('TradeMaxRCUAmount')

        if m.get('TradeMinRCUAmount') is not None:
            self.trade_min_rcuamount = m.get('TradeMinRCUAmount')

        return self

class DescribePriceResponseBodyServerlessPrice(DaraModel):
    def __init__(
        self,
        rcudiscount_max_amount: float = None,
        rcudiscount_min_amount: float = None,
        rcuoriginal_max_amount: float = None,
        rcuoriginal_min_amount: float = None,
        storage_original_amount: float = None,
        total_original_max_amount: float = None,
        total_original_min_amount: float = None,
        trade_max_rcuamount: float = None,
        trade_min_rcuamount: float = None,
        storage_discount_amount: float = None,
    ):
        # The discount amount of the maximum number of RCUs.
        self.rcudiscount_max_amount = rcudiscount_max_amount
        # The discount amount of the minimum number of RCUs.
        self.rcudiscount_min_amount = rcudiscount_min_amount
        # The price of the maximum number of RCUs.
        self.rcuoriginal_max_amount = rcuoriginal_max_amount
        # The price of the minimum number of RCUs.
        self.rcuoriginal_min_amount = rcuoriginal_min_amount
        # The original price of the disk capacity.
        self.storage_original_amount = storage_original_amount
        # The maximum total price before the discount.
        self.total_original_max_amount = total_original_max_amount
        # The minimum total price before the discount.
        self.total_original_min_amount = total_original_min_amount
        # The transaction price of the maximum number of RCUs.
        self.trade_max_rcuamount = trade_max_rcuamount
        # The transaction price of the minimum number of RCUs.
        self.trade_min_rcuamount = trade_min_rcuamount
        # The discounted price of the disk capacity.
        self.storage_discount_amount = storage_discount_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rcudiscount_max_amount is not None:
            result['RCUDiscountMaxAmount'] = self.rcudiscount_max_amount

        if self.rcudiscount_min_amount is not None:
            result['RCUDiscountMinAmount'] = self.rcudiscount_min_amount

        if self.rcuoriginal_max_amount is not None:
            result['RCUOriginalMaxAmount'] = self.rcuoriginal_max_amount

        if self.rcuoriginal_min_amount is not None:
            result['RCUOriginalMinAmount'] = self.rcuoriginal_min_amount

        if self.storage_original_amount is not None:
            result['StorageOriginalAmount'] = self.storage_original_amount

        if self.total_original_max_amount is not None:
            result['TotalOriginalMaxAmount'] = self.total_original_max_amount

        if self.total_original_min_amount is not None:
            result['TotalOriginalMinAmount'] = self.total_original_min_amount

        if self.trade_max_rcuamount is not None:
            result['TradeMaxRCUAmount'] = self.trade_max_rcuamount

        if self.trade_min_rcuamount is not None:
            result['TradeMinRCUAmount'] = self.trade_min_rcuamount

        if self.storage_discount_amount is not None:
            result['storageDiscountAmount'] = self.storage_discount_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RCUDiscountMaxAmount') is not None:
            self.rcudiscount_max_amount = m.get('RCUDiscountMaxAmount')

        if m.get('RCUDiscountMinAmount') is not None:
            self.rcudiscount_min_amount = m.get('RCUDiscountMinAmount')

        if m.get('RCUOriginalMaxAmount') is not None:
            self.rcuoriginal_max_amount = m.get('RCUOriginalMaxAmount')

        if m.get('RCUOriginalMinAmount') is not None:
            self.rcuoriginal_min_amount = m.get('RCUOriginalMinAmount')

        if m.get('StorageOriginalAmount') is not None:
            self.storage_original_amount = m.get('StorageOriginalAmount')

        if m.get('TotalOriginalMaxAmount') is not None:
            self.total_original_max_amount = m.get('TotalOriginalMaxAmount')

        if m.get('TotalOriginalMinAmount') is not None:
            self.total_original_min_amount = m.get('TotalOriginalMinAmount')

        if m.get('TradeMaxRCUAmount') is not None:
            self.trade_max_rcuamount = m.get('TradeMaxRCUAmount')

        if m.get('TradeMinRCUAmount') is not None:
            self.trade_min_rcuamount = m.get('TradeMinRCUAmount')

        if m.get('storageDiscountAmount') is not None:
            self.storage_discount_amount = m.get('storageDiscountAmount')

        return self

class DescribePriceResponseBodyRules(DaraModel):
    def __init__(
        self,
        rule: List[main_models.DescribePriceResponseBodyRulesRule] = None,
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
                temp_model = main_models.DescribePriceResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodyRulesRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        rule_id: int = None,
    ):
        # The description of the promotion rule.
        self.description = description
        # The name of the promotion rule.
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

class DescribePriceResponseBodyPriceInfo(DaraModel):
    def __init__(
        self,
        activity_info: main_models.DescribePriceResponseBodyPriceInfoActivityInfo = None,
        coupons: main_models.DescribePriceResponseBodyPriceInfoCoupons = None,
        currency: str = None,
        discount_price: float = None,
        order_lines: Any = None,
        original_price: float = None,
        rule_ids: main_models.DescribePriceResponseBodyPriceInfoRuleIds = None,
        trade_max_rcuamount: float = None,
        trade_min_rcuamount: float = None,
        trade_price: float = None,
    ):
        # The information about the promotion.
        self.activity_info = activity_info
        # The information about the coupon.
        self.coupons = coupons
        # The currency unit.
        self.currency = currency
        # The discount.
        self.discount_price = discount_price
        # The order information.
        self.order_lines = order_lines
        # The original price.
        self.original_price = original_price
        # An array that consists of the ID of the promotion rule.
        self.rule_ids = rule_ids
        # The estimated hourly cost that is calculated based on the maximum number of RCUs you specify.
        self.trade_max_rcuamount = trade_max_rcuamount
        # The estimated hourly cost that is calculated based on the minimum number of RCUs you specify.
        self.trade_min_rcuamount = trade_min_rcuamount
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

        if self.order_lines is not None:
            result['OrderLines'] = self.order_lines

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()

        if self.trade_max_rcuamount is not None:
            result['TradeMaxRCUAmount'] = self.trade_max_rcuamount

        if self.trade_min_rcuamount is not None:
            result['TradeMinRCUAmount'] = self.trade_min_rcuamount

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityInfo') is not None:
            temp_model = main_models.DescribePriceResponseBodyPriceInfoActivityInfo()
            self.activity_info = temp_model.from_map(m.get('ActivityInfo'))

        if m.get('Coupons') is not None:
            temp_model = main_models.DescribePriceResponseBodyPriceInfoCoupons()
            self.coupons = temp_model.from_map(m.get('Coupons'))

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('OrderLines') is not None:
            self.order_lines = m.get('OrderLines')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('RuleIds') is not None:
            temp_model = main_models.DescribePriceResponseBodyPriceInfoRuleIds()
            self.rule_ids = temp_model.from_map(m.get('RuleIds'))

        if m.get('TradeMaxRCUAmount') is not None:
            self.trade_max_rcuamount = m.get('TradeMaxRCUAmount')

        if m.get('TradeMinRCUAmount') is not None:
            self.trade_min_rcuamount = m.get('TradeMinRCUAmount')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribePriceResponseBodyPriceInfoRuleIds(DaraModel):
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

class DescribePriceResponseBodyPriceInfoCoupons(DaraModel):
    def __init__(
        self,
        coupon: List[main_models.DescribePriceResponseBodyPriceInfoCouponsCoupon] = None,
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
                temp_model = main_models.DescribePriceResponseBodyPriceInfoCouponsCoupon()
                self.coupon.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodyPriceInfoCouponsCoupon(DaraModel):
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
        # The coupon name.
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

class DescribePriceResponseBodyPriceInfoActivityInfo(DaraModel):
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

