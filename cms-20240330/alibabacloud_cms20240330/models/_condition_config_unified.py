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
        # The minimum deviation or absolute deviation dead zone for dynamic baselines. This parameter takes effect only for baseline operators in UMODEL_METRICSET_CONDITION and APM_SIMPLE_CONDITION. If the absolute difference between the current value and the boundary is less than the absDeviation value, no alert is triggered. The unit is the same as the metric unit. The value must be greater than or equal to 0. A value of 0 indicates no limit.
        self.abs_deviation = abs_deviation
        # The aggregation function used for APM_SIMPLE_CONDITION. For UModel conditions, this semantic has been migrated to QueryConfigUnified, and this field no longer takes effect.
        self.aggregate = aggregate
        # The consecutive trigger count threshold for SLS_MULTI_CONDITION. An alert is triggered only after the condition is met for the specified number of consecutive times. Default value: 1.
        self.alert_count = alert_count
        # The baseline period. This parameter takes effect only for baseline operators. Valid values: AUTO (automatic identification), DAILY (daily), WEEKLY (weekly), and NONE (no period). For weekly baselines, the backend automatically extends the historical training window to 14 days or more. Automatic identification cannot echo specific identification conclusions.
        self.baseline_period = baseline_period
        # The list of multiple comparisons for APM_COMPOSITE_CONDITION.
        self.compare_list = compare_list
        # The multi-metric composite trigger configuration for CLOUD_MONITORING_CONDITION when escalationType is set to COMPOSITE. The relation, severity, times, and escalations parameters are required.
        self.composite_escalation = composite_escalation
        # The count comparison operator for UMODEL_LOGSET_CONDITION.
        self.count_operator = count_operator
        # The count threshold for UMODEL_LOGSET_CONDITION.
        self.count_threshold = count_threshold
        # The duration in seconds. This parameter is directly used for PROMETHEUS_SIMPLE, UMODEL_METRICSET_CONDITION, and UMODEL_LOGSET_CONDITION. For UMODEL_METRICSET_MULTI_CONDITION, it serves as the global default value, and each trigger can override it with its own durationSecs value.
        self.duration_secs = duration_secs
        # Specifies whether to enable severity suppression for UMODEL_METRICSET_MULTI_CONDITION and PROMETHEUS_MULTI_CONDITION. Default value: true. When enabled, only the highest severity trigger is reported for the same entity.
        self.enable_severity_suppression = enable_severity_suppression
        # The expression type for CLOUD_MONITORING_CONDITION. Valid values: SIMPLE, COMPOSITE, EXPRESS, and PROMETHEUS. The write path only supports SIMPLE and COMPOSITE. Specify the corresponding escalation sub-object based on the type.
        self.escalation_type = escalation_type
        # The expression trigger configuration for CLOUD_MONITORING_CONDITION when escalationType is set to EXPRESS. This parameter is output only in the read path.
        self.express_escalation = express_escalation
        # The original V1 condition JSON string returned as a fallback when parsing fails in the read path and the type is UNKNOWN_CONDITION. The frontend displays this field as read-only when it is not empty.
        self.legacy_raw = legacy_raw
        # The legacy type returned when the type is UNKNOWN_CONDITION. This indicates that the rule cannot be edited by using the new API. Submit a ticket to contact the CloudMonitor product team.
        self.legacy_type = legacy_type
        # The log field name used for UMODEL_LOGSET_CONDITION when matchOperator is set to CONTAINS, EQUALS, or REGEX.
        self.match_field = match_field
        # The log match operator for UMODEL_LOGSET_CONDITION.
        self.match_operator = match_operator
        # The log match value used for UMODEL_LOGSET_CONDITION when matchOperator is set to CONTAINS, EQUALS, or REGEX.
        self.match_value = match_value
        # The upper bound of the range used for UMODEL_METRICSET_CONDITION when operator is set to IN_RANGE or OUT_OF_RANGE.
        self.max = max
        # The lower bound of the range used for UMODEL_METRICSET_CONDITION when operator is set to IN_RANGE or OUT_OF_RANGE.
        self.min = min
        # The no-data alert level for SLS_MULTI_CONDITION. For APM and Prometheus conditions, this parameter has been migrated to noDataPolicy and noDataAlertSeverity.
        self.no_data_alert_level = no_data_alert_level
        # The no-data alert severity. This parameter takes effect for PROMETHEUS_SIMPLE_CONDITION, PROMETHEUS_MULTI_CONDITION, UMODEL_METRICSET_CONDITION, and UMODEL_METRICSET_MULTI_CONDITION when noDataPolicy is set to NO_DATA_TO_ALERT. For UMODEL_METRICSET conditions, this field is required when noDataPolicy is set to NO_DATA_TO_ALERT, and must not be specified for other policies. SLS_MULTI_CONDITION still uses noDataAlertLevel.
        self.no_data_alert_severity = no_data_alert_severity
        # The compensated value when no data is available for APM_SIMPLE_CONDITION and APM_COMPOSITE_CONDITION. This parameter is nullable.
        self.no_data_append_value = no_data_append_value
        # The tolerance duration in seconds before no data is determined. This parameter takes effect for UMODEL_METRICSET_CONDITION and UMODEL_METRICSET_MULTI_CONDITION when noDataPolicy is not empty. The noDataPolicy is applied only after no data is continuously reported for longer than this duration. This prevents empty query results in a single cycle caused by UModel data write jitter. The value must be a positive integer. If not specified, the backend uses the fallback value of max(collection interval × 2, 300).
        self.no_data_duration_secs = no_data_duration_secs
        # The no-data processing policy for CLOUD_MONITORING_CONDITION, PROMETHEUS_MULTI_CONDITION, PROMETHEUS_SIMPLE_CONDITION, APM_SIMPLE_CONDITION, APM_COMPOSITE_CONDITION, UMODEL_METRICSET_CONDITION, and UMODEL_METRICSET_MULTI_CONDITION. Valid values: NO_DATA_TO_OK (treats no data as normal and recovers existing alerts), NO_DATA_TO_ALERT (triggers an alert for no data), KEEP_LAST_STATE (maintains the last state before no data), and APPEND_VALUE (APM only). If not specified, no-data determination is disabled, and the behavior remains the same as before this feature was released. UMODEL_METRICSET_CONDITION and UMODEL_METRICSET_MULTI_CONDITION do not support APPEND_VALUE because their data sources do not support backfilling.
        self.no_data_policy = no_data_policy
        # The comparison operator. For UMODEL_METRICSET_CONDITION, valid values are GT (greater than), GE (greater than or equal to), LT (less than), LE (less than or equal to), EQ (equal to), NE (not equal to), IN_RANGE (within the range, requires min and max), OUT_OF_RANGE (outside the range, requires min and max), PRESENT (field exists), NOT_PRESENT (field does not exist), ABOVE_UPPER (dynamic baseline spike), BELOW_LOWER (dynamic baseline drop), and OUT_OF_BAND (bidirectional dynamic baseline, requires sensitivity, do not specify threshold, min, or max). This field is not used for UMODEL_LOGSET_CONDITION. For APM_SIMPLE_CONDITION, valid values are GT, GTE, LT, LTE, EQ, NE, YOY_UP, YOY_DOWN (YOY operators require yoyTimeUnit and yoyTimeValue), ABOVE_UPPER, BELOW_LOWER, and OUT_OF_BAND (dynamic baseline, requires sensitivity).
        self.operator = operator
        # The PromQL trigger configuration for CLOUD_MONITORING_CONDITION when escalationType is set to PROMETHEUS. This parameter is output only in the read path.
        self.prometheus = prometheus
        # The logical relation between conditions for APM_COMPOSITE_CONDITION.
        self.relation = relation
        # The dynamic baseline sensitivity for UMODEL_METRICSET_CONDITION and APM_SIMPLE_CONDITION. This parameter takes effect only when operator is set to ABOVE_UPPER, BELOW_LOWER, or OUT_OF_BAND. Valid values: HIGH (narrowest band and most sensitive), MEDIUM, and LOW (widest band and least sensitive).
        self.sensitivity = sensitivity
        # The severity level for UMODEL_METRICSET_CONDITION, UMODEL_LOGSET_CONDITION, PROMETHEUS_SIMPLE, and APM_COMPOSITE.
        self.severity = severity
        # The single-metric multi-level trigger configuration for CLOUD_MONITORING_CONDITION when escalationType is set to SIMPLE. The metricName, period, and escalations parameters are required.
        self.simple_escalation = simple_escalation
        # The threshold used for UMODEL_METRICSET_CONDITION when a non-range operator is specified.
        self.threshold = threshold
        # The list of multiple thresholds for APM_SIMPLE_CONDITION.
        self.threshold_list = threshold_list
        # The list of triggers. This field is polymorphic based on the type. CLOUD_MONITORING_CONDITION does not use this field; use simpleEscalation.escalations or compositeEscalation.escalations instead. For SLS_MULTI_CONDITION, each case includes matchField, matchOperator, matchValue, countOperator, countThreshold, and severity, and at least one case is required. For UMODEL_METRICSET_MULTI_CONDITION, each trigger includes severity, durationSecs, and an expression (SIMPLE or COMPOSITE). For PROMETHEUS_MULTI_CONDITION, each trigger includes severity, durationSecs, and an expression (SIMPLE or COMPOSITE). Triggers are sorted by severity priority, and the first matched trigger is executed.
        self.triggers = triggers
        # The detection condition type. Valid values and required fields: PROMETHEUS_SIMPLE_CONDITION (requires operator, threshold, durationSecs, and severity), UMODEL_METRICSET_CONDITION (requires operator, durationSecs, and severity; requires threshold for non-range operators; requires min and max when operator is IN_RANGE or OUT_OF_RANGE; noDataPolicy and noDataDurationSecs are optional, but noDataAlertSeverity is required when noDataPolicy is NO_DATA_TO_ALERT), UMODEL_LOGSET_CONDITION (requires matchOperator, durationSecs, and severity; requires matchField and matchValue when matchOperator is CONTAINS, EQUALS, or REGEX; countOperator and countThreshold are optional), UMODEL_METRICSET_MULTI_CONDITION (requires triggers; durationSecs as global default and enableSeveritySuppression are optional; noDataPolicy and noDataDurationSecs are optional, but noDataAlertSeverity is required when noDataPolicy is NO_DATA_TO_ALERT), APM_SIMPLE_CONDITION (requires operator and aggregate; requires thresholdList or threshold; requires yoyTimeUnit and yoyTimeValue when operator is YOY_UP or YOY_DOWN; noDataPolicy and noDataAppendValue are optional), APM_COMPOSITE_CONDITION (requires compareList, relation, and severity; noDataPolicy and noDataAppendValue are optional), CLOUD_MONITORING_CONDITION (requires escalationType; requires simpleEscalation when escalationType is SIMPLE; requires compositeEscalation when escalationType is COMPOSITE; noDataPolicy is optional), and UNKNOWN_CONDITION (read-only fallback, do not use in the write path). Non-enum values such as SLS_CONDITION or CMS_BASIC_CONDITION are prohibited. The backend returns an Invalidtype 400 error for invalid values.
        # 
        # This parameter is required.
        self.type = type
        # The year-over-year time unit for APM_SIMPLE_CONDITION. This parameter takes effect only when operator is set to YOY_UP or YOY_DOWN.
        self.yoy_time_unit = yoy_time_unit
        # The year-over-year time value for APM_SIMPLE_CONDITION. This parameter takes effect only when operator is set to YOY_UP or YOY_DOWN.
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

