# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgUserGroupQueryListRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_name: str = None,
        user_group_type: int = None,
    ):
        # The keyword of the user group name. A fuzzy match is performed based on the keyword to search for the user group.
        self.name = name
        # The owner of the user group.
        self.owner = owner
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The name of the compute engine. If you want to query the information about a MaxCompute user group, you need to configure this parameter.
        self.project_name = project_name
        self.user_group_type = user_group_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.user_group_type is not None:
            result['userGroupType'] = self.user_group_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('userGroupType') is not None:
            self.user_group_type = m.get('userGroupType')

        return self

