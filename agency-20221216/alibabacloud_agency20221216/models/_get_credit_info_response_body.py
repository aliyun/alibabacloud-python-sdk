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
        # Result Code:
        # - 200 OK
        # - 1109 System Error
        self.code = code
        # The data returned.
        self.data = data
        # Message Information
        self.message = message
        # Request ID, Alibaba Cloud will track errors with this.
        self.request_id = request_id
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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
        zero_credit_shutdown_policy: str = None,
        new_buy_status: str = None,
    ):
        # The Credit Control status, Value Range:</br>
        # 1. normal - Sub Account status is running as usual.
        # 2. arrearsNotShutdown - Sub Account status is running as usual, but have outstanding bill(s).
        # 3. shutdown -  Sub Account status is down.
        self.account_status = account_status
        # Percentage value, when the available credit limit is lower than this credit limit percentage, a notification E-mail will be sent to the main account.
        self.alarm_threshold = alarm_threshold
        # The Credit available to consume.
        self.available_credit = available_credit
        # Obtain total unpaid amount on demo bill before simulated deduction.
        self.consumed_undeducted_value = consumed_undeducted_value
        # The Credit Line of Sub Account
        self.credit_line = credit_line
        # The Credit have been consumed by Sub Account, and haven\\"t be paid.
        self.outstanding_balance = outstanding_balance
        # The systematic controlling policy for resource management, specifically when the available Credit of Sub Account falls to 0 or less.</br>
        # 
        # - 1: delayStop. The account have Shutdown-delay Privilege,  After Shutdown-delay Credit is ran out, Alibaba Cloud will take over resources and keep the instance for 15 days. In addition, the instance will be released if Sub Account failed to pay the bill within these 15 days.</br>
        # - 2: noStop. Partner will manually manage Shutdown Status for Sub Account. Meanwhile, System would not manage the resource\\"s life-circle of Sub Account.</br>
        # - 3: immediatelyStop. Once valid quota of Sub Account falls below 0 and be identified as defaulting account, it will trigger the instance shutdown immediately.</br>
        self.zero_credit_shutdown_policy = zero_credit_shutdown_policy
        # Manage order operation.
        # - ban：Ban the new purchase action.
        # - normal：The account could raise new purchase order as usual.
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

        if m.get('ZeroCreditShutdownPolicy') is not None:
            self.zero_credit_shutdown_policy = m.get('ZeroCreditShutdownPolicy')

        if m.get('newBuyStatus') is not None:
            self.new_buy_status = m.get('newBuyStatus')

        return self

