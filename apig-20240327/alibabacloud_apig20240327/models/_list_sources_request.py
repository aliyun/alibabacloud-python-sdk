# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSourcesRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        type: str = None,
    ):
        # The instance ID.
        self.gateway_id = gateway_id
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        # The type by which you want to query sources.
        # 
        # Valid values:
        # 
        # *   K8S
        # *   MSE_NACOS
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

