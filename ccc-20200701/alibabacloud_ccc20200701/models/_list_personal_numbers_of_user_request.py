# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPersonalNumbersOfUserRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        is_member: bool = None,
        page_number: int = None,
        page_size: int = None,
        search_pattern: str = None,
        user_id: str = None,
    ):
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Indicates whether the phone numbers are associated with the agent. If true, the API queries the list of personal outbound phone numbers associated with the UserId. If false, it queries the list of personal outbound phone numbers that can be associated with but are not currently associated with the UserId. This parameter is typically used together with the AddPersonalNumbersToUser API.
        # 
        # This parameter is required.
        self.is_member = is_member
        # Page number, ranging from 1 to 100.
        # 
        # This parameter is required.
        self.page_number = page_number
        # Page size, ranging from 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Fuzzy matching based on phone number. Optional. Default value is empty if not specified.
        self.search_pattern = search_pattern
        # Agent ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

