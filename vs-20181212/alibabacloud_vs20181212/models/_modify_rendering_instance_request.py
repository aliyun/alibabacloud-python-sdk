# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRenderingInstanceRequest(DaraModel):
    def __init__(
        self,
        rendering_instance_id: str = None,
        rendering_spec: str = None,
        storage_size: str = None,
    ):
        # This parameter is required.
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
        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.rendering_spec is not None:
            result['RenderingSpec'] = self.rendering_spec

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('RenderingSpec') is not None:
            self.rendering_spec = m.get('RenderingSpec')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self

