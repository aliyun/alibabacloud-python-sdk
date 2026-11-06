# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePolarClawSkillRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        skill_name: str = None,
    ):
        # The region ID of the region where the parameter template resides.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query region IDs.
        self.region_id = region_id
        # The name of the skill.
        # 
        # This parameter is required.
        self.skill_name = skill_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        return self

