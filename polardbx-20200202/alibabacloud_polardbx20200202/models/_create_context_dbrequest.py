# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateContextDBRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        open_search_instance_name: str = None,
        region_id: str = None,
    ):
        # The name of the instance.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The name of the PolarDB-X Search instance.
        # 
        # This parameter is required.
        self.open_search_instance_name = open_search_instance_name
        # The ID of the region where the instance resides. > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196841.html) operation to query the regions supported by PolarDB-X, including region IDs.
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

        if self.open_search_instance_name is not None:
            result['OpenSearchInstanceName'] = self.open_search_instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('OpenSearchInstanceName') is not None:
            self.open_search_instance_name = m.get('OpenSearchInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

