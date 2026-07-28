# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeChatMessageRequest(DaraModel):
    def __init__(
        self,
        query: str = None,
        region_id: str = None,
        session_id: str = None,
        skill: str = None,
        timezone: str = None,
    ):
        # The question statement submitted by the user.
        # 
        # This parameter is required.
        self.query = query
        # The Alibaba Cloud region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        self.session_id = session_id
        self.skill = skill
        # The time zone.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query is not None:
            result['Query'] = self.query

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.skill is not None:
            result['Skill'] = self.skill

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Skill') is not None:
            self.skill = m.get('Skill')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        return self

