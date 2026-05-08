# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeDBResourceGroupResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        groups_info: List[main_models.DescribeDBResourceGroupResponseBodyGroupsInfo] = None,
        request_id: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The queried resource group.
        self.groups_info = groups_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.groups_info:
            for v1 in self.groups_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['GroupsInfo'] = []
        if self.groups_info is not None:
            for k1 in self.groups_info:
                result['GroupsInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.groups_info = []
        if m.get('GroupsInfo') is not None:
            for k1 in m.get('GroupsInfo'):
                temp_model = main_models.DescribeDBResourceGroupResponseBodyGroupsInfo()
                self.groups_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBResourceGroupResponseBodyGroupsInfo(DaraModel):
    def __init__(
        self,
        cluster_mode: str = None,
        cluster_size_resource: str = None,
        connection_string: str = None,
        create_time: str = None,
        elastic_min_compute_resource: str = None,
        engine: str = None,
        engine_params: Dict[str, Any] = None,
        group_name: str = None,
        group_type: str = None,
        group_user_list: List[str] = None,
        group_users: str = None,
        max_cluster_count: int = None,
        max_compute_resource: str = None,
        min_cluster_count: int = None,
        min_compute_resource: str = None,
        node_num: int = None,
        port: str = None,
        running_cluster_count: int = None,
        status: str = None,
        update_time: str = None,
    ):
        # The working mode of the resource group. Valid values:
        # 
        # *   **Disable** (default)
        # *   **AutoScale**
        self.cluster_mode = cluster_mode
        # The resource specifications of a single compute cluster. Unit: ACU.
        self.cluster_size_resource = cluster_size_resource
        # The endpoint of the resource group.
        # 
        # >  This parameter is returned only when the value of Engine is SparkWarehouse.
        self.connection_string = connection_string
        # The time when the resource group was created.
        self.create_time = create_time
        # The minimum amount of elastic computing resources. Unit: ACU.
        self.elastic_min_compute_resource = elastic_min_compute_resource
        # The engine of the resource group. Valid values:
        # 
        # *   **AnalyticDB** (default)
        # *   **SparkWarehouse**
        self.engine = engine
        # The Spark application configuration parameters that can be applied to all Spark jobs executed in the resource group. If you want to configure parameters for a specific Spark job, you can specify values for the parameters in the code editor when you submit the job.
        self.engine_params = engine_params
        # The name of the resource group.
        self.group_name = group_name
        # The query execution mode. Valid values:
        # 
        # *   **interactive** (default)
        # *   **batch**
        # *   **job**
        self.group_type = group_type
        # The database accounts that are associated with the resource group.
        self.group_user_list = group_user_list
        # The database accounts that are associated with the resource group. Multiple database accounts are separated by commas (,).
        self.group_users = group_users
        # The maximum number of compute clusters that are allowed in the resource group. Maximum value: 10.
        self.max_cluster_count = max_cluster_count
        # The maximum amount of reserved computing resources, which refers to the amount of resources that are not allocated in the cluster. Unit: ACU.
        # 
        # *   If the value of GroupType is **interactive**, the amount of reserved computing resources that are not allocated in the cluster is returned in increments of 16ACU.
        # *   If the value of GroupType is **job**, the amount of reserved computing resources that are not allocated in the cluster is returned in increments of 8ACU.
        self.max_compute_resource = max_compute_resource
        # The minimum number of compute clusters that are required in the resource group. Minimum value: 1.
        self.min_cluster_count = min_cluster_count
        # The minimum amount of reserved computing resources. Unit: AnalyticDB compute unit (ACU).
        # 
        # *   If the value of GroupType is **interactive**, 16ACU is returned.
        # *   If the value of GroupType is **job**, 0ACU is returned.
        self.min_compute_resource = min_compute_resource
        # The number of nodes. Each node provides 16 cores and 64 GB memory.
        self.node_num = node_num
        # The port number of the resource group.
        # 
        # >  This parameter is returned only when the value of Engine is SparkWarehouse.
        self.port = port
        # The number of compute clusters running in the resource group.
        self.running_cluster_count = running_cluster_count
        # The status of the resource group. Valid values:
        # 
        # *   **Pending**
        # *   **Running**
        # *   **Scaling**
        # *   **Deleting**
        # *   **Deleted**
        self.status = status
        # The time when the resource group was updated.
        self.update_time = update_time

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

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.elastic_min_compute_resource is not None:
            result['ElasticMinComputeResource'] = self.elastic_min_compute_resource

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_params is not None:
            result['EngineParams'] = self.engine_params

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.group_user_list is not None:
            result['GroupUserList'] = self.group_user_list

        if self.group_users is not None:
            result['GroupUsers'] = self.group_users

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

        if self.port is not None:
            result['Port'] = self.port

        if self.running_cluster_count is not None:
            result['RunningClusterCount'] = self.running_cluster_count

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')

        if m.get('ClusterSizeResource') is not None:
            self.cluster_size_resource = m.get('ClusterSizeResource')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ElasticMinComputeResource') is not None:
            self.elastic_min_compute_resource = m.get('ElasticMinComputeResource')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineParams') is not None:
            self.engine_params = m.get('EngineParams')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('GroupUserList') is not None:
            self.group_user_list = m.get('GroupUserList')

        if m.get('GroupUsers') is not None:
            self.group_users = m.get('GroupUsers')

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

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RunningClusterCount') is not None:
            self.running_cluster_count = m.get('RunningClusterCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

