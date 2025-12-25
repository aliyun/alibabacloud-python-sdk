# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_foasconsole20190601 import models as main_models
from darabonba.model import DaraModel

class QueryConvertInstancePriceResponseBody(DaraModel):
    def __init__(
        self,
        price_info: main_models.QueryConvertInstancePriceResponseBodyPriceInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.price_info = price_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = main_models.QueryConvertInstancePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m.get('PriceInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryConvertInstancePriceResponseBodyPriceInfo(DaraModel):
    def __init__(
        self,
        code: str = None,
        currency: str = None,
        depreciate_info: main_models.QueryConvertInstancePriceResponseBodyPriceInfoDepreciateInfo = None,
        discount_amount: float = None,
        is_contract_activity: bool = None,
        lx_request_id: str = None,
        message: str = None,
        optional_promotions: List[main_models.QueryConvertInstancePriceResponseBodyPriceInfoOptionalPromotions] = None,
        original_amount: float = None,
        rules: List[main_models.QueryConvertInstancePriceResponseBodyPriceInfoRules] = None,
        stand_discount_price: str = None,
        stand_price: str = None,
        trade_amount: float = None,
    ):
        self.code = code
        self.currency = currency
        self.depreciate_info = depreciate_info
        self.discount_amount = discount_amount
        self.is_contract_activity = is_contract_activity
        self.lx_request_id = lx_request_id
        self.message = message
        self.optional_promotions = optional_promotions
        self.original_amount = original_amount
        self.rules = rules
        self.stand_discount_price = stand_discount_price
        self.stand_price = stand_price
        self.trade_amount = trade_amount

    def validate(self):
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
        if self.code is not None:
            result['Code'] = self.code

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.depreciate_info is not None:
            result['DepreciateInfo'] = self.depreciate_info.to_map()

        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        if self.is_contract_activity is not None:
            result['IsContractActivity'] = self.is_contract_activity

        if self.lx_request_id is not None:
            result['LxRequestId'] = self.lx_request_id

        if self.message is not None:
            result['Message'] = self.message

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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DepreciateInfo') is not None:
            temp_model = main_models.QueryConvertInstancePriceResponseBodyPriceInfoDepreciateInfo()
            self.depreciate_info = temp_model.from_map(m.get('DepreciateInfo'))

        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        if m.get('IsContractActivity') is not None:
            self.is_contract_activity = m.get('IsContractActivity')

        if m.get('LxRequestId') is not None:
            self.lx_request_id = m.get('LxRequestId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.optional_promotions = []
        if m.get('OptionalPromotions') is not None:
            for k1 in m.get('OptionalPromotions'):
                temp_model = main_models.QueryConvertInstancePriceResponseBodyPriceInfoOptionalPromotions()
                self.optional_promotions.append(temp_model.from_map(k1))

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.QueryConvertInstancePriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('StandDiscountPrice') is not None:
            self.stand_discount_price = m.get('StandDiscountPrice')

        if m.get('StandPrice') is not None:
            self.stand_price = m.get('StandPrice')

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

class QueryConvertInstancePriceResponseBodyPriceInfoRules(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class QueryConvertInstancePriceResponseBodyPriceInfoOptionalPromotions(DaraModel):
    def __init__(
        self,
        promotion_desc: str = None,
        promotion_name: str = None,
        promotion_option_no: str = None,
        selected: bool = None,
    ):
        self.promotion_desc = promotion_desc
        self.promotion_name = promotion_name
        self.promotion_option_no = promotion_option_no
        self.selected = selected

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

        if self.selected is not None:
            result['Selected'] = self.selected

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')

        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('Selected') is not None:
            self.selected = m.get('Selected')

        return self

class QueryConvertInstancePriceResponseBodyPriceInfoDepreciateInfo(DaraModel):
    def __init__(
        self,
        cheap_rate: str = None,
        cheap_stand_amount: str = None,
        is_show: bool = None,
        month_price: str = None,
        original_stand_amount: str = None,
        start_time: str = None,
    ):
        self.cheap_rate = cheap_rate
        self.cheap_stand_amount = cheap_stand_amount
        self.is_show = is_show
        self.month_price = month_price
        self.original_stand_amount = original_stand_amount
        self.start_time = start_time

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

        if self.month_price is not None:
            result['MonthPrice'] = self.month_price

        if self.original_stand_amount is not None:
            result['OriginalStandAmount'] = self.original_stand_amount

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheapRate') is not None:
            self.cheap_rate = m.get('CheapRate')

        if m.get('CheapStandAmount') is not None:
            self.cheap_stand_amount = m.get('CheapStandAmount')

        if m.get('IsShow') is not None:
            self.is_show = m.get('IsShow')

        if m.get('MonthPrice') is not None:
            self.month_price = m.get('MonthPrice')

        if m.get('OriginalStandAmount') is not None:
            self.original_stand_amount = m.get('OriginalStandAmount')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

