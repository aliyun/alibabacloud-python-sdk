# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class CreateDBResourceGroupRequest(DaraModel):
    def __init__(
        self,
        atm_config: main_models.CreateDBResourceGroupRequestAtmConfig = None,
        auto_stop_interval: str = None,
        classification: str = None,
        cluster_mode: str = None,
        cluster_size_resource: str = None,
        dbcluster_id: str = None,
        enable_spot: bool = None,
        engine: str = None,
        engine_params: Dict[str, Any] = None,
        gpu_elastic_plan: main_models.CreateDBResourceGroupRequestGpuElasticPlan = None,
        group_name: str = None,
        group_type: str = None,
        max_cluster_count: int = None,
        max_compute_resource: str = None,
        max_gpu_quantity: int = None,
        min_cluster_count: int = None,
        min_compute_resource: str = None,
        min_gpu_quantity: int = None,
        ray_config: main_models.CreateDBResourceGroupRequestRayConfig = None,
        region_id: str = None,
        rules: List[main_models.CreateDBResourceGroupRequestRules] = None,
        scale_policy: str = None,
        spec_name: str = None,
        target_resource_group_name: str = None,
    ):
        self.atm_config = atm_config
        # The automatic stop interval. Unit: minutes (m).
        self.auto_stop_interval = auto_stop_interval
        # The classification of the resource group. Valid values:
        # - SQL
        # - SparkSQL
        # - MultiCluster
        # - AI
        self.classification = classification
        # A reserved parameter (not applicable).
        self.cluster_mode = cluster_mode
        # A reserved parameter (not applicable).
        self.cluster_size_resource = cluster_size_resource
        # The ID of the Dedicated Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable the spot instance feature for the resource group. After the spot instance feature is enabled, the unit price of resources is reduced, but the resources may be released. Only Job resource groups support this feature. Valid values:
        # - **True**: enables the spot instance feature.
        # - **False**: disables the spot instance feature.
        self.enable_spot = enable_spot
        # The database engine. Valid values:
        # 
        # - **AnalyticDB** (default): the AnalyticDB for MySQL engine.
        # - **SparkWarehouse**: the SparkWarehouse engine.
        self.engine = engine
        # The engine configuration.
        self.engine_params = engine_params
        # The GPU time-sharing elastic plan.
        self.gpu_elastic_plan = gpu_elastic_plan
        # The name of the resource group.
        # - The name can be up to 255 characters in length.
        # - The name must start with a digit, an uppercase letter, or a lowercase letter.
        # - The name can contain digits, uppercase letters, lowercase letters, hyphens (-), and underscores (_).
        # 
        # This parameter is required.
        self.group_name = group_name
        # The type of the resource group. Valid values:
        # - **Interactive**
        # - **Job**
        # > For more information about Data Lakehouse Edition resource groups, see [Resource group overview (Data Lakehouse Edition)](https://help.aliyun.com/document_detail/428610.html).
        # 
        # This parameter is required.
        self.group_type = group_type
        # A reserved parameter (not applicable).
        self.max_cluster_count = max_cluster_count
        # The maximum amount of reserved computing resources. Unit: ACUs.
        # - If the resource group type is Interactive, the maximum reserved computing resources is the current unallocated resources of the cluster, in increments of 16 ACUs.
        # - If the resource group type is Job, the maximum reserved computing resources is the current unallocated resources of the cluster, in increments of 8 ACUs.
        self.max_compute_resource = max_compute_resource
        # The maximum number of GPUs.
        self.max_gpu_quantity = max_gpu_quantity
        # A reserved parameter (not applicable).
        self.min_cluster_count = min_cluster_count
        # The minimum amount of reserved computing resources. Unit: ACUs.
        # - If the resource group type is Interactive, the minimum reserved computing resources is 16 ACUs.
        # - If the resource group type is Job, the minimum reserved computing resources is 0 ACUs.
        self.min_compute_resource = min_compute_resource
        # The minimum number of GPUs.
        self.min_gpu_quantity = min_gpu_quantity
        # The Ray configuration.
        # > This parameter is required when the resource group is an AI resource group and the corresponding engine is RayCluster.
        self.ray_config = ray_config
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/612393.html) operation to query the region IDs of AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters.
        self.region_id = region_id
        # The job routing rules.
        self.rules = rules
        # The scaling policy of the resource group. Valid values:
        # - AutoScaling: enables the AutoScaling automatic scaling policy.
        # - Disable: disables automatic scaling.
        # - MultiCluster: enables the MultiCluster automatic scaling policy.
        self.scale_policy = scale_policy
        # The specification name.
        self.spec_name = spec_name
        # The name of the destination resource group.
        self.target_resource_group_name = target_resource_group_name

    def validate(self):
        if self.atm_config:
            self.atm_config.validate()
        if self.gpu_elastic_plan:
            self.gpu_elastic_plan.validate()
        if self.ray_config:
            self.ray_config.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.atm_config is not None:
            result['AtmConfig'] = self.atm_config.to_map()

        if self.auto_stop_interval is not None:
            result['AutoStopInterval'] = self.auto_stop_interval

        if self.classification is not None:
            result['Classification'] = self.classification

        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode

        if self.cluster_size_resource is not None:
            result['ClusterSizeResource'] = self.cluster_size_resource

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.enable_spot is not None:
            result['EnableSpot'] = self.enable_spot

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_params is not None:
            result['EngineParams'] = self.engine_params

        if self.gpu_elastic_plan is not None:
            result['GpuElasticPlan'] = self.gpu_elastic_plan.to_map()

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.max_cluster_count is not None:
            result['MaxClusterCount'] = self.max_cluster_count

        if self.max_compute_resource is not None:
            result['MaxComputeResource'] = self.max_compute_resource

        if self.max_gpu_quantity is not None:
            result['MaxGpuQuantity'] = self.max_gpu_quantity

        if self.min_cluster_count is not None:
            result['MinClusterCount'] = self.min_cluster_count

        if self.min_compute_resource is not None:
            result['MinComputeResource'] = self.min_compute_resource

        if self.min_gpu_quantity is not None:
            result['MinGpuQuantity'] = self.min_gpu_quantity

        if self.ray_config is not None:
            result['RayConfig'] = self.ray_config.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.scale_policy is not None:
            result['ScalePolicy'] = self.scale_policy

        if self.spec_name is not None:
            result['SpecName'] = self.spec_name

        if self.target_resource_group_name is not None:
            result['TargetResourceGroupName'] = self.target_resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtmConfig') is not None:
            temp_model = main_models.CreateDBResourceGroupRequestAtmConfig()
            self.atm_config = temp_model.from_map(m.get('AtmConfig'))

        if m.get('AutoStopInterval') is not None:
            self.auto_stop_interval = m.get('AutoStopInterval')

        if m.get('Classification') is not None:
            self.classification = m.get('Classification')

        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')

        if m.get('ClusterSizeResource') is not None:
            self.cluster_size_resource = m.get('ClusterSizeResource')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EnableSpot') is not None:
            self.enable_spot = m.get('EnableSpot')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineParams') is not None:
            self.engine_params = m.get('EngineParams')

        if m.get('GpuElasticPlan') is not None:
            temp_model = main_models.CreateDBResourceGroupRequestGpuElasticPlan()
            self.gpu_elastic_plan = temp_model.from_map(m.get('GpuElasticPlan'))

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('MaxClusterCount') is not None:
            self.max_cluster_count = m.get('MaxClusterCount')

        if m.get('MaxComputeResource') is not None:
            self.max_compute_resource = m.get('MaxComputeResource')

        if m.get('MaxGpuQuantity') is not None:
            self.max_gpu_quantity = m.get('MaxGpuQuantity')

        if m.get('MinClusterCount') is not None:
            self.min_cluster_count = m.get('MinClusterCount')

        if m.get('MinComputeResource') is not None:
            self.min_compute_resource = m.get('MinComputeResource')

        if m.get('MinGpuQuantity') is not None:
            self.min_gpu_quantity = m.get('MinGpuQuantity')

        if m.get('RayConfig') is not None:
            temp_model = main_models.CreateDBResourceGroupRequestRayConfig()
            self.ray_config = temp_model.from_map(m.get('RayConfig'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.CreateDBResourceGroupRequestRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('ScalePolicy') is not None:
            self.scale_policy = m.get('ScalePolicy')

        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')

        if m.get('TargetResourceGroupName') is not None:
            self.target_resource_group_name = m.get('TargetResourceGroupName')

        return self

class CreateDBResourceGroupRequestRules(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        query_time: str = None,
        target_group_name: str = None,
    ):
        # The name of the resource group.
        # - The name can be up to 255 characters in length.
        # - The name must start with a digit, an uppercase letter, or a lowercase letter.
        # - The name can contain digits, uppercase letters, lowercase letters, hyphens (-), and underscores (_).
        self.group_name = group_name
        # The query execution time threshold. Unit: milliseconds (ms).
        self.query_time = query_time
        # The name of the destination resource group.
        self.target_group_name = target_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.query_time is not None:
            result['QueryTime'] = self.query_time

        if self.target_group_name is not None:
            result['TargetGroupName'] = self.target_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')

        if m.get('TargetGroupName') is not None:
            self.target_group_name = m.get('TargetGroupName')

        return self

class CreateDBResourceGroupRequestRayConfig(DaraModel):
    def __init__(
        self,
        category: str = None,
        enable_user_eni: bool = None,
        head_allocate_unit: str = None,
        head_disk_capacity: str = None,
        head_spec: str = None,
        head_spec_type: str = None,
        user_defined_requirements: str = None,
        worker_groups: List[main_models.CreateDBResourceGroupRequestRayConfigWorkerGroups] = None,
    ):
        # The Ray cluster type. Valid values:
        # 
        # - BASIC: basic type, non-high-availability
        # - HIGH_AVAILABILITY: high-availability type
        self.category = category
        # Specifies whether to enable user ENI connectivity.
        self.enable_user_eni = enable_user_eni
        # The allocation unit of the head node.
        self.head_allocate_unit = head_allocate_unit
        # The disk size of the head node.
        self.head_disk_capacity = head_disk_capacity
        # The node specifications of the head node.
        self.head_spec = head_spec
        # The resource type of the head node.
        self.head_spec_type = head_spec_type
        self.user_defined_requirements = user_defined_requirements
        # The list of Ray worker group configurations.
        self.worker_groups = worker_groups

    def validate(self):
        if self.worker_groups:
            for v1 in self.worker_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.enable_user_eni is not None:
            result['EnableUserEni'] = self.enable_user_eni

        if self.head_allocate_unit is not None:
            result['HeadAllocateUnit'] = self.head_allocate_unit

        if self.head_disk_capacity is not None:
            result['HeadDiskCapacity'] = self.head_disk_capacity

        if self.head_spec is not None:
            result['HeadSpec'] = self.head_spec

        if self.head_spec_type is not None:
            result['HeadSpecType'] = self.head_spec_type

        if self.user_defined_requirements is not None:
            result['UserDefinedRequirements'] = self.user_defined_requirements

        result['WorkerGroups'] = []
        if self.worker_groups is not None:
            for k1 in self.worker_groups:
                result['WorkerGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('EnableUserEni') is not None:
            self.enable_user_eni = m.get('EnableUserEni')

        if m.get('HeadAllocateUnit') is not None:
            self.head_allocate_unit = m.get('HeadAllocateUnit')

        if m.get('HeadDiskCapacity') is not None:
            self.head_disk_capacity = m.get('HeadDiskCapacity')

        if m.get('HeadSpec') is not None:
            self.head_spec = m.get('HeadSpec')

        if m.get('HeadSpecType') is not None:
            self.head_spec_type = m.get('HeadSpecType')

        if m.get('UserDefinedRequirements') is not None:
            self.user_defined_requirements = m.get('UserDefinedRequirements')

        self.worker_groups = []
        if m.get('WorkerGroups') is not None:
            for k1 in m.get('WorkerGroups'):
                temp_model = main_models.CreateDBResourceGroupRequestRayConfigWorkerGroups()
                self.worker_groups.append(temp_model.from_map(k1))

        return self

class CreateDBResourceGroupRequestRayConfigWorkerGroups(DaraModel):
    def __init__(
        self,
        allocate_unit: str = None,
        group_name: str = None,
        max_worker_quantity: int = None,
        min_worker_quantity: int = None,
        worker_disk_capacity: str = None,
        worker_spec_name: str = None,
        worker_spec_type: str = None,
    ):
        # The allocation unit.
        self.allocate_unit = allocate_unit
        # The name of the worker group.
        self.group_name = group_name
        # The maximum number of workers.
        self.max_worker_quantity = max_worker_quantity
        # The minimum number of workers.
        self.min_worker_quantity = min_worker_quantity
        # The disk size of the worker node.
        self.worker_disk_capacity = worker_disk_capacity
        # The node specifications of the worker node.
        self.worker_spec_name = worker_spec_name
        # The resource type of the worker node.
        self.worker_spec_type = worker_spec_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocate_unit is not None:
            result['AllocateUnit'] = self.allocate_unit

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.max_worker_quantity is not None:
            result['MaxWorkerQuantity'] = self.max_worker_quantity

        if self.min_worker_quantity is not None:
            result['MinWorkerQuantity'] = self.min_worker_quantity

        if self.worker_disk_capacity is not None:
            result['WorkerDiskCapacity'] = self.worker_disk_capacity

        if self.worker_spec_name is not None:
            result['WorkerSpecName'] = self.worker_spec_name

        if self.worker_spec_type is not None:
            result['WorkerSpecType'] = self.worker_spec_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocateUnit') is not None:
            self.allocate_unit = m.get('AllocateUnit')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('MaxWorkerQuantity') is not None:
            self.max_worker_quantity = m.get('MaxWorkerQuantity')

        if m.get('MinWorkerQuantity') is not None:
            self.min_worker_quantity = m.get('MinWorkerQuantity')

        if m.get('WorkerDiskCapacity') is not None:
            self.worker_disk_capacity = m.get('WorkerDiskCapacity')

        if m.get('WorkerSpecName') is not None:
            self.worker_spec_name = m.get('WorkerSpecName')

        if m.get('WorkerSpecType') is not None:
            self.worker_spec_type = m.get('WorkerSpecType')

        return self

class CreateDBResourceGroupRequestGpuElasticPlan(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        rules: List[main_models.CreateDBResourceGroupRequestGpuElasticPlanRules] = None,
    ):
        # Specifies whether to enable the elastic plan immediately after creation. Valid values:
        # - true: enables the elastic plan immediately.
        # - false: does not enable the elastic plan.
        self.enabled = enabled
        # The list of rules.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.CreateDBResourceGroupRequestGpuElasticPlanRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class CreateDBResourceGroupRequestGpuElasticPlanRules(DaraModel):
    def __init__(
        self,
        end_cron_expression: str = None,
        start_cron_expression: str = None,
    ):
        # The end time as a cron expression. The interval must be at least 1 hour.
        self.end_cron_expression = end_cron_expression
        # The start time as a cron expression. The interval must be at least 1 hour.
        self.start_cron_expression = start_cron_expression

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_cron_expression is not None:
            result['EndCronExpression'] = self.end_cron_expression

        if self.start_cron_expression is not None:
            result['StartCronExpression'] = self.start_cron_expression

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndCronExpression') is not None:
            self.end_cron_expression = m.get('EndCronExpression')

        if m.get('StartCronExpression') is not None:
            self.start_cron_expression = m.get('StartCronExpression')

        return self

class CreateDBResourceGroupRequestAtmConfig(DaraModel):
    def __init__(
        self,
        auth_node_num: int = None,
        auth_node_spec: str = None,
        insert_node_num: int = None,
        insert_node_spec: str = None,
        select_node_cache_size: int = None,
        select_node_num: int = None,
        select_node_spec: str = None,
        storage_node_disk_size: int = None,
        storage_node_disk_type: str = None,
        storage_node_num: int = None,
        storage_node_spec: str = None,
    ):
        self.auth_node_num = auth_node_num
        self.auth_node_spec = auth_node_spec
        self.insert_node_num = insert_node_num
        self.insert_node_spec = insert_node_spec
        self.select_node_cache_size = select_node_cache_size
        self.select_node_num = select_node_num
        self.select_node_spec = select_node_spec
        self.storage_node_disk_size = storage_node_disk_size
        self.storage_node_disk_type = storage_node_disk_type
        self.storage_node_num = storage_node_num
        self.storage_node_spec = storage_node_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_node_num is not None:
            result['AuthNodeNum'] = self.auth_node_num

        if self.auth_node_spec is not None:
            result['AuthNodeSpec'] = self.auth_node_spec

        if self.insert_node_num is not None:
            result['InsertNodeNum'] = self.insert_node_num

        if self.insert_node_spec is not None:
            result['InsertNodeSpec'] = self.insert_node_spec

        if self.select_node_cache_size is not None:
            result['SelectNodeCacheSize'] = self.select_node_cache_size

        if self.select_node_num is not None:
            result['SelectNodeNum'] = self.select_node_num

        if self.select_node_spec is not None:
            result['SelectNodeSpec'] = self.select_node_spec

        if self.storage_node_disk_size is not None:
            result['StorageNodeDiskSize'] = self.storage_node_disk_size

        if self.storage_node_disk_type is not None:
            result['StorageNodeDiskType'] = self.storage_node_disk_type

        if self.storage_node_num is not None:
            result['StorageNodeNum'] = self.storage_node_num

        if self.storage_node_spec is not None:
            result['StorageNodeSpec'] = self.storage_node_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthNodeNum') is not None:
            self.auth_node_num = m.get('AuthNodeNum')

        if m.get('AuthNodeSpec') is not None:
            self.auth_node_spec = m.get('AuthNodeSpec')

        if m.get('InsertNodeNum') is not None:
            self.insert_node_num = m.get('InsertNodeNum')

        if m.get('InsertNodeSpec') is not None:
            self.insert_node_spec = m.get('InsertNodeSpec')

        if m.get('SelectNodeCacheSize') is not None:
            self.select_node_cache_size = m.get('SelectNodeCacheSize')

        if m.get('SelectNodeNum') is not None:
            self.select_node_num = m.get('SelectNodeNum')

        if m.get('SelectNodeSpec') is not None:
            self.select_node_spec = m.get('SelectNodeSpec')

        if m.get('StorageNodeDiskSize') is not None:
            self.storage_node_disk_size = m.get('StorageNodeDiskSize')

        if m.get('StorageNodeDiskType') is not None:
            self.storage_node_disk_type = m.get('StorageNodeDiskType')

        if m.get('StorageNodeNum') is not None:
            self.storage_node_num = m.get('StorageNodeNum')

        if m.get('StorageNodeSpec') is not None:
            self.storage_node_spec = m.get('StorageNodeSpec')

        return self

