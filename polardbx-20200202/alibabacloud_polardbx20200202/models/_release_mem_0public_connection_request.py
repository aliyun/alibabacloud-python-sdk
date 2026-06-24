# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseMem0PublicConnectionRequest(DaraModel):
    def __init__(
        self,
        current_connection_string: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        # The public endpoint to be released. This parameter is optional. If this parameter is not specified, the public endpoint of Mem0 is automatically released.
        self.current_connection_string = current_connection_string
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The region ID of the instance. > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196841.html) operation to query the details of regions supported by PolarDB-X, including region IDs.
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
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

