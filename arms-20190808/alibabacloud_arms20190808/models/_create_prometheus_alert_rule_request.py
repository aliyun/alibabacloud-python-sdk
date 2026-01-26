# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreatePrometheusAlertRuleRequest(DaraModel):
    def __init__(
        self,
        alert_name: str = None,
        annotations: str = None,
        cluster_id: str = None,
        dispatch_rule_id: int = None,
        duration: str = None,
        expression: str = None,
        labels: str = None,
        message: str = None,
        notify_type: str = None,
        region_id: str = None,
        tags: List[main_models.CreatePrometheusAlertRuleRequestTags] = None,
        type: str = None,
    ):
        # The name of the alert rule.
        # 
        # This parameter is required.
        self.alert_name = alert_name
        # The annotations that are described in a JSON string. You must specify the name and value of each annotation.
        self.annotations = annotations
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the notification policy. This parameter is required if the NotifyType parameter is set to `DISPATCH_RULE`.
        self.dispatch_rule_id = dispatch_rule_id
        # The duration. The value ranges from 1 to 1440 minutes.
        # 
        # This parameter is required.
        self.duration = duration
        # The expression of the alert rule. The expression must follow the PromQL syntax.
        # 
        # This parameter is required.
        self.expression = expression
        # The tags that are described in a JSON string. You must specify the name and value of each tag.
        self.labels = labels
        # The content of the alert notification. Tags can be referenced in the {{$labels.xxx}} format.
        # 
        # This parameter is required.
        self.message = message
        # The method that is used to send alert notifications. Valid values:
        # 
        # - `ALERT_MANAGER`: Alert notifications are sent by Operation Center. This is the default value.
        # - `DISPATCH_RULE`: Alert notifications are sent based on the specified notification policy.
        self.notify_type = notify_type
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The tags.
        self.tags = tags
        # The type of the alert rule. Valid values:
        # 
        # - 99: custom alert
        # - 101: Prometheus Service alert
        self.type = type

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.annotations is not None:
            result['Annotations'] = self.annotations

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.message is not None:
            result['Message'] = self.message

        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreatePrometheusAlertRuleRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreatePrometheusAlertRuleRequestTags(DaraModel):
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

