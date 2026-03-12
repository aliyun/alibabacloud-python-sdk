# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class GetSkillResponseBody(DaraModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        created_at: str = None,
        dbtypes: List[str] = None,
        description: str = None,
        id: str = None,
        name: str = None,
        request_id: str = None,
        skill_type: str = None,
        updated_at: str = None,
    ):
        # The content of the skill.
        self.content = content
        # The creation time of the skill.
        self.created_at = created_at
        # The list of database engines.
        self.dbtypes = dbtypes
        # The description of the skill. It can be up to 1000 characters in length.
        self.description = description
        # The unique identifier of the skill.
        self.id = id
        # The name of the skill, which can contain only lowercase letters, numbers, and hyphens.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The type of the skill.
        self.skill_type = skill_type
        # The update time of the skill.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.dbtypes is not None:
            result['Dbtypes'] = self.dbtypes

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.skill_type is not None:
            result['SkillType'] = self.skill_type

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Dbtypes') is not None:
            self.dbtypes = m.get('Dbtypes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SkillType') is not None:
            self.skill_type = m.get('SkillType')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

