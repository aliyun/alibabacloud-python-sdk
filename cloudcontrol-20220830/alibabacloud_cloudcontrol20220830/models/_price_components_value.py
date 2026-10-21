# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudcontrol20220830 import models as main_models
from darabonba.model import DaraModel

class PriceComponentsValue(DaraModel):
    def __init__(
        self,
        charge_composition: str = None,
        currency: str = None,
        effective_module_sum: float = None,
        module_sum: float = None,
        modules: List[main_models.PriceComponentsValueModules] = None,
        original_price: float = None,
        pricing_unit: str = None,
        quantity: float = None,
        trade_price: float = None,
        usage_charges: List[main_models.PriceComponentsValueUsageCharges] = None,
    ):
        # The billing composition. Valid values: recurring_only (all time-based fees), usage_only (all usage-based fees, where a totalAmount of 0 indicates no fixed fees rather than free of charge, and actual costs depend on the unit price and actual usage in usageCharges), or mixed (both, which should be displayed separately). This allows the caller to choose the display text without iterating through modules to determine the composition.
        self.charge_composition = charge_composition
        self.currency = currency
        self.effective_module_sum = effective_module_sum
        self.module_sum = module_sum
        self.modules = modules
        # The total original price before discounts for this pricing inquiry. When originalPrice differs from tradePrice or moduleSum, it indicates that a discount was applied, such as a first-purchase discount or a promotional campaign.
        self.original_price = original_price
        # The billing cycle unit, such as \\"Hour\\", \\"1 Month\\", \\"12 Month\\", or \\"GB·Month\\", which indicates the time dimension of moduleSum. This field is not returned in the BSS response and must be explicitly declared by the mapping maintainer in pricingTarget.pricingUnit. It is optional for subscription scenarios because the CLI infers it from Period and PeriodUnit. However, it is required for pay-as-you-go scenarios in the mapping; otherwise, the amount has no dimension.
        self.pricing_unit = pricing_unit
        # The pricing quantity from OpenAPI input parameters, such as Amount in ECS RunInstances. The moduleSum is the unit price per instance, and effectiveModuleSum = moduleSum × quantity is the total price. The caller should present the actual total price for N instances to the user based on this value to avoid mistaking the unit price for the total price.
        self.quantity = quantity
        self.trade_price = trade_price
        # The list of unit prices for pay-as-you-go, usage-based modules, such as CNY/GB or CNY/CU. The amounts for these modules are not included in moduleSum or effectiveModuleSum. This field is empty when there are no usage-based modules.
        self.usage_charges = usage_charges

    def validate(self):
        if self.modules:
            for v1 in self.modules:
                 if v1:
                    v1.validate()
        if self.usage_charges:
            for v1 in self.usage_charges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_composition is not None:
            result['chargeComposition'] = self.charge_composition

        if self.currency is not None:
            result['currency'] = self.currency

        if self.effective_module_sum is not None:
            result['effectiveModuleSum'] = self.effective_module_sum

        if self.module_sum is not None:
            result['moduleSum'] = self.module_sum

        result['modules'] = []
        if self.modules is not None:
            for k1 in self.modules:
                result['modules'].append(k1.to_map() if k1 else None)

        if self.original_price is not None:
            result['originalPrice'] = self.original_price

        if self.pricing_unit is not None:
            result['pricingUnit'] = self.pricing_unit

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.trade_price is not None:
            result['tradePrice'] = self.trade_price

        result['usageCharges'] = []
        if self.usage_charges is not None:
            for k1 in self.usage_charges:
                result['usageCharges'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeComposition') is not None:
            self.charge_composition = m.get('chargeComposition')

        if m.get('currency') is not None:
            self.currency = m.get('currency')

        if m.get('effectiveModuleSum') is not None:
            self.effective_module_sum = m.get('effectiveModuleSum')

        if m.get('moduleSum') is not None:
            self.module_sum = m.get('moduleSum')

        self.modules = []
        if m.get('modules') is not None:
            for k1 in m.get('modules'):
                temp_model = main_models.PriceComponentsValueModules()
                self.modules.append(temp_model.from_map(k1))

        if m.get('originalPrice') is not None:
            self.original_price = m.get('originalPrice')

        if m.get('pricingUnit') is not None:
            self.pricing_unit = m.get('pricingUnit')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('tradePrice') is not None:
            self.trade_price = m.get('tradePrice')

        self.usage_charges = []
        if m.get('usageCharges') is not None:
            for k1 in m.get('usageCharges'):
                temp_model = main_models.PriceComponentsValueUsageCharges()
                self.usage_charges.append(temp_model.from_map(k1))

        return self

class PriceComponentsValueUsageCharges(DaraModel):
    def __init__(
        self,
        assumed_quantity: float = None,
        assumed_quantity_cost: float = None,
        module_code: str = None,
        original_price_per_unit: float = None,
        price_per_unit: float = None,
        unit: str = None,
    ):
        # The estimated usage passed by the caller through PricingContext. This field has a value only when it is greater than 1. In this case, this entry also provides the assumedQuantityCost calculated based on this assumed usage.
        self.assumed_quantity = assumed_quantity
        # The module cost calculated based on assumedQuantity, which equals pricePerUnit × assumedQuantity. This cost is not included in totalAmount because it is based on the assumed usage reported by the caller and is not a cost necessarily incurred by this call.
        self.assumed_quantity_cost = assumed_quantity_cost
        # The billing module code, such as TrafficOut or NatCu. This corresponds to the moduleCode in modules.
        self.module_code = module_code
        # The original unit price before discounts, in CNY/unit, which is also normalized. This field is empty when not provided by the upstream. The difference between this value and pricePerUnit is the unit price discount for this module.
        self.original_price_per_unit = original_price_per_unit
        # The discounted unit price, in CNY/unit. The actual cost equals pricePerUnit × actual usage. Because the usage is unknown during pricing, it is not included in totalAmount. If the caller passed an estimated usage, the total returned by the upstream is normalized back to the unit price based on that usage.
        self.price_per_unit = price_per_unit
        # The usage unit, such as GB, CU, or 10,000 requests. This comes from the module-level billing.unit annotation in the mapping. The dimension of pricePerUnit is CNY/unit.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assumed_quantity is not None:
            result['assumedQuantity'] = self.assumed_quantity

        if self.assumed_quantity_cost is not None:
            result['assumedQuantityCost'] = self.assumed_quantity_cost

        if self.module_code is not None:
            result['moduleCode'] = self.module_code

        if self.original_price_per_unit is not None:
            result['originalPricePerUnit'] = self.original_price_per_unit

        if self.price_per_unit is not None:
            result['pricePerUnit'] = self.price_per_unit

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assumedQuantity') is not None:
            self.assumed_quantity = m.get('assumedQuantity')

        if m.get('assumedQuantityCost') is not None:
            self.assumed_quantity_cost = m.get('assumedQuantityCost')

        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')

        if m.get('originalPricePerUnit') is not None:
            self.original_price_per_unit = m.get('originalPricePerUnit')

        if m.get('pricePerUnit') is not None:
            self.price_per_unit = m.get('pricePerUnit')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self



class PriceComponentsValueModules(DaraModel):
    def __init__(
        self,
        billing_mode: str = None,
        cost_after_discount: float = None,
        invoice_discount: float = None,
        module_code: str = None,
        original_cost: float = None,
        quantity_used_for_quote: float = None,
        unit_price: float = None,
        usage_unit: str = None,
    ):
        # The billing dimension of this module, which is always explicitly output. Valid values: \\"recurring\\" for time-based fees, which are included in moduleSum and totalAmount; \\"usage\\" for usage-based fees, where costAfterDiscount is the usage unit price (CNY/usageUnit) and is not included in moduleSum, and the unit price is also provided in usageCharges.
        self.billing_mode = billing_mode
        self.cost_after_discount = cost_after_discount
        # The discount amount for this module. The value is calculated as invoiceDiscount = originalCost - costAfterDiscount and is precisely provided by the upstream BSS. Manual subtraction in tax-inclusive scenarios may cause precision loss.
        self.invoice_discount = invoice_discount
        self.module_code = module_code
        self.original_cost = original_cost
        # The estimated usage used for pricing this module. This field has a value only when the caller passes a usage greater than 1 through PricingContext. In this case, costAfterDiscount is the total cost for this usage rather than the unit price. Refer to usageCharges[].pricePerUnit for the normalized unit price. This field is empty when no estimated usage is passed.
        self.quantity_used_for_quote = quantity_used_for_quote
        # The unit price of this module per billing unit, such as CNY/hour, CNY/month, or CNY/unit. This is used to explain the composition of costAfterDiscount in multi-quantity or multi-period scenarios.
        self.unit_price = unit_price
        # The usage unit, such as GB or CU. This field has a value when billingMode is \\"usage\\" and indicates the dimension of costAfterDiscount.
        self.usage_unit = usage_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_mode is not None:
            result['billingMode'] = self.billing_mode

        if self.cost_after_discount is not None:
            result['costAfterDiscount'] = self.cost_after_discount

        if self.invoice_discount is not None:
            result['invoiceDiscount'] = self.invoice_discount

        if self.module_code is not None:
            result['moduleCode'] = self.module_code

        if self.original_cost is not None:
            result['originalCost'] = self.original_cost

        if self.quantity_used_for_quote is not None:
            result['quantityUsedForQuote'] = self.quantity_used_for_quote

        if self.unit_price is not None:
            result['unitPrice'] = self.unit_price

        if self.usage_unit is not None:
            result['usageUnit'] = self.usage_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMode') is not None:
            self.billing_mode = m.get('billingMode')

        if m.get('costAfterDiscount') is not None:
            self.cost_after_discount = m.get('costAfterDiscount')

        if m.get('invoiceDiscount') is not None:
            self.invoice_discount = m.get('invoiceDiscount')

        if m.get('moduleCode') is not None:
            self.module_code = m.get('moduleCode')

        if m.get('originalCost') is not None:
            self.original_cost = m.get('originalCost')

        if m.get('quantityUsedForQuote') is not None:
            self.quantity_used_for_quote = m.get('quantityUsedForQuote')

        if m.get('unitPrice') is not None:
            self.unit_price = m.get('unitPrice')

        if m.get('usageUnit') is not None:
            self.usage_unit = m.get('usageUnit')

        return self

