# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWaitingRoomRuleRequest(DaraModel):
    def __init__(
        self,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        site_id: int = None,
        waiting_room_id: str = None,
    ):
        # Rule content, using conditional expressions to match user requests. This parameter is not required when adding a global configuration. There are two usage scenarios:
        # - Match all incoming requests: Set the value to true
        # - Match specific requests: Set the value to a custom expression, for example: (http.host eq "video.example.com")
        # 
        # This parameter is required.
        self.rule = rule
        # Rule switch. This parameter is not required when adding a global configuration. Value range:
        # - on: Enable.
        # - off: Disable.
        # 
        # This parameter is required.
        self.rule_enable = rule_enable
        # Rule name. This parameter is not required when adding a global configuration.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # Site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) API.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The ID of the waiting room to bypass.
        # 
        # This parameter is required.
        self.waiting_room_id = waiting_room_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')

        return self

