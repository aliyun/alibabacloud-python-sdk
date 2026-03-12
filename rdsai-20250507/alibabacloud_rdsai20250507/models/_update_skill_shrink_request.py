# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSkillShrinkRequest(DaraModel):
    def __init__(
        self,
        content_shrink: str = None,
        dbtypes_shrink: str = None,
        description: str = None,
        name: str = None,
        skill_id: str = None,
    ):
        # The content of the skill.
        self.content_shrink = content_shrink
        # The list of database engines.
        self.dbtypes_shrink = dbtypes_shrink
        # The description of the Skill. It can be up to 1000 characters in length.
        self.description = description
        # The name of the skill, which can contain only lowercase letters, numbers, and hyphens.
        self.name = name
        # The unique identifier of the skill.
        # 
        # This parameter is required.
        self.skill_id = skill_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.dbtypes_shrink is not None:
            result['Dbtypes'] = self.dbtypes_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')

        if m.get('Dbtypes') is not None:
            self.dbtypes_shrink = m.get('Dbtypes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        return self

