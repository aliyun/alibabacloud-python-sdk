# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyOpenSearchAccessProtocolRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        protocol: str = None,
        region_id: str = None,
    ):
        # The instance name.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The access protocol. Valid values:
        # 
        # - **http**: HTTP protocol.
        # - **https**: HTTPS protocol.
        # 
        # This parameter is required.
        self.protocol = protocol
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
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

