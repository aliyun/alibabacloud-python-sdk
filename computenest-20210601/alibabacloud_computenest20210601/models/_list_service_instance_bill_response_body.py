# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListServiceInstanceBillResponseBody(DaraModel):
    def __init__(
        self,
        item: List[main_models.ListServiceInstanceBillResponseBodyItem] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The billing information of the backup schedule.
        self.item = item
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.ListServiceInstanceBillResponseBodyItem()
                self.item.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListServiceInstanceBillResponseBodyItem(DaraModel):
    def __init__(
        self,
        billing_cycle: str = None,
        billing_date: str = None,
        billing_item: str = None,
        billing_item_code: str = None,
        currency: str = None,
        deducted_by_resource_package: str = None,
        instance_id: str = None,
        invoice_discount: str = None,
        list_price: str = None,
        list_price_unit: str = None,
        pretax_amount: str = None,
        pretax_gross_amount: str = None,
        product_code: str = None,
        product_detail: str = None,
        product_name: str = None,
        split_billing_cycle: str = None,
        subscription_type: str = None,
        usage: str = None,
        usage_unit: str = None,
    ):
        # The billing cycle. Format: YYYY-MM.
        self.billing_cycle = billing_cycle
        # The billing date. This parameter is required only if the **Granularity** parameter is set to DAILY. Format: YYYY-MM-DD.
        self.billing_date = billing_date
        # The billable item.
        self.billing_item = billing_item
        # The code of the billable item.
        self.billing_item_code = billing_item_code
        # The currency unit.
        # 
        # *   China site: **CNY**.
        # *   International site: **USD**.
        self.currency = currency
        # The amount deducted with resource plans.
        self.deducted_by_resource_package = deducted_by_resource_package
        # The ID of the instance.
        self.instance_id = instance_id
        # The discount amount.
        self.invoice_discount = invoice_discount
        # The unit price.
        self.list_price = list_price
        # The unit of the unit price.
        self.list_price_unit = list_price_unit
        # The pretax amount.
        self.pretax_amount = pretax_amount
        # The pretax gross amount.
        self.pretax_gross_amount = pretax_gross_amount
        # The code of the service.
        self.product_code = product_code
        # The specific service resource.
        self.product_detail = product_detail
        # The name of the cloud service or the name of the service-linked role with which the cloud service is associated.
        self.product_name = product_name
        # The billing cycle in which the bill is split.
        self.split_billing_cycle = split_billing_cycle
        # The billing method. Valid values:
        # 
        # *   Subscription: the subscription billing method.
        # *   PayAsYouGo: the pay-as-you-go billing method.
        self.subscription_type = subscription_type
        # The amount of resource usage.
        self.usage = usage
        # The unit of usage.
        self.usage_unit = usage_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date

        if self.billing_item is not None:
            result['BillingItem'] = self.billing_item

        if self.billing_item_code is not None:
            result['BillingItemCode'] = self.billing_item_code

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.deducted_by_resource_package is not None:
            result['DeductedByResourcePackage'] = self.deducted_by_resource_package

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount

        if self.list_price is not None:
            result['ListPrice'] = self.list_price

        if self.list_price_unit is not None:
            result['ListPriceUnit'] = self.list_price_unit

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

        if self.split_billing_cycle is not None:
            result['SplitBillingCycle'] = self.split_billing_cycle

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        if self.usage is not None:
            result['Usage'] = self.usage

        if self.usage_unit is not None:
            result['UsageUnit'] = self.usage_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')

        if m.get('BillingItem') is not None:
            self.billing_item = m.get('BillingItem')

        if m.get('BillingItemCode') is not None:
            self.billing_item_code = m.get('BillingItemCode')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DeductedByResourcePackage') is not None:
            self.deducted_by_resource_package = m.get('DeductedByResourcePackage')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')

        if m.get('ListPrice') is not None:
            self.list_price = m.get('ListPrice')

        if m.get('ListPriceUnit') is not None:
            self.list_price_unit = m.get('ListPriceUnit')

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

        if m.get('SplitBillingCycle') is not None:
            self.split_billing_cycle = m.get('SplitBillingCycle')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        if m.get('UsageUnit') is not None:
            self.usage_unit = m.get('UsageUnit')

        return self

