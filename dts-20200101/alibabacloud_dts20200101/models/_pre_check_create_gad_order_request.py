# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PreCheckCreateGadOrderRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        master_database_name: str = None,
        master_engine_arch_type: str = None,
        master_shard_account_name: str = None,
        master_shard_account_password: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        slave_database_name: str = None,
        slave_db_instance_id: str = None,
        slave_db_instance_region: str = None,
        slave_engine_arch_type: str = None,
    ):
        self.instance_id = instance_id
        self.master_database_name = master_database_name
        self.master_engine_arch_type = master_engine_arch_type
        self.master_shard_account_name = master_shard_account_name
        self.master_shard_account_password = master_shard_account_password
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.slave_database_name = slave_database_name
        self.slave_db_instance_id = slave_db_instance_id
        self.slave_db_instance_region = slave_db_instance_region
        self.slave_engine_arch_type = slave_engine_arch_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.master_database_name is not None:
            result['MasterDatabaseName'] = self.master_database_name

        if self.master_engine_arch_type is not None:
            result['MasterEngineArchType'] = self.master_engine_arch_type

        if self.master_shard_account_name is not None:
            result['MasterShardAccountName'] = self.master_shard_account_name

        if self.master_shard_account_password is not None:
            result['MasterShardAccountPassword'] = self.master_shard_account_password

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.slave_database_name is not None:
            result['SlaveDatabaseName'] = self.slave_database_name

        if self.slave_db_instance_id is not None:
            result['SlaveDbInstanceId'] = self.slave_db_instance_id

        if self.slave_db_instance_region is not None:
            result['SlaveDbInstanceRegion'] = self.slave_db_instance_region

        if self.slave_engine_arch_type is not None:
            result['SlaveEngineArchType'] = self.slave_engine_arch_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MasterDatabaseName') is not None:
            self.master_database_name = m.get('MasterDatabaseName')

        if m.get('MasterEngineArchType') is not None:
            self.master_engine_arch_type = m.get('MasterEngineArchType')

        if m.get('MasterShardAccountName') is not None:
            self.master_shard_account_name = m.get('MasterShardAccountName')

        if m.get('MasterShardAccountPassword') is not None:
            self.master_shard_account_password = m.get('MasterShardAccountPassword')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SlaveDatabaseName') is not None:
            self.slave_database_name = m.get('SlaveDatabaseName')

        if m.get('SlaveDbInstanceId') is not None:
            self.slave_db_instance_id = m.get('SlaveDbInstanceId')

        if m.get('SlaveDbInstanceRegion') is not None:
            self.slave_db_instance_region = m.get('SlaveDbInstanceRegion')

        if m.get('SlaveEngineArchType') is not None:
            self.slave_engine_arch_type = m.get('SlaveEngineArchType')

        return self

