# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePluginApisRequest(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        description: str = None,
        group_id: str = None,
        method: str = None,
        page_number: int = None,
        page_size: int = None,
        path: str = None,
        plugin_id: str = None,
        security_token: str = None,
    ):
        # The ID of the API.
        self.api_id = api_id
        # The name of the API.
        self.api_name = api_name
        # The description of the API.
        self.description = description
        # The ID of the API group.
        self.group_id = group_id
        # The request HTTP method of the API.
        self.method = method
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page.
        # Default value:10.
        self.page_size = page_size
        # The request path of the API.
        self.path = path
        # The ID of the gateway plug-in.
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
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.method is not None:
            result['Method'] = self.method

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path is not None:
            result['Path'] = self.path

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

