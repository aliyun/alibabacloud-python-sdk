# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPolarClawSkillRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        modify_type: str = None,
        path: str = None,
        region_id: str = None,
        skill_name: str = None,
        skill_version: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The modification type. Valid values: 
        # * **evaluate**: Evaluates the skill.
        # 
        # This parameter is required.
        self.modify_type = modify_type
        # The destination path.
        self.path = path
        # The region ID.
        self.region_id = region_id
        # The skill name.
        # 
        # This parameter is required.
        self.skill_name = skill_name
        # The skill version.
        self.skill_version = skill_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        if self.path is not None:
            result['Path'] = self.path

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.skill_version is not None:
            result['SkillVersion'] = self.skill_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('SkillVersion') is not None:
            self.skill_version = m.get('SkillVersion')

        return self

