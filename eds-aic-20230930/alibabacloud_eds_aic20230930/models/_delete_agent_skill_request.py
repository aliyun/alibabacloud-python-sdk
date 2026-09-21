# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAgentSkillRequest(DaraModel):
    def __init__(
        self,
        skill_ids: List[str] = None,
    ):
        # The list of skill IDs.
        self.skill_ids = skill_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skill_ids is not None:
            result['SkillIds'] = self.skill_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkillIds') is not None:
            self.skill_ids = m.get('SkillIds')

        return self

