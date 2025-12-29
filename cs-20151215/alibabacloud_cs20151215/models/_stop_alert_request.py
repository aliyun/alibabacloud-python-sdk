# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopAlertRequest(DaraModel):
    def __init__(
        self,
        alert_rule_group_name: str = None,
        alert_rule_name: str = None,
    ):
        # The name of the alert rule group.
        self.alert_rule_group_name = alert_rule_group_name
        # The name of the alert rule.
        self.alert_rule_name = alert_rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_rule_group_name is not None:
            result['alert_rule_group_name'] = self.alert_rule_group_name

        if self.alert_rule_name is not None:
            result['alert_rule_name'] = self.alert_rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alert_rule_group_name') is not None:
            self.alert_rule_group_name = m.get('alert_rule_group_name')

        if m.get('alert_rule_name') is not None:
            self.alert_rule_name = m.get('alert_rule_name')

        return self

