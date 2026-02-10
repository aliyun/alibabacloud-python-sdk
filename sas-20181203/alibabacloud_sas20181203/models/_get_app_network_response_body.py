# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetAppNetworkResponseBody(DaraModel):
    def __init__(
        self,
        app_network: main_models.GetAppNetworkResponseBodyAppNetwork = None,
        request_id: str = None,
    ):
        # The information about the application network topology.
        self.app_network = app_network
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.app_network:
            self.app_network.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_network is not None:
            result['AppNetwork'] = self.app_network.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppNetwork') is not None:
            temp_model = main_models.GetAppNetworkResponseBodyAppNetwork()
            self.app_network = temp_model.from_map(m.get('AppNetwork'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAppNetworkResponseBodyAppNetwork(DaraModel):
    def __init__(
        self,
        edge: List[main_models.GetAppNetworkResponseBodyAppNetworkEdge] = None,
        namespace: List[main_models.GetAppNetworkResponseBodyAppNetworkNamespace] = None,
        node: List[main_models.GetAppNetworkResponseBodyAppNetworkNode] = None,
    ):
        # The information about the topology edge.
        self.edge = edge
        # The namespace.
        self.namespace = namespace
        # The information about the application node.
        self.node = node

    def validate(self):
        if self.edge:
            for v1 in self.edge:
                 if v1:
                    v1.validate()
        if self.namespace:
            for v1 in self.namespace:
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

        result['Namespace'] = []
        if self.namespace is not None:
            for k1 in self.namespace:
                result['Namespace'].append(k1.to_map() if k1 else None)

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
                temp_model = main_models.GetAppNetworkResponseBodyAppNetworkEdge()
                self.edge.append(temp_model.from_map(k1))

        self.namespace = []
        if m.get('Namespace') is not None:
            for k1 in m.get('Namespace'):
                temp_model = main_models.GetAppNetworkResponseBodyAppNetworkNamespace()
                self.namespace.append(temp_model.from_map(k1))

        self.node = []
        if m.get('Node') is not None:
            for k1 in m.get('Node'):
                temp_model = main_models.GetAppNetworkResponseBodyAppNetworkNode()
                self.node.append(temp_model.from_map(k1))

        return self

class GetAppNetworkResponseBodyAppNetworkNode(DaraModel):
    def __init__(
        self,
        container_ids: List[str] = None,
        id: str = None,
        name: str = None,
        namespace_id: str = None,
        risk_level: str = None,
        type: str = None,
    ):
        # The list of the container IDs.
        self.container_ids = container_ids
        # The ID of the node.
        self.id = id
        # The name of the node.
        self.name = name
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The risk level. Valid values:
        # 
        # *   **3**: high
        # *   **2**: medium
        # *   **1**: low
        # *   **0**: warning
        # *   **-1**: unknown
        self.risk_level = risk_level
        # The type of the node. Valid values:
        # 
        # *   **app**: an application
        # *   **internet**: a network node in another cluster
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_ids is not None:
            result['ContainerIds'] = self.container_ids

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerIds') is not None:
            self.container_ids = m.get('ContainerIds')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetAppNetworkResponseBodyAppNetworkNamespace(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The ID of the namespace.
        self.id = id
        # The name of the custom namespace.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetAppNetworkResponseBodyAppNetworkEdge(DaraModel):
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
        # *   **app**: an application
        # *   **internet**: a network node in another cluster
        self.dst_node_type = dst_node_type
        # The ID of the edge.
        self.id = id
        # The number of the destination port.
        self.port = port
        # The ID of the source node.
        self.src_node_id = src_node_id
        # The type of the source node. Valid values:
        # 
        # *   **app**: an application
        # *   **internet**: a network node in another cluster
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

