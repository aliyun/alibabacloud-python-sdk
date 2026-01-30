# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRenderingInstancesRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        rendering_instance_id: str = None,
        rendering_spec: str = None,
        start_time: str = None,
        storage_size: int = None,
    ):
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.rendering_instance_id = rendering_instance_id
        self.rendering_spec = rendering_spec
        self.start_time = start_time
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.rendering_spec is not None:
            result['RenderingSpec'] = self.rendering_spec

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('RenderingSpec') is not None:
            self.rendering_spec = m.get('RenderingSpec')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self

