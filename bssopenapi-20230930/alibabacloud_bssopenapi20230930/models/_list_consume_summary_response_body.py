# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class ListConsumeSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListConsumeSummaryResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The consumption summary records returned in this request. An empty array is returned if no matching records are found.
        self.data = data
        # The maximum number of records per page used in this query.
        self.max_results = max_results
        # The query token for the next page. If a non-empty value is returned, pass it as is to the next request and keep other query conditions unchanged. If it is not returned or is empty, pagination ends.
        self.next_token = next_token
        # The unique identifier of the request, used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListConsumeSummaryResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListConsumeSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        amount_after_coupon_deduction: str = None,
        amount_after_promotion_deduction: str = None,
        amount_after_saving_plan_deduction: str = None,
        billing_date: str = None,
        billing_formula: str = None,
        billing_item_code: str = None,
        billing_item_name: str = None,
        billing_month: str = None,
        billing_quantity: str = None,
        billing_quantity_unit: str = None,
        charge_duration: str = None,
        charge_duration_unit: str = None,
        charge_type: str = None,
        commodity_code: str = None,
        commodity_name: str = None,
        consume_type: str = None,
        coupon_amount: str = None,
        currency: str = None,
        hash_key: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_spec: str = None,
        line_item_type: str = None,
        list_price: str = None,
        list_price_unit: str = None,
        list_unit_price: str = None,
        product_code: str = None,
        product_name: str = None,
        promotion_amount: str = None,
        purchase_configuration: str = None,
        region_code: str = None,
        region_name: str = None,
        require_amount: str = None,
        resource_id: str = None,
        resource_owner_account_id: str = None,
        resource_owner_account_name: str = None,
        resource_purchase_account_id: str = None,
        resource_purchase_account_name: str = None,
        saving_plan_deduct_amount: str = None,
        saving_plan_deduct_list_price: str = None,
        service_entity: str = None,
    ):
        # The amount after coupon deduction, which is the result of deducting coupons from the amount after discount. When all related fields are available, it equals AmountAfterPromotionDeduction - CouponAmount.
        self.amount_after_coupon_deduction = amount_after_coupon_deduction
        # The amount after discount, which represents the amount after applying discounts such as website promotions and contract discounts. Coupons are not deducted at this point. When all related fields are available, it equals AmountAfterSavingPlanDeduction - PromotionAmount.
        self.amount_after_promotion_deduction = amount_after_promotion_deduction
        # The amount after savings plan deduction, which is the remaining amount after deducting the list price portion covered by the savings plan. When all related fields are available, it equals ListPrice - SavingPlanDeductListPrice.
        self.amount_after_saving_plan_deduction = amount_after_saving_plan_deduction
        # The billing date, which is the consumption date of the cloud product, in the format of yyyy-MM-dd. It has a value only when summarized by day.
        self.billing_date = billing_date
        # The billing formula, which describes how the total list price is calculated. It should be understood in conjunction with the list price on the Alibaba Cloud website, usage, duration, and other billing factors.
        self.billing_formula = billing_formula
        # The billing item code, which identifies the billing item to which the fee belongs.
        self.billing_item_code = billing_item_code
        # The billing item name, which is the display name of the billing item to which the fee belongs.
        self.billing_item_name = billing_item_name
        # The billing month, which represents the billing month to which the fee belongs, in the format of yyyy-MM.
        self.billing_month = billing_month
        # The usage that is ultimately used for fee calculation. If usage deduction is applied, this value is the usage before deduction minus the usage deducted by resource plans, free quotas, and other deductions.
        self.billing_quantity = billing_quantity
        # The usage unit, used in conjunction with BillingQuantity.
        self.billing_quantity_unit = billing_quantity_unit
        # The duration, which represents the purchase or usage duration involved in billing. It has a value only when the billing formula involves time. If duration deduction is applied, this value is the duration before deduction minus the deducted duration.
        self.charge_duration = charge_duration
        # The duration unit, used in conjunction with ChargeDuration.
        self.charge_duration_unit = charge_duration_unit
        # The billing method. The display name such as prepaid or pay-as-you-go is returned.
        self.charge_type = charge_type
        # The commodity code, used to uniquely identify a specific commodity under a cloud product.
        self.commodity_code = commodity_code
        # The commodity name, which is the display name of a specific commodity under a cloud product.
        self.commodity_name = commodity_name
        # The transaction type, which describes the transaction behavior that generated the bill, such as new purchase, renewal, upgrade, downgrade, unsubscription, pay-as-you-go, or adjustment. The display name is returned.
        self.consume_type = consume_type
        # The coupon deduction amount, which is the fee covered by coupons. This amount cannot be used for invoicing.
        self.coupon_amount = coupon_amount
        # The currency, which represents the currency used for the list price and amounts in this record. For example, CNY indicates Chinese Yuan.
        self.currency = currency
        # The summary record identifier, used as an opaque string. It can be empty.
        self.hash_key = hash_key
        # The instance ID at the billing granularity, which represents the instance identity used to aggregate fees when a cloud product generates a bill. The billing granularity may differ from the resource management granularity, so it may be different from ResourceId.
        self.instance_id = instance_id
        # The resource name, which is the name set by the user for the cloud resource. Whether it is returned depends on whether the product supports querying and whether the resource information is available.
        self.instance_name = instance_name
        # The specification, used to describe the specification information corresponding to the billing item.
        self.instance_spec = instance_spec
        # The line item type, which describes the nature of the fee, such as subscription prepaid fee, subscription postpaid fee, subscription unsubscription fee, pay-as-you-go fee for cloud resources, adjustment fee, or rounding fee. The display name is returned.
        self.line_item_type = line_item_type
        # The total list price, which represents the total amount calculated based on the list price for the purchased cloud resource configuration. Savings plan deductions, discounts, and coupons are not deducted yet. Note that ListPrice in this API is the total amount. For the list unit price, see ListUnitPrice.
        self.list_price = list_price
        # The price unit, which is the unit corresponding to the list unit price ListUnitPrice, such as CNY/GB.
        self.list_price_unit = list_price_unit
        # The list price on the Alibaba Cloud website, which is the list unit price of the commodity. It differs in meaning from the total list price ListPrice. In scenarios such as tiered pricing, you cannot recalculate the fee by simply multiplying a single unit price by the total usage.
        self.list_unit_price = list_unit_price
        # The product code, used to uniquely identify a specific cloud product.
        self.product_code = product_code
        # The product name, which is the display name of the cloud product.
        self.product_name = product_name
        # The discount amount, which represents the total discounts such as website promotions and contract discounts. Coupon deductions are separately recorded in CouponAmount.
        self.promotion_amount = promotion_amount
        # The configuration, used to describe the configuration options corresponding to the billing item.
        self.purchase_configuration = purchase_configuration
        # The region code, which represents the code of the logical region where the cloud resource is located.
        self.region_code = region_code
        # The region, which represents the display name of the region where the cloud resource is located. For products sold by region, it usually corresponds to the region selected when placing the order.
        self.region_name = region_name
        # The payable amount, which is the fee to be paid after savings plan deductions, discounts, and coupon deductions. In the new version of bills, this corresponds to the payable amount (tax-inclusive) definition. For fee verification, refer to the actual return value of this field.
        self.require_amount = require_amount
        # The resource ID, used to uniquely identify a cloud resource in the corresponding cloud product or service.
        self.resource_id = resource_id
        # The resource ownership account ID, which is the ID of the account that actually uses the cloud resource instance. It may be different from the purchasing account.
        self.resource_owner_account_id = resource_owner_account_id
        # The resource ownership account, which is the name of the account that actually uses the cloud resource instance. It may be different from the purchasing account.
        self.resource_owner_account_name = resource_owner_account_name
        # The ID of the resource purchasing account, which is the ID of the account that placed the order to purchase the cloud resource instance.
        self.resource_purchase_account_id = resource_purchase_account_id
        # The resource purchasing account, which is the name of the account that placed the order to purchase the cloud resource instance.
        self.resource_purchase_account_name = resource_purchase_account_name
        # The savings plan deduction amount, which is the committed spend of the savings plan consumed to complete this deduction. It is not the list price amount of the deducted resource and cannot replace SavingPlanDeductListPrice for deduction from the total list price.
        self.saving_plan_deduct_amount = saving_plan_deduct_amount
        # The savings plan deduction list price, which is the amount calculated based on the list price for the pay-as-you-go resource fees deducted by the savings plan.
        self.saving_plan_deduct_list_price = saving_plan_deduct_list_price
        # The service entity, which is the name of the company that actually provides the product or service. Different products may correspond to different companies.
        self.service_entity = service_entity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount_after_coupon_deduction is not None:
            result['AmountAfterCouponDeduction'] = self.amount_after_coupon_deduction

        if self.amount_after_promotion_deduction is not None:
            result['AmountAfterPromotionDeduction'] = self.amount_after_promotion_deduction

        if self.amount_after_saving_plan_deduction is not None:
            result['AmountAfterSavingPlanDeduction'] = self.amount_after_saving_plan_deduction

        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date

        if self.billing_formula is not None:
            result['BillingFormula'] = self.billing_formula

        if self.billing_item_code is not None:
            result['BillingItemCode'] = self.billing_item_code

        if self.billing_item_name is not None:
            result['BillingItemName'] = self.billing_item_name

        if self.billing_month is not None:
            result['BillingMonth'] = self.billing_month

        if self.billing_quantity is not None:
            result['BillingQuantity'] = self.billing_quantity

        if self.billing_quantity_unit is not None:
            result['BillingQuantityUnit'] = self.billing_quantity_unit

        if self.charge_duration is not None:
            result['ChargeDuration'] = self.charge_duration

        if self.charge_duration_unit is not None:
            result['ChargeDurationUnit'] = self.charge_duration_unit

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        if self.consume_type is not None:
            result['ConsumeType'] = self.consume_type

        if self.coupon_amount is not None:
            result['CouponAmount'] = self.coupon_amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.hash_key is not None:
            result['HashKey'] = self.hash_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.line_item_type is not None:
            result['LineItemType'] = self.line_item_type

        if self.list_price is not None:
            result['ListPrice'] = self.list_price

        if self.list_price_unit is not None:
            result['ListPriceUnit'] = self.list_price_unit

        if self.list_unit_price is not None:
            result['ListUnitPrice'] = self.list_unit_price

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.promotion_amount is not None:
            result['PromotionAmount'] = self.promotion_amount

        if self.purchase_configuration is not None:
            result['PurchaseConfiguration'] = self.purchase_configuration

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.require_amount is not None:
            result['RequireAmount'] = self.require_amount

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_account_id is not None:
            result['ResourceOwnerAccountId'] = self.resource_owner_account_id

        if self.resource_owner_account_name is not None:
            result['ResourceOwnerAccountName'] = self.resource_owner_account_name

        if self.resource_purchase_account_id is not None:
            result['ResourcePurchaseAccountId'] = self.resource_purchase_account_id

        if self.resource_purchase_account_name is not None:
            result['ResourcePurchaseAccountName'] = self.resource_purchase_account_name

        if self.saving_plan_deduct_amount is not None:
            result['SavingPlanDeductAmount'] = self.saving_plan_deduct_amount

        if self.saving_plan_deduct_list_price is not None:
            result['SavingPlanDeductListPrice'] = self.saving_plan_deduct_list_price

        if self.service_entity is not None:
            result['ServiceEntity'] = self.service_entity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AmountAfterCouponDeduction') is not None:
            self.amount_after_coupon_deduction = m.get('AmountAfterCouponDeduction')

        if m.get('AmountAfterPromotionDeduction') is not None:
            self.amount_after_promotion_deduction = m.get('AmountAfterPromotionDeduction')

        if m.get('AmountAfterSavingPlanDeduction') is not None:
            self.amount_after_saving_plan_deduction = m.get('AmountAfterSavingPlanDeduction')

        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')

        if m.get('BillingFormula') is not None:
            self.billing_formula = m.get('BillingFormula')

        if m.get('BillingItemCode') is not None:
            self.billing_item_code = m.get('BillingItemCode')

        if m.get('BillingItemName') is not None:
            self.billing_item_name = m.get('BillingItemName')

        if m.get('BillingMonth') is not None:
            self.billing_month = m.get('BillingMonth')

        if m.get('BillingQuantity') is not None:
            self.billing_quantity = m.get('BillingQuantity')

        if m.get('BillingQuantityUnit') is not None:
            self.billing_quantity_unit = m.get('BillingQuantityUnit')

        if m.get('ChargeDuration') is not None:
            self.charge_duration = m.get('ChargeDuration')

        if m.get('ChargeDurationUnit') is not None:
            self.charge_duration_unit = m.get('ChargeDurationUnit')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        if m.get('ConsumeType') is not None:
            self.consume_type = m.get('ConsumeType')

        if m.get('CouponAmount') is not None:
            self.coupon_amount = m.get('CouponAmount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('LineItemType') is not None:
            self.line_item_type = m.get('LineItemType')

        if m.get('ListPrice') is not None:
            self.list_price = m.get('ListPrice')

        if m.get('ListPriceUnit') is not None:
            self.list_price_unit = m.get('ListPriceUnit')

        if m.get('ListUnitPrice') is not None:
            self.list_unit_price = m.get('ListUnitPrice')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('PromotionAmount') is not None:
            self.promotion_amount = m.get('PromotionAmount')

        if m.get('PurchaseConfiguration') is not None:
            self.purchase_configuration = m.get('PurchaseConfiguration')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('RequireAmount') is not None:
            self.require_amount = m.get('RequireAmount')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerAccountId') is not None:
            self.resource_owner_account_id = m.get('ResourceOwnerAccountId')

        if m.get('ResourceOwnerAccountName') is not None:
            self.resource_owner_account_name = m.get('ResourceOwnerAccountName')

        if m.get('ResourcePurchaseAccountId') is not None:
            self.resource_purchase_account_id = m.get('ResourcePurchaseAccountId')

        if m.get('ResourcePurchaseAccountName') is not None:
            self.resource_purchase_account_name = m.get('ResourcePurchaseAccountName')

        if m.get('SavingPlanDeductAmount') is not None:
            self.saving_plan_deduct_amount = m.get('SavingPlanDeductAmount')

        if m.get('SavingPlanDeductListPrice') is not None:
            self.saving_plan_deduct_list_price = m.get('SavingPlanDeductListPrice')

        if m.get('ServiceEntity') is not None:
            self.service_entity = m.get('ServiceEntity')

        return self

