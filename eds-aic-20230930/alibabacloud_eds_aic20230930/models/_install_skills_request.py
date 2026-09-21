# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InstallSkillsRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        skill_ids: List[str] = None,
    ):
        # The list of cloud phone instance IDs. You can specify 1 to 200 instance IDs.
        self.instance_ids = instance_ids
        # The list of skill IDs. You can specify 1 to 10 skill IDs.
        self.skill_ids = skill_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.skill_ids is not None:
            result['SkillIds'] = self.skill_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('SkillIds') is not None:
            self.skill_ids = m.get('SkillIds')

        return self

