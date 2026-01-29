# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        items: List[main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponseBodyDataItems] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.items = items
        self.max_results = max_results
        self.next_token = next_token
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

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        amortization_period: str = None,
        amortization_period_day: str = None,
        amortization_status: str = None,
        bill_account_id: int = None,
        bill_account_name: str = None,
        bill_owner_id: int = None,
        bill_owner_name: str = None,
        biz_type: str = None,
        consume_period: str = None,
        cost_unit: str = None,
        cost_unit_code: str = None,
        current_amortization_deducted_by_coupons: float = None,
        current_amortization_invoice_discount: float = None,
        current_amortization_pretax_amount: float = None,
        current_amortization_pretax_gross_amount: float = None,
        current_amortization_round_down_discount: float = None,
        deducted_by_coupons: float = None,
        instance_config: str = None,
        instance_id: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        invoice_discount: float = None,
        pretax_amount: float = None,
        pretax_gross_amount: float = None,
        product_code: str = None,
        product_detail: str = None,
        product_detail_code: str = None,
        product_name: str = None,
        refer_fr_instance_id: str = None,
        refer_fr_owner_id: str = None,
        refer_fr_product_detail_code: str = None,
        region: str = None,
        resource_group: str = None,
        round_down_discount: float = None,
        split_account_name: str = None,
        split_item_id: str = None,
        split_item_name: str = None,
        split_product_detail: str = None,
        subscription_type: str = None,
        tag: str = None,
        unused_amortization_deducted_by_coupons: float = None,
        unused_amortization_invoice_discount: float = None,
        unused_amortization_pretax_amount: float = None,
        unused_amortization_pretax_gross_amount: float = None,
        unused_amortization_round_down_discount: float = None,
        zone: str = None,
    ):
        self.amortization_period = amortization_period
        self.amortization_period_day = amortization_period_day
        self.amortization_status = amortization_status
        self.bill_account_id = bill_account_id
        self.bill_account_name = bill_account_name
        self.bill_owner_id = bill_owner_id
        self.bill_owner_name = bill_owner_name
        self.biz_type = biz_type
        self.consume_period = consume_period
        self.cost_unit = cost_unit
        self.cost_unit_code = cost_unit_code
        self.current_amortization_deducted_by_coupons = current_amortization_deducted_by_coupons
        self.current_amortization_invoice_discount = current_amortization_invoice_discount
        self.current_amortization_pretax_amount = current_amortization_pretax_amount
        self.current_amortization_pretax_gross_amount = current_amortization_pretax_gross_amount
        self.current_amortization_round_down_discount = current_amortization_round_down_discount
        self.deducted_by_coupons = deducted_by_coupons
        self.instance_config = instance_config
        self.instance_id = instance_id
        self.internet_ip = internet_ip
        self.intranet_ip = intranet_ip
        self.invoice_discount = invoice_discount
        self.pretax_amount = pretax_amount
        self.pretax_gross_amount = pretax_gross_amount
        self.product_code = product_code
        self.product_detail = product_detail
        self.product_detail_code = product_detail_code
        self.product_name = product_name
        self.refer_fr_instance_id = refer_fr_instance_id
        self.refer_fr_owner_id = refer_fr_owner_id
        self.refer_fr_product_detail_code = refer_fr_product_detail_code
        self.region = region
        self.resource_group = resource_group
        self.round_down_discount = round_down_discount
        self.split_account_name = split_account_name
        self.split_item_id = split_item_id
        self.split_item_name = split_item_name
        self.split_product_detail = split_product_detail
        self.subscription_type = subscription_type
        self.tag = tag
        self.unused_amortization_deducted_by_coupons = unused_amortization_deducted_by_coupons
        self.unused_amortization_invoice_discount = unused_amortization_invoice_discount
        self.unused_amortization_pretax_amount = unused_amortization_pretax_amount
        self.unused_amortization_pretax_gross_amount = unused_amortization_pretax_gross_amount
        self.unused_amortization_round_down_discount = unused_amortization_round_down_discount
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amortization_period is not None:
            result['AmortizationPeriod'] = self.amortization_period

        if self.amortization_period_day is not None:
            result['AmortizationPeriodDay'] = self.amortization_period_day

        if self.amortization_status is not None:
            result['AmortizationStatus'] = self.amortization_status

        if self.bill_account_id is not None:
            result['BillAccountID'] = self.bill_account_id

        if self.bill_account_name is not None:
            result['BillAccountName'] = self.bill_account_name

        if self.bill_owner_id is not None:
            result['BillOwnerID'] = self.bill_owner_id

        if self.bill_owner_name is not None:
            result['BillOwnerName'] = self.bill_owner_name

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.consume_period is not None:
            result['ConsumePeriod'] = self.consume_period

        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit

        if self.cost_unit_code is not None:
            result['CostUnitCode'] = self.cost_unit_code

        if self.current_amortization_deducted_by_coupons is not None:
            result['CurrentAmortizationDeductedByCoupons'] = self.current_amortization_deducted_by_coupons

        if self.current_amortization_invoice_discount is not None:
            result['CurrentAmortizationInvoiceDiscount'] = self.current_amortization_invoice_discount

        if self.current_amortization_pretax_amount is not None:
            result['CurrentAmortizationPretaxAmount'] = self.current_amortization_pretax_amount

        if self.current_amortization_pretax_gross_amount is not None:
            result['CurrentAmortizationPretaxGrossAmount'] = self.current_amortization_pretax_gross_amount

        if self.current_amortization_round_down_discount is not None:
            result['CurrentAmortizationRoundDownDiscount'] = self.current_amortization_round_down_discount

        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons

        if self.instance_config is not None:
            result['InstanceConfig'] = self.instance_config

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.internet_ip is not None:
            result['InternetIP'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIP'] = self.intranet_ip

        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount

        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount

        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail

        if self.product_detail_code is not None:
            result['ProductDetailCode'] = self.product_detail_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.refer_fr_instance_id is not None:
            result['ReferFrInstanceID'] = self.refer_fr_instance_id

        if self.refer_fr_owner_id is not None:
            result['ReferFrOwnerID'] = self.refer_fr_owner_id

        if self.refer_fr_product_detail_code is not None:
            result['ReferFrProductDetailCode'] = self.refer_fr_product_detail_code

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.round_down_discount is not None:
            result['RoundDownDiscount'] = self.round_down_discount

        if self.split_account_name is not None:
            result['SplitAccountName'] = self.split_account_name

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

        if self.unused_amortization_deducted_by_coupons is not None:
            result['UnusedAmortizationDeductedByCoupons'] = self.unused_amortization_deducted_by_coupons

        if self.unused_amortization_invoice_discount is not None:
            result['UnusedAmortizationInvoiceDiscount'] = self.unused_amortization_invoice_discount

        if self.unused_amortization_pretax_amount is not None:
            result['UnusedAmortizationPretaxAmount'] = self.unused_amortization_pretax_amount

        if self.unused_amortization_pretax_gross_amount is not None:
            result['UnusedAmortizationPretaxGrossAmount'] = self.unused_amortization_pretax_gross_amount

        if self.unused_amortization_round_down_discount is not None:
            result['UnusedAmortizationRoundDownDiscount'] = self.unused_amortization_round_down_discount

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AmortizationPeriod') is not None:
            self.amortization_period = m.get('AmortizationPeriod')

        if m.get('AmortizationPeriodDay') is not None:
            self.amortization_period_day = m.get('AmortizationPeriodDay')

        if m.get('AmortizationStatus') is not None:
            self.amortization_status = m.get('AmortizationStatus')

        if m.get('BillAccountID') is not None:
            self.bill_account_id = m.get('BillAccountID')

        if m.get('BillAccountName') is not None:
            self.bill_account_name = m.get('BillAccountName')

        if m.get('BillOwnerID') is not None:
            self.bill_owner_id = m.get('BillOwnerID')

        if m.get('BillOwnerName') is not None:
            self.bill_owner_name = m.get('BillOwnerName')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ConsumePeriod') is not None:
            self.consume_period = m.get('ConsumePeriod')

        if m.get('CostUnit') is not None:
            self.cost_unit = m.get('CostUnit')

        if m.get('CostUnitCode') is not None:
            self.cost_unit_code = m.get('CostUnitCode')

        if m.get('CurrentAmortizationDeductedByCoupons') is not None:
            self.current_amortization_deducted_by_coupons = m.get('CurrentAmortizationDeductedByCoupons')

        if m.get('CurrentAmortizationInvoiceDiscount') is not None:
            self.current_amortization_invoice_discount = m.get('CurrentAmortizationInvoiceDiscount')

        if m.get('CurrentAmortizationPretaxAmount') is not None:
            self.current_amortization_pretax_amount = m.get('CurrentAmortizationPretaxAmount')

        if m.get('CurrentAmortizationPretaxGrossAmount') is not None:
            self.current_amortization_pretax_gross_amount = m.get('CurrentAmortizationPretaxGrossAmount')

        if m.get('CurrentAmortizationRoundDownDiscount') is not None:
            self.current_amortization_round_down_discount = m.get('CurrentAmortizationRoundDownDiscount')

        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')

        if m.get('InstanceConfig') is not None:
            self.instance_config = m.get('InstanceConfig')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InternetIP') is not None:
            self.internet_ip = m.get('InternetIP')

        if m.get('IntranetIP') is not None:
            self.intranet_ip = m.get('IntranetIP')

        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')

        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')

        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')

        if m.get('ProductDetailCode') is not None:
            self.product_detail_code = m.get('ProductDetailCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ReferFrInstanceID') is not None:
            self.refer_fr_instance_id = m.get('ReferFrInstanceID')

        if m.get('ReferFrOwnerID') is not None:
            self.refer_fr_owner_id = m.get('ReferFrOwnerID')

        if m.get('ReferFrProductDetailCode') is not None:
            self.refer_fr_product_detail_code = m.get('ReferFrProductDetailCode')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('RoundDownDiscount') is not None:
            self.round_down_discount = m.get('RoundDownDiscount')

        if m.get('SplitAccountName') is not None:
            self.split_account_name = m.get('SplitAccountName')

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

        if m.get('UnusedAmortizationDeductedByCoupons') is not None:
            self.unused_amortization_deducted_by_coupons = m.get('UnusedAmortizationDeductedByCoupons')

        if m.get('UnusedAmortizationInvoiceDiscount') is not None:
            self.unused_amortization_invoice_discount = m.get('UnusedAmortizationInvoiceDiscount')

        if m.get('UnusedAmortizationPretaxAmount') is not None:
            self.unused_amortization_pretax_amount = m.get('UnusedAmortizationPretaxAmount')

        if m.get('UnusedAmortizationPretaxGrossAmount') is not None:
            self.unused_amortization_pretax_gross_amount = m.get('UnusedAmortizationPretaxGrossAmount')

        if m.get('UnusedAmortizationRoundDownDiscount') is not None:
            self.unused_amortization_round_down_discount = m.get('UnusedAmortizationRoundDownDiscount')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

