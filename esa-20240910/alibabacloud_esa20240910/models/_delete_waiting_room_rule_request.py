# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWaitingRoomRuleRequest(DaraModel):
    def __init__(
        self,
        site_id: int = None,
        waiting_room_rule_id: int = None,
    ):
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The ID of the waiting room bypass rule.
        # 
        # This parameter is required.
        self.waiting_room_rule_id = waiting_room_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.waiting_room_rule_id is not None:
            result['WaitingRoomRuleId'] = self.waiting_room_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('WaitingRoomRuleId') is not None:
            self.waiting_room_rule_id = m.get('WaitingRoomRuleId')

        return self

