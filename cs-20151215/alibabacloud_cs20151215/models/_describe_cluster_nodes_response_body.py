# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterNodesResponseBody(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeClusterNodesResponseBodyNodes] = None,
        page: main_models.DescribeClusterNodesResponseBodyPage = None,
    ):
        # The details of the nodes in the cluster.
        self.nodes = nodes
        # The pagination information.
        self.page = page

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
        result['nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['nodes'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['page'] = self.page.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('nodes') is not None:
            for k1 in m.get('nodes'):
                temp_model = main_models.DescribeClusterNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('page') is not None:
            temp_model = main_models.DescribeClusterNodesResponseBodyPage()
            self.page = temp_model.from_map(m.get('page'))

        return self

class DescribeClusterNodesResponseBodyPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
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
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.total_count is not None:
            result['total_count'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')

        return self

class DescribeClusterNodesResponseBodyNodes(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        error_message: str = None,
        expired_time: str = None,
        host_name: str = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_role: str = None,
        instance_status: str = None,
        instance_type: str = None,
        instance_type_family: str = None,
        ip_address: List[str] = None,
        is_aliyun_node: bool = None,
        node_name: str = None,
        node_status: str = None,
        nodepool_id: str = None,
        source: str = None,
        spot_strategy: str = None,
        state: str = None,
    ):
        # The time when the node was created.
        self.creation_time = creation_time
        # The error message generated when the node was created.
        self.error_message = error_message
        # The expiration date of the node.
        self.expired_time = expired_time
        # The name of the host.
        self.host_name = host_name
        # The ID of the system image that is used by the node.
        self.image_id = image_id
        # The billing method of the node. Valid values:
        # 
        # *   `PrePaid`: the subscription billing method. If the value is PrePaid, make sure that you have a sufficient balance or credit in your account. Otherwise, an `InvalidPayMethod` error is returned.
        # *   `PostPaid`: the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instance on which the node is deployed.
        self.instance_name = instance_name
        # The role of the node. Valid values:
        # 
        # *   Master: master node
        # *   Worker: worker node
        self.instance_role = instance_role
        # The status of the node.
        self.instance_status = instance_status
        # The type of the node.
        self.instance_type = instance_type
        # The ECS instance family of the node.
        self.instance_type_family = instance_type_family
        # The IP address of the node.
        self.ip_address = ip_address
        # Indicates whether the instance on which the node is deployed is provided by Alibaba Cloud. Valid values:
        # 
        # *   `true`: The instance is provided by Alibaba Cloud.
        # *   `false`: The instance is not provided by Alibaba Cloud.
        self.is_aliyun_node = is_aliyun_node
        # The name of the node. This name is the identifier of the node in the cluster.
        self.node_name = node_name
        # Indicates whether the node is ready. Valid values:
        # 
        # *   `Ready`: The node is ready.
        # *   `NotReady`: The node is not ready.
        # *   `Unknown`: The status of the node is unknown.
        # *   `Offline`: The node is offline.
        self.node_status = node_status
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # Indicates how the node is initialized. A node can be manually created or created by using Resource Orchestration Service (ROS).
        self.source = source
        # The type of preemptible instance. Valid values:
        # 
        # *   NoSpot: a non-preemptible instance.
        # *   SpotWithPriceLimit: a preemptible instance that is configured with the highest bid price.
        # *   SpotAsPriceGo: a preemptible instance for which the system automatically bids based on the current market price.
        self.spot_strategy = spot_strategy
        # The status of the node. Valid values:
        # 
        # *   `pending`: The node is being created.
        # *   `running`: The node is running.
        # *   `starting`: The node is being started.
        # *   `stopping`: The node is being stopped.
        # *   `stopped`: The node is stopped.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['creation_time'] = self.creation_time

        if self.error_message is not None:
            result['error_message'] = self.error_message

        if self.expired_time is not None:
            result['expired_time'] = self.expired_time

        if self.host_name is not None:
            result['host_name'] = self.host_name

        if self.image_id is not None:
            result['image_id'] = self.image_id

        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type

        if self.instance_id is not None:
            result['instance_id'] = self.instance_id

        if self.instance_name is not None:
            result['instance_name'] = self.instance_name

        if self.instance_role is not None:
            result['instance_role'] = self.instance_role

        if self.instance_status is not None:
            result['instance_status'] = self.instance_status

        if self.instance_type is not None:
            result['instance_type'] = self.instance_type

        if self.instance_type_family is not None:
            result['instance_type_family'] = self.instance_type_family

        if self.ip_address is not None:
            result['ip_address'] = self.ip_address

        if self.is_aliyun_node is not None:
            result['is_aliyun_node'] = self.is_aliyun_node

        if self.node_name is not None:
            result['node_name'] = self.node_name

        if self.node_status is not None:
            result['node_status'] = self.node_status

        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id

        if self.source is not None:
            result['source'] = self.source

        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creation_time') is not None:
            self.creation_time = m.get('creation_time')

        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')

        if m.get('expired_time') is not None:
            self.expired_time = m.get('expired_time')

        if m.get('host_name') is not None:
            self.host_name = m.get('host_name')

        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')

        if m.get('instance_charge_type') is not None:
            self.instance_charge_type = m.get('instance_charge_type')

        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')

        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')

        if m.get('instance_role') is not None:
            self.instance_role = m.get('instance_role')

        if m.get('instance_status') is not None:
            self.instance_status = m.get('instance_status')

        if m.get('instance_type') is not None:
            self.instance_type = m.get('instance_type')

        if m.get('instance_type_family') is not None:
            self.instance_type_family = m.get('instance_type_family')

        if m.get('ip_address') is not None:
            self.ip_address = m.get('ip_address')

        if m.get('is_aliyun_node') is not None:
            self.is_aliyun_node = m.get('is_aliyun_node')

        if m.get('node_name') is not None:
            self.node_name = m.get('node_name')

        if m.get('node_status') is not None:
            self.node_status = m.get('node_status')

        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('spot_strategy') is not None:
            self.spot_strategy = m.get('spot_strategy')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

