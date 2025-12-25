# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGatewaysShrinkRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        gateway_type: str = None,
        keyword: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        tag_shrink: str = None,
    ):
        # The instance ID. If you specify an ID, an exact search is performed.
        self.gateway_id = gateway_id
        self.gateway_type = gateway_type
        # The search keyword. A full match is performed. The search is case-insensitive.
        self.keyword = keyword
        # The instance name. If you specify a name, an exact search is performed.
        self.name = name
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags that you want to use for the search.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

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

        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

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

        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')

        return self

