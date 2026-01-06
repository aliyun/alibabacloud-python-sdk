# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckCreateDBInstanceRequest(DaraModel):
    def __init__(
        self,
        cache_size: int = None,
        charge_type: str = None,
        client_token: str = None,
        connection_string: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        engine: str = None,
        engine_version: str = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
        security_iplist: str = None,
        used_time: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.cache_size = cache_size
        # This parameter is required.
        self.charge_type = charge_type
        self.client_token = client_token
        self.connection_string = connection_string
        # The specifications of the instance. Valid values:
        # 
        # *   **selectdb.xlarge**: 4 CPU cores and 32 GB of memory.
        # *   **selectdb.2xlarge**: 8 CPU cores and 64 GB of memory.
        # *   **selectdb.4xlarge**: 16 CPU cores and 128 GB of memory.
        # *   **selectdb.8xlarge**: 32 CPU cores and 256 GB of memory.
        # *   **selectdb.16xlarge**: 64 CPU cores and 512 GB of memory.
        # *   **selectdb.24xlarge**: 96 CPU cores and 768 GB of memory.
        # *   **selectdb.32xlarge**: 128 CPU cores and 1,024 GB of memory.
        # 
        # This parameter is required.
        self.dbinstance_class = dbinstance_class
        self.dbinstance_description = dbinstance_description
        # The database engine of the instance.
        self.engine = engine
        # The version of the database engine.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        self.period = period
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        self.security_iplist = security_iplist
        # The subscription duration of the instance. Valid values:
        # 
        # *   If Period is set to Year, valid values of UsedTime are 1, 2, 3, 4, and 5.
        # *   If Period is set to Month, valid values of UsedTime are 1 to 12.
        # 
        # >  This parameter takes effect and is required only if ChargeType is set to Prepaid.
        self.used_time = used_time
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # VPC ID。
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

