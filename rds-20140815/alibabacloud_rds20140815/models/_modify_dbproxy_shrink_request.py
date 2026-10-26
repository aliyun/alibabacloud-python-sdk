# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBProxyShrinkRequest(DaraModel):
    def __init__(
        self,
        config_dbproxy_service: str = None,
        dbinstance_id: str = None,
        dbproxy_engine_type: str = None,
        dbproxy_instance_num: str = None,
        dbproxy_instance_type: str = None,
        dbproxy_nodes_shrink: str = None,
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
        # Specifies whether to enable or disable the database proxy. Valid values:
        # 
        # * **Startup**: Enables the proxy service.
        # * **Shutdown**: Disables the proxy service.
        # * **Modify**: Modifies the proxy service.
        # 
        # This parameter is required.
        self.config_dbproxy_service = config_dbproxy_service
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # **[Deprecated]** This parameter is deprecated and does not need to be configured.
        self.dbproxy_engine_type = dbproxy_engine_type
        # The number of proxy instances to enable. Valid values: **1** to **16**. Default value: **1**.
        # 
        # > More proxy instances can process more requests. You can check the load of proxy instances based on monitoring data and specify an appropriate number of proxy instances.
        self.dbproxy_instance_num = dbproxy_instance_num
        # The type of the database proxy instance. Valid values:
        # - **common**: General-purpose database proxy.
        # - **exclusive**: Dedicated proxy (default).
        self.dbproxy_instance_type = dbproxy_instance_type
        # The list of proxy nodes.
        self.dbproxy_nodes_shrink = dbproxy_nodes_shrink
        # The network type of the instance. Only VPC is supported. Valid value: **VPC**.
        # 
        # > This parameter is required when you enable the database proxy.
        self.instance_network_type = instance_network_type
        self.owner_id = owner_id
        # Specifies whether to enable connection keep-alive. Valid values:
        # - **Enabled**: Enables connection keep-alive.
        # - **Disabled**: Disables connection keep-alive.
        # 
        # > - Only ApsaraDB RDS for MySQL supports this parameter.
        # > - When you modify the connection keep-alive status, set **ConfigDBProxyService** to **Modify**.
        self.persistent_connection_status = persistent_connection_status
        # The region ID. You can call the DescribeRegions operation to query the region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the VPC to which the instance belongs. You can call the DescribeDBInstanceAttribute operation to query the VPC ID.
        # 
        # > This parameter is required when you enable the database proxy.
        self.vpcid = vpcid
        # The ID of the vSwitch to which the instance belongs. You can call the DescribeDBInstanceAttribute operation to query the vSwitch ID.
        # 
        # > This parameter is required when you enable the database proxy.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

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

        if self.dbproxy_nodes_shrink is not None:
            result['DBProxyNodes'] = self.dbproxy_nodes_shrink

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

        if m.get('DBProxyNodes') is not None:
            self.dbproxy_nodes_shrink = m.get('DBProxyNodes')

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

