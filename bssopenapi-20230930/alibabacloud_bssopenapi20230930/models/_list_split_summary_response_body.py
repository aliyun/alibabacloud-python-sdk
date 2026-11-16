# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class ListSplitSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListSplitSummaryResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The array of split bill summary records returned in this request. This array may be empty if no matching records are found.
        self.data = data
        # The maximum number of records per page used in this query.
        self.max_results = max_results
        # The token for querying the next page. If it is not empty, use it as the NextToken for the next request. If it is empty or not returned, the pagination ends. Even if the number of returned records is less than MaxResults or the current page is empty, you must continue to query as long as the token is not empty.
        self.next_token = next_token
        # The unique identifier of the request, which is used to locate the request.
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
                temp_model = main_models.ListSplitSummaryResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSplitSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        amount_after_coupon_deduction: str = None,
        amount_after_promotion_deduction: str = None,
        amount_after_saving_plan_deduction: str = None,
        billing_date: str = None,
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
        cost_categories: str = None,
        coupon_amount: str = None,
        currency: str = None,
        finance_unit_name: str = None,
        hash_key: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_spec: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
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
        resource_group: str = None,
        resource_id: str = None,
        resource_owner_account_id: str = None,
        resource_owner_account_name: str = None,
        resource_purchase_account_id: str = None,
        resource_purchase_account_name: str = None,
        resource_tag: str = None,
        saving_plan_deduct_amount: str = None,
        saving_plan_deduct_list_price: str = None,
        service_entity: str = None,
        split_item_id: str = None,
        split_item_name: str = None,
        zone: str = None,
    ):
        # The amount after coupon deduction, which equals AmountAfterPromotionDeduction minus CouponAmount.
        self.amount_after_coupon_deduction = amount_after_coupon_deduction
        # The amount after discount, which is the amount after official website discounts and contract discounts are applied, but before coupon deductions. When the savings plan deduction data is complete, this equals ListPrice minus SavingPlanDeductListPrice minus PromotionAmount. When the savings plan deduction list price is unavailable, this is calculated as ListPrice minus PromotionAmount.
        self.amount_after_promotion_deduction = amount_after_promotion_deduction
        # The amount after savings plan deduction, which equals ListPrice minus SavingPlanDeductListPrice. This may be empty when there is no savings plan deduction data.
        self.amount_after_saving_plan_deduction = amount_after_saving_plan_deduction
        # The billing date, which is the date when the user consumed the cloud service. The format is yyyy-MM-dd. This has a value only when the data is summarized by day.
        self.billing_date = billing_date
        # The billing item code, which is the billing item to which the cloud resource expense belongs. Whether this field has a value depends on the split bill records and summary data.
        self.billing_item_code = billing_item_code
        # The billing item name.
        self.billing_item_name = billing_item_name
        # The billing month, which is the month to which the expense belongs. The format is yyyy-MM.
        self.billing_month = billing_month
        # The usage, which is the total usage that is ultimately billed. This must be understood in combination with the product, billing item, and unit. Do not directly add up the values if the units or billing rules are different.
        self.billing_quantity = billing_quantity
        # The unit of usage, used in conjunction with BillingQuantity.
        self.billing_quantity_unit = billing_quantity_unit
        # The total duration of purchasing or using cloud products. This field is used when the corresponding billing method includes a duration.
        self.charge_duration = charge_duration
        # The unit of duration, used in conjunction with ChargeDuration.
        self.charge_duration_unit = charge_duration_unit
        # The display name of the billing method, returned based on the request language, such as Subscription or Pay-as-you-go. Use Subscription or PayAsYouGo for filtering.
        self.charge_type = charge_type
        # The commodity code, which is the unique identifier of a specific commodity under a cloud service.
        self.commodity_code = commodity_code
        # The commodity name.
        self.commodity_name = commodity_name
        # The display name of the transaction type, which identifies the transaction corresponding to the bill, such as new purchase, renewal, upgrade, downgrade, unsubscription, pay-as-you-go, and adjustment. Do not use the display name as the ConsumeType filter code.
        self.consume_type = consume_type
        # The cost category, which indicates the cost category and category value to which the record belongs. It is returned as a string. The specific content is subject to the bill record and can be empty.
        self.cost_categories = cost_categories
        # The coupon deduction amount. This amount cannot be used for invoicing.
        self.coupon_amount = coupon_amount
        # The currency corresponding to the amounts and prices.
        self.currency = currency
        # The name of the financial unit. A financial unit is a unit used to group or classify expenses and must be maintained by the user.
        self.finance_unit_name = finance_unit_name
        # The identifier of the summary record, used as an opaque string. This can be empty. The identifier may change when summary dimensions such as resource groups and tags change.
        self.hash_key = hash_key
        # The instance ID at the billing granularity, which is the dimension for expense statistics and summary when a cloud service generates a bill. This may be different from the resource ID.
        self.instance_id = instance_id
        # The resource name, which is the custom name given to the cloud resource by the user. Whether this field has a value depends on whether the product and resource information can be obtained.
        self.instance_name = instance_name
        # The specification, which describes the specification of the resource or billing item associated with this record.
        self.instance_spec = instance_spec
        # The public IP address. This is returned only when the product supports it and the relevant resource information can be obtained.
        self.internet_ip = internet_ip
        # The private IP address. This is returned only when the product supports it and the relevant resource information can be obtained.
        self.intranet_ip = intranet_ip
        # The display name of the expense type, which identifies the nature of the expense generated by the bill, such as subscription prepaid expense, subscription unsubscription expense, pay-as-you-go expense for cloud resources, adjustment expense, and round-down expense. Do not use the display name as the LineItemType filter code.
        self.line_item_type = line_item_type
        # The total list price, which is the total list price of the selected configuration.
        self.list_price = list_price
        # The price unit, used in conjunction with ListUnitPrice.
        self.list_price_unit = list_price_unit
        # The list price on the official website, which is the list unit price of the commodity. Whether this field has a value depends on the split bill and summary data. Do not multiply the total usage by a unit price to recalculate all bills.
        self.list_unit_price = list_unit_price
        # The product code, which is the unique identifier of a specific cloud service on Alibaba Cloud.
        self.product_code = product_code
        # The product name.
        self.product_name = product_name
        # The discount amount, which is the total discount amount on the bill, including official website discounts and contract discounts.
        self.promotion_amount = promotion_amount
        # The purchase configuration of the billing item, which describes the configurations related to the billing item.
        self.purchase_configuration = purchase_configuration
        # The region code, which is the logical region code where the cloud resource is located.
        self.region_code = region_code
        # The region name, which indicates the region selected when the order was placed.
        self.region_name = region_name
        # The payable amount (tax-inclusive), which is the actual amount the user needs to pay after various discounts, savings plan deductions, and coupon deductions are applied. When all amount fields are complete, this equals ListPrice minus SavingPlanDeductListPrice minus PromotionAmount minus CouponAmount. Use this field for expense verification. If other amount fields are missing, do not treat empty values as zero to calculate the payable amount.
        self.require_amount = require_amount
        # The resource group, which is the group where cloud resources are located as configured by the user in the Resource Management console.
        self.resource_group = resource_group
        # The resource ID, which is the identifier used to uniquely identify a resource in a cloud service.
        self.resource_id = resource_id
        # The ID of the resource ownership account, which is the ID of the account that actually uses the resource and may differ from the purchasing account.
        self.resource_owner_account_id = resource_owner_account_id
        # The name of the resource ownership account.
        self.resource_owner_account_name = resource_owner_account_name
        # The ID of the resource purchaser account, which is the ID of the account that purchases the resource.
        self.resource_purchase_account_id = resource_purchase_account_id
        # The name of the resource purchaser account.
        self.resource_purchase_account_name = resource_purchase_account_name
        # The resource tag, which is the custom tag added by the user to Alibaba Cloud resources. It is returned as a string and can be empty.
        self.resource_tag = resource_tag
        # The savings plan deduction amount, which is the committed amount consumed by the savings plan itself. This has a different meaning from SavingPlanDeductListPrice, cannot be used interchangeably, and should not be deducted from the payable amount again.
        self.saving_plan_deduct_amount = saving_plan_deduct_amount
        # The total list price deducted by the savings plan, which is the total list price of the pay-as-you-go cloud resources deducted when a savings plan is applied.
        self.saving_plan_deduct_list_price = saving_plan_deduct_list_price
        # The service entity, which is the name of the company that provides the product or service. Alibaba Cloud sells a wide range of products, and some products may be provided by different companies.
        self.service_entity = service_entity
        # The split item ID, which is the code corresponding to the specific split granularity of the bill. For example, when OSS is split by bucket, this is the bucket code. This field may be empty for records that are not split.
        self.split_item_id = split_item_id
        # The split item name, which is the name corresponding to the specific split granularity of the bill.
        self.split_item_name = split_item_name
        # The zone. The display name may be returned.
        self.zone = zone

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

        if self.cost_categories is not None:
            result['CostCategories'] = self.cost_categories

        if self.coupon_amount is not None:
            result['CouponAmount'] = self.coupon_amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.finance_unit_name is not None:
            result['FinanceUnitName'] = self.finance_unit_name

        if self.hash_key is not None:
            result['HashKey'] = self.hash_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

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

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

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

        if self.resource_tag is not None:
            result['ResourceTag'] = self.resource_tag

        if self.saving_plan_deduct_amount is not None:
            result['SavingPlanDeductAmount'] = self.saving_plan_deduct_amount

        if self.saving_plan_deduct_list_price is not None:
            result['SavingPlanDeductListPrice'] = self.saving_plan_deduct_list_price

        if self.service_entity is not None:
            result['ServiceEntity'] = self.service_entity

        if self.split_item_id is not None:
            result['SplitItemId'] = self.split_item_id

        if self.split_item_name is not None:
            result['SplitItemName'] = self.split_item_name

        if self.zone is not None:
            result['Zone'] = self.zone

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

        if m.get('CostCategories') is not None:
            self.cost_categories = m.get('CostCategories')

        if m.get('CouponAmount') is not None:
            self.coupon_amount = m.get('CouponAmount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('FinanceUnitName') is not None:
            self.finance_unit_name = m.get('FinanceUnitName')

        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

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

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

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

        if m.get('ResourceTag') is not None:
            self.resource_tag = m.get('ResourceTag')

        if m.get('SavingPlanDeductAmount') is not None:
            self.saving_plan_deduct_amount = m.get('SavingPlanDeductAmount')

        if m.get('SavingPlanDeductListPrice') is not None:
            self.saving_plan_deduct_list_price = m.get('SavingPlanDeductListPrice')

        if m.get('ServiceEntity') is not None:
            self.service_entity = m.get('ServiceEntity')

        if m.get('SplitItemId') is not None:
            self.split_item_id = m.get('SplitItemId')

        if m.get('SplitItemName') is not None:
            self.split_item_name = m.get('SplitItemName')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

