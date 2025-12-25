# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCClusterNodesResponseBody(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeRCClusterNodesResponseBodyNodes] = None,
        page: main_models.DescribeRCClusterNodesResponseBodyPage = None,
        request_id: str = None,
    ):
        # The details of the nodes.
        self.nodes = nodes
        # The pagination information.
        self.page = page
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeRCClusterNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            temp_model = main_models.DescribeRCClusterNodesResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRCClusterNodesResponseBodyPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The maximum number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRCClusterNodesResponseBodyNodes(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        docker_version: str = None,
        image_id: str = None,
        instance_id: str = None,
        instance_role: str = None,
        ip_addresses: List[str] = None,
        is_aliyun_node: bool = None,
        node_name: str = None,
        node_pool_id: str = None,
        node_status: str = None,
        runtime_version: str = None,
        state: str = None,
    ):
        # The time when the node was created.
        self.creation_time = creation_time
        # The container version.
        self.docker_version = docker_version
        # The image ID of the node.
        self.image_id = image_id
        # The node ID.
        self.instance_id = instance_id
        # The node role. Valid values:
        # 
        # *   **Master**: master node
        # *   **Worker**: worker node
        self.instance_role = instance_role
        # The IP address.
        self.ip_addresses = ip_addresses
        # Indicates whether the node is provided by Alibaba Cloud. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_aliyun_node = is_aliyun_node
        # The node name, which is the identifier of the RDS Custom node in the cluster.
        self.node_name = node_name
        # The node pool ID.
        self.node_pool_id = node_pool_id
        # Indicates whether the node is ready. Valid values:
        # 
        # *   **Ready**: The node is ready.
        # *   **NotReady**: The node is not ready.
        # *   **Unknown**: The status of the node is unknown.
        # *   **Offline**: The node is offline.
        self.node_status = node_status
        # The runtime of the ACK cluster.
        self.runtime_version = runtime_version
        # The node status. Valid values:
        # 
        # *   **pending**
        # *   **running**
        # *   **starting**
        # *   **stopping**
        # *   **stopped**
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.docker_version is not None:
            result['DockerVersion'] = self.docker_version

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_role is not None:
            result['InstanceRole'] = self.instance_role

        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses

        if self.is_aliyun_node is not None:
            result['IsAliyunNode'] = self.is_aliyun_node

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id

        if self.node_status is not None:
            result['NodeStatus'] = self.node_status

        if self.runtime_version is not None:
            result['RuntimeVersion'] = self.runtime_version

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DockerVersion') is not None:
            self.docker_version = m.get('DockerVersion')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceRole') is not None:
            self.instance_role = m.get('InstanceRole')

        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')

        if m.get('IsAliyunNode') is not None:
            self.is_aliyun_node = m.get('IsAliyunNode')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')

        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')

        if m.get('RuntimeVersion') is not None:
            self.runtime_version = m.get('RuntimeVersion')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

