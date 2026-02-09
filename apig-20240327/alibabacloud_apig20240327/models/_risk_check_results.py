# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class RiskCheckResults(DaraModel):
    def __init__(
        self,
        check_time: int = None,
        gateway_id: str = None,
        metadata: main_models.RiskCheckResultsMetadata = None,
        risk_details: List[main_models.RiskCheckResultsRiskDetails] = None,
        risk_level: str = None,
        score: int = None,
        snapshot_time: int = None,
        status: str = None,
        total_risk: int = None,
    ):
        # The check time
        self.check_time = check_time
        # The gateway ID
        self.gateway_id = gateway_id
        # The instance metadata
        self.metadata = metadata
        # The risk details list
        self.risk_details = risk_details
        # The risk level
        self.risk_level = risk_level
        # The risk score
        self.score = score
        # The snapshot time
        self.snapshot_time = snapshot_time
        # The execution status
        self.status = status
        # The total number of risks
        self.total_risk = total_risk

    def validate(self):
        if self.metadata:
            self.metadata.validate()
        if self.risk_details:
            for v1 in self.risk_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_time is not None:
            result['checkTime'] = self.check_time

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        result['riskDetails'] = []
        if self.risk_details is not None:
            for k1 in self.risk_details:
                result['riskDetails'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level

        if self.score is not None:
            result['score'] = self.score

        if self.snapshot_time is not None:
            result['snapshotTime'] = self.snapshot_time

        if self.status is not None:
            result['status'] = self.status

        if self.total_risk is not None:
            result['totalRisk'] = self.total_risk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkTime') is not None:
            self.check_time = m.get('checkTime')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('metadata') is not None:
            temp_model = main_models.RiskCheckResultsMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        self.risk_details = []
        if m.get('riskDetails') is not None:
            for k1 in m.get('riskDetails'):
                temp_model = main_models.RiskCheckResultsRiskDetails()
                self.risk_details.append(temp_model.from_map(k1))

        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('snapshotTime') is not None:
            self.snapshot_time = m.get('snapshotTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('totalRisk') is not None:
            self.total_risk = m.get('totalRisk')

        return self

class RiskCheckResultsRiskDetails(DaraModel):
    def __init__(
        self,
        check_module: str = None,
        data: Dict[str, str] = None,
        description: str = None,
        is_notice_mute: bool = None,
        risk_code: str = None,
        risk_level: str = None,
        risk_name: str = None,
        risk_type: str = None,
        situation: str = None,
        suggestion: str = None,
    ):
        # The check module
        self.check_module = check_module
        # The risk detailed data
        self.data = data
        # The risk description
        self.description = description
        # Whether to mute notifications
        self.is_notice_mute = is_notice_mute
        # The risk code
        self.risk_code = risk_code
        # The risk level
        self.risk_level = risk_level
        # The risk title
        self.risk_name = risk_name
        # The risk type
        self.risk_type = risk_type
        # The risk situation
        self.situation = situation
        # The fix suggestion
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_module is not None:
            result['checkModule'] = self.check_module

        if self.data is not None:
            result['data'] = self.data

        if self.description is not None:
            result['description'] = self.description

        if self.is_notice_mute is not None:
            result['isNoticeMute'] = self.is_notice_mute

        if self.risk_code is not None:
            result['riskCode'] = self.risk_code

        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level

        if self.risk_name is not None:
            result['riskName'] = self.risk_name

        if self.risk_type is not None:
            result['riskType'] = self.risk_type

        if self.situation is not None:
            result['situation'] = self.situation

        if self.suggestion is not None:
            result['suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkModule') is not None:
            self.check_module = m.get('checkModule')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('isNoticeMute') is not None:
            self.is_notice_mute = m.get('isNoticeMute')

        if m.get('riskCode') is not None:
            self.risk_code = m.get('riskCode')

        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')

        if m.get('riskName') is not None:
            self.risk_name = m.get('riskName')

        if m.get('riskType') is not None:
            self.risk_type = m.get('riskType')

        if m.get('situation') is not None:
            self.situation = m.get('situation')

        if m.get('suggestion') is not None:
            self.suggestion = m.get('suggestion')

        return self

class RiskCheckResultsMetadata(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        replica: int = None,
        spec: str = None,
        version: str = None,
    ):
        # The cluster type
        self.cluster_type = cluster_type
        # The replica count
        self.replica = replica
        # The specification
        self.spec = spec
        # The version
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type

        if self.replica is not None:
            result['replica'] = self.replica

        if self.spec is not None:
            result['spec'] = self.spec

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')

        if m.get('replica') is not None:
            self.replica = m.get('replica')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

