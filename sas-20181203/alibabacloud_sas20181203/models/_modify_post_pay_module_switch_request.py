# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ModifyPostPayModuleSwitchRequest(DaraModel):
    def __init__(
        self,
        post_paid_host_auto_bind: int = None,
        post_paid_host_auto_bind_version: int = None,
        post_pay_instance_id: str = None,
        post_pay_module_switch: str = None,
        post_pay_module_switch_obj: main_models.ModifyPostPayModuleSwitchRequestPostPayModuleSwitchObj = None,
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
        self.post_pay_module_switch_obj = post_pay_module_switch_obj

    def validate(self):
        if self.post_pay_module_switch_obj:
            self.post_pay_module_switch_obj.validate()

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

        if self.post_pay_module_switch_obj is not None:
            result['PostPayModuleSwitchObj'] = self.post_pay_module_switch_obj.to_map()

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
        # Agentless Detection Module. Values:
        # - **0**: Off
        # - **1**: On
        self.agentless = agentless
        # AI Digitization
        self.ai_digital = ai_digital
        # Anti-Ransomware Module. Values:
        # - **0**: Off
        # - **1**: On
        self.anti_ransomware = anti_ransomware
        # Basic service module. Values:
        # - **0**: Off
        # - **1**: On
        # 
        # >Notice: The basic service module switch does not support active modification. When other modules are on, this module is also on. If all other modules are off, then this module is off.
        self.basic_service = basic_service
        # Cloud Security Configuration Check Module. Values:
        # - **0**: Off
        # - **1**: On
        self.cspm = cspm
        # Threat Analysis and Response Module. Values:
        # - **0**: Off
        # - **1**: On
        self.ctdr = ctdr
        # Log Management Module. Values:
        # - **0**: Off
        # - **1**: On
        self.ctdr_storage = ctdr_storage
        # Host and Container Security Module. Values:
        # - **0**: Off
        # - **1**: On
        self.post_host = post_host
        # Application Protection Module. Values:
        # - **0**: Off
        # - **1**: On
        self.rasp = rasp
        # Malicious File Detection SDK Module. Values:
        # - **0**: Off
        # - **1**: On
        self.sdk = sdk
        # Serverless Security Module. Values:
        # - **0**: Off
        # - **1**: On
        self.serverless = serverless
        # Vulnerability Repair Module. Values:
        # - **0**: Off
        # - **1**: On
        self.vul = vul
        # File Tamper Protection Module. Values:
        # - **0**: Off
        # - **1**: On
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

