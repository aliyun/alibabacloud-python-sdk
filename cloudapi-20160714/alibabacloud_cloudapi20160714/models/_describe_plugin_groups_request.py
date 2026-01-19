# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePluginGroupsRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        page_number: int = None,
        page_size: int = None,
        plugin_id: str = None,
        security_token: str = None,
    ):
        # API group description
        self.description = description
        # API group ID
        self.group_id = group_id
        # API group name
        self.group_name = group_name
        # Pagination parameter: current page number
        self.page_number = page_number
        # Pagination parameter: number of items per page
        self.page_size = page_size
        # API Gateway plugin ID
        # 
        # This parameter is required.
        self.plugin_id = plugin_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

