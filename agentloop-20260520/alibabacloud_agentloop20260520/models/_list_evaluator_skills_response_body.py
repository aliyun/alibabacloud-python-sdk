# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ListEvaluatorSkillsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        skills: List[main_models.ListEvaluatorSkillsResponseBodySkills] = None,
        total: int = None,
    ):
        # The number of entries per page used in this request.
        self.max_results = max_results
        # The pagination token for the next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of skill summaries.
        self.skills = skills
        # The total number of skills.
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
                temp_model = main_models.ListEvaluatorSkillsResponseBodySkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListEvaluatorSkillsResponseBodySkills(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        display_name: str = None,
        enable: bool = None,
        latest_version: str = None,
        skill_name: str = None,
        updated_at: int = None,
    ):
        # The creation time. This field is declared as int64 in CloudSpec, but the backend currently returns the StarOps `createTime` string field.
        self.created_at = created_at
        # The skill description.
        self.description = description
        # The display name.
        self.display_name = display_name
        # Indicates whether the skill is enabled.
        self.enable = enable
        # The latest version. This field is declared in CloudSpec but is not currently populated in the backend response.
        self.latest_version = latest_version
        # The skill name.
        self.skill_name = skill_name
        # The update time. This field is declared as int64 in CloudSpec, but the backend currently returns the StarOps `updateTime` string field.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.enable is not None:
            result['enable'] = self.enable

        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

