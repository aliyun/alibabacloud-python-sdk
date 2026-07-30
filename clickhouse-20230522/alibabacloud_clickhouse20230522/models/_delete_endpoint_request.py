# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEndpointRequest(DaraModel):
    def __init__(
        self,
        computing_group_id: str = None,
        connection_string: str = None,
        dbinstance_id: str = None,
        dbinstance_net_type: str = None,
        region_id: str = None,
    ):
        # The ID of the computing group.
        self.computing_group_id = computing_group_id
        # The connection string of the public endpoint to delete.
        self.connection_string = connection_string
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The network type of the endpoint. Valid values:
        # 
        # - VPC: a virtual private cloud (VPC) network.
        # 
        # - Public: a public network.
        self.dbinstance_net_type = dbinstance_net_type
        # The ID of the region.
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

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

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

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

