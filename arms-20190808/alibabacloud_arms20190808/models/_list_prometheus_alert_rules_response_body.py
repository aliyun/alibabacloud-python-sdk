# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListPrometheusAlertRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        prometheus_alert_rules: List[main_models.ListPrometheusAlertRulesResponseBodyPrometheusAlertRules] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed.
        self.code = code
        # The returned message.
        self.message = message
        # The returned struct.
        self.prometheus_alert_rules = prometheus_alert_rules
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.prometheus_alert_rules:
            for v1 in self.prometheus_alert_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        result['PrometheusAlertRules'] = []
        if self.prometheus_alert_rules is not None:
            for k1 in self.prometheus_alert_rules:
                result['PrometheusAlertRules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.prometheus_alert_rules = []
        if m.get('PrometheusAlertRules') is not None:
            for k1 in m.get('PrometheusAlertRules'):
                temp_model = main_models.ListPrometheusAlertRulesResponseBodyPrometheusAlertRules()
                self.prometheus_alert_rules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListPrometheusAlertRulesResponseBodyPrometheusAlertRules(DaraModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_name: str = None,
        annotations: List[main_models.ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations] = None,
        cluster_id: str = None,
        dispatch_rule_id: int = None,
        duration: str = None,
        expression: str = None,
        labels: List[main_models.ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels] = None,
        message: str = None,
        notify_type: str = None,
        status: int = None,
        tags: List[main_models.ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesTags] = None,
        type: str = None,
    ):
        # The ID of the alert rule.
        self.alert_id = alert_id
        # The name of the alert rule.
        self.alert_name = alert_name
        # The annotations of the alert rule.
        self.annotations = annotations
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The ID of the notification policy. This parameter is returned if the NotifyType parameter is set to `DISPATCH_RULE`.
        self.dispatch_rule_id = dispatch_rule_id
        # The duration of the alert. Valid values: 1 to 1440. Unit: minutes.
        self.duration = duration
        # The expression of the alert rule.
        self.expression = expression
        # The tags of the alert rule.
        self.labels = labels
        # The alert message. Tags can be referenced in the {{$labels.xxx}} format.
        self.message = message
        # The method that is used to send alert notifications. Valid values:
        # 
        # - ALERT_MANAGER: Alert notifications are sent by Operation Center.
        # - DISPATCH_RULE: Alert notifications are
        self.notify_type = notify_type
        # Indicates whether the alert rule is enabled. Valid values:
        # 
        # - 1: The alert rule is enabled.
        # - 0: The alert rule is disabled.
        self.status = status
        # The tags.
        self.tags = tags
        # The type of the alert rule.
        self.type = type

    def validate(self):
        if self.annotations:
            for v1 in self.annotations:
                 if v1:
                    v1.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id

        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        result['Annotations'] = []
        if self.annotations is not None:
            for k1 in self.annotations:
                result['Annotations'].append(k1.to_map() if k1 else None)

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.expression is not None:
            result['Expression'] = self.expression

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')

        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        self.annotations = []
        if m.get('Annotations') is not None:
            for k1 in m.get('Annotations'):
                temp_model = main_models.ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations()
                self.annotations.append(temp_model.from_map(k1))

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the tag.
        self.name = name
        # The value of the tag associated with the instance.
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

class ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations(DaraModel):
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

