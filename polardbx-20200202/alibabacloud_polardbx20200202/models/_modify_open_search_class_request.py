# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyOpenSearchClassRequest(DaraModel):
    def __init__(
        self,
        dbinstance_disk_size: int = None,
        dbinstance_name: str = None,
        region_id: str = None,
        search_class_code: str = None,
    ):
        # The target disk size per node, in GB. If not specified, the current disk size is retained.
        self.dbinstance_disk_size = dbinstance_disk_size
        # The name of the instance.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The node specifications code of the PolarDB-X Search data node. This parameter is required. Active node specifications depend on the region and sales configuration, and must differ from the current node specifications.
        self.search_class_code = search_class_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_disk_size is not None:
            result['DBInstanceDiskSize'] = self.dbinstance_disk_size

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_class_code is not None:
            result['SearchClassCode'] = self.search_class_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceDiskSize') is not None:
            self.dbinstance_disk_size = m.get('DBInstanceDiskSize')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchClassCode') is not None:
            self.search_class_code = m.get('SearchClassCode')

        return self

