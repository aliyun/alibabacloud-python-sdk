# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterNetworkResponseBody(DaraModel):
    def __init__(
        self,
        cluster_network: main_models.DescribeClusterNetworkResponseBodyClusterNetwork = None,
        request_id: str = None,
    ):
        # Information about the network topology edge in the cluster.
        self.cluster_network = cluster_network
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.cluster_network:
            self.cluster_network.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_network is not None:
            result['ClusterNetwork'] = self.cluster_network.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterNetwork') is not None:
            temp_model = main_models.DescribeClusterNetworkResponseBodyClusterNetwork()
            self.cluster_network = temp_model.from_map(m.get('ClusterNetwork'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClusterNetworkResponseBodyClusterNetwork(DaraModel):
    def __init__(
        self,
        edge: List[main_models.DescribeClusterNetworkResponseBodyClusterNetworkEdge] = None,
        node: List[main_models.DescribeClusterNetworkResponseBodyClusterNetworkNode] = None,
    ):
        # An array that consists of information about the topology edge.
        self.edge = edge
        # An array that consists of information about the node.
        self.node = node

    def validate(self):
        if self.edge:
            for v1 in self.edge:
                 if v1:
                    v1.validate()
        if self.node:
            for v1 in self.node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Edge'] = []
        if self.edge is not None:
            for k1 in self.edge:
                result['Edge'].append(k1.to_map() if k1 else None)

        result['Node'] = []
        if self.node is not None:
            for k1 in self.node:
                result['Node'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edge = []
        if m.get('Edge') is not None:
            for k1 in m.get('Edge'):
                temp_model = main_models.DescribeClusterNetworkResponseBodyClusterNetworkEdge()
                self.edge.append(temp_model.from_map(k1))

        self.node = []
        if m.get('Node') is not None:
            for k1 in m.get('Node'):
                temp_model = main_models.DescribeClusterNetworkResponseBodyClusterNetworkNode()
                self.node.append(temp_model.from_map(k1))

        return self

class DescribeClusterNetworkResponseBodyClusterNetworkNode(DaraModel):
    def __init__(
        self,
        cnnf_switch: int = None,
        id: str = None,
        interception_type: int = None,
        name: str = None,
        net_topo_switch: str = None,
        risk_level: str = None,
        type: str = None,
    ):
        # The status of the microsegmentation switch. Valid values:
        # 
        # *   **0**: off.
        # *   **1**: on.
        self.cnnf_switch = cnnf_switch
        # The ID of the node.
        self.id = id
        # The network type. Valid values:
        # 
        # *   **0**: classic network.
        # *   **1**: virtual private cloud (VPC).
        self.interception_type = interception_type
        # The name of the node.
        self.name = name
        # The status of the network topology switch. Valid values:
        # 
        # *   **ON**
        # *   **OFF**
        self.net_topo_switch = net_topo_switch
        # The risk level. Valid values:
        # 
        # *   **3**: high.
        # *   **2**: medium.
        # *   **1**: low.
        # *   **0**: secure.
        # *   **-1**: unknown.
        self.risk_level = risk_level
        # The type of the node. Valid values:
        # 
        # *   **cluster**: a cluster.
        # *   **internet**: a network node outside the cluster.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cnnf_switch is not None:
            result['CnnfSwitch'] = self.cnnf_switch

        if self.id is not None:
            result['Id'] = self.id

        if self.interception_type is not None:
            result['InterceptionType'] = self.interception_type

        if self.name is not None:
            result['Name'] = self.name

        if self.net_topo_switch is not None:
            result['NetTopoSwitch'] = self.net_topo_switch

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnnfSwitch') is not None:
            self.cnnf_switch = m.get('CnnfSwitch')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InterceptionType') is not None:
            self.interception_type = m.get('InterceptionType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetTopoSwitch') is not None:
            self.net_topo_switch = m.get('NetTopoSwitch')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeClusterNetworkResponseBodyClusterNetworkEdge(DaraModel):
    def __init__(
        self,
        dst_node_id: str = None,
        dst_node_type: str = None,
        id: str = None,
        port: str = None,
        src_node_id: str = None,
        src_node_type: str = None,
    ):
        # The ID of the destination node.
        self.dst_node_id = dst_node_id
        # The type of the destination node. Valid values:
        # 
        # *   Set the value to **cluster**.
        self.dst_node_type = dst_node_type
        # The ID of the topology edge.
        self.id = id
        # The port number of the topology edge.
        self.port = port
        # The ID of the source node.
        self.src_node_id = src_node_id
        # The type of the source node. Valid values:
        # 
        # *   **cluster**: a cluster.
        # *   **internet**: a network node outside the cluster
        self.src_node_type = src_node_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_node_id is not None:
            result['DstNodeId'] = self.dst_node_id

        if self.dst_node_type is not None:
            result['DstNodeType'] = self.dst_node_type

        if self.id is not None:
            result['Id'] = self.id

        if self.port is not None:
            result['Port'] = self.port

        if self.src_node_id is not None:
            result['SrcNodeId'] = self.src_node_id

        if self.src_node_type is not None:
            result['SrcNodeType'] = self.src_node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstNodeId') is not None:
            self.dst_node_id = m.get('DstNodeId')

        if m.get('DstNodeType') is not None:
            self.dst_node_type = m.get('DstNodeType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SrcNodeId') is not None:
            self.src_node_id = m.get('SrcNodeId')

        if m.get('SrcNodeType') is not None:
            self.src_node_type = m.get('SrcNodeType')

        return self

