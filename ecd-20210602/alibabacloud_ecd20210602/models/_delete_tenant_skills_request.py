# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteTenantSkillsRequest(DaraModel):
    def __init__(
        self,
        skill_channel: str = None,
        skill_ids: List[str] = None,
    ):
        # The skill channel. Valid values:
        # - ENTERPRISE: Enterprise edition.
        # - BUSINESS: Business edition.
        self.skill_channel = skill_channel
        # The list of skill IDs.
        self.skill_ids = skill_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skill_channel is not None:
            result['SkillChannel'] = self.skill_channel

        if self.skill_ids is not None:
            result['SkillIds'] = self.skill_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkillChannel') is not None:
            self.skill_channel = m.get('SkillChannel')

        if m.get('SkillIds') is not None:
            self.skill_ids = m.get('SkillIds')

        return self

