# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class UpdateMultiUserInstancesRequest(DaraModel):
    def __init__(
        self,
        member_instances: List[main_models.UpdateMultiUserInstancesRequestMemberInstances] = None,
    ):
        # Member instances.
        self.member_instances = member_instances

    def validate(self):
        if self.member_instances:
            for v1 in self.member_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MemberInstances'] = []
        if self.member_instances is not None:
            for k1 in self.member_instances:
                result['MemberInstances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_instances = []
        if m.get('MemberInstances') is not None:
            for k1 in m.get('MemberInstances'):
                temp_model = main_models.UpdateMultiUserInstancesRequestMemberInstances()
                self.member_instances.append(temp_model.from_map(k1))

        return self

class UpdateMultiUserInstancesRequestMemberInstances(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        anti_ransomware_capacity: int = None,
        charge_type: str = None,
        cspm_capacity: int = None,
        honeypot_capacity: int = None,
        image_scan_capacity: int = None,
        instance_id: str = None,
        opt_type: str = None,
        rasp_capacity: int = None,
        sdk_capacity: int = None,
        sls_capacity: int = None,
        status: int = None,
        threat_analysis_capacity: int = None,
        threat_analysis_flow: int = None,
        version: str = None,
        version_summary: List[main_models.UpdateMultiUserInstancesRequestMemberInstancesVersionSummary] = None,
        web_lock_capacity: int = None,
    ):
        # The Alibaba Cloud account UID of the member.
        self.ali_uid = ali_uid
        # Anti-ransomware capacity allocated to the member, in GB.
        self.anti_ransomware_capacity = anti_ransomware_capacity
        # Charge type, values:
        # * **PREPAID**: Prepaid.
        # * **POSTPAID** (default): Postpaid.
        self.charge_type = charge_type
        # Cloud platform configuration check scan count allocated to the member. Unit: times per month.
        self.cspm_capacity = cspm_capacity
        # Honeypot authorization count allocated to the member.
        self.honeypot_capacity = honeypot_capacity
        # Image scan authorization count allocated to the member.
        self.image_scan_capacity = image_scan_capacity
        # The Cloud Security Center instance ID purchased by the member account.
        self.instance_id = instance_id
        # Operation type. Values:  
        # - **ADD**: Add 
        # - **CHANGE**: Change
        # - **DEL**: Delete
        self.opt_type = opt_type
        # Application protection count allocated to the member. Unit: per month.
        self.rasp_capacity = rasp_capacity
        # Malicious file detection SDK authorization count allocated to the member.
        self.sdk_capacity = sdk_capacity
        # Log storage capacity allocated to the member, in GB.
        self.sls_capacity = sls_capacity
        # Status of the member account instance. Values: 
        # - **1**: Valid. 
        # - **2**: Invalid.
        self.status = status
        # Threat analysis capacity allocated to the member. Unit: GB.
        self.threat_analysis_capacity = threat_analysis_capacity
        # Threat analysis and response log access traffic allocated to the member. Unit: GB/day.
        self.threat_analysis_flow = threat_analysis_flow
        # The version of Cloud Security Center protection to be bound. Values:  
        # - **1**: Free Edition 
        # - **3**: Enterprise Edition
        # - **5**: Advanced Edition
        # - **6**: Antivirus Edition    
        # - **7**: Flagship Edition
        self.version = version
        # Member account authorization usage information.
        self.version_summary = version_summary
        # Web tamper-proof authorization count allocated to the member.
        self.web_lock_capacity = web_lock_capacity

    def validate(self):
        if self.version_summary:
            for v1 in self.version_summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.anti_ransomware_capacity is not None:
            result['AntiRansomwareCapacity'] = self.anti_ransomware_capacity

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cspm_capacity is not None:
            result['CspmCapacity'] = self.cspm_capacity

        if self.honeypot_capacity is not None:
            result['HoneypotCapacity'] = self.honeypot_capacity

        if self.image_scan_capacity is not None:
            result['ImageScanCapacity'] = self.image_scan_capacity

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.opt_type is not None:
            result['OptType'] = self.opt_type

        if self.rasp_capacity is not None:
            result['RaspCapacity'] = self.rasp_capacity

        if self.sdk_capacity is not None:
            result['SdkCapacity'] = self.sdk_capacity

        if self.sls_capacity is not None:
            result['SlsCapacity'] = self.sls_capacity

        if self.status is not None:
            result['Status'] = self.status

        if self.threat_analysis_capacity is not None:
            result['ThreatAnalysisCapacity'] = self.threat_analysis_capacity

        if self.threat_analysis_flow is not None:
            result['ThreatAnalysisFlow'] = self.threat_analysis_flow

        if self.version is not None:
            result['Version'] = self.version

        result['VersionSummary'] = []
        if self.version_summary is not None:
            for k1 in self.version_summary:
                result['VersionSummary'].append(k1.to_map() if k1 else None)

        if self.web_lock_capacity is not None:
            result['WebLockCapacity'] = self.web_lock_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('AntiRansomwareCapacity') is not None:
            self.anti_ransomware_capacity = m.get('AntiRansomwareCapacity')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CspmCapacity') is not None:
            self.cspm_capacity = m.get('CspmCapacity')

        if m.get('HoneypotCapacity') is not None:
            self.honeypot_capacity = m.get('HoneypotCapacity')

        if m.get('ImageScanCapacity') is not None:
            self.image_scan_capacity = m.get('ImageScanCapacity')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OptType') is not None:
            self.opt_type = m.get('OptType')

        if m.get('RaspCapacity') is not None:
            self.rasp_capacity = m.get('RaspCapacity')

        if m.get('SdkCapacity') is not None:
            self.sdk_capacity = m.get('SdkCapacity')

        if m.get('SlsCapacity') is not None:
            self.sls_capacity = m.get('SlsCapacity')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ThreatAnalysisCapacity') is not None:
            self.threat_analysis_capacity = m.get('ThreatAnalysisCapacity')

        if m.get('ThreatAnalysisFlow') is not None:
            self.threat_analysis_flow = m.get('ThreatAnalysisFlow')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        self.version_summary = []
        if m.get('VersionSummary') is not None:
            for k1 in m.get('VersionSummary'):
                temp_model = main_models.UpdateMultiUserInstancesRequestMemberInstancesVersionSummary()
                self.version_summary.append(temp_model.from_map(k1))

        if m.get('WebLockCapacity') is not None:
            self.web_lock_capacity = m.get('WebLockCapacity')

        return self

class UpdateMultiUserInstancesRequestMemberInstancesVersionSummary(DaraModel):
    def __init__(
        self,
        core_count: int = None,
        ecs_count: int = None,
        version: int = None,
    ):
        # Number of cores authorized for the member.
        self.core_count = core_count
        # Number of authorizations allocated to the member.
        self.ecs_count = ecs_count
        # Version of the Cloud Security Center for the member account. Values:  
        # - **1**: Free Edition 
        # - **3**: Enterprise Edition
        # - **5**: Advanced Edition
        # - **6**: Antivirus Edition    
        # - **7**: Flagship Edition   
        # - **8**: Multiple Versions   
        # - **10**: Only Purchase Value-Added Services
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.core_count is not None:
            result['CoreCount'] = self.core_count

        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreCount') is not None:
            self.core_count = m.get('CoreCount')

        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

