# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PolicyConfiguration(DaraModel):
    def __init__(
        self,
        action_policy_id: str = None,
        alert_policy_id: str = None,
        repeat_interval: str = None,
    ):
        self.action_policy_id = action_policy_id
        self.alert_policy_id = alert_policy_id
        self.repeat_interval = repeat_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_policy_id is not None:
            result['actionPolicyId'] = self.action_policy_id

        if self.alert_policy_id is not None:
            result['alertPolicyId'] = self.alert_policy_id

        if self.repeat_interval is not None:
            result['repeatInterval'] = self.repeat_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionPolicyId') is not None:
            self.action_policy_id = m.get('actionPolicyId')

        if m.get('alertPolicyId') is not None:
            self.alert_policy_id = m.get('alertPolicyId')

        if m.get('repeatInterval') is not None:
            self.repeat_interval = m.get('repeatInterval')

        return self

