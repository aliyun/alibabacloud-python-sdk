# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetTenantSkillEnabledRequest(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        skill_channel: str = None,
        skill_ids: List[str] = None,
    ):
        self.enabled = enabled
        self.skill_channel = skill_channel
        self.skill_ids = skill_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.skill_channel is not None:
            result['SkillChannel'] = self.skill_channel

        if self.skill_ids is not None:
            result['SkillIds'] = self.skill_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('SkillChannel') is not None:
            self.skill_channel = m.get('SkillChannel')

        if m.get('SkillIds') is not None:
            self.skill_ids = m.get('SkillIds')

        return self

