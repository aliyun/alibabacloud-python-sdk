# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseVersionImage(DaraModel):
    def __init__(
        self,
        cpu_architecture: str = None,
        image_id: str = None,
        runtime_engine_type: str = None,
    ):
        self.cpu_architecture = cpu_architecture
        self.image_id = image_id
        self.runtime_engine_type = runtime_engine_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_architecture is not None:
            result['cpuArchitecture'] = self.cpu_architecture

        if self.image_id is not None:
            result['imageId'] = self.image_id

        if self.runtime_engine_type is not None:
            result['runtimeEngineType'] = self.runtime_engine_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuArchitecture') is not None:
            self.cpu_architecture = m.get('cpuArchitecture')

        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')

        if m.get('runtimeEngineType') is not None:
            self.runtime_engine_type = m.get('runtimeEngineType')

        return self

