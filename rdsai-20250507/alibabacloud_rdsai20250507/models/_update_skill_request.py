# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class UpdateSkillRequest(DaraModel):
    def __init__(
        self,
        content: Dict[str, Any] = None,
        dbtypes: List[str] = None,
        description: str = None,
        name: str = None,
        skill_id: str = None,
    ):
        self.content = content
        self.dbtypes = dbtypes
        self.description = description
        self.name = name
        # This parameter is required.
        self.skill_id = skill_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.dbtypes is not None:
            result['Dbtypes'] = self.dbtypes

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
            self.content = m.get('Content')

        if m.get('Dbtypes') is not None:
            self.dbtypes = m.get('Dbtypes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        return self

