# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListInstanceIndicesResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListInstanceIndicesResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListInstanceIndicesResponseBodyResult] = None,
    ):
        # The response headers.
        self.headers = headers
        # The request ID.
        self.request_id = request_id
        # The index list details.
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = main_models.ListInstanceIndicesResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListInstanceIndicesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListInstanceIndicesResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        health: str = None,
        ilm_explain: str = None,
        is_managed: str = None,
        managed_status: str = None,
        name: str = None,
        phase: str = None,
        size: int = None,
    ):
        # The time when the index list was queried.
        self.create_time = create_time
        # The health status of the index. Valid values:
        # 
        # - green: Healthy.
        # 
        # - yellow: Warning.
        # 
        # - red: Abnormal.
        self.health = health
        # The full lifecycle status of the index.
        self.ilm_explain = ilm_explain
        # This parameter is deprecated and can be ignored.
        self.is_managed = is_managed
        # The managed status of the index. Valid values:
        # 
        # - following: Managed.
        # 
        # - closing: Being unmanaged.
        # 
        # - closed: Not managed.
        self.managed_status = managed_status
        # The index name.
        self.name = name
        # The current storage lifecycle phase. Valid values:
        # 
        # - warm: Warm phase.
        # 
        # - cold: Cold phase.
        # 
        # - hot: Hot phase.
        # 
        # - delete: Delete phase.
        # 
        # > If this parameter is empty, the index is not managed by a lifecycle policy.
        self.phase = phase
        # The total storage space occupied by the index. Unit: bytes.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.health is not None:
            result['health'] = self.health

        if self.ilm_explain is not None:
            result['ilmExplain'] = self.ilm_explain

        if self.is_managed is not None:
            result['isManaged'] = self.is_managed

        if self.managed_status is not None:
            result['managedStatus'] = self.managed_status

        if self.name is not None:
            result['name'] = self.name

        if self.phase is not None:
            result['phase'] = self.phase

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('health') is not None:
            self.health = m.get('health')

        if m.get('ilmExplain') is not None:
            self.ilm_explain = m.get('ilmExplain')

        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')

        if m.get('managedStatus') is not None:
            self.managed_status = m.get('managedStatus')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phase') is not None:
            self.phase = m.get('phase')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

class ListInstanceIndicesResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_managed_count: int = None,
        x_managed_storage_size: int = None,
        x_osscount: int = None,
        x_ossstorage_size: int = None,
    ):
        # The total number of managed indexes in the cloud.
        self.x_managed_count = x_managed_count
        # The total size of managed indexes in the cloud. Unit: bytes.
        self.x_managed_storage_size = x_managed_storage_size
        # The total number of OpenStore cold-phase indexes.
        self.x_osscount = x_osscount
        # The total size of OpenStore cold-phase indexes for the instance. Unit: bytes.
        self.x_ossstorage_size = x_ossstorage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_managed_count is not None:
            result['X-Managed-Count'] = self.x_managed_count

        if self.x_managed_storage_size is not None:
            result['X-Managed-StorageSize'] = self.x_managed_storage_size

        if self.x_osscount is not None:
            result['X-OSS-Count'] = self.x_osscount

        if self.x_ossstorage_size is not None:
            result['X-OSS-StorageSize'] = self.x_ossstorage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Managed-Count') is not None:
            self.x_managed_count = m.get('X-Managed-Count')

        if m.get('X-Managed-StorageSize') is not None:
            self.x_managed_storage_size = m.get('X-Managed-StorageSize')

        if m.get('X-OSS-Count') is not None:
            self.x_osscount = m.get('X-OSS-Count')

        if m.get('X-OSS-StorageSize') is not None:
            self.x_ossstorage_size = m.get('X-OSS-StorageSize')

        return self

