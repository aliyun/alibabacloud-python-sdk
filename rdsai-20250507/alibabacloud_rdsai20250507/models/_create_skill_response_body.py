# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class CreateSkillResponseBody(DaraModel):
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
    ):
        self.content = content
        self.created_at = created_at
        self.dbtypes = dbtypes
        self.description = description
        self.id = id
        self.name = name
        self.request_id = request_id
        self.skill_type = skill_type

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

        return self

