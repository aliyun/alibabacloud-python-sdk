# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWaitingRoomRulesRequest(DaraModel):
    def __init__(
        self,
        rule_name: str = None,
        site_id: int = None,
        waiting_room_id: str = None,
        waiting_room_rule_id: int = None,
    ):
        # Rule name, optional, used for querying by the name of the waiting room bypass rule.
        self.rule_name = rule_name
        # Site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) interface.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The ID of the waiting room to bypass, which can be obtained by calling the [ListWaitingRooms](https://help.aliyun.com/document_detail/2850279.html) interface.
        # 
        # This parameter is required.
        self.waiting_room_id = waiting_room_id
        # The ID of the waiting room bypass rule to update, which can be obtained by calling the [ListWaitingRoomRules](https://help.aliyun.com/document_detail/2850279.html) interface.
        self.waiting_room_rule_id = waiting_room_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id

        if self.waiting_room_rule_id is not None:
            result['WaitingRoomRuleId'] = self.waiting_room_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')

        if m.get('WaitingRoomRuleId') is not None:
            self.waiting_room_rule_id = m.get('WaitingRoomRuleId')

        return self

