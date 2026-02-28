# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAutoLiveStreamRuleRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        owner_id: int = None,
        rule_id: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.owner_id = owner_id
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

