# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListDigitalEmployeeSkillsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        skills: List[main_models.ListDigitalEmployeeSkillsResponseBodySkills] = None,
        total: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.skills = skills
        self.total = total

    def validate(self):
        if self.skills:
            for v1 in self.skills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['skills'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.skills = []
        if m.get('skills') is not None:
            for k1 in m.get('skills'):
                temp_model = main_models.ListDigitalEmployeeSkillsResponseBodySkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListDigitalEmployeeSkillsResponseBodySkills(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        enable: bool = None,
        skill_name: str = None,
        update_time: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.description = description
        self.display_name = display_name
        self.enable = enable
        self.skill_name = skill_name
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.enable is not None:
            result['enable'] = self.enable

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

