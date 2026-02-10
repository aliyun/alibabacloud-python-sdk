# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterImageSecuritySummaryResponseBody(DaraModel):
    def __init__(
        self,
        cluster_image_event: main_models.DescribeClusterImageSecuritySummaryResponseBodyClusterImageEvent = None,
        request_id: str = None,
    ):
        # The information about the image-related security events.
        self.cluster_image_event = cluster_image_event
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cluster_image_event:
            self.cluster_image_event.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_image_event is not None:
            result['ClusterImageEvent'] = self.cluster_image_event.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterImageEvent') is not None:
            temp_model = main_models.DescribeClusterImageSecuritySummaryResponseBodyClusterImageEvent()
            self.cluster_image_event = temp_model.from_map(m.get('ClusterImageEvent'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClusterImageSecuritySummaryResponseBodyClusterImageEvent(DaraModel):
    def __init__(
        self,
        image_baseline: List[main_models.DescribeClusterImageSecuritySummaryResponseBodyClusterImageEventImageBaseline] = None,
        image_cve_vul: List[main_models.DescribeClusterImageSecuritySummaryResponseBodyClusterImageEventImageCveVul] = None,
        image_malicious_file: List[main_models.DescribeClusterImageSecuritySummaryResponseBodyClusterImageEventImageMaliciousFile] = None,
        image_sca_vul: List[main_models.DescribeClusterImageSecuritySummaryResponseBodyClusterImageEventImageScaVul] = None,
    ):
        # The information about image baseline risks.
        self.image_baseline = image_baseline
        # The information about image system vulnerabilities.
        self.image_cve_vul = image_cve_vul
        # The information about malicious image samples.
        self.image_malicious_file = image_malicious_file
        # The information about image application vulnerabilities.
        self.image_sca_vul = image_sca_vul

    def validate(self):
        if self.image_baseline:
            for v1 in self.image_baseline:
                 if v1:
                    v1.validate()
        if self.image_cve_vul:
            for v1 in self.image_cve_vul:
                 if v1:
                    v1.validate()
        if self.image_malicious_file:
            for v1 in self.image_malicious_file:
                 if v1:
                    v1.validate()
        if self.image_sca_vul:
            for v1 in self.image_sca_vul:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageBaseline'] = []
        if self.image_baseline is not None:
            for k1 in self.image_baseline:
                result['ImageBaseline'].append(k1.to_map() if k1 else None)

        result['ImageCveVul'] = []
        if self.image_cve_vul is not None:
            for k1 in self.image_cve_vul:
                result['ImageCveVul'].append(k1.to_map() if k1 else None)

        result['ImageMaliciousFile'] = []
        if self.image_malicious_file is not None:
            for k1 in self.image_malicious_file:
                result['ImageMaliciousFile'].append(k1.to_map() if k1 else None)

        result['ImageScaVul'] = []
        if self.image_sca_vul is not None:
            for k1 in self.image_sca_vul:
                result['ImageScaVul'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_baseline = []
        if m.get('ImageBaseline') is not None:
            for k1 in m.get('ImageBaseline'):
                temp_model = main_models.DescribeClusterImageSecuritySummaryResponseBodyClusterImageEventImageBaseline()
                self.image_baseline.append(temp_model.from_map(k1))

        self.image_cve_vul = []
        if m.get('ImageCveVul') is not None:
            for k1 in m.get('ImageCveVul'):
                temp_model = main_models.DescribeClusterImageSecuritySummaryResponseBodyClusterImageEventImageCveVul()
                self.image_cve_vul.append(temp_model.from_map(k1))

        self.image_malicious_file = []
        if m.get('ImageMaliciousFile') is not None:
            for k1 in m.get('ImageMaliciousFile'):
                temp_model = main_models.DescribeClusterImageSecuritySummaryResponseBodyClusterImageEventImageMaliciousFile()
                self.image_malicious_file.append(temp_model.from_map(k1))

        self.image_sca_vul = []
        if m.get('ImageScaVul') is not None:
            for k1 in m.get('ImageScaVul'):
                temp_model = main_models.DescribeClusterImageSecuritySummaryResponseBodyClusterImageEventImageScaVul()
                self.image_sca_vul.append(temp_model.from_map(k1))

        return self

class DescribeClusterImageSecuritySummaryResponseBodyClusterImageEventImageScaVul(DaraModel):
    def __init__(
        self,
        count: int = None,
        risk_level: str = None,
    ):
        # The number of image application vulnerabilities.
        self.count = count
        # The alert level. Valid values:
        # 
        # *   **asap**: high. You must fix the vulnerability at the earliest opportunity.
        # *   **nntf**: medium. You can fix the vulnerability based on your business requirements.
        # *   **later**: low. You can ignore the vulnerability.
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class DescribeClusterImageSecuritySummaryResponseBodyClusterImageEventImageMaliciousFile(DaraModel):
    def __init__(
        self,
        count: int = None,
        risk_level: str = None,
    ):
        # The number of malicious samples.
        self.count = count
        # The risk level. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class DescribeClusterImageSecuritySummaryResponseBodyClusterImageEventImageCveVul(DaraModel):
    def __init__(
        self,
        count: int = None,
        risk_level: str = None,
    ):
        # The number of vulnerabilities.
        self.count = count
        # The alert level. Valid values:
        # 
        # *   **asap**: high. You must fix the vulnerability at the earliest opportunity.
        # *   **nntf**: medium. You can fix the vulnerability based on your business requirements.
        # *   **later**: low. You can ignore the vulnerability.
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class DescribeClusterImageSecuritySummaryResponseBodyClusterImageEventImageBaseline(DaraModel):
    def __init__(
        self,
        count: int = None,
        risk_level: str = None,
    ):
        # The number of baselines.
        self.count = count
        # The risk level. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

