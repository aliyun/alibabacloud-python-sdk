# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHttpDDoSIntelligentRuleRequest(DaraModel):
    def __init__(
        self,
        record_name: str = None,
        rule_id: int = None,
        site_id: int = None,
    ):
        # Record name.
        # 
        # This parameter is required.
        self.record_name = record_name
        # Rule ID.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # Site ID, which can be obtained by calling the [ListSites](~~ListSites~~) interface.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

