# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeMobileAgentPackagePriceResponseBody(DaraModel):
    def __init__(
        self,
        price: main_models.DescribeMobileAgentPackagePriceResponseBodyPrice = None,
        request_id: str = None,
        rules: List[main_models.DescribeMobileAgentPackagePriceResponseBodyRules] = None,
    ):
        # The price.
        self.price = price
        # Id of the request
        self.request_id = request_id
        # The promotion rules.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = main_models.DescribeMobileAgentPackagePriceResponseBodyPrice()
            self.price = temp_model.from_map(m.get('Price'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeMobileAgentPackagePriceResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeMobileAgentPackagePriceResponseBodyRules(DaraModel):
    def __init__(
        self,
        description: str = None,
        rule_id: str = None,
    ):
        # The rule description.
        self.description = description
        # The rule ID.
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

class DescribeMobileAgentPackagePriceResponseBodyPrice(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        price_detail: List[main_models.DescribeMobileAgentPackagePriceResponseBodyPricePriceDetail] = None,
        promotions: List[main_models.DescribeMobileAgentPackagePriceResponseBodyPricePromotions] = None,
        trade_price: float = None,
    ):
        # The currency.
        self.currency = currency
        # The discounted price.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # The price details.
        self.price_detail = price_detail
        # The promotion information.
        self.promotions = promotions
        # The transaction price.
        self.trade_price = trade_price

    def validate(self):
        if self.price_detail:
            for v1 in self.price_detail:
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

        result['PriceDetail'] = []
        if self.price_detail is not None:
            for k1 in self.price_detail:
                result['PriceDetail'].append(k1.to_map() if k1 else None)

        result['Promotions'] = []
        if self.promotions is not None:
            for k1 in self.promotions:
                result['Promotions'].append(k1.to_map() if k1 else None)

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

        self.price_detail = []
        if m.get('PriceDetail') is not None:
            for k1 in m.get('PriceDetail'):
                temp_model = main_models.DescribeMobileAgentPackagePriceResponseBodyPricePriceDetail()
                self.price_detail.append(temp_model.from_map(k1))

        self.promotions = []
        if m.get('Promotions') is not None:
            for k1 in m.get('Promotions'):
                temp_model = main_models.DescribeMobileAgentPackagePriceResponseBodyPricePromotions()
                self.promotions.append(temp_model.from_map(k1))

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribeMobileAgentPackagePriceResponseBodyPricePromotions(DaraModel):
    def __init__(
        self,
        option_code: str = None,
        promotion_desc: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        selected: bool = None,
    ):
        # The coupon code.
        self.option_code = option_code
        # The coupon description.
        self.promotion_desc = promotion_desc
        # The ID of the promotion.
        self.promotion_id = promotion_id
        # The name of the promotion.
        self.promotion_name = promotion_name
        # Indicates whether the promotion is selected.
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

class DescribeMobileAgentPackagePriceResponseBodyPricePriceDetail(DaraModel):
    def __init__(
        self,
        discount_price: float = None,
        module_price: List[main_models.DescribeMobileAgentPackagePriceResponseBodyPricePriceDetailModulePrice] = None,
        original_price: float = None,
        resource_type: str = None,
        trade_price: float = None,
    ):
        # The discounted price.
        self.discount_price = discount_price
        # The prices of the modules.
        self.module_price = module_price
        # The original price.
        self.original_price = original_price
        # The resource type.
        self.resource_type = resource_type
        # The transaction price.
        self.trade_price = trade_price

    def validate(self):
        if self.module_price:
            for v1 in self.module_price:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        result['ModulePrice'] = []
        if self.module_price is not None:
            for k1 in self.module_price:
                result['ModulePrice'].append(k1.to_map() if k1 else None)

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        self.module_price = []
        if m.get('ModulePrice') is not None:
            for k1 in m.get('ModulePrice'):
                temp_model = main_models.DescribeMobileAgentPackagePriceResponseBodyPricePriceDetailModulePrice()
                self.module_price.append(temp_model.from_map(k1))

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribeMobileAgentPackagePriceResponseBodyPricePriceDetailModulePrice(DaraModel):
    def __init__(
        self,
        discount_price: str = None,
        module_name: str = None,
        original_price: str = None,
        trade_price: str = None,
    ):
        # The discounted price.
        self.discount_price = discount_price
        # The name of the module.
        self.module_name = module_name
        # The original price.
        self.original_price = original_price
        # The transaction price.
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

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

