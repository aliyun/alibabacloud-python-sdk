# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ConditionConfigUnified(DaraModel):
    def __init__(
        self,
        abs_deviation: float = None,
        aggregate: str = None,
        alert_count: int = None,
        baseline_period: str = None,
        compare_list: List[main_models.CompareList] = None,
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
        no_data_alert_level: str = None,
        no_data_alert_severity: str = None,
        no_data_append_value: float = None,
        no_data_duration_secs: int = None,
        no_data_policy: str = None,
        operator: str = None,
        prometheus: main_models.CloudMonitoringPrometheusEscalation = None,
        relation: str = None,
        sensitivity: str = None,
        severity: str = None,
        simple_escalation: main_models.CloudMonitoringSimpleEscalation = None,
        threshold: float = None,
        threshold_list: List[main_models.ThresholdList] = None,
        triggers: List[main_models.Triggers] = None,
        type: str = None,
        yoy_time_unit: str = None,
        yoy_time_value: int = None,
    ):
        # The minimum dynamic baseline deviation or absolute deviation dead zone (effective only for baseline operators in UMODEL_METRICSET_CONDITION and APM_SIMPLE_CONDITION). No alert is triggered if |current value - boundary| < absDeviation. The unit is the same as the metric. The value must be greater than or equal to 0. A value of 0 indicates no limit.
        self.abs_deviation = abs_deviation
        # The aggregation function (APM_SIMPLE_CONDITION).
        self.aggregate = aggregate
        # The consecutive trigger count threshold (type=SLS_MULTI_CONDITION). An alert is triggered only after the condition is met N times. Default value: 1.
        self.alert_count = alert_count
        # The baseline period (effective only for baseline operators). Valid values: AUTO for automatic identification, DAILY for daily, WEEKLY for weekly, and NONE for no period. For weekly periods, the backend automatically expands the historical training window to 14 days or more. Automatic identification cannot return specific identification results.
        self.baseline_period = baseline_period
        # The multiple comparisons (APM_COMPOSITE_CONDITION).
        self.compare_list = compare_list
        # The multi-metric composite trigger configuration for CLOUD_MONITORING_CONDITION when escalationType is set to COMPOSITE. The relation, severity, times, and escalations parameters are required.
        self.composite_escalation = composite_escalation
        # The count comparison operator (type=UMODEL_LOGSET_CONDITION).
        self.count_operator = count_operator
        # The count threshold (type=UMODEL_LOGSET_CONDITION).
        self.count_threshold = count_threshold
        # The duration in seconds. This parameter is used by PROMETHEUS_SIMPLE and UMODEL_METRICSET.
        self.duration_secs = duration_secs
        # Specifies whether to enable severity-based suppression (type=UMODEL_METRICSET_MULTI_CONDITION / PROMETHEUS_MULTI_CONDITION). Default value: true. When enabled, only the highest severity trigger is reported for the same entity.
        self.enable_severity_suppression = enable_severity_suppression
        # The expression type for CLOUD_MONITORING_CONDITION. Valid values: SIMPLE, COMPOSITE, EXPRESS, and PROMETHEUS. Only SIMPLE and COMPOSITE are supported in the write path. Specify the corresponding escalation sub-object based on the type.
        self.escalation_type = escalation_type
        # The expression trigger configuration for CLOUD_MONITORING_CONDITION when escalationType is set to EXPRESS. This parameter is output only in the read path.
        self.express_escalation = express_escalation
        # The original V1 condition JSON string returned when type is set to UNKNOWN_CONDITION and read path parsing fails as a fallback. The frontend displays this field as read-only when it is not empty.
        self.legacy_raw = legacy_raw
        # The value returned when type is set to UNKNOWN_CONDITION, which indicates that this rule cannot be edited by using the new API. Submit a ticket to contact the CloudMonitor product team.
        self.legacy_type = legacy_type
        # The log field name. This parameter is used when type is set to UMODEL_LOGSET_CONDITION and matchOperator is set to CONTAINS, EQUALS, or REGEX.
        self.match_field = match_field
        # The log matching operator (type=UMODEL_LOGSET_CONDITION).
        self.match_operator = match_operator
        # The log matching value. This parameter is used when type is set to UMODEL_LOGSET_CONDITION and matchOperator is set to CONTAINS, EQUALS, or REGEX.
        self.match_value = match_value
        # The upper bound of the range. This parameter is used for UMODEL_METRICSET_CONDITION when operator is set to IN_RANGE or OUT_OF_RANGE.
        self.max = max
        # The lower bound of the range. This parameter is used for UMODEL_METRICSET_CONDITION when operator is set to IN_RANGE or OUT_OF_RANGE.
        self.min = min
        # The no-data alert level (SLS_MULTI_CONDITION). APM and Prometheus conditions have been migrated to noDataPolicy and noDataAlertSeverity.
        self.no_data_alert_level = no_data_alert_level
        # The no-data alert severity. This parameter takes effect for PROMETHEUS_SIMPLE_CONDITION and PROMETHEUS_MULTI_CONDITION when noDataPolicy is set to NO_DATA_TO_ALERT. SLS_MULTI_CONDITION still uses noDataAlertLevel.
        self.no_data_alert_severity = no_data_alert_severity
        # The compensated value when no data is available (APM_SIMPLE_CONDITION / APM_COMPOSITE_CONDITION). This parameter is nullable.
        self.no_data_append_value = no_data_append_value
        # The tolerance duration in seconds before determining that no data is available. This parameter applies to UMODEL_METRICSET_CONDITION and UMODEL_METRICSET_MULTI_CONDITION, and takes effect when noDataPolicy is not empty. The no-data policy is applied only after the continuous no-data period exceeds this duration. This is used to offset single-cycle empty queries caused by UModel data write jitter. The value must be a positive integer. If not specified, the backend defaults to the maximum of twice the collection interval and 300.
        self.no_data_duration_secs = no_data_duration_secs
        # The no-data processing policy (CLOUD_MONITORING_CONDITION / PROMETHEUS_MULTI_CONDITION / PROMETHEUS_SIMPLE_CONDITION / APM_SIMPLE_CONDITION / APM_COMPOSITE_CONDITION). Valid values: NO_DATA_TO_OK, NO_DATA_TO_ALERT, KEEP_LAST_STATE, and APPEND_VALUE (APM only).
        self.no_data_policy = no_data_policy
        # The comparison operator (UMODEL_METRICSET_CONDITION or APM_SIMPLE_CONDITION).
        self.operator = operator
        # The PromQL trigger configuration for CLOUD_MONITORING_CONDITION when escalationType is set to PROMETHEUS. This parameter is output only in the read path.
        self.prometheus = prometheus
        # The logical relation between conditions (APM_COMPOSITE_CONDITION).
        self.relation = relation
        # The dynamic baseline sensitivity (UMODEL_METRICSET_CONDITION / APM_SIMPLE_CONDITION). This parameter takes effect only when operator is set to ABOVE_UPPER, BELOW_LOWER, or OUT_OF_BAND. Valid values: HIGH for the narrowest and most sensitive band, MEDIUM, and LOW for the widest and least sensitive band.
        self.sensitivity = sensitivity
        # The severity level (UMODEL / PROMETHEUS_SIMPLE / APM_COMPOSITE).
        self.severity = severity
        # The single-metric multi-level trigger configuration for CLOUD_MONITORING_CONDITION when escalationType is set to SIMPLE. The metricName, period, and escalations parameters are required.
        self.simple_escalation = simple_escalation
        # The threshold (UMODEL_METRICSET_CONDITION).
        self.threshold = threshold
        # The multi-threshold list (APM_SIMPLE_CONDITION).
        self.threshold_list = threshold_list
        # The trigger list. This parameter is polymorphic by type. CLOUD_MONITORING_CONDITION does not use this field; use simpleEscalation.escalations or compositeEscalation.escalations instead. For SLS_MULTI_CONDITION, each case includes matchField, matchOperator, matchValue, countOperator, countThreshold, and severity, and at least one case is required. For UMODEL_METRICSET_MULTI_CONDITION, each trigger includes severity, durationSecs, and an expression (SIMPLE or COMPOSITE). For PROMETHEUS_MULTI_CONDITION, each trigger includes severity, durationSecs, and an expression (SIMPLE or COMPOSITE). The triggers are sorted by severity priority, and the first match triggers the alert.
        self.triggers = triggers
        # The detection condition type.
        # 
        # This parameter is required.
        self.type = type
        # The year-over-year time unit (APM_SIMPLE_CONDITION). This parameter takes effect only when operator is set to YOY_UP or YOY_DOWN.
        self.yoy_time_unit = yoy_time_unit
        # The year-over-year time value (APM_SIMPLE_CONDITION). This parameter takes effect only when operator is set to YOY_UP or YOY_DOWN.
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
        if self.abs_deviation is not None:
            result['absDeviation'] = self.abs_deviation

        if self.aggregate is not None:
            result['aggregate'] = self.aggregate

        if self.alert_count is not None:
            result['alertCount'] = self.alert_count

        if self.baseline_period is not None:
            result['baselinePeriod'] = self.baseline_period

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

        if self.no_data_alert_level is not None:
            result['noDataAlertLevel'] = self.no_data_alert_level

        if self.no_data_alert_severity is not None:
            result['noDataAlertSeverity'] = self.no_data_alert_severity

        if self.no_data_append_value is not None:
            result['noDataAppendValue'] = self.no_data_append_value

        if self.no_data_duration_secs is not None:
            result['noDataDurationSecs'] = self.no_data_duration_secs

        if self.no_data_policy is not None:
            result['noDataPolicy'] = self.no_data_policy

        if self.operator is not None:
            result['operator'] = self.operator

        if self.prometheus is not None:
            result['prometheus'] = self.prometheus.to_map()

        if self.relation is not None:
            result['relation'] = self.relation

        if self.sensitivity is not None:
            result['sensitivity'] = self.sensitivity

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
        if m.get('absDeviation') is not None:
            self.abs_deviation = m.get('absDeviation')

        if m.get('aggregate') is not None:
            self.aggregate = m.get('aggregate')

        if m.get('alertCount') is not None:
            self.alert_count = m.get('alertCount')

        if m.get('baselinePeriod') is not None:
            self.baseline_period = m.get('baselinePeriod')

        self.compare_list = []
        if m.get('compareList') is not None:
            for k1 in m.get('compareList'):
                temp_model = main_models.CompareList()
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

        if m.get('noDataAlertLevel') is not None:
            self.no_data_alert_level = m.get('noDataAlertLevel')

        if m.get('noDataAlertSeverity') is not None:
            self.no_data_alert_severity = m.get('noDataAlertSeverity')

        if m.get('noDataAppendValue') is not None:
            self.no_data_append_value = m.get('noDataAppendValue')

        if m.get('noDataDurationSecs') is not None:
            self.no_data_duration_secs = m.get('noDataDurationSecs')

        if m.get('noDataPolicy') is not None:
            self.no_data_policy = m.get('noDataPolicy')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('prometheus') is not None:
            temp_model = main_models.CloudMonitoringPrometheusEscalation()
            self.prometheus = temp_model.from_map(m.get('prometheus'))

        if m.get('relation') is not None:
            self.relation = m.get('relation')

        if m.get('sensitivity') is not None:
            self.sensitivity = m.get('sensitivity')

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
                temp_model = main_models.ThresholdList()
                self.threshold_list.append(temp_model.from_map(k1))

        self.triggers = []
        if m.get('triggers') is not None:
            for k1 in m.get('triggers'):
                temp_model = main_models.Triggers()
                self.triggers.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('yoyTimeUnit') is not None:
            self.yoy_time_unit = m.get('yoyTimeUnit')

        if m.get('yoyTimeValue') is not None:
            self.yoy_time_value = m.get('yoyTimeValue')

        return self

