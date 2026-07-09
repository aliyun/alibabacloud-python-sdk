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
        composite_escalation: main_models.CloudMonitoringCompositeEscalation = None,
        count_operator: str = None,
        count_threshold: int = None,
        duration_secs: int = None,
        enable_severity_suppression: bool = None,
        escalation_type: str = None,
        express_escalation: main_models.CloudMonitoringExpressEscalation = None,
        legacy_raw: str = None,
        legacy_type: str = None,
        match_field: str = None,
        match_operator: str = None,
        match_value: str = None,
        max: float = None,
        min: float = None,
        no_data_policy: str = None,
        operator: str = None,
        prometheus: main_models.CloudMonitoringPrometheusEscalation = None,
        relation: str = None,
        severity: str = None,
        simple_escalation: main_models.CloudMonitoringSimpleEscalation = None,
        threshold: float = None,
        threshold_list: List[main_models.ApmThresholdConfig] = None,
        triggers: List[main_models.MetricSetMultiTrigger] = None,
        type: str = None,
        yoy_time_unit: str = None,
        yoy_time_value: int = None,
    ):
        self.aggregate = aggregate
        self.compare_list = compare_list
        self.composite_escalation = composite_escalation
        self.count_operator = count_operator
        self.count_threshold = count_threshold
        self.duration_secs = duration_secs
        self.enable_severity_suppression = enable_severity_suppression
        self.escalation_type = escalation_type
        self.express_escalation = express_escalation
        self.legacy_raw = legacy_raw
        self.legacy_type = legacy_type
        self.match_field = match_field
        self.match_operator = match_operator
        self.match_value = match_value
        self.max = max
        self.min = min
        self.no_data_policy = no_data_policy
        self.operator = operator
        self.prometheus = prometheus
        self.relation = relation
        self.severity = severity
        self.simple_escalation = simple_escalation
        self.threshold = threshold
        self.threshold_list = threshold_list
        self.triggers = triggers
        # This parameter is required.
        self.type = type
        self.yoy_time_unit = yoy_time_unit
        self.yoy_time_value = yoy_time_value

    def validate(self):
        if self.compare_list:
            for v1 in self.compare_list:
                 if v1:
                    v1.validate()
        if self.composite_escalation:
            self.composite_escalation.validate()
        if self.express_escalation:
            self.express_escalation.validate()
        if self.prometheus:
            self.prometheus.validate()
        if self.simple_escalation:
            self.simple_escalation.validate()
        if self.threshold_list:
            for v1 in self.threshold_list:
                 if v1:
                    v1.validate()
        if self.triggers:
            for v1 in self.triggers:
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

        if self.composite_escalation is not None:
            result['compositeEscalation'] = self.composite_escalation.to_map()

        if self.count_operator is not None:
            result['countOperator'] = self.count_operator

        if self.count_threshold is not None:
            result['countThreshold'] = self.count_threshold

        if self.duration_secs is not None:
            result['durationSecs'] = self.duration_secs

        if self.enable_severity_suppression is not None:
            result['enableSeveritySuppression'] = self.enable_severity_suppression

        if self.escalation_type is not None:
            result['escalationType'] = self.escalation_type

        if self.express_escalation is not None:
            result['expressEscalation'] = self.express_escalation.to_map()

        if self.legacy_raw is not None:
            result['legacyRaw'] = self.legacy_raw

        if self.legacy_type is not None:
            result['legacyType'] = self.legacy_type

        if self.match_field is not None:
            result['matchField'] = self.match_field

        if self.match_operator is not None:
            result['matchOperator'] = self.match_operator

        if self.match_value is not None:
            result['matchValue'] = self.match_value

        if self.max is not None:
            result['max'] = self.max

        if self.min is not None:
            result['min'] = self.min

        if self.no_data_policy is not None:
            result['noDataPolicy'] = self.no_data_policy

        if self.operator is not None:
            result['operator'] = self.operator

        if self.prometheus is not None:
            result['prometheus'] = self.prometheus.to_map()

        if self.relation is not None:
            result['relation'] = self.relation

        if self.severity is not None:
            result['severity'] = self.severity

        if self.simple_escalation is not None:
            result['simpleEscalation'] = self.simple_escalation.to_map()

        if self.threshold is not None:
            result['threshold'] = self.threshold

        result['thresholdList'] = []
        if self.threshold_list is not None:
            for k1 in self.threshold_list:
                result['thresholdList'].append(k1.to_map() if k1 else None)

        result['triggers'] = []
        if self.triggers is not None:
            for k1 in self.triggers:
                result['triggers'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        if self.yoy_time_unit is not None:
            result['yoyTimeUnit'] = self.yoy_time_unit

        if self.yoy_time_value is not None:
            result['yoyTimeValue'] = self.yoy_time_value

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

        if m.get('compositeEscalation') is not None:
            temp_model = main_models.CloudMonitoringCompositeEscalation()
            self.composite_escalation = temp_model.from_map(m.get('compositeEscalation'))

        if m.get('countOperator') is not None:
            self.count_operator = m.get('countOperator')

        if m.get('countThreshold') is not None:
            self.count_threshold = m.get('countThreshold')

        if m.get('durationSecs') is not None:
            self.duration_secs = m.get('durationSecs')

        if m.get('enableSeveritySuppression') is not None:
            self.enable_severity_suppression = m.get('enableSeveritySuppression')

        if m.get('escalationType') is not None:
            self.escalation_type = m.get('escalationType')

        if m.get('expressEscalation') is not None:
            temp_model = main_models.CloudMonitoringExpressEscalation()
            self.express_escalation = temp_model.from_map(m.get('expressEscalation'))

        if m.get('legacyRaw') is not None:
            self.legacy_raw = m.get('legacyRaw')

        if m.get('legacyType') is not None:
            self.legacy_type = m.get('legacyType')

        if m.get('matchField') is not None:
            self.match_field = m.get('matchField')

        if m.get('matchOperator') is not None:
            self.match_operator = m.get('matchOperator')

        if m.get('matchValue') is not None:
            self.match_value = m.get('matchValue')

        if m.get('max') is not None:
            self.max = m.get('max')

        if m.get('min') is not None:
            self.min = m.get('min')

        if m.get('noDataPolicy') is not None:
            self.no_data_policy = m.get('noDataPolicy')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('prometheus') is not None:
            temp_model = main_models.CloudMonitoringPrometheusEscalation()
            self.prometheus = temp_model.from_map(m.get('prometheus'))

        if m.get('relation') is not None:
            self.relation = m.get('relation')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('simpleEscalation') is not None:
            temp_model = main_models.CloudMonitoringSimpleEscalation()
            self.simple_escalation = temp_model.from_map(m.get('simpleEscalation'))

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        self.threshold_list = []
        if m.get('thresholdList') is not None:
            for k1 in m.get('thresholdList'):
                temp_model = main_models.ApmThresholdConfig()
                self.threshold_list.append(temp_model.from_map(k1))

        self.triggers = []
        if m.get('triggers') is not None:
            for k1 in m.get('triggers'):
                temp_model = main_models.MetricSetMultiTrigger()
                self.triggers.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('yoyTimeUnit') is not None:
            self.yoy_time_unit = m.get('yoyTimeUnit')

        if m.get('yoyTimeValue') is not None:
            self.yoy_time_value = m.get('yoyTimeValue')

        return self

