# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListMemoryStoresResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        memory_stores: List[main_models.ListMemoryStoresResponseBodyMemoryStores] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.max_results = max_results
        self.memory_stores = memory_stores
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.memory_stores:
            for v1 in self.memory_stores:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        result['memoryStores'] = []
        if self.memory_stores is not None:
            for k1 in self.memory_stores:
                result['memoryStores'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        self.memory_stores = []
        if m.get('memoryStores') is not None:
            for k1 in m.get('memoryStores'):
                temp_model = main_models.ListMemoryStoresResponseBodyMemoryStores()
                self.memory_stores.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListMemoryStoresResponseBodyMemoryStores(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        memory_store_name: str = None,
        region_id: str = None,
        update_time: str = None,
        workspace: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.description = description
        self.memory_store_name = memory_store_name
        self.region_id = region_id
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.memory_store_name is not None:
            result['memoryStoreName'] = self.memory_store_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('memoryStoreName') is not None:
            self.memory_store_name = m.get('memoryStoreName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

