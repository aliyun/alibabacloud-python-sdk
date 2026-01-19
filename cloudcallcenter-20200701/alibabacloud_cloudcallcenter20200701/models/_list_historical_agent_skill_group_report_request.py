# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHistoricalAgentSkillGroupReportRequest(DaraModel):
    def __init__(
        self,
        agent_id_list: str = None,
        end_time: int = None,
        instance_id: str = None,
        media_type: str = None,
        page_number: int = None,
        page_size: int = None,
        skill_group_id_list: str = None,
        start_time: int = None,
    ):
        self.agent_id_list = agent_id_list
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        self.media_type = media_type
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.skill_group_id_list = skill_group_id_list
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id_list is not None:
            result['AgentIdList'] = self.agent_id_list

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.skill_group_id_list is not None:
            result['SkillGroupIdList'] = self.skill_group_id_list

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIdList') is not None:
            self.agent_id_list = m.get('AgentIdList')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SkillGroupIdList') is not None:
            self.skill_group_id_list = m.get('SkillGroupIdList')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

