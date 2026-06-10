# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListSkillSpacesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        skill_spaces: List[main_models.ListSkillSpacesResponseBodySkillSpaces] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.skill_spaces = skill_spaces
        self.total_count = total_count

    def validate(self):
        if self.skill_spaces:
            for v1 in self.skill_spaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SkillSpaces'] = []
        if self.skill_spaces is not None:
            for k1 in self.skill_spaces:
                result['SkillSpaces'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.skill_spaces = []
        if m.get('SkillSpaces') is not None:
            for k1 in m.get('SkillSpaces'):
                temp_model = main_models.ListSkillSpacesResponseBodySkillSpaces()
                self.skill_spaces.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSkillSpacesResponseBodySkillSpaces(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        skill_space_description: str = None,
        skill_space_id: str = None,
        skill_space_name: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.skill_space_description = skill_space_description
        # SkillSpace ID
        self.skill_space_id = skill_space_id
        self.skill_space_name = skill_space_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.skill_space_description is not None:
            result['SkillSpaceDescription'] = self.skill_space_description

        if self.skill_space_id is not None:
            result['SkillSpaceId'] = self.skill_space_id

        if self.skill_space_name is not None:
            result['SkillSpaceName'] = self.skill_space_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('SkillSpaceDescription') is not None:
            self.skill_space_description = m.get('SkillSpaceDescription')

        if m.get('SkillSpaceId') is not None:
            self.skill_space_id = m.get('SkillSpaceId')

        if m.get('SkillSpaceName') is not None:
            self.skill_space_name = m.get('SkillSpaceName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

