# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribePriceResponseBody(DaraModel):
    def __init__(
        self,
        price_info: main_models.DescribePriceResponseBodyPriceInfo = None,
        request_id: str = None,
    ):
        # The detailed pricing information.
        self.price_info = price_info
        # Id of the request
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
            temp_model = main_models.DescribePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m.get('PriceInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePriceResponseBodyPriceInfo(DaraModel):
    def __init__(
        self,
        price: main_models.DescribePriceResponseBodyPriceInfoPrice = None,
        rules: List[main_models.DescribePriceResponseBodyPriceInfoRules] = None,
    ):
        # The pricing information.
        self.price = price
        # The activity rule information.
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
            temp_model = main_models.DescribePriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m.get('Price'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribePriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodyPriceInfoRules(DaraModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        # The custom parameter description.
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

class DescribePriceResponseBodyPriceInfoPrice(DaraModel):
    def __init__(
        self,
        coupons: List[main_models.DescribePriceResponseBodyPriceInfoPriceCoupons] = None,
        currency: str = None,
        detail_infos: List[main_models.DescribePriceResponseBodyPriceInfoPriceDetailInfos] = None,
        discount_price: float = None,
        is_contract_promotion: bool = None,
        original_price: float = None,
        promotions: List[main_models.DescribePriceResponseBodyPriceInfoPricePromotions] = None,
        standard_discount_price: float = None,
        standard_price: float = None,
        sub_prices: List[main_models.DescribePriceResponseBodyPriceInfoPriceSubPrices] = None,
        trade_price: float = None,
    ):
        # Specifies whether the coupon is selected.
        self.coupons = coupons
        # The currency. Valid values:
        # 
        # - CNY: Chinese yuan.
        # - USD: US dollar.
        self.currency = currency
        # The detailed pricing information of the configuration.
        self.detail_infos = detail_infos
        # The discounted price.
        self.discount_price = discount_price
        # Specifies whether a promotion is matched.
        self.is_contract_promotion = is_contract_promotion
        # The original price.
        self.original_price = original_price
        # The promotion information.
        self.promotions = promotions
        # The discounted price based on the official website discount.
        self.standard_discount_price = standard_discount_price
        # The discounted price on the official website or the discounted price in the direct sales contract.
        self.standard_price = standard_price
        # The list of price details.
        self.sub_prices = sub_prices
        # The transaction price.
        self.trade_price = trade_price

    def validate(self):
        if self.coupons:
            for v1 in self.coupons:
                 if v1:
                    v1.validate()
        if self.detail_infos:
            for v1 in self.detail_infos:
                 if v1:
                    v1.validate()
        if self.promotions:
            for v1 in self.promotions:
                 if v1:
                    v1.validate()
        if self.sub_prices:
            for v1 in self.sub_prices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Coupons'] = []
        if self.coupons is not None:
            for k1 in self.coupons:
                result['Coupons'].append(k1.to_map() if k1 else None)

        if self.currency is not None:
            result['Currency'] = self.currency

        result['DetailInfos'] = []
        if self.detail_infos is not None:
            for k1 in self.detail_infos:
                result['DetailInfos'].append(k1.to_map() if k1 else None)

        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.is_contract_promotion is not None:
            result['IsContractPromotion'] = self.is_contract_promotion

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        result['Promotions'] = []
        if self.promotions is not None:
            for k1 in self.promotions:
                result['Promotions'].append(k1.to_map() if k1 else None)

        if self.standard_discount_price is not None:
            result['StandardDiscountPrice'] = self.standard_discount_price

        if self.standard_price is not None:
            result['StandardPrice'] = self.standard_price

        result['SubPrices'] = []
        if self.sub_prices is not None:
            for k1 in self.sub_prices:
                result['SubPrices'].append(k1.to_map() if k1 else None)

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.coupons = []
        if m.get('Coupons') is not None:
            for k1 in m.get('Coupons'):
                temp_model = main_models.DescribePriceResponseBodyPriceInfoPriceCoupons()
                self.coupons.append(temp_model.from_map(k1))

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        self.detail_infos = []
        if m.get('DetailInfos') is not None:
            for k1 in m.get('DetailInfos'):
                temp_model = main_models.DescribePriceResponseBodyPriceInfoPriceDetailInfos()
                self.detail_infos.append(temp_model.from_map(k1))

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('IsContractPromotion') is not None:
            self.is_contract_promotion = m.get('IsContractPromotion')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        self.promotions = []
        if m.get('Promotions') is not None:
            for k1 in m.get('Promotions'):
                temp_model = main_models.DescribePriceResponseBodyPriceInfoPricePromotions()
                self.promotions.append(temp_model.from_map(k1))

        if m.get('StandardDiscountPrice') is not None:
            self.standard_discount_price = m.get('StandardDiscountPrice')

        if m.get('StandardPrice') is not None:
            self.standard_price = m.get('StandardPrice')

        self.sub_prices = []
        if m.get('SubPrices') is not None:
            for k1 in m.get('SubPrices'):
                temp_model = main_models.DescribePriceResponseBodyPriceInfoPriceSubPrices()
                self.sub_prices.append(temp_model.from_map(k1))

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribePriceResponseBodyPriceInfoPriceSubPrices(DaraModel):
    def __init__(
        self,
        discount_price: float = None,
        instance_id: str = None,
        is_contract_promotion: bool = None,
        original_price: float = None,
        promotions: List[main_models.DescribePriceResponseBodyPriceInfoPriceSubPricesPromotions] = None,
        rule_ids: List[int] = None,
        standard_discount_price: float = None,
        standard_price: float = None,
        trade_price: float = None,
    ):
        # The order discount amount.
        self.discount_price = discount_price
        # The instance ID of the Simple Application Server.
        self.instance_id = instance_id
        # Specifies whether a promotion is matched.
        self.is_contract_promotion = is_contract_promotion
        # The original price of the order (CNY).
        self.original_price = original_price
        # The promotion name.
        self.promotions = promotions
        # The collection of activity rule IDs.
        self.rule_ids = rule_ids
        # The discounted price based on the official website discount.
        self.standard_discount_price = standard_discount_price
        # The discounted price on the official website or the discounted price in the direct sales contract.
        self.standard_price = standard_price
        # The transaction price.
        self.trade_price = trade_price

    def validate(self):
        if self.promotions:
            for v1 in self.promotions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_contract_promotion is not None:
            result['IsContractPromotion'] = self.is_contract_promotion

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        result['Promotions'] = []
        if self.promotions is not None:
            for k1 in self.promotions:
                result['Promotions'].append(k1.to_map() if k1 else None)

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        if self.standard_discount_price is not None:
            result['StandardDiscountPrice'] = self.standard_discount_price

        if self.standard_price is not None:
            result['StandardPrice'] = self.standard_price

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsContractPromotion') is not None:
            self.is_contract_promotion = m.get('IsContractPromotion')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        self.promotions = []
        if m.get('Promotions') is not None:
            for k1 in m.get('Promotions'):
                temp_model = main_models.DescribePriceResponseBodyPriceInfoPriceSubPricesPromotions()
                self.promotions.append(temp_model.from_map(k1))

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        if m.get('StandardDiscountPrice') is not None:
            self.standard_discount_price = m.get('StandardDiscountPrice')

        if m.get('StandardPrice') is not None:
            self.standard_price = m.get('StandardPrice')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribePriceResponseBodyPriceInfoPriceSubPricesPromotions(DaraModel):
    def __init__(
        self,
        discount_off: float = None,
        name: str = None,
        rule_ids: List[int] = None,
    ):
        # The coupon discount amount.
        self.discount_off = discount_off
        # The name.
        self.name = name
        # The promotion rule ID.
        self.rule_ids = rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_off is not None:
            result['DiscountOff'] = self.discount_off

        if self.name is not None:
            result['Name'] = self.name

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountOff') is not None:
            self.discount_off = m.get('DiscountOff')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        return self

class DescribePriceResponseBodyPriceInfoPricePromotions(DaraModel):
    def __init__(
        self,
        discount_off: float = None,
        name: str = None,
        rule_ids: List[int] = None,
    ):
        # The coupon discount amount.
        self.discount_off = discount_off
        # The coupon name.
        self.name = name
        # The promotion ID.
        self.rule_ids = rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_off is not None:
            result['DiscountOff'] = self.discount_off

        if self.name is not None:
            result['Name'] = self.name

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountOff') is not None:
            self.discount_off = m.get('DiscountOff')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        return self

class DescribePriceResponseBodyPriceInfoPriceDetailInfos(DaraModel):
    def __init__(
        self,
        commodity_type: str = None,
        discount_price: float = None,
        original_price: float = None,
        promotions: List[main_models.DescribePriceResponseBodyPriceInfoPriceDetailInfosPromotions] = None,
        trade_price: float = None,
    ):
        # The resource name.
        self.commodity_type = commodity_type
        # The discounted price.
        self.discount_price = discount_price
        # The original price.
        self.original_price = original_price
        # The promotion information matched by the configuration details.
        self.promotions = promotions
        # The transaction price.
        self.trade_price = trade_price

    def validate(self):
        if self.promotions:
            for v1 in self.promotions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_type is not None:
            result['CommodityType'] = self.commodity_type

        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        result['Promotions'] = []
        if self.promotions is not None:
            for k1 in self.promotions:
                result['Promotions'].append(k1.to_map() if k1 else None)

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityType') is not None:
            self.commodity_type = m.get('CommodityType')

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        self.promotions = []
        if m.get('Promotions') is not None:
            for k1 in m.get('Promotions'):
                temp_model = main_models.DescribePriceResponseBodyPriceInfoPriceDetailInfosPromotions()
                self.promotions.append(temp_model.from_map(k1))

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class DescribePriceResponseBodyPriceInfoPriceDetailInfosPromotions(DaraModel):
    def __init__(
        self,
        discount_off: float = None,
        name: str = None,
        rule_id: int = None,
    ):
        # The discount amount.
        self.discount_off = discount_off
        # The promotion name.
        self.name = name
        # The promotion rule ID.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_off is not None:
            result['DiscountOff'] = self.discount_off

        if self.name is not None:
            result['Name'] = self.name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountOff') is not None:
            self.discount_off = m.get('DiscountOff')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

class DescribePriceResponseBodyPriceInfoPriceCoupons(DaraModel):
    def __init__(
        self,
        coupon_no: str = None,
        description: str = None,
        discount_off: float = None,
        is_selected: bool = None,
        name: str = None,
        option_code: str = None,
    ):
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The custom parameter description.
        self.description = description
        # The discount.
        self.discount_off = discount_off
        # Specifies whether the coupon is selected.
        self.is_selected = is_selected
        # The command name.
        self.name = name
        # The promotion ID.
        self.option_code = option_code

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

        if self.discount_off is not None:
            result['DiscountOff'] = self.discount_off

        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected

        if self.name is not None:
            result['Name'] = self.name

        if self.option_code is not None:
            result['OptionCode'] = self.option_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiscountOff') is not None:
            self.discount_off = m.get('DiscountOff')

        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')

        return self

