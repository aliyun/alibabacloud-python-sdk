# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetSkillResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        request_id: str = None,
        skill_description: str = None,
        skill_id: str = None,
        skill_labels: List[str] = None,
        skill_name: str = None,
        skill_space_id: str = None,
        update_time: str = None,
    ):
        # The time the Skill was created.
        self.create_time = create_time
        # The request ID.
        self.request_id = request_id
        # The description of the Skill.
        self.skill_description = skill_description
        # The ID of the Skill.
        self.skill_id = skill_id
        # The labels of the Skill.
        self.skill_labels = skill_labels
        # The name of the Skill.
        self.skill_name = skill_name
        # The ID of the SkillSpace to which the Skill belongs.
        self.skill_space_id = skill_space_id
        # The time the Skill was last updated.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

