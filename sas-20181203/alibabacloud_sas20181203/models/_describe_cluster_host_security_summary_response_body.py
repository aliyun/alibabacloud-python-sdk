# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterHostSecuritySummaryResponseBody(DaraModel):
    def __init__(
        self,
        cluster_host_event: main_models.DescribeClusterHostSecuritySummaryResponseBodyClusterHostEvent = None,
        request_id: str = None,
    ):
        # The alert details of the hosts.
        self.cluster_host_event = cluster_host_event
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cluster_host_event:
            self.cluster_host_event.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_host_event is not None:
            result['ClusterHostEvent'] = self.cluster_host_event.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterHostEvent') is not None:
            temp_model = main_models.DescribeClusterHostSecuritySummaryResponseBodyClusterHostEvent()
            self.cluster_host_event = temp_model.from_map(m.get('ClusterHostEvent'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClusterHostSecuritySummaryResponseBodyClusterHostEvent(DaraModel):
    def __init__(
        self,
        alarm_event: List[main_models.DescribeClusterHostSecuritySummaryResponseBodyClusterHostEventAlarmEvent] = None,
        baseline_event: List[main_models.DescribeClusterHostSecuritySummaryResponseBodyClusterHostEventBaselineEvent] = None,
        vul_event: List[main_models.DescribeClusterHostSecuritySummaryResponseBodyClusterHostEventVulEvent] = None,
    ):
        # The alert details of the host.
        self.alarm_event = alarm_event
        # The baseline details of the host.
        self.baseline_event = baseline_event
        # The vulnerability details of the host.
        self.vul_event = vul_event

    def validate(self):
        if self.alarm_event:
            for v1 in self.alarm_event:
                 if v1:
                    v1.validate()
        if self.baseline_event:
            for v1 in self.baseline_event:
                 if v1:
                    v1.validate()
        if self.vul_event:
            for v1 in self.vul_event:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlarmEvent'] = []
        if self.alarm_event is not None:
            for k1 in self.alarm_event:
                result['AlarmEvent'].append(k1.to_map() if k1 else None)

        result['BaselineEvent'] = []
        if self.baseline_event is not None:
            for k1 in self.baseline_event:
                result['BaselineEvent'].append(k1.to_map() if k1 else None)

        result['VulEvent'] = []
        if self.vul_event is not None:
            for k1 in self.vul_event:
                result['VulEvent'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_event = []
        if m.get('AlarmEvent') is not None:
            for k1 in m.get('AlarmEvent'):
                temp_model = main_models.DescribeClusterHostSecuritySummaryResponseBodyClusterHostEventAlarmEvent()
                self.alarm_event.append(temp_model.from_map(k1))

        self.baseline_event = []
        if m.get('BaselineEvent') is not None:
            for k1 in m.get('BaselineEvent'):
                temp_model = main_models.DescribeClusterHostSecuritySummaryResponseBodyClusterHostEventBaselineEvent()
                self.baseline_event.append(temp_model.from_map(k1))

        self.vul_event = []
        if m.get('VulEvent') is not None:
            for k1 in m.get('VulEvent'):
                temp_model = main_models.DescribeClusterHostSecuritySummaryResponseBodyClusterHostEventVulEvent()
                self.vul_event.append(temp_model.from_map(k1))

        return self

class DescribeClusterHostSecuritySummaryResponseBodyClusterHostEventVulEvent(DaraModel):
    def __init__(
        self,
        count: int = None,
        risk_level: str = None,
    ):
        # The number of vulnerabilities.
        self.count = count
        # The risk level of the vulnerability. Valid values:
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

class DescribeClusterHostSecuritySummaryResponseBodyClusterHostEventBaselineEvent(DaraModel):
    def __init__(
        self,
        count: int = None,
        risk_level: str = None,
    ):
        # The number of baselines.
        self.count = count
        # The risk level of the baseline. Valid values:
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

class DescribeClusterHostSecuritySummaryResponseBodyClusterHostEventAlarmEvent(DaraModel):
    def __init__(
        self,
        count: int = None,
        risk_level: str = None,
    ):
        # The number of alerts.
        self.count = count
        # The alert level. Valid values:
        # 
        # *   **serious**
        # *   **suspicious**
        # *   **remind**
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

