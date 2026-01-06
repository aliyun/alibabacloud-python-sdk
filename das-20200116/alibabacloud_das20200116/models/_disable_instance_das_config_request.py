# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableInstanceDasConfigRequest(DaraModel):
    def __init__(
        self,
        engine: str = None,
        instance_id: str = None,
        scale_type: str = None,
    ):
        # The database engine. Set the value to Redis.
        # 
        # This parameter is required.
        self.engine = engine
        # The database instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of auto scaling. Valid values:
        # 
        # *   **specScale**: The specifications of a database instance are automatically scaled up or down.
        # *   **shardScale**: The number of shards for a database instance is automatically increased or decreased.
        # *   **bandwidthScale**: The bandwidth of a database instance is automatically increased or decreased.
        # 
        # This parameter is required.
        self.scale_type = scale_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')

        return self

