# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribePriceResponseBody(DaraModel):
    def __init__(
        self,
        order: main_models.DescribePriceResponseBodyOrder = None,
        order_params: str = None,
        request_id: str = None,
        rules: main_models.DescribePriceResponseBodyRules = None,
        sub_orders: main_models.DescribePriceResponseBodySubOrders = None,
        trace_id: str = None,
    ):
        # The order information.
        self.order = order
        # The order parameters.
        # 
        # > This parameter is returned only when the **OrderParamOut** parameter is set to **true**.
        self.order_params = order_params
        # The request ID.
        self.request_id = request_id
        # The promotion rules.
        self.rules = rules
        # The coupon rules.
        self.sub_orders = sub_orders
        # The ID of the trace.
        self.trace_id = trace_id

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

        if self.order_params is not None:
            result['OrderParams'] = self.order_params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        if self.sub_orders is not None:
            result['SubOrders'] = self.sub_orders.to_map()

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            temp_model = main_models.DescribePriceResponseBodyOrder()
            self.order = temp_model.from_map(m.get('Order'))

        if m.get('OrderParams') is not None:
            self.order_params = m.get('OrderParams')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rules') is not None:
            temp_model = main_models.DescribePriceResponseBodyRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        if m.get('SubOrders') is not None:
            temp_model = main_models.DescribePriceResponseBodySubOrders()
            self.sub_orders = temp_model.from_map(m.get('SubOrders'))

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribePriceResponseBodySubOrders(DaraModel):
    def __init__(
        self,
        sub_order: List[main_models.DescribePriceResponseBodySubOrdersSubOrder] = None,
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
                temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrder()
                self.sub_order.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodySubOrdersSubOrder(DaraModel):
    def __init__(
        self,
        contract_activity: bool = None,
        depreciate_info: main_models.DescribePriceResponseBodySubOrdersSubOrderDepreciateInfo = None,
        discount_amount: str = None,
        instance_id: str = None,
        is_contract_activity: bool = None,
        is_new_official_activity: str = None,
        module_instance: main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstance = None,
        optional_promotions: main_models.DescribePriceResponseBodySubOrdersSubOrderOptionalPromotions = None,
        original_amount: str = None,
        prom_detail_list: main_models.DescribePriceResponseBodySubOrdersSubOrderPromDetailList = None,
        rule_ids: main_models.DescribePriceResponseBodySubOrdersSubOrderRuleIds = None,
        stand_discount_price: float = None,
        stand_price: float = None,
        trade_amount: str = None,
    ):
        # Indicates whether the contract promotion is hit.
        self.contract_activity = contract_activity
        # The price reduction information.
        self.depreciate_info = depreciate_info
        # The discount amount of the order.
        self.discount_amount = discount_amount
        # The instance ID.
        self.instance_id = instance_id
        # Indicates whether the contract promotion is hit.
        self.is_contract_activity = is_contract_activity
        # Indicates whether the discount is hit.
        self.is_new_official_activity = is_new_official_activity
        # The configuration item of the instance in the order.
        self.module_instance = module_instance
        # The promotional options that can be configured.
        self.optional_promotions = optional_promotions
        # The original price of the order.
        self.original_amount = original_amount
        # The promotion details.
        self.prom_detail_list = prom_detail_list
        # The activity rules.
        self.rule_ids = rule_ids
        # The discount.
        self.stand_discount_price = stand_discount_price
        # The discount.
        self.stand_price = stand_price
        # The actual price of the order.
        self.trade_amount = trade_amount

    def validate(self):
        if self.depreciate_info:
            self.depreciate_info.validate()
        if self.module_instance:
            self.module_instance.validate()
        if self.optional_promotions:
            self.optional_promotions.validate()
        if self.prom_detail_list:
            self.prom_detail_list.validate()
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contract_activity is not None:
            result['ContractActivity'] = self.contract_activity

        if self.depreciate_info is not None:
            result['DepreciateInfo'] = self.depreciate_info.to_map()

        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_contract_activity is not None:
            result['IsContractActivity'] = self.is_contract_activity

        if self.is_new_official_activity is not None:
            result['IsNewOfficialActivity'] = self.is_new_official_activity

        if self.module_instance is not None:
            result['ModuleInstance'] = self.module_instance.to_map()

        if self.optional_promotions is not None:
            result['OptionalPromotions'] = self.optional_promotions.to_map()

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        if self.prom_detail_list is not None:
            result['PromDetailList'] = self.prom_detail_list.to_map()

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()

        if self.stand_discount_price is not None:
            result['StandDiscountPrice'] = self.stand_discount_price

        if self.stand_price is not None:
            result['StandPrice'] = self.stand_price

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContractActivity') is not None:
            self.contract_activity = m.get('ContractActivity')

        if m.get('DepreciateInfo') is not None:
            temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderDepreciateInfo()
            self.depreciate_info = temp_model.from_map(m.get('DepreciateInfo'))

        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsContractActivity') is not None:
            self.is_contract_activity = m.get('IsContractActivity')

        if m.get('IsNewOfficialActivity') is not None:
            self.is_new_official_activity = m.get('IsNewOfficialActivity')

        if m.get('ModuleInstance') is not None:
            temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstance()
            self.module_instance = temp_model.from_map(m.get('ModuleInstance'))

        if m.get('OptionalPromotions') is not None:
            temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderOptionalPromotions()
            self.optional_promotions = temp_model.from_map(m.get('OptionalPromotions'))

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        if m.get('PromDetailList') is not None:
            temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderPromDetailList()
            self.prom_detail_list = temp_model.from_map(m.get('PromDetailList'))

        if m.get('RuleIds') is not None:
            temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderRuleIds()
            self.rule_ids = temp_model.from_map(m.get('RuleIds'))

        if m.get('StandDiscountPrice') is not None:
            self.stand_discount_price = m.get('StandDiscountPrice')

        if m.get('StandPrice') is not None:
            self.stand_price = m.get('StandPrice')

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

class DescribePriceResponseBodySubOrdersSubOrderRuleIds(DaraModel):
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

class DescribePriceResponseBodySubOrdersSubOrderPromDetailList(DaraModel):
    def __init__(
        self,
        prom_detail: List[main_models.DescribePriceResponseBodySubOrdersSubOrderPromDetailListPromDetail] = None,
    ):
        self.prom_detail = prom_detail

    def validate(self):
        if self.prom_detail:
            for v1 in self.prom_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PromDetail'] = []
        if self.prom_detail is not None:
            for k1 in self.prom_detail:
                result['PromDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prom_detail = []
        if m.get('PromDetail') is not None:
            for k1 in m.get('PromDetail'):
                temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderPromDetailListPromDetail()
                self.prom_detail.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodySubOrdersSubOrderPromDetailListPromDetail(DaraModel):
    def __init__(
        self,
        activity_ext_info: Dict[str, Any] = None,
        derived_prom_type: str = None,
        final_prom_fee: float = None,
        option_code: str = None,
        prom_type: str = None,
        promotion_code: str = None,
        promotion_id: int = None,
        promotion_name: str = None,
    ):
        # The additional activity information.
        self.activity_ext_info = activity_ext_info
        # The sub-type of the promotion.
        self.derived_prom_type = derived_prom_type
        # The discount amount.
        self.final_prom_fee = final_prom_fee
        # The code of the coupon.
        self.option_code = option_code
        # The sub-type of the promotion.
        self.prom_type = prom_type
        # The coupon code.
        self.promotion_code = promotion_code
        # The promotion ID.
        self.promotion_id = promotion_id
        # The name of the promotional activity.
        self.promotion_name = promotion_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_ext_info is not None:
            result['ActivityExtInfo'] = self.activity_ext_info

        if self.derived_prom_type is not None:
            result['DerivedPromType'] = self.derived_prom_type

        if self.final_prom_fee is not None:
            result['FinalPromFee'] = self.final_prom_fee

        if self.option_code is not None:
            result['OptionCode'] = self.option_code

        if self.prom_type is not None:
            result['PromType'] = self.prom_type

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityExtInfo') is not None:
            self.activity_ext_info = m.get('ActivityExtInfo')

        if m.get('DerivedPromType') is not None:
            self.derived_prom_type = m.get('DerivedPromType')

        if m.get('FinalPromFee') is not None:
            self.final_prom_fee = m.get('FinalPromFee')

        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')

        if m.get('PromType') is not None:
            self.prom_type = m.get('PromType')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')

        return self

class DescribePriceResponseBodySubOrdersSubOrderOptionalPromotions(DaraModel):
    def __init__(
        self,
        optional_promotion: List[main_models.DescribePriceResponseBodySubOrdersSubOrderOptionalPromotionsOptionalPromotion] = None,
    ):
        self.optional_promotion = optional_promotion

    def validate(self):
        if self.optional_promotion:
            for v1 in self.optional_promotion:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OptionalPromotion'] = []
        if self.optional_promotion is not None:
            for k1 in self.optional_promotion:
                result['OptionalPromotion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.optional_promotion = []
        if m.get('OptionalPromotion') is not None:
            for k1 in m.get('OptionalPromotion'):
                temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderOptionalPromotionsOptionalPromotion()
                self.optional_promotion.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodySubOrdersSubOrderOptionalPromotionsOptionalPromotion(DaraModel):
    def __init__(
        self,
        activity_category: str = None,
        activity_ext_info: Dict[str, Any] = None,
        can_prom_fee: float = None,
        option_code: str = None,
        promotion_name: str = None,
        promotion_option_no: str = None,
        promotion_rule_id_list: main_models.DescribePriceResponseBodySubOrdersSubOrderOptionalPromotionsOptionalPromotionPromotionRuleIdList = None,
        selected: bool = None,
        show: bool = None,
        target_article_item_codes: main_models.DescribePriceResponseBodySubOrdersSubOrderOptionalPromotionsOptionalPromotionTargetArticleItemCodes = None,
    ):
        # The activity type.
        self.activity_category = activity_category
        # The additional activity information.
        self.activity_ext_info = activity_ext_info
        # The amount that can be deducted by using the coupon.
        self.can_prom_fee = can_prom_fee
        # The promotion type.
        self.option_code = option_code
        # The promotion name.
        self.promotion_name = promotion_name
        # The promotion ID.
        self.promotion_option_no = promotion_option_no
        # The promotion IDs.
        self.promotion_rule_id_list = promotion_rule_id_list
        # Indicates whether
        self.selected = selected
        # Indicates whether the discount is displayed.
        self.show = show
        # The specification codes of the product.
        self.target_article_item_codes = target_article_item_codes

    def validate(self):
        if self.promotion_rule_id_list:
            self.promotion_rule_id_list.validate()
        if self.target_article_item_codes:
            self.target_article_item_codes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_category is not None:
            result['ActivityCategory'] = self.activity_category

        if self.activity_ext_info is not None:
            result['ActivityExtInfo'] = self.activity_ext_info

        if self.can_prom_fee is not None:
            result['CanPromFee'] = self.can_prom_fee

        if self.option_code is not None:
            result['OptionCode'] = self.option_code

        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        if self.promotion_rule_id_list is not None:
            result['PromotionRuleIdList'] = self.promotion_rule_id_list.to_map()

        if self.selected is not None:
            result['Selected'] = self.selected

        if self.show is not None:
            result['Show'] = self.show

        if self.target_article_item_codes is not None:
            result['TargetArticleItemCodes'] = self.target_article_item_codes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityCategory') is not None:
            self.activity_category = m.get('ActivityCategory')

        if m.get('ActivityExtInfo') is not None:
            self.activity_ext_info = m.get('ActivityExtInfo')

        if m.get('CanPromFee') is not None:
            self.can_prom_fee = m.get('CanPromFee')

        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')

        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('PromotionRuleIdList') is not None:
            temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderOptionalPromotionsOptionalPromotionPromotionRuleIdList()
            self.promotion_rule_id_list = temp_model.from_map(m.get('PromotionRuleIdList'))

        if m.get('Selected') is not None:
            self.selected = m.get('Selected')

        if m.get('Show') is not None:
            self.show = m.get('Show')

        if m.get('TargetArticleItemCodes') is not None:
            temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderOptionalPromotionsOptionalPromotionTargetArticleItemCodes()
            self.target_article_item_codes = temp_model.from_map(m.get('TargetArticleItemCodes'))

        return self

class DescribePriceResponseBodySubOrdersSubOrderOptionalPromotionsOptionalPromotionTargetArticleItemCodes(DaraModel):
    def __init__(
        self,
        target_article_item_code: List[str] = None,
    ):
        self.target_article_item_code = target_article_item_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_article_item_code is not None:
            result['targetArticleItemCode'] = self.target_article_item_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('targetArticleItemCode') is not None:
            self.target_article_item_code = m.get('targetArticleItemCode')

        return self

class DescribePriceResponseBodySubOrdersSubOrderOptionalPromotionsOptionalPromotionPromotionRuleIdList(DaraModel):
    def __init__(
        self,
        promotion_rule_id: List[str] = None,
    ):
        self.promotion_rule_id = promotion_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.promotion_rule_id is not None:
            result['promotionRuleId'] = self.promotion_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('promotionRuleId') is not None:
            self.promotion_rule_id = m.get('promotionRuleId')

        return self

class DescribePriceResponseBodySubOrdersSubOrderModuleInstance(DaraModel):
    def __init__(
        self,
        module_instance: List[main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstance] = None,
    ):
        self.module_instance = module_instance

    def validate(self):
        if self.module_instance:
            for v1 in self.module_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModuleInstance'] = []
        if self.module_instance is not None:
            for k1 in self.module_instance:
                result['ModuleInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_instance = []
        if m.get('ModuleInstance') is not None:
            for k1 in m.get('ModuleInstance'):
                temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstance()
                self.module_instance.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstance(DaraModel):
    def __init__(
        self,
        contract_activity: bool = None,
        cycle_fee: str = None,
        depreciate_info: main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstanceDepreciateInfo = None,
        discount_fee: str = None,
        module_attrs: main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstanceModuleAttrs = None,
        module_code: str = None,
        module_id: int = None,
        module_name: str = None,
        need_order_pay: bool = None,
        pay_fee: float = None,
        pricing_module: bool = None,
        prom_detail_list: main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstancePromDetailList = None,
        stand_discount_price: float = None,
        stand_price: float = None,
        total_product_fee: float = None,
        unit_price_unit_4buy: str = None,
        price_type: str = None,
        price_unit: str = None,
    ):
        # Indicates whether the contract promotion is hit.
        self.contract_activity = contract_activity
        # The cycle fee of the module.
        self.cycle_fee = cycle_fee
        # The activity information.
        self.depreciate_info = depreciate_info
        # The discount.
        self.discount_fee = discount_fee
        # The module attributes.
        self.module_attrs = module_attrs
        # The module code.
        self.module_code = module_code
        # The module ID
        self.module_id = module_id
        # The module name.
        self.module_name = module_name
        # Indicates whether the order is paid.
        self.need_order_pay = need_order_pay
        # The actual amount paid.
        self.pay_fee = pay_fee
        # Indicates whether the item is billed.
        self.pricing_module = pricing_module
        # The promotion details.
        self.prom_detail_list = prom_detail_list
        # The discounted price.
        self.stand_discount_price = stand_discount_price
        # The discount.
        self.stand_price = stand_price
        # The original price of the product.
        self.total_product_fee = total_product_fee
        self.unit_price_unit_4buy = unit_price_unit_4buy
        # The price type.
        self.price_type = price_type
        # The unit of the price.
        self.price_unit = price_unit

    def validate(self):
        if self.depreciate_info:
            self.depreciate_info.validate()
        if self.module_attrs:
            self.module_attrs.validate()
        if self.prom_detail_list:
            self.prom_detail_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contract_activity is not None:
            result['ContractActivity'] = self.contract_activity

        if self.cycle_fee is not None:
            result['CycleFee'] = self.cycle_fee

        if self.depreciate_info is not None:
            result['DepreciateInfo'] = self.depreciate_info.to_map()

        if self.discount_fee is not None:
            result['DiscountFee'] = self.discount_fee

        if self.module_attrs is not None:
            result['ModuleAttrs'] = self.module_attrs.to_map()

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.need_order_pay is not None:
            result['NeedOrderPay'] = self.need_order_pay

        if self.pay_fee is not None:
            result['PayFee'] = self.pay_fee

        if self.pricing_module is not None:
            result['PricingModule'] = self.pricing_module

        if self.prom_detail_list is not None:
            result['PromDetailList'] = self.prom_detail_list.to_map()

        if self.stand_discount_price is not None:
            result['StandDiscountPrice'] = self.stand_discount_price

        if self.stand_price is not None:
            result['StandPrice'] = self.stand_price

        if self.total_product_fee is not None:
            result['TotalProductFee'] = self.total_product_fee

        if self.unit_price_unit_4buy is not None:
            result['UnitPriceUnit4Buy'] = self.unit_price_unit_4buy

        if self.price_type is not None:
            result['priceType'] = self.price_type

        if self.price_unit is not None:
            result['priceUnit'] = self.price_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContractActivity') is not None:
            self.contract_activity = m.get('ContractActivity')

        if m.get('CycleFee') is not None:
            self.cycle_fee = m.get('CycleFee')

        if m.get('DepreciateInfo') is not None:
            temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstanceDepreciateInfo()
            self.depreciate_info = temp_model.from_map(m.get('DepreciateInfo'))

        if m.get('DiscountFee') is not None:
            self.discount_fee = m.get('DiscountFee')

        if m.get('ModuleAttrs') is not None:
            temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstanceModuleAttrs()
            self.module_attrs = temp_model.from_map(m.get('ModuleAttrs'))

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('NeedOrderPay') is not None:
            self.need_order_pay = m.get('NeedOrderPay')

        if m.get('PayFee') is not None:
            self.pay_fee = m.get('PayFee')

        if m.get('PricingModule') is not None:
            self.pricing_module = m.get('PricingModule')

        if m.get('PromDetailList') is not None:
            temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstancePromDetailList()
            self.prom_detail_list = temp_model.from_map(m.get('PromDetailList'))

        if m.get('StandDiscountPrice') is not None:
            self.stand_discount_price = m.get('StandDiscountPrice')

        if m.get('StandPrice') is not None:
            self.stand_price = m.get('StandPrice')

        if m.get('TotalProductFee') is not None:
            self.total_product_fee = m.get('TotalProductFee')

        if m.get('UnitPriceUnit4Buy') is not None:
            self.unit_price_unit_4buy = m.get('UnitPriceUnit4Buy')

        if m.get('priceType') is not None:
            self.price_type = m.get('priceType')

        if m.get('priceUnit') is not None:
            self.price_unit = m.get('priceUnit')

        return self

class DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstancePromDetailList(DaraModel):
    def __init__(
        self,
        prom_detail: List[main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstancePromDetailListPromDetail] = None,
    ):
        self.prom_detail = prom_detail

    def validate(self):
        if self.prom_detail:
            for v1 in self.prom_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PromDetail'] = []
        if self.prom_detail is not None:
            for k1 in self.prom_detail:
                result['PromDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prom_detail = []
        if m.get('PromDetail') is not None:
            for k1 in m.get('PromDetail'):
                temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstancePromDetailListPromDetail()
                self.prom_detail.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstancePromDetailListPromDetail(DaraModel):
    def __init__(
        self,
        activity_ext_info: Dict[str, Any] = None,
        derived_prom_type: str = None,
        final_prom_fee: float = None,
        option_code: str = None,
        prom_type: str = None,
        promotion_code: str = None,
        promotion_id: int = None,
        promotion_name: str = None,
    ):
        # The additional promotion information.
        self.activity_ext_info = activity_ext_info
        # The sub-type of the promotion.
        self.derived_prom_type = derived_prom_type
        # The discount amount.
        self.final_prom_fee = final_prom_fee
        # The code of the commodity to which the coupon can be applied.
        self.option_code = option_code
        # The sub-type of the promotion.
        self.prom_type = prom_type
        # The coupon code.
        self.promotion_code = promotion_code
        # The ID of the promotional activity.
        self.promotion_id = promotion_id
        # The promotional activity name.
        self.promotion_name = promotion_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_ext_info is not None:
            result['ActivityExtInfo'] = self.activity_ext_info

        if self.derived_prom_type is not None:
            result['DerivedPromType'] = self.derived_prom_type

        if self.final_prom_fee is not None:
            result['FinalPromFee'] = self.final_prom_fee

        if self.option_code is not None:
            result['OptionCode'] = self.option_code

        if self.prom_type is not None:
            result['PromType'] = self.prom_type

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityExtInfo') is not None:
            self.activity_ext_info = m.get('ActivityExtInfo')

        if m.get('DerivedPromType') is not None:
            self.derived_prom_type = m.get('DerivedPromType')

        if m.get('FinalPromFee') is not None:
            self.final_prom_fee = m.get('FinalPromFee')

        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')

        if m.get('PromType') is not None:
            self.prom_type = m.get('PromType')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')

        return self

class DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstanceModuleAttrs(DaraModel):
    def __init__(
        self,
        module_attr: List[main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstanceModuleAttrsModuleAttr] = None,
    ):
        self.module_attr = module_attr

    def validate(self):
        if self.module_attr:
            for v1 in self.module_attr:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['moduleAttr'] = []
        if self.module_attr is not None:
            for k1 in self.module_attr:
                result['moduleAttr'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_attr = []
        if m.get('moduleAttr') is not None:
            for k1 in m.get('moduleAttr'):
                temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstanceModuleAttrsModuleAttr()
                self.module_attr.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstanceModuleAttrsModuleAttr(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The attribute code.
        self.code = code
        # The attribute name.
        self.name = name
        # The attribute type.
        self.type = type
        # The attribute value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribePriceResponseBodySubOrdersSubOrderModuleInstanceModuleInstanceDepreciateInfo(DaraModel):
    def __init__(
        self,
        cheap_rate: float = None,
        cheap_stand_amount: float = None,
        differential: float = None,
        differential_name: str = None,
        is_contract_activity: bool = None,
        is_show: str = None,
        list_price: float = None,
        month_price: float = None,
        original_stand_amount: float = None,
    ):
        # The price reduction rate.
        self.cheap_rate = cheap_rate
        # The new total price displayed on the official website.
        self.cheap_stand_amount = cheap_stand_amount
        # The price difference displayed in the total order amount.
        self.differential = differential
        # The name of the price difference.
        self.differential_name = differential_name
        # Indicates whether the contract promotion is hit.
        self.is_contract_activity = is_contract_activity
        # Indicates whether the price reduction rate is displayed.
        self.is_show = is_show
        # The list price.
        self.list_price = list_price
        # The monthly price.
        self.month_price = month_price
        # The original total price displayed on the official website.
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

        if self.differential is not None:
            result['Differential'] = self.differential

        if self.differential_name is not None:
            result['DifferentialName'] = self.differential_name

        if self.is_contract_activity is not None:
            result['IsContractActivity'] = self.is_contract_activity

        if self.is_show is not None:
            result['IsShow'] = self.is_show

        if self.list_price is not None:
            result['ListPrice'] = self.list_price

        if self.month_price is not None:
            result['MonthPrice'] = self.month_price

        if self.original_stand_amount is not None:
            result['OriginalStandAmount'] = self.original_stand_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheapRate') is not None:
            self.cheap_rate = m.get('CheapRate')

        if m.get('CheapStandAmount') is not None:
            self.cheap_stand_amount = m.get('CheapStandAmount')

        if m.get('Differential') is not None:
            self.differential = m.get('Differential')

        if m.get('DifferentialName') is not None:
            self.differential_name = m.get('DifferentialName')

        if m.get('IsContractActivity') is not None:
            self.is_contract_activity = m.get('IsContractActivity')

        if m.get('IsShow') is not None:
            self.is_show = m.get('IsShow')

        if m.get('ListPrice') is not None:
            self.list_price = m.get('ListPrice')

        if m.get('MonthPrice') is not None:
            self.month_price = m.get('MonthPrice')

        if m.get('OriginalStandAmount') is not None:
            self.original_stand_amount = m.get('OriginalStandAmount')

        return self

class DescribePriceResponseBodySubOrdersSubOrderDepreciateInfo(DaraModel):
    def __init__(
        self,
        cheap_rate: float = None,
        cheap_stand_amount: float = None,
        contract_activity: main_models.DescribePriceResponseBodySubOrdersSubOrderDepreciateInfoContractActivity = None,
        differential: float = None,
        differential_name: str = None,
        is_contract_activity: bool = None,
        is_show: str = None,
        list_price: float = None,
        month_price: float = None,
        original_stand_amount: float = None,
        start_time: str = None,
    ):
        # The price reduction rate.
        self.cheap_rate = cheap_rate
        # The new total price displayed on the official website.
        self.cheap_stand_amount = cheap_stand_amount
        # The activity information.
        self.contract_activity = contract_activity
        # The price difference displayed in the total order amount.
        self.differential = differential
        # The name of the price difference.
        self.differential_name = differential_name
        # Indicates whether the contract promotion is hit.
        self.is_contract_activity = is_contract_activity
        # Indicates whether the price reduction rate is displayed.
        self.is_show = is_show
        # The list price.
        self.list_price = list_price
        # The monthly price.
        self.month_price = month_price
        # The original total price displayed on the official website.
        self.original_stand_amount = original_stand_amount
        # The start time of the activity.
        self.start_time = start_time

    def validate(self):
        if self.contract_activity:
            self.contract_activity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cheap_rate is not None:
            result['CheapRate'] = self.cheap_rate

        if self.cheap_stand_amount is not None:
            result['CheapStandAmount'] = self.cheap_stand_amount

        if self.contract_activity is not None:
            result['ContractActivity'] = self.contract_activity.to_map()

        if self.differential is not None:
            result['Differential'] = self.differential

        if self.differential_name is not None:
            result['DifferentialName'] = self.differential_name

        if self.is_contract_activity is not None:
            result['IsContractActivity'] = self.is_contract_activity

        if self.is_show is not None:
            result['IsShow'] = self.is_show

        if self.list_price is not None:
            result['ListPrice'] = self.list_price

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

        if m.get('ContractActivity') is not None:
            temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderDepreciateInfoContractActivity()
            self.contract_activity = temp_model.from_map(m.get('ContractActivity'))

        if m.get('Differential') is not None:
            self.differential = m.get('Differential')

        if m.get('DifferentialName') is not None:
            self.differential_name = m.get('DifferentialName')

        if m.get('IsContractActivity') is not None:
            self.is_contract_activity = m.get('IsContractActivity')

        if m.get('IsShow') is not None:
            self.is_show = m.get('IsShow')

        if m.get('ListPrice') is not None:
            self.list_price = m.get('ListPrice')

        if m.get('MonthPrice') is not None:
            self.month_price = m.get('MonthPrice')

        if m.get('OriginalStandAmount') is not None:
            self.original_stand_amount = m.get('OriginalStandAmount')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribePriceResponseBodySubOrdersSubOrderDepreciateInfoContractActivity(DaraModel):
    def __init__(
        self,
        activity_id: int = None,
        activity_name: str = None,
        final_fee: float = None,
        final_prom_fee: float = None,
        option_code: str = None,
        option_ids: main_models.DescribePriceResponseBodySubOrdersSubOrderDepreciateInfoContractActivityOptionIds = None,
        prod_fee: float = None,
    ):
        # The activity ID.
        self.activity_id = activity_id
        # The activity name.
        self.activity_name = activity_name
        # The price after the promotion.
        self.final_fee = final_fee
        # The total discount amount.
        self.final_prom_fee = final_prom_fee
        # The promotion ID.
        self.option_code = option_code
        # The promotion IDs.
        self.option_ids = option_ids
        # The original price.
        self.prod_fee = prod_fee

    def validate(self):
        if self.option_ids:
            self.option_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.final_fee is not None:
            result['FinalFee'] = self.final_fee

        if self.final_prom_fee is not None:
            result['FinalPromFee'] = self.final_prom_fee

        if self.option_code is not None:
            result['OptionCode'] = self.option_code

        if self.option_ids is not None:
            result['OptionIds'] = self.option_ids.to_map()

        if self.prod_fee is not None:
            result['ProdFee'] = self.prod_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('FinalFee') is not None:
            self.final_fee = m.get('FinalFee')

        if m.get('FinalPromFee') is not None:
            self.final_prom_fee = m.get('FinalPromFee')

        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')

        if m.get('OptionIds') is not None:
            temp_model = main_models.DescribePriceResponseBodySubOrdersSubOrderDepreciateInfoContractActivityOptionIds()
            self.option_ids = temp_model.from_map(m.get('OptionIds'))

        if m.get('ProdFee') is not None:
            self.prod_fee = m.get('ProdFee')

        return self

class DescribePriceResponseBodySubOrdersSubOrderDepreciateInfoContractActivityOptionIds(DaraModel):
    def __init__(
        self,
        option_id: List[int] = None,
    ):
        self.option_id = option_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.option_id is not None:
            result['OptionId'] = self.option_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionId') is not None:
            self.option_id = m.get('OptionId')

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
        name: str = None,
        rule_desc_id: int = None,
        title: str = None,
    ):
        # The rule name.
        self.name = name
        # The rule ID.
        self.rule_desc_id = rule_desc_id
        # The rule title.
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

class DescribePriceResponseBodyOrder(DaraModel):
    def __init__(
        self,
        code: str = None,
        contract_activity: bool = None,
        coupons: main_models.DescribePriceResponseBodyOrderCoupons = None,
        currency: str = None,
        depreciate_info: main_models.DescribePriceResponseBodyOrderDepreciateInfo = None,
        discount_amount: str = None,
        is_contract_activity: bool = None,
        message: str = None,
        optional_promotions: str = None,
        original_amount: str = None,
        prom_detail_list: str = None,
        rule_ids: main_models.DescribePriceResponseBodyOrderRuleIds = None,
        show_discount_info: bool = None,
        stand_discount_price: float = None,
        stand_price: float = None,
        total_cost_amount: float = None,
        trade_amount: str = None,
    ):
        # The order code.
        self.code = code
        # Indicates whether the contract promotion is hit.
        self.contract_activity = contract_activity
        # The information of coupons.
        self.coupons = coupons
        # The currency.
        self.currency = currency
        # The price reduction information.
        self.depreciate_info = depreciate_info
        # The discount amount of the order.
        self.discount_amount = discount_amount
        # Indicates whether the contract promotion is hit.
        self.is_contract_activity = is_contract_activity
        # The order information.
        self.message = message
        # The promotional activity information.
        self.optional_promotions = optional_promotions
        # The original price of the order.
        self.original_amount = original_amount
        # The promotional activity that is hit.
        self.prom_detail_list = prom_detail_list
        # The rules of the order.
        self.rule_ids = rule_ids
        # Indicates whether the discount information is displayed.
        self.show_discount_info = show_discount_info
        # The discount.
        self.stand_discount_price = stand_discount_price
        # The discount.
        self.stand_price = stand_price
        self.total_cost_amount = total_cost_amount
        # The final price of the order.
        self.trade_amount = trade_amount

    def validate(self):
        if self.coupons:
            self.coupons.validate()
        if self.depreciate_info:
            self.depreciate_info.validate()
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.contract_activity is not None:
            result['ContractActivity'] = self.contract_activity

        if self.coupons is not None:
            result['Coupons'] = self.coupons.to_map()

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.depreciate_info is not None:
            result['DepreciateInfo'] = self.depreciate_info.to_map()

        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount

        if self.is_contract_activity is not None:
            result['IsContractActivity'] = self.is_contract_activity

        if self.message is not None:
            result['Message'] = self.message

        if self.optional_promotions is not None:
            result['OptionalPromotions'] = self.optional_promotions

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        if self.prom_detail_list is not None:
            result['PromDetailList'] = self.prom_detail_list

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()

        if self.show_discount_info is not None:
            result['ShowDiscountInfo'] = self.show_discount_info

        if self.stand_discount_price is not None:
            result['StandDiscountPrice'] = self.stand_discount_price

        if self.stand_price is not None:
            result['StandPrice'] = self.stand_price

        if self.total_cost_amount is not None:
            result['TotalCostAmount'] = self.total_cost_amount

        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ContractActivity') is not None:
            self.contract_activity = m.get('ContractActivity')

        if m.get('Coupons') is not None:
            temp_model = main_models.DescribePriceResponseBodyOrderCoupons()
            self.coupons = temp_model.from_map(m.get('Coupons'))

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DepreciateInfo') is not None:
            temp_model = main_models.DescribePriceResponseBodyOrderDepreciateInfo()
            self.depreciate_info = temp_model.from_map(m.get('DepreciateInfo'))

        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')

        if m.get('IsContractActivity') is not None:
            self.is_contract_activity = m.get('IsContractActivity')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OptionalPromotions') is not None:
            self.optional_promotions = m.get('OptionalPromotions')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        if m.get('PromDetailList') is not None:
            self.prom_detail_list = m.get('PromDetailList')

        if m.get('RuleIds') is not None:
            temp_model = main_models.DescribePriceResponseBodyOrderRuleIds()
            self.rule_ids = temp_model.from_map(m.get('RuleIds'))

        if m.get('ShowDiscountInfo') is not None:
            self.show_discount_info = m.get('ShowDiscountInfo')

        if m.get('StandDiscountPrice') is not None:
            self.stand_discount_price = m.get('StandDiscountPrice')

        if m.get('StandPrice') is not None:
            self.stand_price = m.get('StandPrice')

        if m.get('TotalCostAmount') is not None:
            self.total_cost_amount = m.get('TotalCostAmount')

        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')

        return self

class DescribePriceResponseBodyOrderRuleIds(DaraModel):
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

class DescribePriceResponseBodyOrderDepreciateInfo(DaraModel):
    def __init__(
        self,
        cheap_rate: float = None,
        cheap_stand_amount: float = None,
        contract_activity: main_models.DescribePriceResponseBodyOrderDepreciateInfoContractActivity = None,
        differential: float = None,
        differential_name: str = None,
        is_contract_activity: bool = None,
        is_show: str = None,
        list_price: float = None,
        month_price: float = None,
        original_stand_amount: float = None,
    ):
        # The price reduction rate.
        self.cheap_rate = cheap_rate
        # The new total price displayed on the official website.
        self.cheap_stand_amount = cheap_stand_amount
        # The contract promotion.
        self.contract_activity = contract_activity
        # The price difference displayed in the total order amount.
        self.differential = differential
        # The name of the price difference.
        self.differential_name = differential_name
        # Indicates whether the contract promotion is hit.
        self.is_contract_activity = is_contract_activity
        # Indicates whether the price reduction rate is displayed.
        self.is_show = is_show
        # The list price.
        self.list_price = list_price
        # The monthly price.
        self.month_price = month_price
        # The original total price displayed on the official website.
        self.original_stand_amount = original_stand_amount

    def validate(self):
        if self.contract_activity:
            self.contract_activity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cheap_rate is not None:
            result['CheapRate'] = self.cheap_rate

        if self.cheap_stand_amount is not None:
            result['CheapStandAmount'] = self.cheap_stand_amount

        if self.contract_activity is not None:
            result['ContractActivity'] = self.contract_activity.to_map()

        if self.differential is not None:
            result['Differential'] = self.differential

        if self.differential_name is not None:
            result['DifferentialName'] = self.differential_name

        if self.is_contract_activity is not None:
            result['IsContractActivity'] = self.is_contract_activity

        if self.is_show is not None:
            result['IsShow'] = self.is_show

        if self.list_price is not None:
            result['ListPrice'] = self.list_price

        if self.month_price is not None:
            result['MonthPrice'] = self.month_price

        if self.original_stand_amount is not None:
            result['OriginalStandAmount'] = self.original_stand_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheapRate') is not None:
            self.cheap_rate = m.get('CheapRate')

        if m.get('CheapStandAmount') is not None:
            self.cheap_stand_amount = m.get('CheapStandAmount')

        if m.get('ContractActivity') is not None:
            temp_model = main_models.DescribePriceResponseBodyOrderDepreciateInfoContractActivity()
            self.contract_activity = temp_model.from_map(m.get('ContractActivity'))

        if m.get('Differential') is not None:
            self.differential = m.get('Differential')

        if m.get('DifferentialName') is not None:
            self.differential_name = m.get('DifferentialName')

        if m.get('IsContractActivity') is not None:
            self.is_contract_activity = m.get('IsContractActivity')

        if m.get('IsShow') is not None:
            self.is_show = m.get('IsShow')

        if m.get('ListPrice') is not None:
            self.list_price = m.get('ListPrice')

        if m.get('MonthPrice') is not None:
            self.month_price = m.get('MonthPrice')

        if m.get('OriginalStandAmount') is not None:
            self.original_stand_amount = m.get('OriginalStandAmount')

        return self

class DescribePriceResponseBodyOrderDepreciateInfoContractActivity(DaraModel):
    def __init__(
        self,
        activity_id: int = None,
        activity_name: str = None,
        final_fee: float = None,
        final_prom_fee: float = None,
        option_code: str = None,
        option_ids: main_models.DescribePriceResponseBodyOrderDepreciateInfoContractActivityOptionIds = None,
        prod_fee: float = None,
    ):
        # The activity ID.
        self.activity_id = activity_id
        # The activity name.
        self.activity_name = activity_name
        # The price after the promotion.
        self.final_fee = final_fee
        # The total discount amount.
        self.final_prom_fee = final_prom_fee
        # The promotion ID.
        self.option_code = option_code
        # The promotion IDs.
        self.option_ids = option_ids
        # The original price.
        self.prod_fee = prod_fee

    def validate(self):
        if self.option_ids:
            self.option_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.final_fee is not None:
            result['FinalFee'] = self.final_fee

        if self.final_prom_fee is not None:
            result['FinalPromFee'] = self.final_prom_fee

        if self.option_code is not None:
            result['OptionCode'] = self.option_code

        if self.option_ids is not None:
            result['OptionIds'] = self.option_ids.to_map()

        if self.prod_fee is not None:
            result['ProdFee'] = self.prod_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('FinalFee') is not None:
            self.final_fee = m.get('FinalFee')

        if m.get('FinalPromFee') is not None:
            self.final_prom_fee = m.get('FinalPromFee')

        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')

        if m.get('OptionIds') is not None:
            temp_model = main_models.DescribePriceResponseBodyOrderDepreciateInfoContractActivityOptionIds()
            self.option_ids = temp_model.from_map(m.get('OptionIds'))

        if m.get('ProdFee') is not None:
            self.prod_fee = m.get('ProdFee')

        return self

class DescribePriceResponseBodyOrderDepreciateInfoContractActivityOptionIds(DaraModel):
    def __init__(
        self,
        option_id: List[int] = None,
    ):
        self.option_id = option_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.option_id is not None:
            result['OptionId'] = self.option_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionId') is not None:
            self.option_id = m.get('OptionId')

        return self

class DescribePriceResponseBodyOrderCoupons(DaraModel):
    def __init__(
        self,
        coupon: List[main_models.DescribePriceResponseBodyOrderCouponsCoupon] = None,
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
                temp_model = main_models.DescribePriceResponseBodyOrderCouponsCoupon()
                self.coupon.append(temp_model.from_map(k1))

        return self

class DescribePriceResponseBodyOrderCouponsCoupon(DaraModel):
    def __init__(
        self,
        activity_category: str = None,
        coupon_no: str = None,
        description: str = None,
        is_selected: str = None,
        name: str = None,
        option_code: str = None,
        promotion_option_code: str = None,
        promotion_rule_id_list: main_models.DescribePriceResponseBodyOrderCouponsCouponPromotionRuleIdList = None,
    ):
        # The activity type of the coupon. Valid values:
        # 
        # *   **payondemand**: subscription
        # *   **payasyougo**: pay-as-you-go
        self.activity_category = activity_category
        # The coupon ID.
        self.coupon_no = coupon_no
        # The description of the coupon.
        self.description = description
        # Indicates whether the coupon was selected. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_selected = is_selected
        # The coupon name.
        self.name = name
        # The code of the coupon.
        self.option_code = option_code
        # The promotional option code.
        self.promotion_option_code = promotion_option_code
        # The IDs of the rules that correspond to the coupon.
        self.promotion_rule_id_list = promotion_rule_id_list

    def validate(self):
        if self.promotion_rule_id_list:
            self.promotion_rule_id_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_category is not None:
            result['ActivityCategory'] = self.activity_category

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.description is not None:
            result['Description'] = self.description

        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected

        if self.name is not None:
            result['Name'] = self.name

        if self.option_code is not None:
            result['OptionCode'] = self.option_code

        if self.promotion_option_code is not None:
            result['PromotionOptionCode'] = self.promotion_option_code

        if self.promotion_rule_id_list is not None:
            result['PromotionRuleIdList'] = self.promotion_rule_id_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityCategory') is not None:
            self.activity_category = m.get('ActivityCategory')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')

        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')

        if m.get('PromotionRuleIdList') is not None:
            temp_model = main_models.DescribePriceResponseBodyOrderCouponsCouponPromotionRuleIdList()
            self.promotion_rule_id_list = temp_model.from_map(m.get('PromotionRuleIdList'))

        return self

class DescribePriceResponseBodyOrderCouponsCouponPromotionRuleIdList(DaraModel):
    def __init__(
        self,
        promotion_rule_id: List[int] = None,
    ):
        self.promotion_rule_id = promotion_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.promotion_rule_id is not None:
            result['PromotionRuleId'] = self.promotion_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionRuleId') is not None:
            self.promotion_rule_id = m.get('PromotionRuleId')

        return self

