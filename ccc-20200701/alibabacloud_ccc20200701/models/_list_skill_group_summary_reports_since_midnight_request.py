# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSkillGroupSummaryReportsSinceMidnightRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        skill_groups: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number to return. The value must be in the range of 1 to 100.
        self.page_number = page_number
        # The number of entries to return on each page. The value must be in the range of 1 to 100.
        self.page_size = page_size
        # A JSON-formatted string that contains the IDs of the skill groups to query. If this parameter is omitted, the query includes all skill groups.
        self.skill_groups = skill_groups

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.skill_groups is not None:
            result['SkillGroups'] = self.skill_groups

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SkillGroups') is not None:
            self.skill_groups = m.get('SkillGroups')

        return self

