# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ConditionConfigUnified(DaraModel):
    def __init__(
        self,
        aggregate: str = None,
        compare_list: List[main_models.ApmCompositeCompareConfig] = None,
        duration_secs: int = None,
        operator: str = None,
        relation: str = None,
        severity: str = None,
        threshold: float = None,
        threshold_list: List[main_models.ApmThresholdConfig] = None,
        type: str = None,
    ):
        # 聚合函数（APM_SIMPLE_CONDITION）
        self.aggregate = aggregate
        # 多条比较（APM_COMPOSITE_CONDITION）
        self.compare_list = compare_list
        # 持续时间（秒），PROMETHEUS_SIMPLE / UMODEL_METRICSET 使用
        self.duration_secs = duration_secs
        # 比较操作符（UMODEL_METRICSET_CONDITION 或 APM_SIMPLE_CONDITION）
        self.operator = operator
        # 条件间逻辑关系（APM_COMPOSITE_CONDITION）
        self.relation = relation
        # 严重等级（UMODEL / PROMETHEUS_SIMPLE / APM_COMPOSITE）
        self.severity = severity
        # 阈值（UMODEL_METRICSET_CONDITION）
        self.threshold = threshold
        # 多阈值列表（APM_SIMPLE_CONDITION）
        self.threshold_list = threshold_list
        # 检测条件类型
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.compare_list:
            for v1 in self.compare_list:
                 if v1:
                    v1.validate()
        if self.threshold_list:
            for v1 in self.threshold_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregate is not None:
            result['aggregate'] = self.aggregate

        result['compareList'] = []
        if self.compare_list is not None:
            for k1 in self.compare_list:
                result['compareList'].append(k1.to_map() if k1 else None)

        if self.duration_secs is not None:
            result['durationSecs'] = self.duration_secs

        if self.operator is not None:
            result['operator'] = self.operator

        if self.relation is not None:
            result['relation'] = self.relation

        if self.severity is not None:
            result['severity'] = self.severity

        if self.threshold is not None:
            result['threshold'] = self.threshold

        result['thresholdList'] = []
        if self.threshold_list is not None:
            for k1 in self.threshold_list:
                result['thresholdList'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggregate') is not None:
            self.aggregate = m.get('aggregate')

        self.compare_list = []
        if m.get('compareList') is not None:
            for k1 in m.get('compareList'):
                temp_model = main_models.ApmCompositeCompareConfig()
                self.compare_list.append(temp_model.from_map(k1))

        if m.get('durationSecs') is not None:
            self.duration_secs = m.get('durationSecs')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('relation') is not None:
            self.relation = m.get('relation')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        self.threshold_list = []
        if m.get('thresholdList') is not None:
            for k1 in m.get('thresholdList'):
                temp_model = main_models.ApmThresholdConfig()
                self.threshold_list.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

