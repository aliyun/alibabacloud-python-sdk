# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class AlertEvent(DaraModel):
    def __init__(
        self,
        alert_name: str = None,
        alert_status: str = None,
        arn: str = None,
        content: str = None,
        custom_labels: Dict[str, Any] = None,
        de_dup_id: str = None,
        details: str = None,
        event_name: str = None,
        event_type: str = None,
        expression: str = None,
        metrics: List[main_models.AlertEventMetrics] = None,
        product: str = None,
        resource_info: Dict[str, Any] = None,
        rule_name: str = None,
        severity: str = None,
        source: str = None,
        summary: str = None,
        timestamp: int = None,
        trace_id: str = None,
        user_id: str = None,
    ):
        self.alert_name = alert_name
        self.alert_status = alert_status
        self.arn = arn
        self.content = content
        self.custom_labels = custom_labels
        self.de_dup_id = de_dup_id
        self.details = details
        self.event_name = event_name
        self.event_type = event_type
        self.expression = expression
        self.metrics = metrics
        self.product = product
        self.resource_info = resource_info
        self.rule_name = rule_name
        self.severity = severity
        self.source = source
        self.summary = summary
        self.timestamp = timestamp
        self.trace_id = trace_id
        self.user_id = user_id

    def validate(self):
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status

        if self.arn is not None:
            result['Arn'] = self.arn

        if self.content is not None:
            result['Content'] = self.content

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        if self.de_dup_id is not None:
            result['DeDupId'] = self.de_dup_id

        if self.details is not None:
            result['Details'] = self.details

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.expression is not None:
            result['Expression'] = self.expression

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.product is not None:
            result['Product'] = self.product

        if self.resource_info is not None:
            result['ResourceInfo'] = self.resource_info

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.source is not None:
            result['Source'] = self.source

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')

        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('DeDupId') is not None:
            self.de_dup_id = m.get('DeDupId')

        if m.get('Details') is not None:
            self.details = m.get('Details')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.AlertEventMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('ResourceInfo') is not None:
            self.resource_info = m.get('ResourceInfo')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self



class AlertEventMetrics(DaraModel):
    def __init__(
        self,
        cur_value: str = None,
        metric_name: str = None,
        metric_name_en: str = None,
        metric_name_zh: str = None,
        operator: str = None,
        statistics: str = None,
        threshold: str = None,
        unit: str = None,
        unit_factor: float = None,
    ):
        self.cur_value = cur_value
        self.metric_name = metric_name
        self.metric_name_en = metric_name_en
        self.metric_name_zh = metric_name_zh
        self.operator = operator
        self.statistics = statistics
        self.threshold = threshold
        self.unit = unit
        self.unit_factor = unit_factor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cur_value is not None:
            result['CurValue'] = self.cur_value

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_name_en is not None:
            result['MetricNameEn'] = self.metric_name_en

        if self.metric_name_zh is not None:
            result['MetricNameZh'] = self.metric_name_zh

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.unit_factor is not None:
            result['UnitFactor'] = self.unit_factor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurValue') is not None:
            self.cur_value = m.get('CurValue')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricNameEn') is not None:
            self.metric_name_en = m.get('MetricNameEn')

        if m.get('MetricNameZh') is not None:
            self.metric_name_zh = m.get('MetricNameZh')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('UnitFactor') is not None:
            self.unit_factor = m.get('UnitFactor')

        return self

