# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListPublicSkillsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        skills: List[main_models.ListPublicSkillsResponseBodySkills] = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The token to retrieve the next page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of public skills.
        self.skills = skills
        # The total number of entries.
        self.total_count = total_count

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
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['Skills'].append(k1.to_map() if k1 else None)

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

        self.skills = []
        if m.get('Skills') is not None:
            for k1 in m.get('Skills'):
                temp_model = main_models.ListPublicSkillsResponseBodySkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPublicSkillsResponseBodySkills(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        download_url: str = None,
        skill_description: str = None,
        skill_id: str = None,
        skill_labels: List[str] = None,
        skill_name: str = None,
        skill_space_id: str = None,
        update_time: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The download link for the skill package.
        self.download_url = download_url
        # The description of the skill.
        self.skill_description = skill_description
        # The ID of the skill.
        self.skill_id = skill_id
        # The labels attached to the skill.
        self.skill_labels = skill_labels
        # The name of the skill.
        self.skill_name = skill_name
        # The ID of the skill space.
        self.skill_space_id = skill_space_id
        # The update time.
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

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.skill_description is not None:
            result['SkillDescription'] = self.skill_description

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_labels is not None:
            result['SkillLabels'] = self.skill_labels

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.skill_space_id is not None:
            result['SkillSpaceId'] = self.skill_space_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('SkillDescription') is not None:
            self.skill_description = m.get('SkillDescription')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillLabels') is not None:
            self.skill_labels = m.get('SkillLabels')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('SkillSpaceId') is not None:
            self.skill_space_id = m.get('SkillSpaceId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

