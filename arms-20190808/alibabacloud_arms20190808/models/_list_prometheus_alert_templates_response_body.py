# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListPrometheusAlertTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        prometheus_alert_templates: List[main_models.ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates] = None,
        request_id: str = None,
    ):
        # The returned struct.
        self.prometheus_alert_templates = prometheus_alert_templates
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.prometheus_alert_templates:
            for v1 in self.prometheus_alert_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PrometheusAlertTemplates'] = []
        if self.prometheus_alert_templates is not None:
            for k1 in self.prometheus_alert_templates:
                result['PrometheusAlertTemplates'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prometheus_alert_templates = []
        if m.get('PrometheusAlertTemplates') is not None:
            for k1 in m.get('PrometheusAlertTemplates'):
                temp_model = main_models.ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates()
                self.prometheus_alert_templates.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates(DaraModel):
    def __init__(
        self,
        alert_name: str = None,
        annotations: List[main_models.ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations] = None,
        description: str = None,
        duration: str = None,
        expression: str = None,
        labels: List[main_models.ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels] = None,
        type: str = None,
        version: str = None,
    ):
        # The name of the alert rule.
        self.alert_name = alert_name
        # The annotations of the alert rule.
        self.annotations = annotations
        # The content of the alert notification. Tags can be referenced in the {{$labels.xxx}} format.
        self.description = description
        # The duration of the alert. Valid values: 1 to 1440. Unit: minutes.
        self.duration = duration
        # The expression of the alert rule.
        self.expression = expression
        # The tags of the alert rule.
        self.labels = labels
        # The type of the alert rule.
        self.type = type
        # The version of the alert rule.
        self.version = version

    def validate(self):
        if self.annotations:
            for v1 in self.annotations:
                 if v1:
                    v1.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        result['Annotations'] = []
        if self.annotations is not None:
            for k1 in self.annotations:
                result['Annotations'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.expression is not None:
            result['Expression'] = self.expression

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        self.annotations = []
        if m.get('Annotations') is not None:
            for k1 in m.get('Annotations'):
                temp_model = main_models.ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations()
                self.annotations.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the tag.
        self.name = name
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the annotation.
        self.name = name
        # The value of the annotation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

