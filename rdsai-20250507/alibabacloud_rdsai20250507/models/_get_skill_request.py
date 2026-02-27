# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSkillRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        skill_id: str = None,
    ):
        self.language = language
        # This parameter is required.
        self.skill_id = skill_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        return self

