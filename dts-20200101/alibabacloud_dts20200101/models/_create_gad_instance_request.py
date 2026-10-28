# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGadInstanceRequest(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        instance_type: str = None,
        master_db_engine_type: str = None,
        master_db_instance_id: str = None,
        master_db_instance_region: str = None,
        master_db_zone_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The name of the group. The name must be globally unique.
        self.instance_name = instance_name
        # The instance type. Valid values: DR (disaster recovery) and GAD (active geo-redundancy).
        self.instance_type = instance_type
        # The database engine. Valid values: MySQL, SQL Server, and PostgreSQL.
        self.master_db_engine_type = master_db_engine_type
        # The ID of the primary ApsaraDB RDS instance.
        self.master_db_instance_id = master_db_instance_id
        # The region of the primary instance.
        self.master_db_instance_region = master_db_instance_region
        # The zone of the primary instance.
        self.master_db_zone_id = master_db_zone_id
        self.owner_id = owner_id
        # The region of the primary instance.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.master_db_engine_type is not None:
            result['MasterDbEngineType'] = self.master_db_engine_type

        if self.master_db_instance_id is not None:
            result['MasterDbInstanceId'] = self.master_db_instance_id

        if self.master_db_instance_region is not None:
            result['MasterDbInstanceRegion'] = self.master_db_instance_region

        if self.master_db_zone_id is not None:
            result['MasterDbZoneId'] = self.master_db_zone_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MasterDbEngineType') is not None:
            self.master_db_engine_type = m.get('MasterDbEngineType')

        if m.get('MasterDbInstanceId') is not None:
            self.master_db_instance_id = m.get('MasterDbInstanceId')

        if m.get('MasterDbInstanceRegion') is not None:
            self.master_db_instance_region = m.get('MasterDbInstanceRegion')

        if m.get('MasterDbZoneId') is not None:
            self.master_db_zone_id = m.get('MasterDbZoneId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

