# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterNodePoolsResponseBody(DaraModel):
    def __init__(
        self,
        node_pools: List[main_models.DescribeClusterNodePoolsResponseBodyNodePools] = None,
        page: main_models.DescribeClusterNodePoolsResponseBodyPage = None,
        request_id: str = None,
    ):
        self.node_pools = node_pools
        self.page = page
        self.request_id = request_id

    def validate(self):
        if self.node_pools:
            for v1 in self.node_pools:
                 if v1:
                    v1.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodePools'] = []
        if self.node_pools is not None:
            for k1 in self.node_pools:
                result['NodePools'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_pools = []
        if m.get('NodePools') is not None:
            for k1 in m.get('NodePools'):
                temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodePools()
                self.node_pools.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClusterNodePoolsResponseBodyPage(DaraModel):
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

class DescribeClusterNodePoolsResponseBodyNodePools(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        kubernetes_config: main_models.DescribeClusterNodePoolsResponseBodyNodePoolsKubernetesConfig = None,
        nodepool_info: main_models.DescribeClusterNodePoolsResponseBodyNodePoolsNodepoolInfo = None,
        scaling_group: main_models.DescribeClusterNodePoolsResponseBodyNodePoolsScalingGroup = None,
        status: main_models.DescribeClusterNodePoolsResponseBodyNodePoolsStatus = None,
    ):
        self.cluster_id = cluster_id
        self.kubernetes_config = kubernetes_config
        self.nodepool_info = nodepool_info
        self.scaling_group = scaling_group
        self.status = status

    def validate(self):
        if self.kubernetes_config:
            self.kubernetes_config.validate()
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.kubernetes_config is not None:
            result['KubernetesConfig'] = self.kubernetes_config.to_map()

        if self.nodepool_info is not None:
            result['NodepoolInfo'] = self.nodepool_info.to_map()

        if self.scaling_group is not None:
            result['ScalingGroup'] = self.scaling_group.to_map()

        if self.status is not None:
            result['Status'] = self.status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('KubernetesConfig') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodePoolsKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m.get('KubernetesConfig'))

        if m.get('NodepoolInfo') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodePoolsNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m.get('NodepoolInfo'))

        if m.get('ScalingGroup') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodePoolsScalingGroup()
            self.scaling_group = temp_model.from_map(m.get('ScalingGroup'))

        if m.get('Status') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodePoolsStatus()
            self.status = temp_model.from_map(m.get('Status'))

        return self

class DescribeClusterNodePoolsResponseBodyNodePoolsStatus(DaraModel):
    def __init__(
        self,
        desired_nodes: int = None,
        initial_nodes: int = None,
        removing_nodes: int = None,
        serving_nodes: int = None,
        state: str = None,
        total_nodes: int = None,
    ):
        self.desired_nodes = desired_nodes
        self.initial_nodes = initial_nodes
        self.removing_nodes = removing_nodes
        self.serving_nodes = serving_nodes
        self.state = state
        self.total_nodes = total_nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desired_nodes is not None:
            result['DesiredNodes'] = self.desired_nodes

        if self.initial_nodes is not None:
            result['InitialNodes'] = self.initial_nodes

        if self.removing_nodes is not None:
            result['RemovingNodes'] = self.removing_nodes

        if self.serving_nodes is not None:
            result['ServingNodes'] = self.serving_nodes

        if self.state is not None:
            result['State'] = self.state

        if self.total_nodes is not None:
            result['TotalNodes'] = self.total_nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesiredNodes') is not None:
            self.desired_nodes = m.get('DesiredNodes')

        if m.get('InitialNodes') is not None:
            self.initial_nodes = m.get('InitialNodes')

        if m.get('RemovingNodes') is not None:
            self.removing_nodes = m.get('RemovingNodes')

        if m.get('ServingNodes') is not None:
            self.serving_nodes = m.get('ServingNodes')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TotalNodes') is not None:
            self.total_nodes = m.get('TotalNodes')

        return self

class DescribeClusterNodePoolsResponseBodyNodePoolsScalingGroup(DaraModel):
    def __init__(
        self,
        data_disks: List[main_models.DescribeClusterNodePoolsResponseBodyNodePoolsScalingGroupDataDisks] = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_types: List[str] = None,
        key_pair_name: str = None,
        password: str = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
        vswitch_ids: List[str] = None,
    ):
        self.data_disks = data_disks
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_types = instance_types
        self.key_pair_name = key_pair_name
        self.password = password
        self.system_disk_category = system_disk_category
        self.system_disk_size = system_disk_size
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.data_disks:
            for v1 in self.data_disks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k1 in self.data_disks:
                result['DataDisks'].append(k1.to_map() if k1 else None)

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.password is not None:
            result['Password'] = self.password

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        if self.vswitch_ids is not None:
            result['VswitchIds'] = self.vswitch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k1 in m.get('DataDisks'):
                temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodePoolsScalingGroupDataDisks()
                self.data_disks.append(temp_model.from_map(k1))

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('VswitchIds') is not None:
            self.vswitch_ids = m.get('VswitchIds')

        return self

class DescribeClusterNodePoolsResponseBodyNodePoolsScalingGroupDataDisks(DaraModel):
    def __init__(
        self,
        category: str = None,
        size: int = None,
    ):
        self.category = category
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class DescribeClusterNodePoolsResponseBodyNodePoolsNodepoolInfo(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        name: str = None,
        nodepool_id: str = None,
    ):
        self.ens_region_id = ens_region_id
        self.name = name
        self.nodepool_id = nodepool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.name is not None:
            result['Name'] = self.name

        if self.nodepool_id is not None:
            result['NodepoolId'] = self.nodepool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodepoolId') is not None:
            self.nodepool_id = m.get('NodepoolId')

        return self

class DescribeClusterNodePoolsResponseBodyNodePoolsKubernetesConfig(DaraModel):
    def __init__(
        self,
        pre_user_data: str = None,
        user_data: str = None,
    ):
        self.pre_user_data = pre_user_data
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pre_user_data is not None:
            result['PreUserData'] = self.pre_user_data

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreUserData') is not None:
            self.pre_user_data = m.get('PreUserData')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

