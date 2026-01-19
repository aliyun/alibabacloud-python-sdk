# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFlashSmsSettingsShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        skill_group_id_list_shrink: str = None,
        skill_group_name: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.skill_group_id_list_shrink = skill_group_id_list_shrink
        self.skill_group_name = skill_group_name

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

        if self.skill_group_id_list_shrink is not None:
            result['SkillGroupIdList'] = self.skill_group_id_list_shrink

        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SkillGroupIdList') is not None:
            self.skill_group_id_list_shrink = m.get('SkillGroupIdList')

        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')

        return self

