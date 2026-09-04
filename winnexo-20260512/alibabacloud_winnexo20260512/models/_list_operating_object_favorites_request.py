# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOperatingObjectFavoritesRequest(DaraModel):
    def __init__(
        self,
        graph_name: str = None,
        next_token: str = None,
        object_type: str = None,
        operating_object_name: str = None,
        page_size: int = None,
        tenant_id: str = None,
    ):
        # The graph name. Call listGraphs to retrieve available graphs.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # The pagination cursor.
        self.next_token = next_token
        # The object type, such as customer. This parameter has a value when type is set to mention.
        # 
        # This parameter is required.
        self.object_type = object_type
        # The digital employee name (operating object name). Optional.
        # 
        # This parameter is required.
        self.operating_object_name = operating_object_name
        # The page size.
        self.page_size = page_size
        # The tenant ID to take effect.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

