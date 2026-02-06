# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSkillDetailRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        skill_id: str = None,
        source_id_of_assistant_id: str = None,
    ):
        self.group_id = group_id
        self.skill_id = skill_id
        self.source_id_of_assistant_id = source_id_of_assistant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.source_id_of_assistant_id is not None:
            result['SourceIdOfAssistantId'] = self.source_id_of_assistant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SourceIdOfAssistantId') is not None:
            self.source_id_of_assistant_id = m.get('SourceIdOfAssistantId')

        return self

