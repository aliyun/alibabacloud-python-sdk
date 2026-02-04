# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGadInstancesRequest(DaraModel):
    def __init__(
        self,
        db_engine_types: str = None,
        instance_name: str = None,
        master_db_instance_id: str = None,
        owner_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        slave_db_instance_id: str = None,
    ):
        self.db_engine_types = db_engine_types
        self.instance_name = instance_name
        self.master_db_instance_id = master_db_instance_id
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.slave_db_instance_id = slave_db_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_engine_types is not None:
            result['DbEngineTypes'] = self.db_engine_types

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.master_db_instance_id is not None:
            result['MasterDbInstanceId'] = self.master_db_instance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.slave_db_instance_id is not None:
            result['SlaveDbInstanceId'] = self.slave_db_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbEngineTypes') is not None:
            self.db_engine_types = m.get('DbEngineTypes')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MasterDbInstanceId') is not None:
            self.master_db_instance_id = m.get('MasterDbInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SlaveDbInstanceId') is not None:
            self.slave_db_instance_id = m.get('SlaveDbInstanceId')

        return self

