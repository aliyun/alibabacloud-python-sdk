# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWaitingRoomRuleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        waiting_room_rule_id: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Waiting room bypass rule ID.
        self.waiting_room_rule_id = waiting_room_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.waiting_room_rule_id is not None:
            result['WaitingRoomRuleId'] = self.waiting_room_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WaitingRoomRuleId') is not None:
            self.waiting_room_rule_id = m.get('WaitingRoomRuleId')

        return self

