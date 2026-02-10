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
        # Automatic binding switch for new assets in host and container protection. Values:
        # 
        # - **0**: Off
        # - **1**: On
        self.post_paid_host_auto_bind = post_paid_host_auto_bind
        # Version for automatic binding of new assets in host and container protection. Values:
        # - **1**: Free Edition 
        # - **3**: Enterprise Edition
        # - **5**: Advanced Edition
        # - **6**: Antivirus Edition    
        # - **7**: Flagship Edition
        self.post_paid_host_auto_bind_version = post_paid_host_auto_bind_version
        # Pay-as-you-go instance ID, which must be filled in.
        # 
        # > Call the [DescribeVersionConfig](~~DescribeVersionConfig~~) interface to obtain this parameter.
        self.post_pay_instance_id = post_pay_instance_id
        # Status of the pay-as-you-go module switch, in JsonString format. Values:
        # - Key:
        #   - **VUL**: Vulnerability Repair Module
        #   - **CSPM**: Cloud Security Posture Management Module
        #   - **AGENTLESS**: Agentless Detection Module
        #   - **SERVERLESS**: Serverless Security Module
        #   - **CTDR**: Threat Analysis and Response Module
        #   - **POST_HOST**: Host and Container Security Module
        #   - **SDK**: Malicious File Detection SDK Module
        #   - **RASP**: Application Protection Module
        #   - **CTDR_STORAGE**: Log Management Module
        #   - **ANTI_RANSOMWARE**: Anti-Ransomware Management
        # - Value: 0 means off, 1 means on
        # 
        # > The values of modules not passed will not change.
        # 
        # <notice>The meaning is the same as the PostPayModuleSwitchObj field. When both exist, the value of PostPayModuleSwitch takes precedence.
        self.post_pay_module_switch = post_pay_module_switch
        # Pay-as-you-go module switch.
        # >Notice:  The meaning is the same as the PostPayModuleSwitch field. When both exist, the value of PostPayModuleSwitch takes precedence.
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

