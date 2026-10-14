# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterNodesResponseBody(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeClusterNodesResponseBodyNodes] = None,
        page: main_models.DescribeClusterNodesResponseBodyPage = None,
        request_id: str = None,
    ):
        # The node information.
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
                temp_model = main_models.DescribeClusterNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            temp_model = main_models.DescribeClusterNodesResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClusterNodesResponseBodyPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
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

class DescribeClusterNodesResponseBodyNodes(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        ens_region_id: str = None,
        image_id: str = None,
        instance_id: str = None,
        ip_address: List[str] = None,
        node_info: main_models.DescribeClusterNodesResponseBodyNodesNodeInfo = None,
        nodepool_id: str = None,
        pay_type: str = None,
        state: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The ENS edge zone ID.
        self.ens_region_id = ens_region_id
        # The instance image ID.
        self.image_id = image_id
        # The instance ID.
        self.instance_id = instance_id
        # The IP address of the ENS instance.
        self.ip_address = ip_address
        # The node information.
        self.node_info = node_info
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # The billing method. Valid values:
        # - PostPaid: pay-as-you-go.
        self.pay_type = pay_type
        # The status of the node pool. Valid values:
        # - initial: The node pool is being created.
        # - running: The node pool is created.
        # - removing: The node pool is being removed.
        self.state = state

    def validate(self):
        if self.node_info:
            self.node_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.node_info is not None:
            result['NodeInfo'] = self.node_info.to_map()

        if self.nodepool_id is not None:
            result['NodepoolId'] = self.nodepool_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('NodeInfo') is not None:
            temp_model = main_models.DescribeClusterNodesResponseBodyNodesNodeInfo()
            self.node_info = temp_model.from_map(m.get('NodeInfo'))

        if m.get('NodepoolId') is not None:
            self.nodepool_id = m.get('NodepoolId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class DescribeClusterNodesResponseBodyNodesNodeInfo(DaraModel):
    def __init__(
        self,
        container_runtime_version: str = None,
        kubelet_version: str = None,
        os_image: str = None,
    ):
        # The container runtime version.
        self.container_runtime_version = container_runtime_version
        # The kubelet version of the node.
        self.kubelet_version = kubelet_version
        # The operating system image of the node.
        self.os_image = os_image

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_runtime_version is not None:
            result['ContainerRuntimeVersion'] = self.container_runtime_version

        if self.kubelet_version is not None:
            result['KubeletVersion'] = self.kubelet_version

        if self.os_image is not None:
            result['OsImage'] = self.os_image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerRuntimeVersion') is not None:
            self.container_runtime_version = m.get('ContainerRuntimeVersion')

        if m.get('KubeletVersion') is not None:
            self.kubelet_version = m.get('KubeletVersion')

        if m.get('OsImage') is not None:
            self.os_image = m.get('OsImage')

        return self

