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
        self.nodes = nodes
        self.page = page
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
        self.page_number = page_number
        self.page_size = page_size
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
        nodepool_id: str = None,
        pay_type: str = None,
        state: str = None,
    ):
        self.cluster_id = cluster_id
        self.ens_region_id = ens_region_id
        self.image_id = image_id
        self.instance_id = instance_id
        self.ip_address = ip_address
        self.nodepool_id = nodepool_id
        self.pay_type = pay_type
        self.state = state

    def validate(self):
        pass

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

        if m.get('NodepoolId') is not None:
            self.nodepool_id = m.get('NodepoolId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

