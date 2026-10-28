# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePxfsRequest(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        dbinstance_name: str = None,
        node_count: int = None,
        region_id: str = None,
        security_iplist: str = None,
        storage_size: int = None,
    ):
        # The node specifications.
        self.class_code = class_code
        # The PolarDB-X instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The number of nodes.
        self.node_count = node_count
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IP whitelist.
        self.security_iplist = security_iplist
        # The storage capacity.
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self

