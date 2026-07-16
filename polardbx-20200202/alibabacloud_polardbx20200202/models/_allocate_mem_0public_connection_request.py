# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateMem0PublicConnectionRequest(DaraModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        dbinstance_name: str = None,
        port: str = None,
        region_id: str = None,
    ):
        # The prefix of the public network connection string.
        # 
        # This parameter is required.
        self.connection_string_prefix = connection_string_prefix
        # The name of the instance.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The port number.
        # 
        # This parameter is required.
        self.port = port
        # The region in which the instance resides.
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
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

