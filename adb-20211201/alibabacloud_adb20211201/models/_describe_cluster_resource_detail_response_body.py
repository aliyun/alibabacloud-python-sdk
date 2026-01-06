# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterResourceDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeClusterResourceDetailResponseBodyData = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The queried resource usage.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeClusterResourceDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClusterResourceDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        compute_resource: str = None,
        dbcluster_id: str = None,
        free_compute_resource: str = None,
        resource_group_list: List[main_models.DescribeClusterResourceDetailResponseBodyDataResourceGroupList] = None,
        storage_resource: str = None,
    ):
        # The amount of reserved computing resources. Unit: AnalyticDB compute units (ACUs). Valid values: 0 to 4096. The value must be in increments of 16 ACUs. Each ACU is equivalent to 1 core and 4 GB memory.
        self.compute_resource = compute_resource
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The amount of idle reserved computing resources. Unit: ACUs. Valid values: 0 to 4096. The value must be in increments of 16 ACUs. Each ACU is equivalent to 1 core and 4 GB memory.
        self.free_compute_resource = free_compute_resource
        # The resource groups.
        self.resource_group_list = resource_group_list
        # The amount of reserved storage resources. Unit: ACUs. Valid values: 0 to 2064. The value must be in increments of 24 ACUs. Each ACU is equivalent to 1 core and 4 GB memory.
        self.storage_resource = storage_resource

    def validate(self):
        if self.resource_group_list:
            for v1 in self.resource_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.free_compute_resource is not None:
            result['FreeComputeResource'] = self.free_compute_resource

        result['ResourceGroupList'] = []
        if self.resource_group_list is not None:
            for k1 in self.resource_group_list:
                result['ResourceGroupList'].append(k1.to_map() if k1 else None)

        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FreeComputeResource') is not None:
            self.free_compute_resource = m.get('FreeComputeResource')

        self.resource_group_list = []
        if m.get('ResourceGroupList') is not None:
            for k1 in m.get('ResourceGroupList'):
                temp_model = main_models.DescribeClusterResourceDetailResponseBodyDataResourceGroupList()
                self.resource_group_list.append(temp_model.from_map(k1))

        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')

        return self

class DescribeClusterResourceDetailResponseBodyDataResourceGroupList(DaraModel):
    def __init__(
        self,
        cluster_mode: str = None,
        cluster_size_resource: str = None,
        enable_spot: bool = None,
        max_cluster_count: int = None,
        max_compute_resource: str = None,
        min_cluster_count: int = None,
        min_compute_resource: str = None,
        pool_id: int = None,
        pool_name: str = None,
        pool_type: str = None,
        pool_users: str = None,
        running_cluster_count: int = None,
        status: str = None,
    ):
        # A reserved parameter.
        # 
        # This parameter is required.
        self.cluster_mode = cluster_mode
        # A reserved parameter.
        self.cluster_size_resource = cluster_size_resource
        # Indicates whether the preemptible instance feature is enabled for the resource group. After the preemptible instance feature is enabled, you are charged for resources at a lower unit price but the resources are probably released. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # The True value is returned only for job resource groups.
        self.enable_spot = enable_spot
        # A reserved parameter.
        self.max_cluster_count = max_cluster_count
        # The maximum amount of reserved computing resources.
        self.max_compute_resource = max_compute_resource
        # A reserved parameter.
        self.min_cluster_count = min_cluster_count
        # The minimum amount of reserved computing resources.
        self.min_compute_resource = min_compute_resource
        # The resource group ID.
        self.pool_id = pool_id
        # The name of the resource group.
        self.pool_name = pool_name
        # The type of the resource group.
        self.pool_type = pool_type
        # The user of the resource group.
        self.pool_users = pool_users
        # A reserved parameter.
        self.running_cluster_count = running_cluster_count
        # The status of the resource group. Valid values:
        # 
        # *   **running**
        # *   **deleting**
        # *   **scaling**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode

        if self.cluster_size_resource is not None:
            result['ClusterSizeResource'] = self.cluster_size_resource

        if self.enable_spot is not None:
            result['EnableSpot'] = self.enable_spot

        if self.max_cluster_count is not None:
            result['MaxClusterCount'] = self.max_cluster_count

        if self.max_compute_resource is not None:
            result['MaxComputeResource'] = self.max_compute_resource

        if self.min_cluster_count is not None:
            result['MinClusterCount'] = self.min_cluster_count

        if self.min_compute_resource is not None:
            result['MinComputeResource'] = self.min_compute_resource

        if self.pool_id is not None:
            result['PoolId'] = self.pool_id

        if self.pool_name is not None:
            result['PoolName'] = self.pool_name

        if self.pool_type is not None:
            result['PoolType'] = self.pool_type

        if self.pool_users is not None:
            result['PoolUsers'] = self.pool_users

        if self.running_cluster_count is not None:
            result['RunningClusterCount'] = self.running_cluster_count

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')

        if m.get('ClusterSizeResource') is not None:
            self.cluster_size_resource = m.get('ClusterSizeResource')

        if m.get('EnableSpot') is not None:
            self.enable_spot = m.get('EnableSpot')

        if m.get('MaxClusterCount') is not None:
            self.max_cluster_count = m.get('MaxClusterCount')

        if m.get('MaxComputeResource') is not None:
            self.max_compute_resource = m.get('MaxComputeResource')

        if m.get('MinClusterCount') is not None:
            self.min_cluster_count = m.get('MinClusterCount')

        if m.get('MinComputeResource') is not None:
            self.min_compute_resource = m.get('MinComputeResource')

        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')

        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')

        if m.get('PoolType') is not None:
            self.pool_type = m.get('PoolType')

        if m.get('PoolUsers') is not None:
            self.pool_users = m.get('PoolUsers')

        if m.get('RunningClusterCount') is not None:
            self.running_cluster_count = m.get('RunningClusterCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

