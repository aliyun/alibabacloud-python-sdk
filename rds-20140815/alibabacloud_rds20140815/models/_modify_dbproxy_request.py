# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class ModifyDBProxyRequest(DaraModel):
    def __init__(
        self,
        config_dbproxy_service: str = None,
        dbinstance_id: str = None,
        dbproxy_engine_type: str = None,
        dbproxy_instance_num: str = None,
        dbproxy_instance_type: str = None,
        dbproxy_nodes: List[main_models.ModifyDBProxyRequestDBProxyNodes] = None,
        instance_network_type: str = None,
        owner_id: int = None,
        persistent_connection_status: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # Specifies whether to enable or disable the database proxy feature. Valid values:
        # 
        # *   **Startup**: enables the feature.
        # *   **Shutdown**: disables the feature.
        # *   **Modify**: modifies the configuration of the feature.
        # 
        # This parameter is required.
        self.config_dbproxy_service = config_dbproxy_service
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # A deprecated parameter. You do not need to specify this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        # The number of proxy instances that are enabled. Valid values: **1** to **16**. Default value: **1**.
        # 
        # >  The capability of the database proxy to process requests increases with the number of proxy instances that are enabled. You can monitor the load on the instance and specify an appropriate number of proxy instances based on the load monitoring data.
        self.dbproxy_instance_num = dbproxy_instance_num
        # The database proxy type. Valid values:
        # 
        # *   **common**: general-purpose database proxy
        # *   **exclusive** (default): dedicated database proxy
        self.dbproxy_instance_type = dbproxy_instance_type
        # The proxy nodes.
        self.dbproxy_nodes = dbproxy_nodes
        # The network type of the instance. Only the VPC network type is supported. Set the value to **VPC**.
        # 
        # >  If you enable the database proxy feature for the instance, you must specify this parameter.
        self.instance_network_type = instance_network_type
        self.owner_id = owner_id
        # Specifies whether to enable persistent connections. Valid values:
        # 
        # *   **Enabled**
        # *   **Disabled**
        # 
        # > 
        # 
        # *   This parameter is available only for instances that run MySQL.
        # 
        # *   If you want to modify persistent connections, you must set the **ConfigDBProxyService** parameter to **Modify**.
        self.persistent_connection_status = persistent_connection_status
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the virtual private cloud (VPC) to which the instance belongs. You can call the DescribeDBInstanceAttribute operation to query the ID.
        # 
        # >  If you enable the database proxy feature for the instance, you must specify this parameter.
        self.vpcid = vpcid
        # The ID of the vSwitch to which the instance belongs. You can call the DescribeDBInstanceAttribute operation to query the ID.
        # 
        # >  If you enable the database proxy feature for the instance, you must specify this parameter.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.dbproxy_nodes:
            for v1 in self.dbproxy_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_dbproxy_service is not None:
            result['ConfigDBProxyService'] = self.config_dbproxy_service

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

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.persistent_connection_status is not None:
            result['PersistentConnectionStatus'] = self.persistent_connection_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigDBProxyService') is not None:
            self.config_dbproxy_service = m.get('ConfigDBProxyService')

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
                temp_model = main_models.ModifyDBProxyRequestDBProxyNodes()
                self.dbproxy_nodes.append(temp_model.from_map(k1))

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PersistentConnectionStatus') is not None:
            self.persistent_connection_status = m.get('PersistentConnectionStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class ModifyDBProxyRequestDBProxyNodes(DaraModel):
    def __init__(
        self,
        cpu_cores: str = None,
        node_counts: str = None,
        zone_id: str = None,
    ):
        # The number of CPU cores of the node. Valid values: **1** to **16**.
        # 
        # >  This parameter is required when you configure the **DBProxyNodes** parameter.
        self.cpu_cores = cpu_cores
        # The number of proxy nodes in the zone. Valid values: **1** and **2**.
        # 
        # >  This parameter is required when you configure the **DBProxyNodes** parameter.
        self.node_counts = node_counts
        # The ID of the zone in which the node resides.
        # 
        # >  This parameter is required when you configure the **DBProxyNodes** parameter.
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

