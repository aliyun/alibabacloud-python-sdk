# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListOperatingObjectFavoritesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        graph_name: str = None,
        has_more: bool = None,
        items: List[main_models.ListOperatingObjectFavoritesResponseBodyItems] = None,
        message: str = None,
        next_token: str = None,
        object_type: str = None,
        operating_object_name: str = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The error code.
        self.code = code
        # The graph name. Call listGraphs to retrieve available graphs.
        self.graph_name = graph_name
        # Indicates whether more pages are available.
        self.has_more = has_more
        # The MCP card list.
        self.items = items
        # The status code description.
        self.message = message
        # The pagination cursor.
        self.next_token = next_token
        # The object type, such as customer. This parameter has a value when type is set to mention.
        self.object_type = object_type
        # The digital employee name (operating object name).
        self.operating_object_name = operating_object_name
        # The page size.
        self.page_size = page_size
        # The request trace ID.
        self.request_id = request_id
        # The total number of results.
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListOperatingObjectFavoritesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListOperatingObjectFavoritesResponseBodyItems(DaraModel):
    def __init__(
        self,
        description: str = None,
        followed_at: int = None,
        graph_name: str = None,
        object_id: str = None,
        object_name: str = None,
        object_type: str = None,
    ):
        # The to-do card type description.
        self.description = description
        # The follow time. The value is a Unix timestamp in seconds.
        self.followed_at = followed_at
        # The graph name.
        self.graph_name = graph_name
        # The ID of the recommended item. The value can be a **feedId** or a micro-application ID.
        self.object_id = object_id
        # The object name.
        self.object_name = object_name
        # The bound object type, such as customer or project.
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.followed_at is not None:
            result['followedAt'] = self.followed_at

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_name is not None:
            result['objectName'] = self.object_name

        if self.object_type is not None:
            result['objectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('followedAt') is not None:
            self.followed_at = m.get('followedAt')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectName') is not None:
            self.object_name = m.get('objectName')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        return self

