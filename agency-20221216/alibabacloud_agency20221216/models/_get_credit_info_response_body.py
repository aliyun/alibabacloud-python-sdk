# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class GetCreditInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCreditInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code. Valid values:
        # - 200: OK.
        # - 1109: System error.
        self.code = code
        # The returned data.
        self.data = data
        # The message information.
        self.message = message
        # The request ID. Alibaba Cloud uses this ID for error tracking.
        self.request_id = request_id
        # Indicates whether the current API call is successful. Valid values:
        # - True: Successful.
        # - False: Failed.
        # 
        # This does not indicate whether the subsequent business operation is successful.
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
            temp_model = main_models.GetCreditInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCreditInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        account_status: str = None,
        alarm_threshold: str = None,
        available_credit: str = None,
        consumed_undeducted_value: str = None,
        credit_line: str = None,
        outstanding_balance: str = None,
        paygfreeze_status: str = None,
        zero_credit_shutdown_policy: str = None,
        new_buy_status: str = None,
    ):
        # The credit control status of the sub-account. Valid values:
        # 1. normal: Normal.
        # 2. arrearsNotShutdown: The account has an overdue payment but is not shut down.
        # 3. shutdown: Shut down.
        self.account_status = account_status
        # The percentage value. When the available credit drops below this percentage of the credit limit, an email notification is sent to the main account.
        self.alarm_threshold = alarm_threshold
        # The available credit.
        self.available_credit = available_credit
        # The total outstanding amount of virtual bills before simulated deduction.
        self.consumed_undeducted_value = consumed_undeducted_value
        # The credit limit of the sub-account.
        self.credit_line = credit_line
        # The credit amount consumed by the sub-account that has not yet been paid.
        self.outstanding_balance = outstanding_balance
        # The freeze status of pay-as-you-go. Valid values:
        # - freeze: Frozen.
        # - normal: Normal.
        self.paygfreeze_status = paygfreeze_status
        # The policy that the system uses to manage resources when the active credit is 0 or less. Valid values:
        # 
        # 1: delayStop. Alibaba Cloud takes over the resources. Instances are shut down after the credit is exhausted with a delay epoch. If payment is not made within 15 days, storage resources are released.
        # 
        # 2: noStop. The system does not manage the resource lifecycle of the non-trusteeship linked account. The partner must manage it manually.
        # 
        # 3: immediatelyStop. Instances are shut down immediately when the account enters the overdue payment state, which triggers instance shutdown.
        self.zero_credit_shutdown_policy = zero_credit_shutdown_policy
        # The status that manages the purchase actions of the customer. Valid values:
        # 
        # - ban: New purchases are prohibited.
        # - cancelBan: Normal status.
        self.new_buy_status = new_buy_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status

        if self.alarm_threshold is not None:
            result['AlarmThreshold'] = self.alarm_threshold

        if self.available_credit is not None:
            result['AvailableCredit'] = self.available_credit

        if self.consumed_undeducted_value is not None:
            result['ConsumedUndeductedValue'] = self.consumed_undeducted_value

        if self.credit_line is not None:
            result['CreditLine'] = self.credit_line

        if self.outstanding_balance is not None:
            result['OutstandingBalance'] = self.outstanding_balance

        if self.paygfreeze_status is not None:
            result['PAYGFreezeStatus'] = self.paygfreeze_status

        if self.zero_credit_shutdown_policy is not None:
            result['ZeroCreditShutdownPolicy'] = self.zero_credit_shutdown_policy

        if self.new_buy_status is not None:
            result['newBuyStatus'] = self.new_buy_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')

        if m.get('AlarmThreshold') is not None:
            self.alarm_threshold = m.get('AlarmThreshold')

        if m.get('AvailableCredit') is not None:
            self.available_credit = m.get('AvailableCredit')

        if m.get('ConsumedUndeductedValue') is not None:
            self.consumed_undeducted_value = m.get('ConsumedUndeductedValue')

        if m.get('CreditLine') is not None:
            self.credit_line = m.get('CreditLine')

        if m.get('OutstandingBalance') is not None:
            self.outstanding_balance = m.get('OutstandingBalance')

        if m.get('PAYGFreezeStatus') is not None:
            self.paygfreeze_status = m.get('PAYGFreezeStatus')

        if m.get('ZeroCreditShutdownPolicy') is not None:
            self.zero_credit_shutdown_policy = m.get('ZeroCreditShutdownPolicy')

        if m.get('newBuyStatus') is not None:
            self.new_buy_status = m.get('newBuyStatus')

        return self

