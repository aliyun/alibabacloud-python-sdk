# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ModifyPostPayModuleSwitchRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        edr_module_switch: main_models.ModifyPostPayModuleSwitchRequestEdrModuleSwitch = None,
        post_paid_host_auto_bind: int = None,
        post_paid_host_auto_bind_version: int = None,
        post_pay_instance_id: str = None,
        post_pay_module_switch: str = None,
        post_pay_module_switch_obj: main_models.ModifyPostPayModuleSwitchRequestPostPayModuleSwitchObj = None,
    ):
        # The client token that is used to ensure the idempotence of the request. Different requests must use different tokens. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform a dry run on the request. Valid values:
        # - true: Performs a dry run. The system checks the request but does not perform the actual operation.
        # - false: Performs the request normally.
        # Default value: false.
        self.dry_run = dry_run
        # The switch configuration of the EDR module.
        self.edr_module_switch = edr_module_switch
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
        self.post_pay_module_switch_obj = post_pay_module_switch_obj

    def validate(self):
        if self.edr_module_switch:
            self.edr_module_switch.validate()
        if self.post_pay_module_switch_obj:
            self.post_pay_module_switch_obj.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.edr_module_switch is not None:
            result['EdrModuleSwitch'] = self.edr_module_switch.to_map()

        if self.post_paid_host_auto_bind is not None:
            result['PostPaidHostAutoBind'] = self.post_paid_host_auto_bind

        if self.post_paid_host_auto_bind_version is not None:
            result['PostPaidHostAutoBindVersion'] = self.post_paid_host_auto_bind_version

        if self.post_pay_instance_id is not None:
            result['PostPayInstanceId'] = self.post_pay_instance_id

        if self.post_pay_module_switch is not None:
            result['PostPayModuleSwitch'] = self.post_pay_module_switch

        if self.post_pay_module_switch_obj is not None:
            result['PostPayModuleSwitchObj'] = self.post_pay_module_switch_obj.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EdrModuleSwitch') is not None:
            temp_model = main_models.ModifyPostPayModuleSwitchRequestEdrModuleSwitch()
            self.edr_module_switch = temp_model.from_map(m.get('EdrModuleSwitch'))

        if m.get('PostPaidHostAutoBind') is not None:
            self.post_paid_host_auto_bind = m.get('PostPaidHostAutoBind')

        if m.get('PostPaidHostAutoBindVersion') is not None:
            self.post_paid_host_auto_bind_version = m.get('PostPaidHostAutoBindVersion')

        if m.get('PostPayInstanceId') is not None:
            self.post_pay_instance_id = m.get('PostPayInstanceId')

        if m.get('PostPayModuleSwitch') is not None:
            self.post_pay_module_switch = m.get('PostPayModuleSwitch')

        if m.get('PostPayModuleSwitchObj') is not None:
            temp_model = main_models.ModifyPostPayModuleSwitchRequestPostPayModuleSwitchObj()
            self.post_pay_module_switch_obj = temp_model.from_map(m.get('PostPayModuleSwitchObj'))

        return self

class ModifyPostPayModuleSwitchRequestPostPayModuleSwitchObj(DaraModel):
    def __init__(
        self,
        agentless: int = None,
        ai_digital: int = None,
        anti_ransomware: int = None,
        basic_service: int = None,
        cspm: int = None,
        ctdr: int = None,
        ctdr_storage: int = None,
        post_host: int = None,
        rasp: int = None,
        sdk: int = None,
        serverless: int = None,
        vul: int = None,
        web_lock: int = None,
    ):
        # The agentless detection module. Valid values:
        # - **0**: disabled
        # - **1**: enabled
        self.agentless = agentless
        # The AI digitalization feature.
        self.ai_digital = ai_digital
        # The anti-ransomware module. Valid values:
        # - **0**: disabled
        # - **1**: enabled
        self.anti_ransomware = anti_ransomware
        # The basic service module. Valid values:
        # - **0**: disabled
        # - **1**: enabled
        # 
        # >Notice: You cannot manually change the switch of the basic service module. If any other module is enabled, the enabling status of this module is enabled. If all other modules are shutdown, this module is not in the shutdown state.</notice>
        self.basic_service = basic_service
        # The Cloud Security Posture Management (CSPM) module. Valid values:
        # - **0**: disabled
        # - **1**: enabled
        self.cspm = cspm
        # The Cloud Threat Detection and Response (CTDR) module. Valid values:
        # - **0**: disabled
        # - **1**: enabled
        self.ctdr = ctdr
        # The log management module. Valid values:
        # - **0**: disabled
        # - **1**: enabled
        self.ctdr_storage = ctdr_storage
        # The host and container security module. Valid values:
        # - **0**: disabled
        # - **1**: enabled
        self.post_host = post_host
        # The application protection module. Valid values:
        # - **0**: disabled
        # - **1**: enabled
        self.rasp = rasp
        # The malicious file detection SDK module. Valid values:
        # - **0**: disabled
        # - **1**: enabled
        self.sdk = sdk
        # The Serverless security module. Valid values:
        # - **0**: disabled
        # - **1**: enabled
        self.serverless = serverless
        # The vulnerability fixing module. Valid values:
        # - **0**: disabled
        # - **1**: enabled
        self.vul = vul
        # The file tamper-proofing module. Valid values:
        # - **0**: disabled
        # - **1**: enabled
        self.web_lock = web_lock

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentless is not None:
            result['Agentless'] = self.agentless

        if self.ai_digital is not None:
            result['AiDigital'] = self.ai_digital

        if self.anti_ransomware is not None:
            result['AntiRansomware'] = self.anti_ransomware

        if self.basic_service is not None:
            result['BasicService'] = self.basic_service

        if self.cspm is not None:
            result['Cspm'] = self.cspm

        if self.ctdr is not None:
            result['Ctdr'] = self.ctdr

        if self.ctdr_storage is not None:
            result['CtdrStorage'] = self.ctdr_storage

        if self.post_host is not None:
            result['PostHost'] = self.post_host

        if self.rasp is not None:
            result['Rasp'] = self.rasp

        if self.sdk is not None:
            result['Sdk'] = self.sdk

        if self.serverless is not None:
            result['Serverless'] = self.serverless

        if self.vul is not None:
            result['Vul'] = self.vul

        if self.web_lock is not None:
            result['WebLock'] = self.web_lock

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agentless') is not None:
            self.agentless = m.get('Agentless')

        if m.get('AiDigital') is not None:
            self.ai_digital = m.get('AiDigital')

        if m.get('AntiRansomware') is not None:
            self.anti_ransomware = m.get('AntiRansomware')

        if m.get('BasicService') is not None:
            self.basic_service = m.get('BasicService')

        if m.get('Cspm') is not None:
            self.cspm = m.get('Cspm')

        if m.get('Ctdr') is not None:
            self.ctdr = m.get('Ctdr')

        if m.get('CtdrStorage') is not None:
            self.ctdr_storage = m.get('CtdrStorage')

        if m.get('PostHost') is not None:
            self.post_host = m.get('PostHost')

        if m.get('Rasp') is not None:
            self.rasp = m.get('Rasp')

        if m.get('Sdk') is not None:
            self.sdk = m.get('Sdk')

        if m.get('Serverless') is not None:
            self.serverless = m.get('Serverless')

        if m.get('Vul') is not None:
            self.vul = m.get('Vul')

        if m.get('WebLock') is not None:
            self.web_lock = m.get('WebLock')

        return self

class ModifyPostPayModuleSwitchRequestEdrModuleSwitch(DaraModel):
    def __init__(
        self,
        auto_bind: int = None,
        edr_host_usage: int = None,
    ):
        # Specifies whether to enable automatic binding of new assets to the EDR module. A value of 0 indicates that the feature is disabled. A value of 1 indicates that the feature is enabled.
        self.auto_bind = auto_bind
        # The authorized quota for EDR hosts.
        self.edr_host_usage = edr_host_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_bind is not None:
            result['AutoBind'] = self.auto_bind

        if self.edr_host_usage is not None:
            result['EDR_HOST_USAGE'] = self.edr_host_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBind') is not None:
            self.auto_bind = m.get('AutoBind')

        if m.get('EDR_HOST_USAGE') is not None:
            self.edr_host_usage = m.get('EDR_HOST_USAGE')

        return self

