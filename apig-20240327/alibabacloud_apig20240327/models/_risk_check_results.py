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
        self.check_time = check_time
        # 网关实例的唯一标识符
        self.gateway_id = gateway_id
        # 实例的基本信息
        self.metadata = metadata
        # 详细的风险项信息列表
        self.risk_details = risk_details
        # 整体风险等级，可选值：LOW（低风险）、MEDIUM（中风险）、HIGH（高风险）、CRITICAL（严重风险）
        self.risk_level = risk_level
        # 风险综合评分，取值范围0-100分，分数越高表示风险越低
        self.score = score
        self.snapshot_time = snapshot_time
        # 风险检测状态，可选值：SUCCESS（成功）、FAIL（失败）、RUNNING（运行中）
        self.status = status
        # 检测到的风险项总数量
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
        # 执行检测的模块名称
        self.check_module = check_module
        # 风险相关的详细数据，不同风险类型数据结构不同
        self.data = data
        # 风险的详细描述，JSON字符串格式
        self.description = description
        # 该风险项的告警通知是否已被屏蔽
        self.is_notice_mute = is_notice_mute
        # 风险项的唯一标识码
        self.risk_code = risk_code
        # 该风险项的等级，可选值：LOW、MEDIUM、HIGH、CRITICAL
        self.risk_level = risk_level
        # 风险项的名称
        self.risk_name = risk_name
        # 风险分类，可选值：SYSTEM（系统风险）、VERSION（版本风险）、SAFE（安全风险）、CAPACITY（容量风险）
        self.risk_type = risk_type
        # 当前实例的风险现状，JSON字符串格式
        self.situation = situation
        # 针对该风险的优化建议，JSON字符串格式，包含描述和操作链接
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
        self.cluster_type = cluster_type
        self.replica = replica
        self.spec = spec
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

