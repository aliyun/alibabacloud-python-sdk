# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePrometheusAlertRuleRequest(DaraModel):
    def __init__(
        self,
        alert_id: int = None,
        cluster_id: str = None,
    ):
        # The ID of the alert rule. You can call the ListPrometheusAlertRules operation to query the ID of the alert rule.
        # 
        # This parameter is required.
        self.alert_id = alert_id
        # The cluster ID of the Prometheus monitoring alarm rule.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        return self

