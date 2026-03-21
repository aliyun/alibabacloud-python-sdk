# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class DescribeMultiPriceResponseBody(DaraModel):
    def __init__(
        self,
        price_info: main_models.DescribeMultiPriceResponseBodyPriceInfo = None,
        request_id: str = None,
    ):
        self.price_info = price_info
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceInfo') is not None:
            temp_model = main_models.DescribeMultiPriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m.get('PriceInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMultiPriceResponseBodyPriceInfo(DaraModel):
    def __init__(
        self,
        price: main_models.DescribeMultiPriceResponseBodyPriceInfoPrice = None,
        rules: List[main_models.DescribeMultiPriceResponseBodyPriceInfoRules] = None,
    ):
        self.price = price
        self.rules = rules

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price is not None:
            result['Price'] = self.price.to_map()

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = main_models.DescribeMultiPriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m.get('Price'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeMultiPriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeMultiPriceResponseBodyPriceInfoRules(DaraModel):
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

class DescribeMultiPriceResponseBodyPriceInfoPrice(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        price_details: List[main_models.DescribeMultiPriceResponseBodyPriceInfoPricePriceDetails] = None,
        promotions: List[main_models.DescribeMultiPriceResponseBodyPriceInfoPricePromotions] = None,
        refund_instance_id_price_map: Dict[str, float] = None,
        refund_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.price_details = price_details
        self.promotions = promotions
        self.refund_instance_id_price_map = refund_instance_id_price_map
        self.refund_price = refund_price
        self.trade_price = trade_price

    def validate(self):
        if self.price_details:
            for v1 in self.price_details:
                 if v1:
                    v1.validate()
        if self.promotions:
            for v1 in self.promotions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        result['PriceDetails'] = []
        if self.price_details is not None:
            for k1 in self.price_details:
                result['PriceDetails'].append(k1.to_map() if k1 else None)

        result['Promotions'] = []
        if self.promotions is not None:
            for k1 in self.promotions:
                result['Promotions'].append(k1.to_map() if k1 else None)

        if self.refund_instance_id_price_map is not None:
            result['RefundInstanceIdPriceMap'] = self.refund_instance_id_price_map

        if self.refund_price is not None:
            result['RefundPrice'] = self.refund_price

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

        self.price_details = []
        if m.get('PriceDetails') is not None:
            for k1 in m.get('PriceDetails'):
                temp_model = main_models.DescribeMultiPriceResponseBodyPriceInfoPricePriceDetails()
                self.price_details.append(temp_model.from_map(k1))

        self.promotions = []
        if m.get('Promotions') is not None:
            for k1 in m.get('Promotions'):
                temp_model = main_models.DescribeMultiPriceResponseBodyPriceInfoPricePromotions()
                self.promotions.append(temp_model.from_map(k1))

        if m.get('RefundInstanceIdPriceMap') is not None:
            self.refund_instance_id_price_map = m.get('RefundInstanceIdPriceMap')

        if m.get('RefundPrice') is not None:
            self.refund_price = m.get('RefundPrice')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribeMultiPriceResponseBodyPriceInfoPricePromotions(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeMultiPriceResponseBodyPriceInfoPricePriceDetails(DaraModel):
    def __init__(
        self,
        module_details: List[main_models.DescribeMultiPriceResponseBodyPriceInfoPricePriceDetailsModuleDetails] = None,
        order_item: int = None,
        price_detail: main_models.DescribeMultiPriceResponseBodyPriceInfoPricePriceDetailsPriceDetail = None,
    ):
        self.module_details = module_details
        self.order_item = order_item
        self.price_detail = price_detail

    def validate(self):
        if self.module_details:
            for v1 in self.module_details:
                 if v1:
                    v1.validate()
        if self.price_detail:
            self.price_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModuleDetails'] = []
        if self.module_details is not None:
            for k1 in self.module_details:
                result['ModuleDetails'].append(k1.to_map() if k1 else None)

        if self.order_item is not None:
            result['OrderItem'] = self.order_item

        if self.price_detail is not None:
            result['PriceDetail'] = self.price_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_details = []
        if m.get('ModuleDetails') is not None:
            for k1 in m.get('ModuleDetails'):
                temp_model = main_models.DescribeMultiPriceResponseBodyPriceInfoPricePriceDetailsModuleDetails()
                self.module_details.append(temp_model.from_map(k1))

        if m.get('OrderItem') is not None:
            self.order_item = m.get('OrderItem')

        if m.get('PriceDetail') is not None:
            temp_model = main_models.DescribeMultiPriceResponseBodyPriceInfoPricePriceDetailsPriceDetail()
            self.price_detail = temp_model.from_map(m.get('PriceDetail'))

        return self

class DescribeMultiPriceResponseBodyPriceInfoPricePriceDetailsPriceDetail(DaraModel):
    def __init__(
        self,
        discount_price: float = None,
        original_price: float = None,
        resource_type: str = None,
        saving_plan_recommend_price: float = None,
        trade_price: float = None,
    ):
        self.discount_price = discount_price
        self.original_price = original_price
        self.resource_type = resource_type
        self.saving_plan_recommend_price = saving_plan_recommend_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.saving_plan_recommend_price is not None:
            result['SavingPlanRecommendPrice'] = self.saving_plan_recommend_price

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SavingPlanRecommendPrice') is not None:
            self.saving_plan_recommend_price = m.get('SavingPlanRecommendPrice')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribeMultiPriceResponseBodyPriceInfoPricePriceDetailsModuleDetails(DaraModel):
    def __init__(
        self,
        discount_price: float = None,
        module_code: str = None,
        module_name: str = None,
        module_value: str = None,
        original_price: float = None,
        saving_plan_discount_price: float = None,
        trade_price: float = None,
    ):
        self.discount_price = discount_price
        self.module_code = module_code
        self.module_name = module_name
        self.module_value = module_value
        self.original_price = original_price
        self.saving_plan_discount_price = saving_plan_discount_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.module_value is not None:
            result['ModuleValue'] = self.module_value

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.saving_plan_discount_price is not None:
            result['SavingPlanDiscountPrice'] = self.saving_plan_discount_price

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('ModuleValue') is not None:
            self.module_value = m.get('ModuleValue')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('SavingPlanDiscountPrice') is not None:
            self.saving_plan_discount_price = m.get('SavingPlanDiscountPrice')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

