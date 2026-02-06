# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetSkillsRequest(DaraModel):
    def __init__(
        self,
        group_ids: List[str] = None,
        skill_ids: List[str] = None,
        source_id_of_assistant_id: str = None,
    ):
        self.group_ids = group_ids
        self.skill_ids = skill_ids
        self.source_id_of_assistant_id = source_id_of_assistant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.skill_ids is not None:
            result['SkillIds'] = self.skill_ids

        if self.source_id_of_assistant_id is not None:
            result['SourceIdOfAssistantId'] = self.source_id_of_assistant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('SkillIds') is not None:
            self.skill_ids = m.get('SkillIds')

        if m.get('SourceIdOfAssistantId') is not None:
            self.source_id_of_assistant_id = m.get('SourceIdOfAssistantId')

        return self

