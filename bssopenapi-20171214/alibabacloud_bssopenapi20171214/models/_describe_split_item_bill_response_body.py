# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeSplitItemBillResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSplitItemBillResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeSplitItemBillResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSplitItemBillResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        billing_cycle: str = None,
        items: List[main_models.DescribeSplitItemBillResponseBodyDataItems] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The ID of the account.
        self.account_id = account_id
        # The ID of the account.
        self.account_name = account_name
        # The billing cycle. Format: YYYY-MM.
        self.billing_cycle = billing_cycle
        # The details of the bill.
        self.items = items
        # The maximum number of entries returned.
        self.max_results = max_results
        # The token used for the next query. If this parameter is empty, all the results are returned. When you perform the next query, you must set the NextToken parameter to this value.
        self.next_token = next_token
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountID'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeSplitItemBillResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSplitItemBillResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        adjust_amount: float = None,
        after_discount_amount: float = None,
        bill_account_id: str = None,
        bill_account_name: str = None,
        billing_date: str = None,
        billing_item: str = None,
        billing_item_code: str = None,
        billing_type: str = None,
        biz_type: str = None,
        cash_amount: float = None,
        commodity_code: str = None,
        cost_unit: str = None,
        currency: str = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        deducted_by_resource_package: str = None,
        instance_config: str = None,
        instance_id: str = None,
        instance_spec: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        invoice_discount: float = None,
        item: str = None,
        item_name: str = None,
        list_price: str = None,
        list_price_unit: str = None,
        nick_name: str = None,
        outstanding_amount: float = None,
        owner_id: str = None,
        payment_amount: float = None,
        pip_code: str = None,
        pretax_amount: float = None,
        pretax_gross_amount: float = None,
        product_code: str = None,
        product_detail: str = None,
        product_name: str = None,
        product_type: str = None,
        region: str = None,
        resource_group: str = None,
        service_period: str = None,
        service_period_unit: str = None,
        split_account_id: str = None,
        split_account_name: str = None,
        split_billing_cycle: str = None,
        split_billing_date: str = None,
        split_commodity_code: str = None,
        split_item_id: str = None,
        split_item_name: str = None,
        split_product_detail: str = None,
        subscription_type: str = None,
        tag: str = None,
        usage: str = None,
        usage_unit: str = None,
        zone: str = None,
    ):
        # The amount deducted with credit refund.
        self.adjust_amount = adjust_amount
        self.after_discount_amount = after_discount_amount
        # The ID of the account to which the bill belongs.
        self.bill_account_id = bill_account_id
        # The name of the account to which the bill belongs.
        self.bill_account_name = bill_account_name
        # The billing date. Format: YYYY-MM-DD. This parameter is not supported.
        self.billing_date = billing_date
        # The billable item.
        self.billing_item = billing_item
        # The code of the billable item.
        self.billing_item_code = billing_item_code
        # The billing method.
        self.billing_type = billing_type
        # The type of the business.
        self.biz_type = biz_type
        # The amount paid in cash. The amount deducted with credit refund is not included.
        self.cash_amount = cash_amount
        # The code of the commodity. The code is the same as that displayed in the Split Bill module of the User Center console.
        self.commodity_code = commodity_code
        # The cost center.
        self.cost_unit = cost_unit
        # The type of currency. Valid values: CNY, USD, and JPY.
        self.currency = currency
        # The amount deducted with vouchers.
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        # The amount deducted with coupons.
        self.deducted_by_coupons = deducted_by_coupons
        # The amount deducted with prepaid cards.
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        # The amount deducted with resource plans.
        self.deducted_by_resource_package = deducted_by_resource_package
        # The configurations of the instance.
        self.instance_config = instance_config
        # The ID of the instance.
        self.instance_id = instance_id
        # The type of the instance.
        self.instance_spec = instance_spec
        # The public IP address.
        self.internet_ip = internet_ip
        # The private IP address.
        self.intranet_ip = intranet_ip
        # The discount amount.
        self.invoice_discount = invoice_discount
        # The type of the bill. Valid values: SubscriptionOrder: the subscription bill. PayAsYouGoBill: the pay-as-you-go bill. Refund: the refund. Adjustment: the adjustment bill.
        self.item = item
        # The name of the split item.
        self.item_name = item_name
        # The unit price.
        self.list_price = list_price
        # The unit of the unit price.
        self.list_price_unit = list_price_unit
        # The name of the instance.
        self.nick_name = nick_name
        # The amount that is unsettled.
        self.outstanding_amount = outstanding_amount
        # The ID of the account that owns the resource. This parameter is returned in multi-account scenario.
        self.owner_id = owner_id
        # The amount paid in cash. The amount deducted with credit refund is included.
        self.payment_amount = payment_amount
        # The code of the service. The code is the same as that displayed in the Split Bill module of the User Center console.
        self.pip_code = pip_code
        # The pretax amount.
        self.pretax_amount = pretax_amount
        # The pretax gross amount.
        self.pretax_gross_amount = pretax_gross_amount
        # The code of the service.
        self.product_code = product_code
        # The details of the service.
        self.product_detail = product_detail
        # The name of the service.
        self.product_name = product_name
        # The type of the service.
        self.product_type = product_type
        # The ID of the region.
        self.region = region
        # The ID of the resource group.
        self.resource_group = resource_group
        # The duration of the service.
        self.service_period = service_period
        # The unit of the service duration.
        self.service_period_unit = service_period_unit
        # The ID of the account to which the split bill belongs.
        self.split_account_id = split_account_id
        # The name of the account to which the split item belongs.
        self.split_account_name = split_account_name
        # The billing cycle in which the bill is split.
        self.split_billing_cycle = split_billing_cycle
        # The day on which the bill is split.
        self.split_billing_date = split_billing_date
        # The code of the split item.
        self.split_commodity_code = split_commodity_code
        # The ID of the split item.
        self.split_item_id = split_item_id
        # The name of the split item.
        self.split_item_name = split_item_name
        # The details of the service.
        self.split_product_detail = split_product_detail
        # The billing method. Valid values: Subscription: the subscription billing method. PayAsYouGo: the pay-as-you-go billing method.
        self.subscription_type = subscription_type
        # The tag of the resource. If tags added to resources change, the bills generated during the period in which resources and tags are associated are returned.
        self.tag = tag
        # The amount of resource usage.
        self.usage = usage
        # The unit of usage.
        self.usage_unit = usage_unit
        # The zone.
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjust_amount is not None:
            result['AdjustAmount'] = self.adjust_amount

        if self.after_discount_amount is not None:
            result['AfterDiscountAmount'] = self.after_discount_amount

        if self.bill_account_id is not None:
            result['BillAccountID'] = self.bill_account_id

        if self.bill_account_name is not None:
            result['BillAccountName'] = self.bill_account_name

        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date

        if self.billing_item is not None:
            result['BillingItem'] = self.billing_item

        if self.billing_item_code is not None:
            result['BillingItemCode'] = self.billing_item_code

        if self.billing_type is not None:
            result['BillingType'] = self.billing_type

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.cash_amount is not None:
            result['CashAmount'] = self.cash_amount

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons

        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons

        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card

        if self.deducted_by_resource_package is not None:
            result['DeductedByResourcePackage'] = self.deducted_by_resource_package

        if self.instance_config is not None:
            result['InstanceConfig'] = self.instance_config

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.internet_ip is not None:
            result['InternetIP'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIP'] = self.intranet_ip

        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount

        if self.item is not None:
            result['Item'] = self.item

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        if self.list_price is not None:
            result['ListPrice'] = self.list_price

        if self.list_price_unit is not None:
            result['ListPriceUnit'] = self.list_price_unit

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount

        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id

        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount

        if self.pip_code is not None:
            result['PipCode'] = self.pip_code

        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount

        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.service_period is not None:
            result['ServicePeriod'] = self.service_period

        if self.service_period_unit is not None:
            result['ServicePeriodUnit'] = self.service_period_unit

        if self.split_account_id is not None:
            result['SplitAccountID'] = self.split_account_id

        if self.split_account_name is not None:
            result['SplitAccountName'] = self.split_account_name

        if self.split_billing_cycle is not None:
            result['SplitBillingCycle'] = self.split_billing_cycle

        if self.split_billing_date is not None:
            result['SplitBillingDate'] = self.split_billing_date

        if self.split_commodity_code is not None:
            result['SplitCommodityCode'] = self.split_commodity_code

        if self.split_item_id is not None:
            result['SplitItemID'] = self.split_item_id

        if self.split_item_name is not None:
            result['SplitItemName'] = self.split_item_name

        if self.split_product_detail is not None:
            result['SplitProductDetail'] = self.split_product_detail

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.usage is not None:
            result['Usage'] = self.usage

        if self.usage_unit is not None:
            result['UsageUnit'] = self.usage_unit

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustAmount') is not None:
            self.adjust_amount = m.get('AdjustAmount')

        if m.get('AfterDiscountAmount') is not None:
            self.after_discount_amount = m.get('AfterDiscountAmount')

        if m.get('BillAccountID') is not None:
            self.bill_account_id = m.get('BillAccountID')

        if m.get('BillAccountName') is not None:
            self.bill_account_name = m.get('BillAccountName')

        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')

        if m.get('BillingItem') is not None:
            self.billing_item = m.get('BillingItem')

        if m.get('BillingItemCode') is not None:
            self.billing_item_code = m.get('BillingItemCode')

        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CashAmount') is not None:
            self.cash_amount = m.get('CashAmount')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CostUnit') is not None:
            self.cost_unit = m.get('CostUnit')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')

        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')

        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')

        if m.get('DeductedByResourcePackage') is not None:
            self.deducted_by_resource_package = m.get('DeductedByResourcePackage')

        if m.get('InstanceConfig') is not None:
            self.instance_config = m.get('InstanceConfig')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('InternetIP') is not None:
            self.internet_ip = m.get('InternetIP')

        if m.get('IntranetIP') is not None:
            self.intranet_ip = m.get('IntranetIP')

        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        if m.get('ListPrice') is not None:
            self.list_price = m.get('ListPrice')

        if m.get('ListPriceUnit') is not None:
            self.list_price_unit = m.get('ListPriceUnit')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')

        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')

        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')

        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')

        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')

        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('ServicePeriod') is not None:
            self.service_period = m.get('ServicePeriod')

        if m.get('ServicePeriodUnit') is not None:
            self.service_period_unit = m.get('ServicePeriodUnit')

        if m.get('SplitAccountID') is not None:
            self.split_account_id = m.get('SplitAccountID')

        if m.get('SplitAccountName') is not None:
            self.split_account_name = m.get('SplitAccountName')

        if m.get('SplitBillingCycle') is not None:
            self.split_billing_cycle = m.get('SplitBillingCycle')

        if m.get('SplitBillingDate') is not None:
            self.split_billing_date = m.get('SplitBillingDate')

        if m.get('SplitCommodityCode') is not None:
            self.split_commodity_code = m.get('SplitCommodityCode')

        if m.get('SplitItemID') is not None:
            self.split_item_id = m.get('SplitItemID')

        if m.get('SplitItemName') is not None:
            self.split_item_name = m.get('SplitItemName')

        if m.get('SplitProductDetail') is not None:
            self.split_product_detail = m.get('SplitProductDetail')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        if m.get('UsageUnit') is not None:
            self.usage_unit = m.get('UsageUnit')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

