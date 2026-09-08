# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPhoneNumbersOfSkillGroupRequest(DaraModel):
    def __init__(
        self,
        active: bool = None,
        instance_id: str = None,
        is_member: bool = None,
        page_number: int = None,
        page_size: int = None,
        search_pattern: str = None,
        skill_group_id: str = None,
    ):
        # Indicates whether the phone number is active. This parameter is optional. The default value is empty, which means no filtering is applied.
        self.active = active
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Indicates whether the phone numbers are associated with the skill group. If true, the API queries the list of phone numbers already associated with the specified SkillGroupId. If false, the API queries the list of phone numbers that can be associated with the specified SkillGroupId but are not currently associated. This parameter is typically used together with the AddNumbersToSkillGroup API.
        # 
        # This parameter is required.
        self.is_member = is_member
        # Page number for paging. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_number = page_number
        # Page size for paging. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Performs Fuzzy Matching on phone numbers. This parameter is optional. The default value is empty, which means no filtering is applied.
        self.search_pattern = search_pattern
        # Skill group ID.
        # 
        # This parameter is required.
        self.skill_group_id = skill_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_member is not None:
            result['IsMember'] = self.is_member

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_pattern is not None:
            result['SearchPattern'] = self.search_pattern

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsMember') is not None:
            self.is_member = m.get('IsMember')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchPattern') is not None:
            self.search_pattern = m.get('SearchPattern')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        return self

