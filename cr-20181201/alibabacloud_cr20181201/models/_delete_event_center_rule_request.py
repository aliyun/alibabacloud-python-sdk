# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEventCenterRuleRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        rule_id: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the event notification rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

