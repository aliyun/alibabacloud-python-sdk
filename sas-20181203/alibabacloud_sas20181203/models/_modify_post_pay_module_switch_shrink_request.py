# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPostPayModuleSwitchShrinkRequest(DaraModel):
    def __init__(
        self,
        post_paid_host_auto_bind: int = None,
        post_paid_host_auto_bind_version: int = None,
        post_pay_instance_id: str = None,
        post_pay_module_switch: str = None,
        post_pay_module_switch_obj_shrink: str = None,
    ):
        # Specifies whether to automatically bind newly added assets for host and container protection. Valid values:
        # 
        # - **0**: Disabled.
        # - **1**: Enabled.
        self.post_paid_host_auto_bind = post_paid_host_auto_bind
        # The version to which newly added assets are automatically bound for host and container protection. Valid values:
        # - **1**: Free Edition. 
        # - **3**: Enterprise Edition.
        # - **5**: Advanced Edition.
        # - **6**: Anti-virus Edition.    
        # - **7**: Ultimate Edition.
        self.post_paid_host_auto_bind_version = post_paid_host_auto_bind_version
        # The pay-as-you-go instance ID. This parameter is required.
        # 
        # > Invoke the [DescribeVersionConfig](~~DescribeVersionConfig~~) operation to obtain this parameter.
        self.post_pay_instance_id = post_pay_instance_id
        # The switch status of pay-as-you-go modules in JSON string format. Valid values:
        # - Key:
        #   - **VUL**: vulnerability fix module
        #   - **CSPM**: Cloud Security Posture Management (CSPM) module
        #   - **AGENTLESS**: agentless detection module
        #   - **SERVERLESS**: serverless security module
        #   - **CTDR**: threat detection and response module
        #   - **POST_HOST**: host and container security module
        #   - **SDK**: malicious file detection SDK module
        #   - **RASP**: application protection module
        #   - **CTDR_STORAGE**: log management module
        #   - **ANTI_RANSOMWARE**: anti-ransomware management
        # - Value: 0 indicates disabled. 1 indicates enabled.
        # 
        # > Modules for which no value is specified remain unchanged.
        # 
        # <notice>This parameter has the same meaning as PostPayModuleSwitchObj. If both parameters are specified, the value of PostPayModuleSwitch takes precedence..
        self.post_pay_module_switch = post_pay_module_switch
        # The pay-as-you-go module switch.
        # >Notice: This parameter has the same meaning as PostPayModuleSwitch. If both parameters are specified, the value of PostPayModuleSwitch takes precedence..
        self.post_pay_module_switch_obj_shrink = post_pay_module_switch_obj_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.post_paid_host_auto_bind is not None:
            result['PostPaidHostAutoBind'] = self.post_paid_host_auto_bind

        if self.post_paid_host_auto_bind_version is not None:
            result['PostPaidHostAutoBindVersion'] = self.post_paid_host_auto_bind_version

        if self.post_pay_instance_id is not None:
            result['PostPayInstanceId'] = self.post_pay_instance_id

        if self.post_pay_module_switch is not None:
            result['PostPayModuleSwitch'] = self.post_pay_module_switch

        if self.post_pay_module_switch_obj_shrink is not None:
            result['PostPayModuleSwitchObj'] = self.post_pay_module_switch_obj_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PostPaidHostAutoBind') is not None:
            self.post_paid_host_auto_bind = m.get('PostPaidHostAutoBind')

        if m.get('PostPaidHostAutoBindVersion') is not None:
            self.post_paid_host_auto_bind_version = m.get('PostPaidHostAutoBindVersion')

        if m.get('PostPayInstanceId') is not None:
            self.post_pay_instance_id = m.get('PostPayInstanceId')

        if m.get('PostPayModuleSwitch') is not None:
            self.post_pay_module_switch = m.get('PostPayModuleSwitch')

        if m.get('PostPayModuleSwitchObj') is not None:
            self.post_pay_module_switch_obj_shrink = m.get('PostPayModuleSwitchObj')

        return self

