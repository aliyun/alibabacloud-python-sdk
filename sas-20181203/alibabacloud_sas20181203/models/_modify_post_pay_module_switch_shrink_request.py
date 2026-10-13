# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPostPayModuleSwitchShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        edr_module_switch_shrink: str = None,
        post_paid_host_auto_bind: int = None,
        post_paid_host_auto_bind_version: int = None,
        post_pay_instance_id: str = None,
        post_pay_module_switch: str = None,
        post_pay_module_switch_obj_shrink: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. Different requests must use different tokens. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform a dry run on the request. Valid values:
        # - true: Performs a dry run. The system checks the request but does not perform the actual operation.
        # - false: Performs the request normally.
        # Default value: false.
        self.dry_run = dry_run
        # The switch configuration of the EDR module.
        self.edr_module_switch_shrink = edr_module_switch_shrink
        # Specifies whether to automatically bind new assets to the host and container protection feature. Valid values:
        # 
        # - **0**: disabled
        # - **1**: enabled
        self.post_paid_host_auto_bind = post_paid_host_auto_bind
        # The edition to which new assets are automatically bound for host and container protection. Valid values:
        # - **1**: Free Edition 
        # - **3**: Enterprise Edition
        # - **5**: Advanced Edition
        # - **6**: Anti-virus Edition    
        # - **7**: Ultimate Edition
        self.post_paid_host_auto_bind_version = post_paid_host_auto_bind_version
        # The pay-as-you-go instance ID. This parameter is required.
        # 
        # > Invoke the [DescribeVersionConfig](~~DescribeVersionConfig~~) operation to obtain the value of this parameter.
        self.post_pay_instance_id = post_pay_instance_id
        # The switch status of pay-as-you-go modules. The value is a JSON string. Valid values:
        # - Key:
        #   - **VUL**: Vulnerability fixing module
        #   - **CSPM**: Cloud Security Posture Management module
        #   - **AGENTLESS**: Agentless detection module
        #   - **SERVERLESS**: Serverless security module
        #   - **CTDR**: Cloud Threat Detection and Response module
        #   - **POST_HOST**: Host and container security module
        #   - **SDK**: Malicious file detection SDK module
        #   - **RASP**: Application protection module
        #   - **CTDR_STORAGE**: Log management module
        #   - **ANTI_RANSOMWARE**: Anti-ransomware management
        # - Value: 0 indicates disabled. 1 indicates enabled.
        # 
        # > The values of modules that are not specified remain unchanged.
        # 
        # <notice>This parameter has the same meaning as the PostPayModuleSwitchObj parameter. If both parameters are specified, the value of PostPayModuleSwitch takes precedence.</notice>
        self.post_pay_module_switch = post_pay_module_switch
        # The switches of pay-as-you-go modules.
        # >Notice:  This parameter has the same meaning as the PostPayModuleSwitch parameter. If both parameters are specified, the value of PostPayModuleSwitch takes precedence.</notice>
        self.post_pay_module_switch_obj_shrink = post_pay_module_switch_obj_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.edr_module_switch_shrink is not None:
            result['EdrModuleSwitch'] = self.edr_module_switch_shrink

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EdrModuleSwitch') is not None:
            self.edr_module_switch_shrink = m.get('EdrModuleSwitch')

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

