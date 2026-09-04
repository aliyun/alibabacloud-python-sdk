# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListVisibleKnowledgeBasesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListVisibleKnowledgeBasesResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The response status code.
        self.code = code
        # The file information.
        self.items = items
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The total number of records.
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

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListVisibleKnowledgeBasesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListVisibleKnowledgeBasesResponseBodyItems(DaraModel):
    def __init__(
        self,
        creator_name: str = None,
        description: str = None,
        directory_id: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        name: str = None,
        path: str = None,
        source_failed_count: int = None,
        source_ready_count: int = None,
        source_total_count: int = None,
    ):
        # The creator.
        self.creator_name = creator_name
        # The description.
        self.description = description
        # The directory ID. You can obtain this value by calling the API operation for retrieving the knowledge base directory.
        self.directory_id = directory_id
        # The creation time. The value is a timestamp in milliseconds.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The skill name.
        self.name = name
        # The file directory information.
        self.path = path
        # The number of resources in the FAILED state. This parameter is returned only when the top-level knowledge base directory list is queried.
        self.source_failed_count = source_failed_count
        # The number of resources in the READY state. This parameter is returned only when the top-level knowledge base directory list is queried.
        self.source_ready_count = source_ready_count
        # The total number of resources in the directory and its subdirectories. This parameter is returned only when the top-level knowledge base directory list is queried.
        self.source_total_count = source_total_count

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

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.name is not None:
            result['name'] = self.name

        if self.path is not None:
            result['path'] = self.path

        if self.source_failed_count is not None:
            result['sourceFailedCount'] = self.source_failed_count

        if self.source_ready_count is not None:
            result['sourceReadyCount'] = self.source_ready_count

        if self.source_total_count is not None:
            result['sourceTotalCount'] = self.source_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('sourceFailedCount') is not None:
            self.source_failed_count = m.get('sourceFailedCount')

        if m.get('sourceReadyCount') is not None:
            self.source_ready_count = m.get('sourceReadyCount')

        if m.get('sourceTotalCount') is not None:
            self.source_total_count = m.get('sourceTotalCount')

        return self

