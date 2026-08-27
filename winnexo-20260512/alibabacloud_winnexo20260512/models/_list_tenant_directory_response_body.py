# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListTenantDirectoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListTenantDirectoryResponseBodyItems] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The status code.
        self.code = code
        # The file information.
        self.items = items
        # The description of the status code.
        self.message = message
        # The page number. Default value: 1. Minimum value: 1. Maximum value: 200.
        self.page = page
        # The number of entries per page. Default value: 100. Maximum value: 500.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

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

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListTenantDirectoryResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListTenantDirectoryResponseBodyItems(DaraModel):
    def __init__(
        self,
        creator_name: str = None,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        item_id: str = None,
        item_type: str = None,
        name: str = None,
        object_bindings: List[Dict[str, Any]] = None,
        source_failed_count: int = None,
        source_ready_count: int = None,
        source_status: str = None,
        source_total_count: int = None,
        source_type: str = None,
    ):
        # The nickname of the creator.
        self.creator_name = creator_name
        # The description of the to-do card type.
        self.description = description
        # The creation time.
        self.gmt_create = gmt_create
        # The last modification time.
        self.gmt_modified = gmt_modified
        # The signing record ID.
        self.item_id = item_id
        # The data type (group, user, or role).
        self.item_type = item_type
        # The name.
        self.name = name
        # The object bindings.
        self.object_bindings = object_bindings
        # The number of resources with the FAILED status. This field is returned only when the top-level directory list of the knowledge base is queried.
        self.source_failed_count = source_failed_count
        # The number of resources with the READY status. This field is returned only when the top-level directory list of the knowledge base is queried.
        self.source_ready_count = source_ready_count
        # The resource status. This field has a value only when itemType is set to resource.
        self.source_status = source_status
        # The total number of resources in the directory and its subdirectories. This field is returned only when the top-level directory list of the knowledge base is queried.
        self.source_total_count = source_total_count
        # The data source type.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.description is not None:
            result['description'] = self.description

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.item_id is not None:
            result['itemId'] = self.item_id

        if self.item_type is not None:
            result['itemType'] = self.item_type

        if self.name is not None:
            result['name'] = self.name

        if self.object_bindings is not None:
            result['objectBindings'] = self.object_bindings

        if self.source_failed_count is not None:
            result['sourceFailedCount'] = self.source_failed_count

        if self.source_ready_count is not None:
            result['sourceReadyCount'] = self.source_ready_count

        if self.source_status is not None:
            result['sourceStatus'] = self.source_status

        if self.source_total_count is not None:
            result['sourceTotalCount'] = self.source_total_count

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')

        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('objectBindings') is not None:
            self.object_bindings = m.get('objectBindings')

        if m.get('sourceFailedCount') is not None:
            self.source_failed_count = m.get('sourceFailedCount')

        if m.get('sourceReadyCount') is not None:
            self.source_ready_count = m.get('sourceReadyCount')

        if m.get('sourceStatus') is not None:
            self.source_status = m.get('sourceStatus')

        if m.get('sourceTotalCount') is not None:
            self.source_total_count = m.get('sourceTotalCount')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

