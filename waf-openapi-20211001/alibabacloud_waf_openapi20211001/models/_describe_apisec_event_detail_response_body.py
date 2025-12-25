# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeApisecEventDetailResponseBody(DaraModel):
    def __init__(
        self,
        attack_cnt: str = None,
        attacker_list: List[str] = None,
        detail_value: str = None,
        end_ts: str = None,
        event_id: str = None,
        event_level: str = None,
        event_scope: str = None,
        event_tag: str = None,
        note: str = None,
        origin: str = None,
        request_id: str = None,
        start_ts: str = None,
        user_status: str = None,
    ):
        self.attack_cnt = attack_cnt
        self.attacker_list = attacker_list
        self.detail_value = detail_value
        self.end_ts = end_ts
        self.event_id = event_id
        self.event_level = event_level
        self.event_scope = event_scope
        self.event_tag = event_tag
        self.note = note
        self.origin = origin
        self.request_id = request_id
        self.start_ts = start_ts
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_cnt is not None:
            result['AttackCnt'] = self.attack_cnt

        if self.attacker_list is not None:
            result['AttackerList'] = self.attacker_list

        if self.detail_value is not None:
            result['DetailValue'] = self.detail_value

        if self.end_ts is not None:
            result['EndTs'] = self.end_ts

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_scope is not None:
            result['EventScope'] = self.event_scope

        if self.event_tag is not None:
            result['EventTag'] = self.event_tag

        if self.note is not None:
            result['Note'] = self.note

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackCnt') is not None:
            self.attack_cnt = m.get('AttackCnt')

        if m.get('AttackerList') is not None:
            self.attacker_list = m.get('AttackerList')

        if m.get('DetailValue') is not None:
            self.detail_value = m.get('DetailValue')

        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventScope') is not None:
            self.event_scope = m.get('EventScope')

        if m.get('EventTag') is not None:
            self.event_tag = m.get('EventTag')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        return self

