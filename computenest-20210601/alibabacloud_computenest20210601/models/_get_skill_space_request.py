# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSkillSpaceRequest(DaraModel):
    def __init__(
        self,
        skill_space_id: str = None,
    ):
        # This parameter is required.
        self.skill_space_id = skill_space_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skill_space_id is not None:
            result['SkillSpaceId'] = self.skill_space_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkillSpaceId') is not None:
            self.skill_space_id = m.get('SkillSpaceId')

        return self

