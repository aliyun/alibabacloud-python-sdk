# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetHttpDDoSAttackRuleStatusRequest(DaraModel):
    def __init__(
        self,
        rule_ids: str = None,
        site_id: int = None,
        status: str = None,
    ):
        # This parameter is required.
        self.rule_ids = rule_ids
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

