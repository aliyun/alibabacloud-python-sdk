# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ObserveGroupPromInstance(DaraModel):
    def __init__(
        self,
        id: str = None,
        kind: str = None,
        region: str = None,
        time: str = None,
    ):
        # The ID of the Managed Service for Prometheus instance, such as rw-xxxxxxxxxx.
        self.id = id
        # The source of the instance. Valid values:
        # - system: The system automatically identifies the instance based on the workspace or UModel.
        # - custom: The user manually selects the instance in the console.
        self.kind = kind
        # The region where the Managed Service for Prometheus instance resides. If this parameter is left empty, the backend automatically populates the region based on the workspace to which the application group belongs.
        self.region = region
        # The time when the record was written or selected. Format: yyyy-MM-dd HH:mm:ss.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.kind is not None:
            result['kind'] = self.kind

        if self.region is not None:
            result['region'] = self.region

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

