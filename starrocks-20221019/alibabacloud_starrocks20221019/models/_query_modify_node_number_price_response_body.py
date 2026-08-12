# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class QueryModifyNodeNumberPriceResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: main_models.QueryModifyNodeNumberPriceResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # AccessDeniedDetail
        self.access_denied_detail = access_denied_detail
        # The order information.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Data') is not None:
            temp_model = main_models.QueryModifyNodeNumberPriceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryModifyNodeNumberPriceResponseBodyData(DaraModel):
    def __init__(
        self,
        component_prices: List[main_models.QueryModifyNodeNumberPriceResponseBodyDataComponentPrices] = None,
        currency: str = None,
        depreciate_info: main_models.QueryModifyNodeNumberPriceResponseBodyDataDepreciateInfo = None,
        discount_amount: float = None,
        optional_promotions: List[main_models.QueryModifyNodeNumberPriceResponseBodyDataOptionalPromotions] = None,
        original_amount: float = None,
        rules: List[main_models.QueryModifyNodeNumberPriceResponseBodyDataRules] = None,
        stand_discount_price: float = None,
        stand_price: float = None,
        trade_amount: float = None,
    ):
        # The component prices.
        self.component_prices = component_prices
        # The currency. Valid values:
        # 
        # - CNY: Chinese Yuan.
        # 
        # - USD: US Dollar.
        # 
        # - JPY: Japanese Yen.
        self.currency = currency
        # The price reduction ratio.
        self.depreciate_info = depreciate_info
        # The discount amount is the difference between the original amount and the amount payable. The amount payable is the final cost after any coupon deductions.
        self.discount_amount = discount_amount
        # The coupon information.
        self.optional_promotions = optional_promotions
        # The original price. This is calculated as: List Price × Billable Usage.
        self.original_amount = original_amount
        # The returned data structure.
        self.rules = rules
        # The discounted price based on the official website discount.
        self.stand_discount_price = stand_discount_price
        # The official website discount price.
        self.stand_price = stand_price
        # The payable amount.
        self.trade_amount = trade_amount

    def validate(self):
        if self.component_prices:
            for v1 in self.component_prices:
                 if v1:
                    v1.validate()
        if self.depreciate_info:
            self.depreciate_info.validate()
        if self.optional_promotions:
            for v1 in self.optional_promotions:
                 if v1:
                    v1.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComponentPrices'] = []
        if self.component_prices is not None:
            for k1 in self.component_prices:
                result['ComponentPrices'].append(k1.to_map() if k1 else None)

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.depreciate_info is not None:
            result['DepreciateInfo'] = self.depreciate_info.to_map()

        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        result['OptionalPromotions'] = []
        if self.optional_promotions is not None:
            for k1 in self.optional_promotions:
                result['OptionalPromotions'].append(k1.to_map() if k1 else None)

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.stand_discount_price is not None:
            result['StandDiscountPrice'] = self.stand_discount_price

        if self.stand_price is not None:
            result['StandPrice'] = self.stand_price

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component_prices = []
        if m.get('ComponentPrices') is not None:
            for k1 in m.get('ComponentPrices'):
                temp_model = main_models.QueryModifyNodeNumberPriceResponseBodyDataComponentPrices()
                self.component_prices.append(temp_model.from_map(k1))

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DepreciateInfo') is not None:
            temp_model = main_models.QueryModifyNodeNumberPriceResponseBodyDataDepreciateInfo()
            self.depreciate_info = temp_model.from_map(m.get('DepreciateInfo'))

        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        self.optional_promotions = []
        if m.get('OptionalPromotions') is not None:
            for k1 in m.get('OptionalPromotions'):
                temp_model = main_models.QueryModifyNodeNumberPriceResponseBodyDataOptionalPromotions()
                self.optional_promotions.append(temp_model.from_map(k1))

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.QueryModifyNodeNumberPriceResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('StandDiscountPrice') is not None:
            self.stand_discount_price = m.get('StandDiscountPrice')

        if m.get('StandPrice') is not None:
            self.stand_price = m.get('StandPrice')

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

class QueryModifyNodeNumberPriceResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        amount: float = None,
        name: str = None,
        rule_desc_id: str = None,
    ):
        # The price for purchasing a batch of Elastic Compute Service (ECS) instances with a specific configuration. Valid values: 1 to 1000.
        # 
        # Default value: 1.
        self.amount = amount
        # The rule name.
        self.name = name
        # The rule ID.
        self.rule_desc_id = rule_desc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.name is not None:
            result['Name'] = self.name

        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')

        return self

class QueryModifyNodeNumberPriceResponseBodyDataOptionalPromotions(DaraModel):
    def __init__(
        self,
        promotion_desc: str = None,
        promotion_name: str = None,
        promotion_option_no: str = None,
    ):
        # The coupon description.
        self.promotion_desc = promotion_desc
        # The coupon name.
        self.promotion_name = promotion_name
        # The coupon ID.
        self.promotion_option_no = promotion_option_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc

        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')

        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        return self

class QueryModifyNodeNumberPriceResponseBodyDataDepreciateInfo(DaraModel):
    def __init__(
        self,
        cheap_rate: float = None,
        cheap_stand_amount: float = None,
        is_show: bool = None,
        original_stand_amount: float = None,
    ):
        # The price reduction ratio.
        self.cheap_rate = cheap_rate
        # The total price on the official website after the price reduction.
        self.cheap_stand_amount = cheap_stand_amount
        # Indicates whether to display the price reduction range.
        self.is_show = is_show
        # The original total price on the official website.
        self.original_stand_amount = original_stand_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cheap_rate is not None:
            result['CheapRate'] = self.cheap_rate

        if self.cheap_stand_amount is not None:
            result['CheapStandAmount'] = self.cheap_stand_amount

        if self.is_show is not None:
            result['IsShow'] = self.is_show

        if self.original_stand_amount is not None:
            result['OriginalStandAmount'] = self.original_stand_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheapRate') is not None:
            self.cheap_rate = m.get('CheapRate')

        if m.get('CheapStandAmount') is not None:
            self.cheap_stand_amount = m.get('CheapStandAmount')

        if m.get('IsShow') is not None:
            self.is_show = m.get('IsShow')

        if m.get('OriginalStandAmount') is not None:
            self.original_stand_amount = m.get('OriginalStandAmount')

        return self

class QueryModifyNodeNumberPriceResponseBodyDataComponentPrices(DaraModel):
    def __init__(
        self,
        component_name: str = None,
        discount_amount: float = None,
        original_amount: float = None,
        trade_amount: float = None,
    ):
        # The component name.
        self.component_name = component_name
        # The discount.
        self.discount_amount = discount_amount
        # The original price of the order.
        self.original_amount = original_amount
        # The actual transaction price of the order.
        self.trade_amount = trade_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

