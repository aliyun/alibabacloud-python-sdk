# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateDBResourceGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cluster_mode: str = None,
        cluster_size_resource: str = None,
        dbcluster_id: str = None,
        engine: str = None,
        engine_params: Dict[str, Any] = None,
        group_name: str = None,
        group_type: str = None,
        max_cluster_count: int = None,
        max_compute_resource: str = None,
        min_cluster_count: int = None,
        min_compute_resource: str = None,
        node_num: int = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.client_token = client_token
        # The working mode of the resource group. Valid values:
        # 
        # *   **Disable** (default)
        # *   **AutoScale**
        self.cluster_mode = cluster_mode
        # The resource specifications of a single compute cluster. Unit: ACU.
        self.cluster_size_resource = cluster_size_resource
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the cluster IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a specific region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The engine of the resource group. Valid values:
        # 
        # *   **AnalyticDB** (default)
        # *   **SparkWarehouse**
        self.engine = engine
        # The Spark application configuration parameters that can be applied to all Spark jobs executed in the resource group. If you want to configure parameters for a specific Spark job, you can specify values for the parameters in the code editor when you submit the job.
        self.engine_params = engine_params
        # The name of the resource group.
        # 
        # *   The name can be up to 255 characters in length.
        # *   The name must start with an uppercase letter or a digit.
        # *   The name can contain uppercase letters, digits, hyphens (-), and underscores (_).
        # 
        # This parameter is required.
        self.group_name = group_name
        # The query execution mode. Valid values:
        # 
        # *   **interactive** (default)
        # *   **batch**
        # *   **job**
        self.group_type = group_type
        # The maximum number of compute clusters that are allowed in the resource group. Maximum value: 10.
        self.max_cluster_count = max_cluster_count
        # The maximum amount of reserved computing resources, which refers to the amount of resources that are not allocated in the cluster. Unit: ACU.
        # 
        # *   When GroupType is set to interactive, set this parameter to a value in increments of 16ACU.
        # *   When GroupType is set to job, set this parameter to a value in increments of 8ACU.
        self.max_compute_resource = max_compute_resource
        # The minimum number of compute clusters that are required in the resource group. Minimum value: 1.
        self.min_cluster_count = min_cluster_count
        # The minimum amount of reserved computing resources. Unit: AnalyticDB compute unit (ACU).
        # 
        # *   When GroupType is set to interactive, set this parameter to 16ACU.
        # *   When GroupType is set to job, set this parameter to 0ACU.
        self.min_compute_resource = min_compute_resource
        # The number of nodes. Default value: 0.
        # 
        # *   Each node is configured with the resources of 16 cores and 64 GB memory.
        # *   Make sure that the amount of resources of the nodes (Number of nodes × 16 cores and 64 GB memory) is less than or equal to the amount of unused resources of the cluster.
        self.node_num = node_num
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode

        if self.cluster_size_resource is not None:
            result['ClusterSizeResource'] = self.cluster_size_resource

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_params is not None:
            result['EngineParams'] = self.engine_params

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.max_cluster_count is not None:
            result['MaxClusterCount'] = self.max_cluster_count

        if self.max_compute_resource is not None:
            result['MaxComputeResource'] = self.max_compute_resource

        if self.min_cluster_count is not None:
            result['MinClusterCount'] = self.min_cluster_count

        if self.min_compute_resource is not None:
            result['MinComputeResource'] = self.min_compute_resource

        if self.node_num is not None:
            result['NodeNum'] = self.node_num

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')

        if m.get('ClusterSizeResource') is not None:
            self.cluster_size_resource = m.get('ClusterSizeResource')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineParams') is not None:
            self.engine_params = m.get('EngineParams')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('MaxClusterCount') is not None:
            self.max_cluster_count = m.get('MaxClusterCount')

        if m.get('MaxComputeResource') is not None:
            self.max_compute_resource = m.get('MaxComputeResource')

        if m.get('MinClusterCount') is not None:
            self.min_cluster_count = m.get('MinClusterCount')

        if m.get('MinComputeResource') is not None:
            self.min_compute_resource = m.get('MinComputeResource')

        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

