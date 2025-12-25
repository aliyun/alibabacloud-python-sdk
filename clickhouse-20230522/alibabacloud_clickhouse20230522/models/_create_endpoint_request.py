# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEndpointRequest(DaraModel):
    def __init__(
        self,
        computing_group_id: str = None,
        connection_prefix: str = None,
        dbinstance_id: str = None,
        dbinstance_net_type: str = None,
        region_id: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The prefix of the new endpoint. The prefix of the ConnectionString parameter.
        self.connection_prefix = connection_prefix
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The network type.
        # 
        # Valid values:
        # 
        # *   Public
        self.dbinstance_net_type = dbinstance_net_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id

        if self.connection_prefix is not None:
            result['ConnectionPrefix'] = self.connection_prefix

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')

        if m.get('ConnectionPrefix') is not None:
            self.connection_prefix = m.get('ConnectionPrefix')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

