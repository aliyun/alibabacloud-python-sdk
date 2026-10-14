# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyInstanceChargeTypeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        billing_cycle: str = None,
        include_data_disks: bool = None,
        instance_charge_type: str = None,
        instance_ids: List[str] = None,
        period: str = None,
        period_unit: str = None,
    ):
        # Specifies whether to automatically complete the payment when you switch the billing method of the instance from pay-as-you-go to subscription. Valid values:
        # 
        # true: The payment is automatically completed. Make sure that your account balance is sufficient.
        # 
        # false: Only an order is generated but no payment is made. This is the default value.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal when converting the instance from pay-as-you-go to subscription. Valid values:
        # 
        # - true: Auto-renewal is enabled.
        # - false: Auto-renewal is not enabled (default).
        self.auto_renew = auto_renew
        # The billing cycle. Valid values: Month, Day, and Hour.
        self.billing_cycle = billing_cycle
        # Specifies whether to convert all pay-as-you-go data cloud disks created with the instance to subscription data cloud disks when converting an instance-level pay-as-you-go instance to a subscription instance. Valid values:
        self.include_data_disks = include_data_disks
        # The target billing method of the instance. Valid values:
        # 
        # This parameter is required.
        self.instance_charge_type = instance_charge_type
        # The list of instance IDs.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The subscription duration when converting a pay-as-you-go instance to subscription. This parameter is required in this scenario. Valid values:
        # 
        # If PeriodUnit is set to Day, Period can only be set to 3.
        # 
        # If PeriodUnit is set to Month, Period can be set to 1-9 or 12.
        self.period = period
        # The unit of the subscription duration when converting an instance-level pay-as-you-go instance to a subscription instance. This parameter is required in this scenario. Valid values:
        self.period_unit = period_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.include_data_disks is not None:
            result['IncludeDataDisks'] = self.include_data_disks

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('IncludeDataDisks') is not None:
            self.include_data_disks = m.get('IncludeDataDisks')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        return self

