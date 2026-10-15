# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceAmortizedCostByAmortizationPeriodResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The message.
        self.message = message
        # The request ID.
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
            temp_model = main_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeInstanceAmortizedCostByAmortizationPeriodResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        items: List[main_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponseBodyDataItems] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The account ID.
        self.account_id = account_id
        # The account.
        self.account_name = account_name
        # The data entries.
        self.items = items
        # The maximum number of entries returned for the current request.
        self.max_results = max_results
        # The position from which to start reading the current call. The value of this parameter must be empty or the value of NextToken that is returned in the last call. Otherwise, an error is reported. If this parameter is empty, the query starts from the beginning.
        self.next_token = next_token
        # The total number of entries.
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
                temp_model = main_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceAmortizedCostByAmortizationPeriodResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        after_discount_amount: float = None,
        amortization_period: str = None,
        amortization_status: str = None,
        bill_account_id: int = None,
        bill_account_name: str = None,
        bill_owner_id: int = None,
        bill_owner_name: str = None,
        biz_type: str = None,
        consume_period: str = None,
        cost_unit: str = None,
        cost_unit_code: str = None,
        current_amortization_after_discount_amount: float = None,
        current_amortization_deducted_by_cash_coupons: float = None,
        current_amortization_deducted_by_coupons: float = None,
        current_amortization_deducted_by_prepaid_card: float = None,
        current_amortization_expenditure_amount: float = None,
        current_amortization_invoice_discount: float = None,
        current_amortization_pretax_amount: float = None,
        current_amortization_pretax_gross_amount: float = None,
        current_amortization_round_down_discount: float = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        expenditure_amount: float = None,
        instance_id: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        invoice_discount: float = None,
        pretax_amount: float = None,
        pretax_gross_amount: float = None,
        previously_amortized_after_discount_amount: float = None,
        previously_amortized_deducted_by_cash_coupons: float = None,
        previously_amortized_deducted_by_coupons: float = None,
        previously_amortized_deducted_by_prepaid_card: float = None,
        previously_amortized_expenditure_amount: float = None,
        previously_amortized_invoice_discount: float = None,
        previously_amortized_pretax_amount: float = None,
        previously_amortized_pretax_gross_amount: float = None,
        previously_amortized_round_down_discount: float = None,
        product_code: str = None,
        product_detail: str = None,
        product_detail_code: str = None,
        product_name: str = None,
        region: str = None,
        remaining_amortization_after_discount_amount: float = None,
        remaining_amortization_deducted_by_cash_coupons: float = None,
        remaining_amortization_deducted_by_coupons: float = None,
        remaining_amortization_deducted_by_prepaid_card: float = None,
        remaining_amortization_expenditure_amount: float = None,
        remaining_amortization_invoice_discount: float = None,
        remaining_amortization_pretax_amount: float = None,
        remaining_amortization_pretax_gross_amount: float = None,
        remaining_amortization_round_down_discount: float = None,
        resource_group: str = None,
        round_down_discount: float = None,
        split_account_name: str = None,
        split_item_id: str = None,
        split_item_name: str = None,
        split_product_detail: str = None,
        subscription_type: str = None,
        tag: str = None,
        zone: str = None,
    ):
        # The amount after a discount.
        self.after_discount_amount = after_discount_amount
        # The amortization month.
        # Format: YYYYMM.
        self.amortization_period = amortization_period
        # The amortization status. Valid values:
        # 
        # - amortized: amortized
        # 
        # - unAmortized: unamortized
        self.amortization_status = amortization_status
        # The ID of the account to which the bill belongs.
        self.bill_account_id = bill_account_id
        # The name of the account to which the bill belongs.
        self.bill_account_name = bill_account_name
        # The ID of the account to which the resource belongs.
        self.bill_owner_id = bill_owner_id
        # The name of the account to which the resource belongs.
        self.bill_owner_name = bill_owner_name
        # The business type.
        self.biz_type = biz_type
        # The billing cycle.
        # Format: YYYYMM.
        self.consume_period = consume_period
        # The cost center.
        self.cost_unit = cost_unit
        # The code of the cost center.
        self.cost_unit_code = cost_unit_code
        # Current amortized amount after discount.
        self.current_amortization_after_discount_amount = current_amortization_after_discount_amount
        # Current amortized deduction by cash coupons.
        self.current_amortization_deducted_by_cash_coupons = current_amortization_deducted_by_cash_coupons
        # Current amortized deduction by coupons.
        self.current_amortization_deducted_by_coupons = current_amortization_deducted_by_coupons
        # Current amortized payment by prepaid card.
        self.current_amortization_deducted_by_prepaid_card = current_amortization_deducted_by_prepaid_card
        # Current amortized expenditure amount (invoicable).
        self.current_amortization_expenditure_amount = current_amortization_expenditure_amount
        # Current amortized discount amount.
        self.current_amortization_invoice_discount = current_amortization_invoice_discount
        # Current amortized pretax amount.
        self.current_amortization_pretax_amount = current_amortization_pretax_amount
        # Current amortized list price.
        self.current_amortization_pretax_gross_amount = current_amortization_pretax_gross_amount
        # Current amortized rounded-down discount.
        self.current_amortization_round_down_discount = current_amortization_round_down_discount
        # The amount deducted by cash coupons.
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        # The amount deducted by coupons.
        self.deducted_by_coupons = deducted_by_coupons
        # The amount paid with a prepaid card.
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        # The expenditure amount (invoicable).
        self.expenditure_amount = expenditure_amount
        # The instance ID.
        self.instance_id = instance_id
        # The public IP address.
        self.internet_ip = internet_ip
        # The internal IP address.
        self.intranet_ip = intranet_ip
        # The discount amount.
        self.invoice_discount = invoice_discount
        # The pretax amount.
        self.pretax_amount = pretax_amount
        # The list price.
        self.pretax_gross_amount = pretax_gross_amount
        # Previously amortized amount after discount.
        self.previously_amortized_after_discount_amount = previously_amortized_after_discount_amount
        # Previously amortized deduction by cash coupons.
        self.previously_amortized_deducted_by_cash_coupons = previously_amortized_deducted_by_cash_coupons
        # Previously amortized deduction by coupons.
        self.previously_amortized_deducted_by_coupons = previously_amortized_deducted_by_coupons
        # Previously amortized payment by prepaid card.
        self.previously_amortized_deducted_by_prepaid_card = previously_amortized_deducted_by_prepaid_card
        # Previously amortized expenditure amount (invoicable).
        self.previously_amortized_expenditure_amount = previously_amortized_expenditure_amount
        # Previously amortized discount amount.
        self.previously_amortized_invoice_discount = previously_amortized_invoice_discount
        # Previously amortized pretax amount.
        self.previously_amortized_pretax_amount = previously_amortized_pretax_amount
        # Previously amortized list price.
        self.previously_amortized_pretax_gross_amount = previously_amortized_pretax_gross_amount
        # Previously amortized rounding discount.
        self.previously_amortized_round_down_discount = previously_amortized_round_down_discount
        # The product code.
        self.product_code = product_code
        # The product details.
        self.product_detail = product_detail
        # The code of the product details.
        self.product_detail_code = product_detail_code
        # The product name.
        self.product_name = product_name
        # The region.
        self.region = region
        # Remaining unamortized amount after discount.
        self.remaining_amortization_after_discount_amount = remaining_amortization_after_discount_amount
        # Remaining unamortized deduction by cash coupons.
        self.remaining_amortization_deducted_by_cash_coupons = remaining_amortization_deducted_by_cash_coupons
        # Remaining unamortized deduction by coupons.
        self.remaining_amortization_deducted_by_coupons = remaining_amortization_deducted_by_coupons
        # Remaining unamortized payment by prepaid card.
        self.remaining_amortization_deducted_by_prepaid_card = remaining_amortization_deducted_by_prepaid_card
        # Remaining unamortized expenditure amount (invoicable).
        self.remaining_amortization_expenditure_amount = remaining_amortization_expenditure_amount
        # Remaining unamortized discount amount.
        self.remaining_amortization_invoice_discount = remaining_amortization_invoice_discount
        # Remaining unamortized pretax amount.
        self.remaining_amortization_pretax_amount = remaining_amortization_pretax_amount
        # Remaining unamortized list price.
        self.remaining_amortization_pretax_gross_amount = remaining_amortization_pretax_gross_amount
        # Remaining unamortized rounding discount.
        self.remaining_amortization_round_down_discount = remaining_amortization_round_down_discount
        # The resource group.
        self.resource_group = resource_group
        # The rounded-down discount.
        self.round_down_discount = round_down_discount
        # The name of the account to which the attached resource belongs.
        self.split_account_name = split_account_name
        # The ID of the attached resource.
        self.split_item_id = split_item_id
        # The name of the attached resource.
        self.split_item_name = split_item_name
        # The name of the product details for the attached resource.
        self.split_product_detail = split_product_detail
        # The subscription type. Valid values:
        # 
        # - Subscription: subscription.
        # 
        # - PayAsYouGo: pay-as-you-go.
        self.subscription_type = subscription_type
        # The tags of the instance.
        self.tag = tag
        # The zone.
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_discount_amount is not None:
            result['AfterDiscountAmount'] = self.after_discount_amount

        if self.amortization_period is not None:
            result['AmortizationPeriod'] = self.amortization_period

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

        if self.current_amortization_after_discount_amount is not None:
            result['CurrentAmortizationAfterDiscountAmount'] = self.current_amortization_after_discount_amount

        if self.current_amortization_deducted_by_cash_coupons is not None:
            result['CurrentAmortizationDeductedByCashCoupons'] = self.current_amortization_deducted_by_cash_coupons

        if self.current_amortization_deducted_by_coupons is not None:
            result['CurrentAmortizationDeductedByCoupons'] = self.current_amortization_deducted_by_coupons

        if self.current_amortization_deducted_by_prepaid_card is not None:
            result['CurrentAmortizationDeductedByPrepaidCard'] = self.current_amortization_deducted_by_prepaid_card

        if self.current_amortization_expenditure_amount is not None:
            result['CurrentAmortizationExpenditureAmount'] = self.current_amortization_expenditure_amount

        if self.current_amortization_invoice_discount is not None:
            result['CurrentAmortizationInvoiceDiscount'] = self.current_amortization_invoice_discount

        if self.current_amortization_pretax_amount is not None:
            result['CurrentAmortizationPretaxAmount'] = self.current_amortization_pretax_amount

        if self.current_amortization_pretax_gross_amount is not None:
            result['CurrentAmortizationPretaxGrossAmount'] = self.current_amortization_pretax_gross_amount

        if self.current_amortization_round_down_discount is not None:
            result['CurrentAmortizationRoundDownDiscount'] = self.current_amortization_round_down_discount

        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons

        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons

        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card

        if self.expenditure_amount is not None:
            result['ExpenditureAmount'] = self.expenditure_amount

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

        if self.previously_amortized_after_discount_amount is not None:
            result['PreviouslyAmortizedAfterDiscountAmount'] = self.previously_amortized_after_discount_amount

        if self.previously_amortized_deducted_by_cash_coupons is not None:
            result['PreviouslyAmortizedDeductedByCashCoupons'] = self.previously_amortized_deducted_by_cash_coupons

        if self.previously_amortized_deducted_by_coupons is not None:
            result['PreviouslyAmortizedDeductedByCoupons'] = self.previously_amortized_deducted_by_coupons

        if self.previously_amortized_deducted_by_prepaid_card is not None:
            result['PreviouslyAmortizedDeductedByPrepaidCard'] = self.previously_amortized_deducted_by_prepaid_card

        if self.previously_amortized_expenditure_amount is not None:
            result['PreviouslyAmortizedExpenditureAmount'] = self.previously_amortized_expenditure_amount

        if self.previously_amortized_invoice_discount is not None:
            result['PreviouslyAmortizedInvoiceDiscount'] = self.previously_amortized_invoice_discount

        if self.previously_amortized_pretax_amount is not None:
            result['PreviouslyAmortizedPretaxAmount'] = self.previously_amortized_pretax_amount

        if self.previously_amortized_pretax_gross_amount is not None:
            result['PreviouslyAmortizedPretaxGrossAmount'] = self.previously_amortized_pretax_gross_amount

        if self.previously_amortized_round_down_discount is not None:
            result['PreviouslyAmortizedRoundDownDiscount'] = self.previously_amortized_round_down_discount

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail

        if self.product_detail_code is not None:
            result['ProductDetailCode'] = self.product_detail_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.region is not None:
            result['Region'] = self.region

        if self.remaining_amortization_after_discount_amount is not None:
            result['RemainingAmortizationAfterDiscountAmount'] = self.remaining_amortization_after_discount_amount

        if self.remaining_amortization_deducted_by_cash_coupons is not None:
            result['RemainingAmortizationDeductedByCashCoupons'] = self.remaining_amortization_deducted_by_cash_coupons

        if self.remaining_amortization_deducted_by_coupons is not None:
            result['RemainingAmortizationDeductedByCoupons'] = self.remaining_amortization_deducted_by_coupons

        if self.remaining_amortization_deducted_by_prepaid_card is not None:
            result['RemainingAmortizationDeductedByPrepaidCard'] = self.remaining_amortization_deducted_by_prepaid_card

        if self.remaining_amortization_expenditure_amount is not None:
            result['RemainingAmortizationExpenditureAmount'] = self.remaining_amortization_expenditure_amount

        if self.remaining_amortization_invoice_discount is not None:
            result['RemainingAmortizationInvoiceDiscount'] = self.remaining_amortization_invoice_discount

        if self.remaining_amortization_pretax_amount is not None:
            result['RemainingAmortizationPretaxAmount'] = self.remaining_amortization_pretax_amount

        if self.remaining_amortization_pretax_gross_amount is not None:
            result['RemainingAmortizationPretaxGrossAmount'] = self.remaining_amortization_pretax_gross_amount

        if self.remaining_amortization_round_down_discount is not None:
            result['RemainingAmortizationRoundDownDiscount'] = self.remaining_amortization_round_down_discount

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

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDiscountAmount') is not None:
            self.after_discount_amount = m.get('AfterDiscountAmount')

        if m.get('AmortizationPeriod') is not None:
            self.amortization_period = m.get('AmortizationPeriod')

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

        if m.get('CurrentAmortizationAfterDiscountAmount') is not None:
            self.current_amortization_after_discount_amount = m.get('CurrentAmortizationAfterDiscountAmount')

        if m.get('CurrentAmortizationDeductedByCashCoupons') is not None:
            self.current_amortization_deducted_by_cash_coupons = m.get('CurrentAmortizationDeductedByCashCoupons')

        if m.get('CurrentAmortizationDeductedByCoupons') is not None:
            self.current_amortization_deducted_by_coupons = m.get('CurrentAmortizationDeductedByCoupons')

        if m.get('CurrentAmortizationDeductedByPrepaidCard') is not None:
            self.current_amortization_deducted_by_prepaid_card = m.get('CurrentAmortizationDeductedByPrepaidCard')

        if m.get('CurrentAmortizationExpenditureAmount') is not None:
            self.current_amortization_expenditure_amount = m.get('CurrentAmortizationExpenditureAmount')

        if m.get('CurrentAmortizationInvoiceDiscount') is not None:
            self.current_amortization_invoice_discount = m.get('CurrentAmortizationInvoiceDiscount')

        if m.get('CurrentAmortizationPretaxAmount') is not None:
            self.current_amortization_pretax_amount = m.get('CurrentAmortizationPretaxAmount')

        if m.get('CurrentAmortizationPretaxGrossAmount') is not None:
            self.current_amortization_pretax_gross_amount = m.get('CurrentAmortizationPretaxGrossAmount')

        if m.get('CurrentAmortizationRoundDownDiscount') is not None:
            self.current_amortization_round_down_discount = m.get('CurrentAmortizationRoundDownDiscount')

        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')

        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')

        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')

        if m.get('ExpenditureAmount') is not None:
            self.expenditure_amount = m.get('ExpenditureAmount')

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

        if m.get('PreviouslyAmortizedAfterDiscountAmount') is not None:
            self.previously_amortized_after_discount_amount = m.get('PreviouslyAmortizedAfterDiscountAmount')

        if m.get('PreviouslyAmortizedDeductedByCashCoupons') is not None:
            self.previously_amortized_deducted_by_cash_coupons = m.get('PreviouslyAmortizedDeductedByCashCoupons')

        if m.get('PreviouslyAmortizedDeductedByCoupons') is not None:
            self.previously_amortized_deducted_by_coupons = m.get('PreviouslyAmortizedDeductedByCoupons')

        if m.get('PreviouslyAmortizedDeductedByPrepaidCard') is not None:
            self.previously_amortized_deducted_by_prepaid_card = m.get('PreviouslyAmortizedDeductedByPrepaidCard')

        if m.get('PreviouslyAmortizedExpenditureAmount') is not None:
            self.previously_amortized_expenditure_amount = m.get('PreviouslyAmortizedExpenditureAmount')

        if m.get('PreviouslyAmortizedInvoiceDiscount') is not None:
            self.previously_amortized_invoice_discount = m.get('PreviouslyAmortizedInvoiceDiscount')

        if m.get('PreviouslyAmortizedPretaxAmount') is not None:
            self.previously_amortized_pretax_amount = m.get('PreviouslyAmortizedPretaxAmount')

        if m.get('PreviouslyAmortizedPretaxGrossAmount') is not None:
            self.previously_amortized_pretax_gross_amount = m.get('PreviouslyAmortizedPretaxGrossAmount')

        if m.get('PreviouslyAmortizedRoundDownDiscount') is not None:
            self.previously_amortized_round_down_discount = m.get('PreviouslyAmortizedRoundDownDiscount')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')

        if m.get('ProductDetailCode') is not None:
            self.product_detail_code = m.get('ProductDetailCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RemainingAmortizationAfterDiscountAmount') is not None:
            self.remaining_amortization_after_discount_amount = m.get('RemainingAmortizationAfterDiscountAmount')

        if m.get('RemainingAmortizationDeductedByCashCoupons') is not None:
            self.remaining_amortization_deducted_by_cash_coupons = m.get('RemainingAmortizationDeductedByCashCoupons')

        if m.get('RemainingAmortizationDeductedByCoupons') is not None:
            self.remaining_amortization_deducted_by_coupons = m.get('RemainingAmortizationDeductedByCoupons')

        if m.get('RemainingAmortizationDeductedByPrepaidCard') is not None:
            self.remaining_amortization_deducted_by_prepaid_card = m.get('RemainingAmortizationDeductedByPrepaidCard')

        if m.get('RemainingAmortizationExpenditureAmount') is not None:
            self.remaining_amortization_expenditure_amount = m.get('RemainingAmortizationExpenditureAmount')

        if m.get('RemainingAmortizationInvoiceDiscount') is not None:
            self.remaining_amortization_invoice_discount = m.get('RemainingAmortizationInvoiceDiscount')

        if m.get('RemainingAmortizationPretaxAmount') is not None:
            self.remaining_amortization_pretax_amount = m.get('RemainingAmortizationPretaxAmount')

        if m.get('RemainingAmortizationPretaxGrossAmount') is not None:
            self.remaining_amortization_pretax_gross_amount = m.get('RemainingAmortizationPretaxGrossAmount')

        if m.get('RemainingAmortizationRoundDownDiscount') is not None:
            self.remaining_amortization_round_down_discount = m.get('RemainingAmortizationRoundDownDiscount')

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

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

