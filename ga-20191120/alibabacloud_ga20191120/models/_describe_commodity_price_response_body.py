# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class DescribeCommodityPriceResponseBody(DaraModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        order_details: List[main_models.DescribeCommodityPriceResponseBodyOrderDetails] = None,
        original_price: float = None,
        promotions: List[main_models.DescribeCommodityPriceResponseBodyPromotions] = None,
        request_id: str = None,
        rule_details: List[main_models.DescribeCommodityPriceResponseBodyRuleDetails] = None,
        trade_price: float = None,
    ):
        # The currency unit.
        # 
        # *   China site: **CNY**.
        # *   International site: **USD**.
        self.currency = currency
        # The discount.
        self.discount_price = discount_price
        # The details of the commodity module.
        self.order_details = order_details
        # The original price.
        self.original_price = original_price
        # The details of the coupon.
        # 
        # >  This parameter does not take effect for accounts registered on the China site (aliyun.com).
        self.promotions = promotions
        # The ID of the request.
        self.request_id = request_id
        # The details about the discount rules.
        self.rule_details = rule_details
        # The transaction price, which is equal to the original price minus the discount.
        self.trade_price = trade_price

    def validate(self):
        if self.order_details:
            for v1 in self.order_details:
                 if v1:
                    v1.validate()
        if self.promotions:
            for v1 in self.promotions:
                 if v1:
                    v1.validate()
        if self.rule_details:
            for v1 in self.rule_details:
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

        result['OrderDetails'] = []
        if self.order_details is not None:
            for k1 in self.order_details:
                result['OrderDetails'].append(k1.to_map() if k1 else None)

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        result['Promotions'] = []
        if self.promotions is not None:
            for k1 in self.promotions:
                result['Promotions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleDetails'] = []
        if self.rule_details is not None:
            for k1 in self.rule_details:
                result['RuleDetails'].append(k1.to_map() if k1 else None)

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        self.order_details = []
        if m.get('OrderDetails') is not None:
            for k1 in m.get('OrderDetails'):
                temp_model = main_models.DescribeCommodityPriceResponseBodyOrderDetails()
                self.order_details.append(temp_model.from_map(k1))

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        self.promotions = []
        if m.get('Promotions') is not None:
            for k1 in m.get('Promotions'):
                temp_model = main_models.DescribeCommodityPriceResponseBodyPromotions()
                self.promotions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_details = []
        if m.get('RuleDetails') is not None:
            for k1 in m.get('RuleDetails'):
                temp_model = main_models.DescribeCommodityPriceResponseBodyRuleDetails()
                self.rule_details.append(temp_model.from_map(k1))

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribeCommodityPriceResponseBodyRuleDetails(DaraModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
    ):
        # The ID of the discount rule.
        self.rule_id = rule_id
        # The name of the discount rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class DescribeCommodityPriceResponseBodyPromotions(DaraModel):
    def __init__(
        self,
        can_prom_fee: float = None,
        option_code: str = None,
        promotion_name: str = None,
        promotion_option_no: str = None,
        selected: bool = None,
    ):
        # The discounted amount.
        # 
        # >  This parameter does not take effect for accounts registered on the China site (aliyun.com).
        self.can_prom_fee = can_prom_fee
        # The code of the commodity to which the coupon can be applied.
        # 
        # >  This parameter does not take effect for accounts registered on the China site (aliyun.com).
        self.option_code = option_code
        # The name of the coupon.
        # 
        # >  This parameter does not take effect for accounts registered on the China site (aliyun.com).
        self.promotion_name = promotion_name
        # The code of the coupon.
        # > *   `youhuiquan_promotion_option_id_for_blank` indicates coupons that cannot be applied to the commodity.
        # > *   This parameter does not take effect for accounts registered on the China site (aliyun.com).
        self.promotion_option_no = promotion_option_no
        # Indicates whether the coupon was selected.
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter does not take effect for accounts registered on the China site (aliyun.com).
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_prom_fee is not None:
            result['CanPromFee'] = self.can_prom_fee

        if self.option_code is not None:
            result['OptionCode'] = self.option_code

        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        if self.selected is not None:
            result['Selected'] = self.selected

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanPromFee') is not None:
            self.can_prom_fee = m.get('CanPromFee')

        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')

        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('Selected') is not None:
            self.selected = m.get('Selected')

        return self

class DescribeCommodityPriceResponseBodyOrderDetails(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_name: str = None,
        discount_price: float = None,
        module_details: List[main_models.DescribeCommodityPriceResponseBodyOrderDetailsModuleDetails] = None,
        original_price: float = None,
        prom_details: List[main_models.DescribeCommodityPriceResponseBodyOrderDetailsPromDetails] = None,
        quantity: int = None,
        rule_ids: List[int] = None,
        trade_price: float = None,
    ):
        # The code of the commodity.
        self.commodity_code = commodity_code
        # The name of the commodity.
        self.commodity_name = commodity_name
        # The discount.
        self.discount_price = discount_price
        # The information about the commodity module.
        self.module_details = module_details
        # The original price.
        self.original_price = original_price
        # The details of the discount.
        # 
        # >  This parameter does not take effect for accounts registered on the China site (aliyun.com).
        self.prom_details = prom_details
        # The number of instances that are purchased.
        self.quantity = quantity
        # The IDs of discount rules.
        self.rule_ids = rule_ids
        # The transaction price, which is equal to the original price minus the discount.
        self.trade_price = trade_price

    def validate(self):
        if self.module_details:
            for v1 in self.module_details:
                 if v1:
                    v1.validate()
        if self.prom_details:
            for v1 in self.prom_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        result['ModuleDetails'] = []
        if self.module_details is not None:
            for k1 in self.module_details:
                result['ModuleDetails'].append(k1.to_map() if k1 else None)

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        result['PromDetails'] = []
        if self.prom_details is not None:
            for k1 in self.prom_details:
                result['PromDetails'].append(k1.to_map() if k1 else None)

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        self.module_details = []
        if m.get('ModuleDetails') is not None:
            for k1 in m.get('ModuleDetails'):
                temp_model = main_models.DescribeCommodityPriceResponseBodyOrderDetailsModuleDetails()
                self.module_details.append(temp_model.from_map(k1))

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        self.prom_details = []
        if m.get('PromDetails') is not None:
            for k1 in m.get('PromDetails'):
                temp_model = main_models.DescribeCommodityPriceResponseBodyOrderDetailsPromDetails()
                self.prom_details.append(temp_model.from_map(k1))

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribeCommodityPriceResponseBodyOrderDetailsPromDetails(DaraModel):
    def __init__(
        self,
        final_prom_fee: float = None,
        option_code: str = None,
        prom_type: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
    ):
        # The discounted price.
        # 
        # >  This parameter does not take effect for accounts registered on the China site (aliyun.com).
        self.final_prom_fee = final_prom_fee
        # The code of the discount option.
        # 
        # >  This parameter does not take effect for accounts registered on the China site (aliyun.com).
        self.option_code = option_code
        # The sub-type of the discount.
        # 
        # >  This parameter does not take effect for accounts registered on the China site (aliyun.com).
        self.prom_type = prom_type
        # The ID of the discount item.
        # 
        # >  This parameter does not take effect for accounts registered on the China site (aliyun.com).
        self.promotion_id = promotion_id
        # The name of the discount item.
        # 
        # >  This parameter does not take effect for accounts registered on the China site (aliyun.com).
        self.promotion_name = promotion_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.final_prom_fee is not None:
            result['FinalPromFee'] = self.final_prom_fee

        if self.option_code is not None:
            result['OptionCode'] = self.option_code

        if self.prom_type is not None:
            result['PromType'] = self.prom_type

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinalPromFee') is not None:
            self.final_prom_fee = m.get('FinalPromFee')

        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')

        if m.get('PromType') is not None:
            self.prom_type = m.get('PromType')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')

        return self

class DescribeCommodityPriceResponseBodyOrderDetailsModuleDetails(DaraModel):
    def __init__(
        self,
        discount_price: float = None,
        module_code: str = None,
        module_name: str = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        # The discount.
        self.discount_price = discount_price
        # The code of the commodity module.
        self.module_code = module_code
        # The name of the commodity module.
        self.module_name = module_name
        # The original price.
        self.original_price = original_price
        # The transaction price, which is equal to the original price minus the discount.
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

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

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

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

