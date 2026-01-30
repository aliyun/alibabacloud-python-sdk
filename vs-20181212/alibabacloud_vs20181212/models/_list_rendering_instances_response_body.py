# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListRenderingInstancesResponseBody(DaraModel):
    def __init__(
        self,
        rendering_instances: List[main_models.ListRenderingInstancesResponseBodyRenderingInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.rendering_instances = rendering_instances
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.rendering_instances:
            for v1 in self.rendering_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RenderingInstances'] = []
        if self.rendering_instances is not None:
            for k1 in self.rendering_instances:
                result['RenderingInstances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rendering_instances = []
        if m.get('RenderingInstances') is not None:
            for k1 in m.get('RenderingInstances'):
                temp_model = main_models.ListRenderingInstancesResponseBodyRenderingInstances()
                self.rendering_instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRenderingInstancesResponseBodyRenderingInstances(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        rendering_instance_id: str = None,
        rendering_spec: str = None,
        storage_size: int = None,
    ):
        self.creation_time = creation_time
        self.rendering_instance_id = rendering_instance_id
        self.rendering_spec = rendering_spec
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.rendering_spec is not None:
            result['RenderingSpec'] = self.rendering_spec

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('RenderingSpec') is not None:
            self.rendering_spec = m.get('RenderingSpec')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self

