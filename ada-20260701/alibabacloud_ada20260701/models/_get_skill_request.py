# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSkillRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        network: str = None,
        skill_version: int = None,
    ):
        # The Skill name.
        # 
        # This parameter is required.
        self.name = name
        # The network type of the download URL. Valid values: public and internal. If omitted, no download URL is generated.
        self.network = network
        # The release history version number to query. If omitted, the current Skill main record is returned.
        self.skill_version = skill_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.network is not None:
            result['Network'] = self.network

        if self.skill_version is not None:
            result['SkillVersion'] = self.skill_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('SkillVersion') is not None:
            self.skill_version = m.get('SkillVersion')

        return self

