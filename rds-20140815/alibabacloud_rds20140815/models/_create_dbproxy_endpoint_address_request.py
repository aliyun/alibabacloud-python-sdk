# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBProxyEndpointAddressRequest(DaraModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        dbinstance_id: str = None,
        dbproxy_connect_string_net_type: str = None,
        dbproxy_endpoint_id: str = None,
        dbproxy_engine_type: str = None,
        dbproxy_new_connect_string_port: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # The prefix of the proxy endpoint Enter a custom prefix.
        # 
        # This parameter is required.
        self.connection_string_prefix = connection_string_prefix
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The network type of the proxy endpoint. Valid values:
        # 
        # *   **Public**: Internet
        # *   **VPC**: Virtual Private Cloud (VPC)
        # *   **Classic**: classic network
        # 
        # Default value: **Classic**
        # 
        # This parameter is required.
        self.dbproxy_connect_string_net_type = dbproxy_connect_string_net_type
        # The proxy endpoint ID. You can call the DescribeDBProxyEndpoint operation to query the proxy endpoint ID.
        # 
        # This parameter is required.
        self.dbproxy_endpoint_id = dbproxy_endpoint_id
        # A reserved parameter. You do not need to specify this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        # The port number that is associated with the proxy endpoint.
        # 
        # *   If the instance runs MySQL, the default value is **3306**.
        # *   If the instance runs PostgreSQL, the default value is **5432**.
        self.dbproxy_new_connect_string_port = dbproxy_new_connect_string_port
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the VPC to which the proxy endpoint belongs. You can call the DescribeDBInstanceAttribute operation to query the information.
        # 
        # >  This parameter must be specified when **DBProxyConnectStringNetType** is set to **VPC**.
        self.vpcid = vpcid
        # The ID of the vSwitch that is associated with the specified VPC. You can call the DescribeDBInstanceAttribute operation to query the vSwitch ID.
        # 
        # >  This parameter must be specified when **DBProxyConnectStringNetType** is set to **VPC**.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbproxy_connect_string_net_type is not None:
            result['DBProxyConnectStringNetType'] = self.dbproxy_connect_string_net_type

        if self.dbproxy_endpoint_id is not None:
            result['DBProxyEndpointId'] = self.dbproxy_endpoint_id

        if self.dbproxy_engine_type is not None:
            result['DBProxyEngineType'] = self.dbproxy_engine_type

        if self.dbproxy_new_connect_string_port is not None:
            result['DBProxyNewConnectStringPort'] = self.dbproxy_new_connect_string_port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBProxyConnectStringNetType') is not None:
            self.dbproxy_connect_string_net_type = m.get('DBProxyConnectStringNetType')

        if m.get('DBProxyEndpointId') is not None:
            self.dbproxy_endpoint_id = m.get('DBProxyEndpointId')

        if m.get('DBProxyEngineType') is not None:
            self.dbproxy_engine_type = m.get('DBProxyEngineType')

        if m.get('DBProxyNewConnectStringPort') is not None:
            self.dbproxy_new_connect_string_port = m.get('DBProxyNewConnectStringPort')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

