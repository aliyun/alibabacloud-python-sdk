# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListDataStreamsResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListDataStreamsResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListDataStreamsResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
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
            temp_model = main_models.ListDataStreamsResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListDataStreamsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListDataStreamsResponseBodyResult(DaraModel):
    def __init__(
        self,
        health: str = None,
        ilm_policy_name: str = None,
        index_template_name: str = None,
        indices: List[main_models.ListDataStreamsResponseBodyResultIndices] = None,
        managed_storage_size: int = None,
        name: str = None,
        total_storage_size: int = None,
    ):
        self.health = health
        self.ilm_policy_name = ilm_policy_name
        self.index_template_name = index_template_name
        self.indices = indices
        self.managed_storage_size = managed_storage_size
        self.name = name
        self.total_storage_size = total_storage_size

    def validate(self):
        if self.indices:
            for v1 in self.indices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.health is not None:
            result['health'] = self.health

        if self.ilm_policy_name is not None:
            result['ilmPolicyName'] = self.ilm_policy_name

        if self.index_template_name is not None:
            result['indexTemplateName'] = self.index_template_name

        result['indices'] = []
        if self.indices is not None:
            for k1 in self.indices:
                result['indices'].append(k1.to_map() if k1 else None)

        if self.managed_storage_size is not None:
            result['managedStorageSize'] = self.managed_storage_size

        if self.name is not None:
            result['name'] = self.name

        if self.total_storage_size is not None:
            result['totalStorageSize'] = self.total_storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('health') is not None:
            self.health = m.get('health')

        if m.get('ilmPolicyName') is not None:
            self.ilm_policy_name = m.get('ilmPolicyName')

        if m.get('indexTemplateName') is not None:
            self.index_template_name = m.get('indexTemplateName')

        self.indices = []
        if m.get('indices') is not None:
            for k1 in m.get('indices'):
                temp_model = main_models.ListDataStreamsResponseBodyResultIndices()
                self.indices.append(temp_model.from_map(k1))

        if m.get('managedStorageSize') is not None:
            self.managed_storage_size = m.get('managedStorageSize')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('totalStorageSize') is not None:
            self.total_storage_size = m.get('totalStorageSize')

        return self

class ListDataStreamsResponseBodyResultIndices(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        health: str = None,
        is_managed: bool = None,
        managed_status: str = None,
        name: str = None,
        size: int = None,
    ):
        self.create_time = create_time
        self.health = health
        self.is_managed = is_managed
        self.managed_status = managed_status
        self.name = name
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

        if self.is_managed is not None:
            result['isManaged'] = self.is_managed

        if self.managed_status is not None:
            result['managedStatus'] = self.managed_status

        if self.name is not None:
            result['name'] = self.name

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('health') is not None:
            self.health = m.get('health')

        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')

        if m.get('managedStatus') is not None:
            self.managed_status = m.get('managedStatus')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

class ListDataStreamsResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_managed_count: int = None,
        x_managed_storage_size: int = None,
    ):
        self.x_managed_count = x_managed_count
        self.x_managed_storage_size = x_managed_storage_size

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Managed-Count') is not None:
            self.x_managed_count = m.get('X-Managed-Count')

        if m.get('X-Managed-StorageSize') is not None:
            self.x_managed_storage_size = m.get('X-Managed-StorageSize')

        return self

