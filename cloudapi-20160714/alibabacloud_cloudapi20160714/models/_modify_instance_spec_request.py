# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceSpecRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        instance_id: str = None,
        instance_spec: str = None,
        modify_action: str = None,
        skip_wait_switch: bool = None,
        token: str = None,
    ):
        # Specifies whether payment is automatically made during renewal. Valid values:
        # 
        # *   **True**: Automatic payment is enabled. Make sure that your Alibaba Cloud account has adequate balance.
        # *   **False**: Automatic payment is disabled. You have to manually pay in the console. Log on to the console. In the upper-right corner, choose **Expenses > User Center**. In the left-side navigation pane, click **Orders**. On the page that appears, find your order and complete the payment.
        # 
        # Default value: **False**.
        self.auto_pay = auto_pay
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The specifications of the instance.
        # 
        # This parameter is required.
        self.instance_spec = instance_spec
        # Specifies whether to upgrade or downgrade the instance. Valid values:
        # 
        # *   **UPGRADE**
        # *   **DOWNGRADE**
        # 
        # Default value: **UPGRADE**.
        self.modify_action = modify_action
        # Specifies whether to skip the Waiting for Traffic Switchover state. During the upgrade or downgrade, a new outbound IP address may be added to the API Gateway instance. The Waiting for Traffic Switchover state is used to remind users of adding the new outbound IP address to the whitelist. If you set the SkipWaitSwitch parameter to true, the instance does not enter the Waiting for Traffic Switchover state when a new outbound IP address is available. Instead, the system sends internal messages to the user.
        self.skip_wait_switch = skip_wait_switch
        # The password.
        # 
        # This parameter is required.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.modify_action is not None:
            result['ModifyAction'] = self.modify_action

        if self.skip_wait_switch is not None:
            result['SkipWaitSwitch'] = self.skip_wait_switch

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('ModifyAction') is not None:
            self.modify_action = m.get('ModifyAction')

        if m.get('SkipWaitSwitch') is not None:
            self.skip_wait_switch = m.get('SkipWaitSwitch')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

