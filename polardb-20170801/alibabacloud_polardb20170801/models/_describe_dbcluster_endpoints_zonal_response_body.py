# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterEndpointsZonalResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDBClusterEndpointsZonalResponseBodyItems] = None,
        request_id: str = None,
    ):
        # The details of the cluster endpoints.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDBClusterEndpointsZonalResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterEndpointsZonalResponseBodyItems(DaraModel):
    def __init__(
        self,
        address_items: List[main_models.DescribeDBClusterEndpointsZonalResponseBodyItemsAddressItems] = None,
        auto_add_new_nodes: str = None,
        dbcluster_id: str = None,
        dbendpoint_description: str = None,
        dbendpoint_id: str = None,
        endpoint_config: str = None,
        endpoint_type: str = None,
        node_with_roles: str = None,
        nodes: str = None,
        polar_scc_timeout_action: str = None,
        polar_scc_wait_timeout: str = None,
        read_write_mode: str = None,
        scc_mode: str = None,
    ):
        # The connection string information.
        self.address_items = address_items
        # Specifies whether new nodes are automatically added to the default cluster endpoint. Valid values:
        # 
        # - Enable.
        # 
        # - Disable.
        self.auto_add_new_nodes = auto_add_new_nodes
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The name of the endpoint.
        self.dbendpoint_description = dbendpoint_description
        # The endpoint ID.
        self.dbendpoint_id = dbendpoint_id
        # The advanced configurations of the cluster endpoint.
        # 
        # - **DistributedTransaction**: The status of transaction splitting. Valid values:
        # 
        #   - **on**: Transaction splitting is enabled.
        # 
        #   - **off**: Transaction splitting is disabled.
        # 
        # - **ConsistLevel**: The consistency level. Valid values:
        # 
        #   - **0**: Eventual consistency.
        # 
        #   - **1**: Session consistency.
        # 
        #   - **2**: Global consistency.
        # 
        # - **LoadBalanceStrategy**: The load balancing policy for automatic scheduling based on loads. The value is fixed as **load**.
        # 
        # - **MasterAcceptReads**: Specifies whether the primary node accepts read requests. Valid values:
        # 
        #   - **on**: The primary node accepts read requests.
        # 
        #   - **off**: The primary node does not accept read requests.
        self.endpoint_config = endpoint_config
        # The type of the cluster endpoint. Valid values:
        # 
        # - Cluster: the default cluster endpoint.
        # 
        # - Primary: the primary endpoint.
        # 
        # - Custom: a custom cluster endpoint.
        self.endpoint_type = endpoint_type
        # The role of each node in the endpoint. The primary node has the Writer role. Because multiple read-only nodes can be added to an endpoint, each read-only node is assigned a role name suffixed with a number, such as Reader1 and Reader2.
        self.node_with_roles = node_with_roles
        # The list of nodes that are configured for the endpoint.
        self.nodes = nodes
        # The policy for global consistency timeout. Valid values:
        # 
        # - 0: Sends the request to the primary node.
        # 
        # - 2: Degrades the request. If a global consistency read times out, the query is automatically degraded to a regular request. The client does not receive an error message.
        self.polar_scc_timeout_action = polar_scc_timeout_action
        # The timeout period for global consistency.
        self.polar_scc_wait_timeout = polar_scc_wait_timeout
        # The read/write mode. Valid values:
        # 
        # - ReadWrite: read and write (automatic read/write splitting).
        # 
        # - ReadOnly: read-only.
        self.read_write_mode = read_write_mode
        # Specifies whether global consistency (high-performance mode) is enabled for the node. Valid values:
        # 
        # - on: enabled.
        # 
        # - off: disabled.
        self.scc_mode = scc_mode

    def validate(self):
        if self.address_items:
            for v1 in self.address_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddressItems'] = []
        if self.address_items is not None:
            for k1 in self.address_items:
                result['AddressItems'].append(k1.to_map() if k1 else None)

        if self.auto_add_new_nodes is not None:
            result['AutoAddNewNodes'] = self.auto_add_new_nodes

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbendpoint_description is not None:
            result['DBEndpointDescription'] = self.dbendpoint_description

        if self.dbendpoint_id is not None:
            result['DBEndpointId'] = self.dbendpoint_id

        if self.endpoint_config is not None:
            result['EndpointConfig'] = self.endpoint_config

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.node_with_roles is not None:
            result['NodeWithRoles'] = self.node_with_roles

        if self.nodes is not None:
            result['Nodes'] = self.nodes

        if self.polar_scc_timeout_action is not None:
            result['PolarSccTimeoutAction'] = self.polar_scc_timeout_action

        if self.polar_scc_wait_timeout is not None:
            result['PolarSccWaitTimeout'] = self.polar_scc_wait_timeout

        if self.read_write_mode is not None:
            result['ReadWriteMode'] = self.read_write_mode

        if self.scc_mode is not None:
            result['SccMode'] = self.scc_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address_items = []
        if m.get('AddressItems') is not None:
            for k1 in m.get('AddressItems'):
                temp_model = main_models.DescribeDBClusterEndpointsZonalResponseBodyItemsAddressItems()
                self.address_items.append(temp_model.from_map(k1))

        if m.get('AutoAddNewNodes') is not None:
            self.auto_add_new_nodes = m.get('AutoAddNewNodes')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBEndpointDescription') is not None:
            self.dbendpoint_description = m.get('DBEndpointDescription')

        if m.get('DBEndpointId') is not None:
            self.dbendpoint_id = m.get('DBEndpointId')

        if m.get('EndpointConfig') is not None:
            self.endpoint_config = m.get('EndpointConfig')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('NodeWithRoles') is not None:
            self.node_with_roles = m.get('NodeWithRoles')

        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')

        if m.get('PolarSccTimeoutAction') is not None:
            self.polar_scc_timeout_action = m.get('PolarSccTimeoutAction')

        if m.get('PolarSccWaitTimeout') is not None:
            self.polar_scc_wait_timeout = m.get('PolarSccWaitTimeout')

        if m.get('ReadWriteMode') is not None:
            self.read_write_mode = m.get('ReadWriteMode')

        if m.get('SccMode') is not None:
            self.scc_mode = m.get('SccMode')

        return self

class DescribeDBClusterEndpointsZonalResponseBodyItemsAddressItems(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dashboard_used: bool = None,
        ipaddress: str = None,
        net_type: str = None,
        port: str = None,
        private_zone_connection_string: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        vpc_instance_id: str = None,
    ):
        # The connection string.
        self.connection_string = connection_string
        # Specifies whether the endpoint is the dashboard endpoint of a PolarDB search node. Valid values:
        # 
        # - True: Yes.
        # 
        # - False: No.
        self.dashboard_used = dashboard_used
        # The IP address.
        self.ipaddress = ipaddress
        # The network type. Valid values:
        # 
        # - Public: Internet.
        # 
        # - Private: internal network.
        self.net_type = net_type
        # The port number.
        self.port = port
        # The private domain name that is bound to the endpoint.
        self.private_zone_connection_string = private_zone_connection_string
        # The ID of the virtual private cloud (VPC).
        self.vpcid = vpcid
        # The virtual switch ID.
        self.v_switch_id = v_switch_id
        # The VPC instance ID.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dashboard_used is not None:
            result['DashboardUsed'] = self.dashboard_used

        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        if self.private_zone_connection_string is not None:
            result['PrivateZoneConnectionString'] = self.private_zone_connection_string

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DashboardUsed') is not None:
            self.dashboard_used = m.get('DashboardUsed')

        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrivateZoneConnectionString') is not None:
            self.private_zone_connection_string = m.get('PrivateZoneConnectionString')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

