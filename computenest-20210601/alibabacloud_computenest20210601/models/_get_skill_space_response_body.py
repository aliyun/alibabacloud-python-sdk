# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSkillSpaceResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        request_id: str = None,
        skill_space_description: str = None,
        skill_space_id: str = None,
        skill_space_name: str = None,
        update_time: str = None,
    ):
        # The time when the SkillSpace was created.
        self.create_time = create_time
        # The ID of the request.
        self.request_id = request_id
        # The description of the SkillSpace.
        self.skill_space_description = skill_space_description
        # The ID of the SkillSpace.
        self.skill_space_id = skill_space_id
        # The name of the SkillSpace.
        self.skill_space_name = skill_space_name
        # The time when the SkillSpace was last updated.
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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SkillSpaceDescription') is not None:
            self.skill_space_description = m.get('SkillSpaceDescription')

        if m.get('SkillSpaceId') is not None:
            self.skill_space_id = m.get('SkillSpaceId')

        if m.get('SkillSpaceName') is not None:
            self.skill_space_name = m.get('SkillSpaceName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

