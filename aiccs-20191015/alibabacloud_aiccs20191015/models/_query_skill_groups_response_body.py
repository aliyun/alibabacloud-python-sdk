# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class QuerySkillGroupsResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.QuerySkillGroupsResponseBodyData] = None,
        one_page_size: int = None,
        request_id: str = None,
        total_page: int = None,
        total_results: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.one_page_size = one_page_size
        self.request_id = request_id
        self.total_page = total_page
        self.total_results = total_results

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.one_page_size is not None:
            result['OnePageSize'] = self.one_page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        if self.total_results is not None:
            result['TotalResults'] = self.total_results

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QuerySkillGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('OnePageSize') is not None:
            self.one_page_size = m.get('OnePageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')

        return self

class QuerySkillGroupsResponseBodyData(DaraModel):
    def __init__(
        self,
        channel_type: int = None,
        description: str = None,
        display_name: str = None,
        skill_group_id: int = None,
        skill_group_name: str = None,
    ):
        self.channel_type = channel_type
        self.description = description
        self.display_name = display_name
        self.skill_group_id = skill_group_id
        self.skill_group_name = skill_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')

        return self

