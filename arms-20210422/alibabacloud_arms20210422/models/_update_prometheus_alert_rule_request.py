# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePrometheusAlertRuleRequest(DaraModel):
    def __init__(
        self,
        alert_id: int = None,
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
        type: str = None,
    ):
        # This parameter is required.
        self.alert_id = alert_id
        # This parameter is required.
        self.alert_name = alert_name
        self.annotations = annotations
        # This parameter is required.
        self.cluster_id = cluster_id
        self.dispatch_rule_id = dispatch_rule_id
        # This parameter is required.
        self.duration = duration
        # This parameter is required.
        self.expression = expression
        self.labels = labels
        # This parameter is required.
        self.message = message
        self.notify_type = notify_type
        # This parameter is required.
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')

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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

