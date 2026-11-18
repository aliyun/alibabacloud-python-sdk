# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelApisRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        include_legacy: bool = None,
        keyword: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        # The gateway instance ID used to filter results.
        self.gateway_id = gateway_id
        # Specifies whether to return legacy model APIs created by scenario. If this parameter is omitted or set to false, only APIs created by selecting a model are returned. If this parameter is set to true, APIs created by both methods are returned on the same page, excluding common HTTP, MCP, or Agent APIs.
        self.include_legacy = include_legacy
        # The search keyword. Supports fuzzy search by API name or exact search by API ID.
        self.keyword = keyword
        # The API name for exact search.
        self.name = name
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The ID of the resource group used to filter results.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.include_legacy is not None:
            result['includeLegacy'] = self.include_legacy

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.name is not None:
            result['name'] = self.name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('includeLegacy') is not None:
            self.include_legacy = m.get('includeLegacy')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        return self

