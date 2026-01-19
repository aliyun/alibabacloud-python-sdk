# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIntervalAgentSkillGroupReportRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        interval: str = None,
        media_type: str = None,
        show_default_if_empty: bool = None,
        skill_group_id: str = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.agent_id = agent_id
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        self.interval = interval
        self.media_type = media_type
        self.show_default_if_empty = show_default_if_empty
        # This parameter is required.
        self.skill_group_id = skill_group_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.show_default_if_empty is not None:
            result['ShowDefaultIfEmpty'] = self.show_default_if_empty

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('ShowDefaultIfEmpty') is not None:
            self.show_default_if_empty = m.get('ShowDefaultIfEmpty')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

