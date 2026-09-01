# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetInstanceAuthRangeResponseBody(DaraModel):
    def __init__(
        self,
        instance_auth_range: main_models.GetInstanceAuthRangeResponseBodyInstanceAuthRange = None,
        request_id: str = None,
    ):
        # The instance authorization range validation.
        self.instance_auth_range = instance_auth_range
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.instance_auth_range:
            self.instance_auth_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_auth_range is not None:
            result['InstanceAuthRange'] = self.instance_auth_range.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceAuthRange') is not None:
            temp_model = main_models.GetInstanceAuthRangeResponseBodyInstanceAuthRange()
            self.instance_auth_range = temp_model.from_map(m.get('InstanceAuthRange'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceAuthRangeResponseBodyInstanceAuthRange(DaraModel):
    def __init__(
        self,
        advanced_count: str = None,
        anti_ransomware_capacity: str = None,
        anti_ransomware_service: int = None,
        anti_virus_core: str = None,
        container_core: str = None,
        container_count: str = None,
        cspm_capacity: str = None,
        cspm_instance_capacity: str = None,
        enterprise_count: str = None,
        honeypot_capacity: str = None,
        image_scan_capacity: str = None,
        rasp_capacity: str = None,
        sdk_capacity: str = None,
        sls_capacity: str = None,
        threat_analysis_capacity: str = None,
        threat_analysis_flow: str = None,
        web_lock_capacity: str = None,
    ):
        # The number of instances for the Advanced Edition. Valid values:
        # 
        # - **1-2000000000**: range
        # - **1**: step
        self.advanced_count = advanced_count
        # The anti-ransomware capacity. Valid values:
        # 
        # - **1-9000000000**: range
        # - **10**: step
        self.anti_ransomware_capacity = anti_ransomware_capacity
        # The anti-ransomware managed service. Valid values:
        # - **0**: Not activated.
        # - **1**: Activated.
        self.anti_ransomware_service = anti_ransomware_service
        # The number of cores for Anti-virus Edition. Valid values:
        # 
        # - **1-2000000000**: range
        # - **1**: step
        self.anti_virus_core = anti_virus_core
        # The number of cores for the Ultimate Edition. Valid values:
        # 
        # - **1-2000000000**: range
        # - **1**: step
        self.container_core = container_core
        # The number of instances for the Ultimate Edition. Valid values:
        # 
        # - **1-2000000000**: range
        # - **1**: step
        self.container_count = container_count
        # The number of cloud platform configuration check scans. Valid values:
        # 
        # - **15000-9999999999**: range
        # - **55000**: step
        self.cspm_capacity = cspm_capacity
        self.cspm_instance_capacity = cspm_instance_capacity
        # The number of instances for the Enterprise Edition. Valid values:
        # - **Value**: 1-2000000000
        # - **Step**: 1
        self.enterprise_count = enterprise_count
        # The number of honeypot authorizations. Valid values:
        # 
        # - **20-500**: range
        # - **1**: step
        self.honeypot_capacity = honeypot_capacity
        # The number of image scan authorizations. Valid values:
        # 
        # - **1-200000**: range
        # - **20**: step
        self.image_scan_capacity = image_scan_capacity
        # The number of application protection authorizations. Valid values:
        # 
        # - **1-100000000**: range
        # - **1**: step
        self.rasp_capacity = rasp_capacity
        # The number of malicious file detection SDK authorizations. Valid values:
        # 
        # - **10-9999999999**: range
        # - **10**: step
        self.sdk_capacity = sdk_capacity
        # The log storage capacity. Valid values:
        # 
        # - **1-600000000**: range
        # - **10**: step
        self.sls_capacity = sls_capacity
        # The threat analysis capacity. Valid values:
        # 
        # - **1-9999999999**: range
        # - **1000**: step
        self.threat_analysis_capacity = threat_analysis_capacity
        # The log ingestion traffic for threat detection and response. Valid values:
        # 
        # - **1-9999999999**: range
        # - **100**: step
        self.threat_analysis_flow = threat_analysis_flow
        # The number of web tamper-proofing authorizations. Valid values:
        # 
        # - **1-9999**: range
        # - **1**: step
        self.web_lock_capacity = web_lock_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_count is not None:
            result['AdvancedCount'] = self.advanced_count

        if self.anti_ransomware_capacity is not None:
            result['AntiRansomwareCapacity'] = self.anti_ransomware_capacity

        if self.anti_ransomware_service is not None:
            result['AntiRansomwareService'] = self.anti_ransomware_service

        if self.anti_virus_core is not None:
            result['AntiVirusCore'] = self.anti_virus_core

        if self.container_core is not None:
            result['ContainerCore'] = self.container_core

        if self.container_count is not None:
            result['ContainerCount'] = self.container_count

        if self.cspm_capacity is not None:
            result['CspmCapacity'] = self.cspm_capacity

        if self.cspm_instance_capacity is not None:
            result['CspmInstanceCapacity'] = self.cspm_instance_capacity

        if self.enterprise_count is not None:
            result['EnterpriseCount'] = self.enterprise_count

        if self.honeypot_capacity is not None:
            result['HoneypotCapacity'] = self.honeypot_capacity

        if self.image_scan_capacity is not None:
            result['ImageScanCapacity'] = self.image_scan_capacity

        if self.rasp_capacity is not None:
            result['RaspCapacity'] = self.rasp_capacity

        if self.sdk_capacity is not None:
            result['SdkCapacity'] = self.sdk_capacity

        if self.sls_capacity is not None:
            result['SlsCapacity'] = self.sls_capacity

        if self.threat_analysis_capacity is not None:
            result['ThreatAnalysisCapacity'] = self.threat_analysis_capacity

        if self.threat_analysis_flow is not None:
            result['ThreatAnalysisFlow'] = self.threat_analysis_flow

        if self.web_lock_capacity is not None:
            result['WebLockCapacity'] = self.web_lock_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedCount') is not None:
            self.advanced_count = m.get('AdvancedCount')

        if m.get('AntiRansomwareCapacity') is not None:
            self.anti_ransomware_capacity = m.get('AntiRansomwareCapacity')

        if m.get('AntiRansomwareService') is not None:
            self.anti_ransomware_service = m.get('AntiRansomwareService')

        if m.get('AntiVirusCore') is not None:
            self.anti_virus_core = m.get('AntiVirusCore')

        if m.get('ContainerCore') is not None:
            self.container_core = m.get('ContainerCore')

        if m.get('ContainerCount') is not None:
            self.container_count = m.get('ContainerCount')

        if m.get('CspmCapacity') is not None:
            self.cspm_capacity = m.get('CspmCapacity')

        if m.get('CspmInstanceCapacity') is not None:
            self.cspm_instance_capacity = m.get('CspmInstanceCapacity')

        if m.get('EnterpriseCount') is not None:
            self.enterprise_count = m.get('EnterpriseCount')

        if m.get('HoneypotCapacity') is not None:
            self.honeypot_capacity = m.get('HoneypotCapacity')

        if m.get('ImageScanCapacity') is not None:
            self.image_scan_capacity = m.get('ImageScanCapacity')

        if m.get('RaspCapacity') is not None:
            self.rasp_capacity = m.get('RaspCapacity')

        if m.get('SdkCapacity') is not None:
            self.sdk_capacity = m.get('SdkCapacity')

        if m.get('SlsCapacity') is not None:
            self.sls_capacity = m.get('SlsCapacity')

        if m.get('ThreatAnalysisCapacity') is not None:
            self.threat_analysis_capacity = m.get('ThreatAnalysisCapacity')

        if m.get('ThreatAnalysisFlow') is not None:
            self.threat_analysis_flow = m.get('ThreatAnalysisFlow')

        if m.get('WebLockCapacity') is not None:
            self.web_lock_capacity = m.get('WebLockCapacity')

        return self

