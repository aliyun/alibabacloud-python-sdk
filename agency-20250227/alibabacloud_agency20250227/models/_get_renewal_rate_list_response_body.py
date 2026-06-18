# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20250227 import models as main_models
from darabonba.model import DaraModel

class GetRenewalRateListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetRenewalRateListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The prompt message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetRenewalRateListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRenewalRateListResponseBodyData(DaraModel):
    def __init__(
        self,
        customer_adjusted_renewal_amount_due: float = None,
        customer_other_bill_amount: float = None,
        final_customer_renewal_amount_due: float = None,
        final_customer_renewal_rate: float = None,
        final_customer_renewed_amount: float = None,
        final_other_bill_amount: float = None,
        final_renewal_amount_due: float = None,
        final_renewal_rate: float = None,
        final_renewed_amount: float = None,
        final_sub_partner_renewal_amount_due: float = None,
        final_sub_partner_renewal_rate: float = None,
        final_sub_partner_renewed_amount: float = None,
        fiscal_year_and_quarter: str = None,
        master_pid: str = None,
        master_pid_name: str = None,
        special_customer_renew_ratio: float = None,
        special_customer_renewal_amount_due: float = None,
        special_customer_renewed_amount: float = None,
        special_final_renew_ratio: float = None,
        special_final_renewal_amount_due: float = None,
        special_final_renewed_amount: float = None,
        special_sub_partner_renew_ratio: float = None,
        special_sub_partner_renewal_amount_due: float = None,
        special_sub_partner_renewed_amount: float = None,
        sub_partner_adjusted_renewal_amount_due: float = None,
        sub_partner_other_bill_amount: float = None,
    ):
        # The adjusted customer acquisition amount due for renewal.
        self.customer_adjusted_renewal_amount_due = customer_adjusted_renewal_amount_due
        # The customer acquisition amount for new purchases, upgrades, and refunds.
        self.customer_other_bill_amount = customer_other_bill_amount
        # The customer acquisition amount due for renewal.
        self.final_customer_renewal_amount_due = final_customer_renewal_amount_due
        # The customer acquisition commission renewal rate.
        self.final_customer_renewal_rate = final_customer_renewal_rate
        # The customer acquisition renewed amount.
        self.final_customer_renewed_amount = final_customer_renewed_amount
        # The total amount for new purchases, upgrades, and refunds.
        self.final_other_bill_amount = final_other_bill_amount
        # The final amount due for renewal.
        self.final_renewal_amount_due = final_renewal_amount_due
        # The final commission renewal rate.
        self.final_renewal_rate = final_renewal_rate
        # The final renewed amount.
        self.final_renewed_amount = final_renewed_amount
        # The sub-partner acquisition amount due for renewal.
        self.final_sub_partner_renewal_amount_due = final_sub_partner_renewal_amount_due
        # The sub-partner acquisition commission renewal rate.
        self.final_sub_partner_renewal_rate = final_sub_partner_renewal_rate
        # The sub-partner acquisition renewed amount.
        self.final_sub_partner_renewed_amount = final_sub_partner_renewed_amount
        # The fiscal year and quarter.
        self.fiscal_year_and_quarter = fiscal_year_and_quarter
        # The partner PID.
        self.master_pid = master_pid
        # The partner PID name.
        self.master_pid_name = master_pid_name
        # The customer acquisition commission renewal rate including special approvals.
        self.special_customer_renew_ratio = special_customer_renew_ratio
        # The customer acquisition amount due for renewal including special approvals.
        self.special_customer_renewal_amount_due = special_customer_renewal_amount_due
        # The customer acquisition renewed amount including special approvals.
        self.special_customer_renewed_amount = special_customer_renewed_amount
        # The final quarterly commission renewal rate including special approvals.
        self.special_final_renew_ratio = special_final_renew_ratio
        # The final quarterly commission amount due for renewal including special approvals.
        self.special_final_renewal_amount_due = special_final_renewal_amount_due
        # The final quarterly commission renewed amount including special approvals.
        self.special_final_renewed_amount = special_final_renewed_amount
        # The sub-partner acquisition commission renewal rate including special approvals.
        self.special_sub_partner_renew_ratio = special_sub_partner_renew_ratio
        # The sub-partner acquisition amount due for renewal including special approvals.
        self.special_sub_partner_renewal_amount_due = special_sub_partner_renewal_amount_due
        # The sub-partner acquisition renewed amount including special approvals.
        self.special_sub_partner_renewed_amount = special_sub_partner_renewed_amount
        # The adjusted sub-partner acquisition amount due for renewal.
        self.sub_partner_adjusted_renewal_amount_due = sub_partner_adjusted_renewal_amount_due
        # The sub-partner acquisition amount for new purchases, upgrades, and refunds.
        self.sub_partner_other_bill_amount = sub_partner_other_bill_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_adjusted_renewal_amount_due is not None:
            result['CustomerAdjustedRenewalAmountDue'] = self.customer_adjusted_renewal_amount_due

        if self.customer_other_bill_amount is not None:
            result['CustomerOtherBillAmount'] = self.customer_other_bill_amount

        if self.final_customer_renewal_amount_due is not None:
            result['FinalCustomerRenewalAmountDue'] = self.final_customer_renewal_amount_due

        if self.final_customer_renewal_rate is not None:
            result['FinalCustomerRenewalRate'] = self.final_customer_renewal_rate

        if self.final_customer_renewed_amount is not None:
            result['FinalCustomerRenewedAmount'] = self.final_customer_renewed_amount

        if self.final_other_bill_amount is not None:
            result['FinalOtherBillAmount'] = self.final_other_bill_amount

        if self.final_renewal_amount_due is not None:
            result['FinalRenewalAmountDue'] = self.final_renewal_amount_due

        if self.final_renewal_rate is not None:
            result['FinalRenewalRate'] = self.final_renewal_rate

        if self.final_renewed_amount is not None:
            result['FinalRenewedAmount'] = self.final_renewed_amount

        if self.final_sub_partner_renewal_amount_due is not None:
            result['FinalSubPartnerRenewalAmountDue'] = self.final_sub_partner_renewal_amount_due

        if self.final_sub_partner_renewal_rate is not None:
            result['FinalSubPartnerRenewalRate'] = self.final_sub_partner_renewal_rate

        if self.final_sub_partner_renewed_amount is not None:
            result['FinalSubPartnerRenewedAmount'] = self.final_sub_partner_renewed_amount

        if self.fiscal_year_and_quarter is not None:
            result['FiscalYearAndQuarter'] = self.fiscal_year_and_quarter

        if self.master_pid is not None:
            result['MasterPid'] = self.master_pid

        if self.master_pid_name is not None:
            result['MasterPidName'] = self.master_pid_name

        if self.special_customer_renew_ratio is not None:
            result['SpecialCustomerRenewRatio'] = self.special_customer_renew_ratio

        if self.special_customer_renewal_amount_due is not None:
            result['SpecialCustomerRenewalAmountDue'] = self.special_customer_renewal_amount_due

        if self.special_customer_renewed_amount is not None:
            result['SpecialCustomerRenewedAmount'] = self.special_customer_renewed_amount

        if self.special_final_renew_ratio is not None:
            result['SpecialFinalRenewRatio'] = self.special_final_renew_ratio

        if self.special_final_renewal_amount_due is not None:
            result['SpecialFinalRenewalAmountDue'] = self.special_final_renewal_amount_due

        if self.special_final_renewed_amount is not None:
            result['SpecialFinalRenewedAmount'] = self.special_final_renewed_amount

        if self.special_sub_partner_renew_ratio is not None:
            result['SpecialSubPartnerRenewRatio'] = self.special_sub_partner_renew_ratio

        if self.special_sub_partner_renewal_amount_due is not None:
            result['SpecialSubPartnerRenewalAmountDue'] = self.special_sub_partner_renewal_amount_due

        if self.special_sub_partner_renewed_amount is not None:
            result['SpecialSubPartnerRenewedAmount'] = self.special_sub_partner_renewed_amount

        if self.sub_partner_adjusted_renewal_amount_due is not None:
            result['SubPartnerAdjustedRenewalAmountDue'] = self.sub_partner_adjusted_renewal_amount_due

        if self.sub_partner_other_bill_amount is not None:
            result['SubPartnerOtherBillAmount'] = self.sub_partner_other_bill_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerAdjustedRenewalAmountDue') is not None:
            self.customer_adjusted_renewal_amount_due = m.get('CustomerAdjustedRenewalAmountDue')

        if m.get('CustomerOtherBillAmount') is not None:
            self.customer_other_bill_amount = m.get('CustomerOtherBillAmount')

        if m.get('FinalCustomerRenewalAmountDue') is not None:
            self.final_customer_renewal_amount_due = m.get('FinalCustomerRenewalAmountDue')

        if m.get('FinalCustomerRenewalRate') is not None:
            self.final_customer_renewal_rate = m.get('FinalCustomerRenewalRate')

        if m.get('FinalCustomerRenewedAmount') is not None:
            self.final_customer_renewed_amount = m.get('FinalCustomerRenewedAmount')

        if m.get('FinalOtherBillAmount') is not None:
            self.final_other_bill_amount = m.get('FinalOtherBillAmount')

        if m.get('FinalRenewalAmountDue') is not None:
            self.final_renewal_amount_due = m.get('FinalRenewalAmountDue')

        if m.get('FinalRenewalRate') is not None:
            self.final_renewal_rate = m.get('FinalRenewalRate')

        if m.get('FinalRenewedAmount') is not None:
            self.final_renewed_amount = m.get('FinalRenewedAmount')

        if m.get('FinalSubPartnerRenewalAmountDue') is not None:
            self.final_sub_partner_renewal_amount_due = m.get('FinalSubPartnerRenewalAmountDue')

        if m.get('FinalSubPartnerRenewalRate') is not None:
            self.final_sub_partner_renewal_rate = m.get('FinalSubPartnerRenewalRate')

        if m.get('FinalSubPartnerRenewedAmount') is not None:
            self.final_sub_partner_renewed_amount = m.get('FinalSubPartnerRenewedAmount')

        if m.get('FiscalYearAndQuarter') is not None:
            self.fiscal_year_and_quarter = m.get('FiscalYearAndQuarter')

        if m.get('MasterPid') is not None:
            self.master_pid = m.get('MasterPid')

        if m.get('MasterPidName') is not None:
            self.master_pid_name = m.get('MasterPidName')

        if m.get('SpecialCustomerRenewRatio') is not None:
            self.special_customer_renew_ratio = m.get('SpecialCustomerRenewRatio')

        if m.get('SpecialCustomerRenewalAmountDue') is not None:
            self.special_customer_renewal_amount_due = m.get('SpecialCustomerRenewalAmountDue')

        if m.get('SpecialCustomerRenewedAmount') is not None:
            self.special_customer_renewed_amount = m.get('SpecialCustomerRenewedAmount')

        if m.get('SpecialFinalRenewRatio') is not None:
            self.special_final_renew_ratio = m.get('SpecialFinalRenewRatio')

        if m.get('SpecialFinalRenewalAmountDue') is not None:
            self.special_final_renewal_amount_due = m.get('SpecialFinalRenewalAmountDue')

        if m.get('SpecialFinalRenewedAmount') is not None:
            self.special_final_renewed_amount = m.get('SpecialFinalRenewedAmount')

        if m.get('SpecialSubPartnerRenewRatio') is not None:
            self.special_sub_partner_renew_ratio = m.get('SpecialSubPartnerRenewRatio')

        if m.get('SpecialSubPartnerRenewalAmountDue') is not None:
            self.special_sub_partner_renewal_amount_due = m.get('SpecialSubPartnerRenewalAmountDue')

        if m.get('SpecialSubPartnerRenewedAmount') is not None:
            self.special_sub_partner_renewed_amount = m.get('SpecialSubPartnerRenewedAmount')

        if m.get('SubPartnerAdjustedRenewalAmountDue') is not None:
            self.sub_partner_adjusted_renewal_amount_due = m.get('SubPartnerAdjustedRenewalAmountDue')

        if m.get('SubPartnerOtherBillAmount') is not None:
            self.sub_partner_other_bill_amount = m.get('SubPartnerOtherBillAmount')

        return self

