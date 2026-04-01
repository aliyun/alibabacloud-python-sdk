# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class ModifyDBProxyInstanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbproxy_engine_type: str = None,
        dbproxy_instance_num: str = None,
        dbproxy_instance_type: str = None,
        dbproxy_nodes: List[main_models.ModifyDBProxyInstanceRequestDBProxyNodes] = None,
        effective_specific_time: str = None,
        effective_time: str = None,
        migrate_az: List[main_models.ModifyDBProxyInstanceRequestMigrateAZ] = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        v_switch_ids: str = None,
    ):
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # A deprecated parameter. You do not need to specify this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        # The number of database proxies. If you set this parameter to 0, the database proxy feature is disabled for the instance. Valid values: **1** to **16**.
        # 
        # >  The capability of the database proxy feature to process requests increases with the number of database proxies that are enabled. You can monitor the load on the instance and specify an appropriate number of database proxies based on the load monitoring data.
        # 
        # This parameter is required.
        self.dbproxy_instance_num = dbproxy_instance_num
        # The database proxy type. Valid values:
        # 
        # *   **common**: general-purpose database proxy
        # *   **exclusive** (default): dedicated database proxy
        # 
        # This parameter is required.
        self.dbproxy_instance_type = dbproxy_instance_type
        # List of proxy nodes.
        # 
        # > This parameter must be passed when the current proxy instance is deployed in multiple availability zones.
        self.dbproxy_nodes = dbproxy_nodes
        # The point in time that you want to specify. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # >  If the **EffectiveTime** parameter is set to **SpecificTime**, you must specify this parameter.
        self.effective_specific_time = effective_specific_time
        # The effective time. Valid values:
        # 
        # *   **Immediate**: The effective time is immediate.
        # *   **MaintainTime**: The effective time is within the maintenance window. For more information, see ModifyDBInstanceMaintainTime.
        # *   **SpecificTime**: The effective time is a specified point in time.
        # 
        # Default value: **MaintainTime**.
        self.effective_time = effective_time
        # The list of available zones for migration agents.
        # 
        # > Currently, only RDS MySQL cloud disk version agent instance migration is supported.
        self.migrate_az = migrate_az
        self.owner_id = owner_id
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the vSwitch in the destination zone. You can call the [DescribeVSwitches](https://help.aliyun.com/document_detail/610431.html) operation to query existing vSwitches.
        # 
        # >  Only database proxies for ApsaraDB RDS for MySQL instances that use cloud disks can be migrated to different zones.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.dbproxy_nodes:
            for v1 in self.dbproxy_nodes:
                 if v1:
                    v1.validate()
        if self.migrate_az:
            for v1 in self.migrate_az:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbproxy_engine_type is not None:
            result['DBProxyEngineType'] = self.dbproxy_engine_type

        if self.dbproxy_instance_num is not None:
            result['DBProxyInstanceNum'] = self.dbproxy_instance_num

        if self.dbproxy_instance_type is not None:
            result['DBProxyInstanceType'] = self.dbproxy_instance_type

        result['DBProxyNodes'] = []
        if self.dbproxy_nodes is not None:
            for k1 in self.dbproxy_nodes:
                result['DBProxyNodes'].append(k1.to_map() if k1 else None)

        if self.effective_specific_time is not None:
            result['EffectiveSpecificTime'] = self.effective_specific_time

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        result['MigrateAZ'] = []
        if self.migrate_az is not None:
            for k1 in self.migrate_az:
                result['MigrateAZ'].append(k1.to_map() if k1 else None)

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBProxyEngineType') is not None:
            self.dbproxy_engine_type = m.get('DBProxyEngineType')

        if m.get('DBProxyInstanceNum') is not None:
            self.dbproxy_instance_num = m.get('DBProxyInstanceNum')

        if m.get('DBProxyInstanceType') is not None:
            self.dbproxy_instance_type = m.get('DBProxyInstanceType')

        self.dbproxy_nodes = []
        if m.get('DBProxyNodes') is not None:
            for k1 in m.get('DBProxyNodes'):
                temp_model = main_models.ModifyDBProxyInstanceRequestDBProxyNodes()
                self.dbproxy_nodes.append(temp_model.from_map(k1))

        if m.get('EffectiveSpecificTime') is not None:
            self.effective_specific_time = m.get('EffectiveSpecificTime')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        self.migrate_az = []
        if m.get('MigrateAZ') is not None:
            for k1 in m.get('MigrateAZ'):
                temp_model = main_models.ModifyDBProxyInstanceRequestMigrateAZ()
                self.migrate_az.append(temp_model.from_map(k1))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

class ModifyDBProxyInstanceRequestMigrateAZ(DaraModel):
    def __init__(
        self,
        db_proxy_endpoint_id: str = None,
        dest_vswitch_id: str = None,
        dest_vpc_id: str = None,
    ):
        # The proxy connection address ID. You can obtain it through the DescribeDBProxyEndpoint interface.
        # 
        # > This parameter is required when MigrateAZ is selected.
        self.db_proxy_endpoint_id = db_proxy_endpoint_id
        # The target VSwitchId corresponding to the proxy instance migration.
        # 
        # > This parameter is required when MigrateAZ is selected.
        self.dest_vswitch_id = dest_vswitch_id
        # The target vpc id corresponding to the proxy instance migration.
        self.dest_vpc_id = dest_vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_proxy_endpoint_id is not None:
            result['dbProxyEndpointId'] = self.db_proxy_endpoint_id

        if self.dest_vswitch_id is not None:
            result['destVSwitchId'] = self.dest_vswitch_id

        if self.dest_vpc_id is not None:
            result['destVpcId'] = self.dest_vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dbProxyEndpointId') is not None:
            self.db_proxy_endpoint_id = m.get('dbProxyEndpointId')

        if m.get('destVSwitchId') is not None:
            self.dest_vswitch_id = m.get('destVSwitchId')

        if m.get('destVpcId') is not None:
            self.dest_vpc_id = m.get('destVpcId')

        return self

class ModifyDBProxyInstanceRequestDBProxyNodes(DaraModel):
    def __init__(
        self,
        cpu_cores: str = None,
        node_counts: str = None,
        zone_id: str = None,
    ):
        # The number of cpu cores for the node, valid values: **1** to **16**.
        # >This parameter is required when selecting **DBProxyNodes**.
        self.cpu_cores = cpu_cores
        # The number of proxy nodes in the availability zone, valid values: **1** to **16**.
        # >This parameter is required when selecting **DBProxyNodes**.
        self.node_counts = node_counts
        # The id of the availability zone where the node is located.
        # >This parameter is required when selecting **DBProxyNodes**.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_cores is not None:
            result['cpuCores'] = self.cpu_cores

        if self.node_counts is not None:
            result['nodeCounts'] = self.node_counts

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCores') is not None:
            self.cpu_cores = m.get('cpuCores')

        if m.get('nodeCounts') is not None:
            self.node_counts = m.get('nodeCounts')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

