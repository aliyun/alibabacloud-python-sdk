# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ModifyDBResourceGroupRequest(DaraModel):
    def __init__(
        self,
        atm_config: main_models.ModifyDBResourceGroupRequestAtmConfig = None,
        auto_stop_interval: str = None,
        cluster_mode: str = None,
        cluster_size_resource: str = None,
        dbcluster_id: str = None,
        enable_spot: bool = None,
        engine_params: Dict[str, Any] = None,
        gpu_elastic_plan: main_models.ModifyDBResourceGroupRequestGpuElasticPlan = None,
        group_name: str = None,
        group_type: str = None,
        max_cluster_count: int = None,
        max_compute_resource: str = None,
        max_gpu_quantity: int = None,
        min_cluster_count: int = None,
        min_compute_resource: str = None,
        min_gpu_quantity: int = None,
        ray_config: main_models.ModifyDBResourceGroupRequestRayConfig = None,
        region_id: str = None,
        rules: List[main_models.ModifyDBResourceGroupRequestRules] = None,
        spec_name: str = None,
        status: str = None,
        target_resource_group_name: str = None,
    ):
        self.atm_config = atm_config
        # The idle duration after which the resource group is automatically stopped.
        self.auto_stop_interval = auto_stop_interval
        # This parameter is reserved.
        self.cluster_mode = cluster_mode
        # This parameter is reserved.
        self.cluster_size_resource = cluster_size_resource
        # <props="china">The ID of the Data Lakehouse Edition, Enterprise Edition, or Basic Edition cluster.
        # <props="intl">The ID of the Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable the spot instance feature for the resource group. This feature provides resources at a lower unit price, but they can be reclaimed at any time. Only `Job` resource groups support this feature. Valid values:
        # 
        # - **True**: enables the spot instance feature.
        # 
        # - **False**: disables the spot instance feature.
        self.enable_spot = enable_spot
        # The engine configuration.
        self.engine_params = engine_params
        # The time-based scaling plan for GPUs.
        self.gpu_elastic_plan = gpu_elastic_plan
        # The name of the resource group.
        # 
        # > You can call the [DescribeDBResourceGroup](https://help.aliyun.com/document_detail/459446.html) operation to query the resource group name for a specific cluster.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The type of the resource group. Valid values:
        # 
        # - **Interactive**
        # 
        # - **Job**
        # 
        # > For more information about resource groups in Data Lakehouse Edition clusters, see [Resource groups](https://help.aliyun.com/document_detail/428610.html).
        # 
        # This parameter is required.
        self.group_type = group_type
        # This parameter is reserved.
        self.max_cluster_count = max_cluster_count
        # The maximum amount of reserved computing resources. The value cannot exceed the unallocated computing resources of the cluster.
        # 
        # - If the resource group type is `Interactive`, the value is specified in increments of 16 ACU.
        # 
        # - If the resource group type is `Job`, the value is specified in increments of 8 ACU.
        self.max_compute_resource = max_compute_resource
        # This parameter is reserved.
        self.max_gpu_quantity = max_gpu_quantity
        # This parameter is reserved.
        self.min_cluster_count = min_cluster_count
        # The minimum amount of reserved computing resources.
        # 
        # - If the resource group type is `Interactive`, the minimum amount of reserved computing resources is 16 ACU.
        # 
        # - If the resource group type is `Job`, the minimum amount of reserved computing resources is 0 ACU.
        self.min_compute_resource = min_compute_resource
        # This parameter is reserved.
        self.min_gpu_quantity = min_gpu_quantity
        # The Ray configuration. This parameter is required if the resource group is an AI group and uses a Ray cluster as its engine.
        self.ray_config = ray_config
        # The region ID of the cluster.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) operation to query available regions.
        self.region_id = region_id
        # The job submission rules.
        self.rules = rules
        # This parameter is reserved.
        self.spec_name = spec_name
        # The desired state of the resource group. Specify **starting** to start the resource group or **stopping** to stop it.
        self.status = status
        # This parameter is reserved.
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

        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode

        if self.cluster_size_resource is not None:
            result['ClusterSizeResource'] = self.cluster_size_resource

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.enable_spot is not None:
            result['EnableSpot'] = self.enable_spot

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

        if self.spec_name is not None:
            result['SpecName'] = self.spec_name

        if self.status is not None:
            result['Status'] = self.status

        if self.target_resource_group_name is not None:
            result['TargetResourceGroupName'] = self.target_resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtmConfig') is not None:
            temp_model = main_models.ModifyDBResourceGroupRequestAtmConfig()
            self.atm_config = temp_model.from_map(m.get('AtmConfig'))

        if m.get('AutoStopInterval') is not None:
            self.auto_stop_interval = m.get('AutoStopInterval')

        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')

        if m.get('ClusterSizeResource') is not None:
            self.cluster_size_resource = m.get('ClusterSizeResource')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EnableSpot') is not None:
            self.enable_spot = m.get('EnableSpot')

        if m.get('EngineParams') is not None:
            self.engine_params = m.get('EngineParams')

        if m.get('GpuElasticPlan') is not None:
            temp_model = main_models.ModifyDBResourceGroupRequestGpuElasticPlan()
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
            temp_model = main_models.ModifyDBResourceGroupRequestRayConfig()
            self.ray_config = temp_model.from_map(m.get('RayConfig'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ModifyDBResourceGroupRequestRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetResourceGroupName') is not None:
            self.target_resource_group_name = m.get('TargetResourceGroupName')

        return self

class ModifyDBResourceGroupRequestRules(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        query_time: str = None,
        target_group_name: str = None,
    ):
        # The name of the resource group.
        self.group_name = group_name
        # The query execution time threshold, in milliseconds (ms).
        self.query_time = query_time
        # The name of the target resource group.
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

class ModifyDBResourceGroupRequestRayConfig(DaraModel):
    def __init__(
        self,
        app_config: main_models.ModifyDBResourceGroupRequestRayConfigAppConfig = None,
        category: str = None,
        enable_user_eni: bool = None,
        head_allocate_unit: str = None,
        head_disk_capacity: str = None,
        head_spec: str = None,
        head_spec_type: str = None,
        storage_mounts: List[main_models.ModifyDBResourceGroupRequestRayConfigStorageMounts] = None,
        user_defined_requirements: str = None,
        worker_groups: List[main_models.ModifyDBResourceGroupRequestRayConfigWorkerGroups] = None,
    ):
        # The Ray application configuration.
        self.app_config = app_config
        # The type of the Ray cluster. Valid values:
        # 
        # - **BASIC**: A basic, non-high-availability cluster.
        # 
        # - **HIGH_AVAILABILITY**: A high-availability cluster.
        self.category = category
        # Specifies whether to enable the ENI.
        self.enable_user_eni = enable_user_eni
        # The allocation unit of the head node.
        self.head_allocate_unit = head_allocate_unit
        # The disk size of the head node.
        self.head_disk_capacity = head_disk_capacity
        # The specifications of the head node.
        self.head_spec = head_spec
        # The resource type of the head node.
        self.head_spec_type = head_spec_type
        # A list of storage mounts.
        self.storage_mounts = storage_mounts
        self.user_defined_requirements = user_defined_requirements
        # A list of configurations for Ray worker groups.
        self.worker_groups = worker_groups

    def validate(self):
        if self.app_config:
            self.app_config.validate()
        if self.storage_mounts:
            for v1 in self.storage_mounts:
                 if v1:
                    v1.validate()
        if self.worker_groups:
            for v1 in self.worker_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_config is not None:
            result['AppConfig'] = self.app_config.to_map()

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

        result['StorageMounts'] = []
        if self.storage_mounts is not None:
            for k1 in self.storage_mounts:
                result['StorageMounts'].append(k1.to_map() if k1 else None)

        if self.user_defined_requirements is not None:
            result['UserDefinedRequirements'] = self.user_defined_requirements

        result['WorkerGroups'] = []
        if self.worker_groups is not None:
            for k1 in self.worker_groups:
                result['WorkerGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConfig') is not None:
            temp_model = main_models.ModifyDBResourceGroupRequestRayConfigAppConfig()
            self.app_config = temp_model.from_map(m.get('AppConfig'))

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

        self.storage_mounts = []
        if m.get('StorageMounts') is not None:
            for k1 in m.get('StorageMounts'):
                temp_model = main_models.ModifyDBResourceGroupRequestRayConfigStorageMounts()
                self.storage_mounts.append(temp_model.from_map(k1))

        if m.get('UserDefinedRequirements') is not None:
            self.user_defined_requirements = m.get('UserDefinedRequirements')

        self.worker_groups = []
        if m.get('WorkerGroups') is not None:
            for k1 in m.get('WorkerGroups'):
                temp_model = main_models.ModifyDBResourceGroupRequestRayConfigWorkerGroups()
                self.worker_groups.append(temp_model.from_map(k1))

        return self

class ModifyDBResourceGroupRequestRayConfigWorkerGroups(DaraModel):
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
        # The maximum number of worker nodes.
        self.max_worker_quantity = max_worker_quantity
        # The minimum number of worker nodes.
        self.min_worker_quantity = min_worker_quantity
        # The disk size of a worker node.
        self.worker_disk_capacity = worker_disk_capacity
        # The specifications of a worker node.
        self.worker_spec_name = worker_spec_name
        # The resource type of a worker node.
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

class ModifyDBResourceGroupRequestRayConfigStorageMounts(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        storage_id: int = None,
    ):
        # The mount path.
        self.mount_path = mount_path
        # The storage ID.
        self.storage_id = storage_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.storage_id is not None:
            result['StorageId'] = self.storage_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('StorageId') is not None:
            self.storage_id = m.get('StorageId')

        return self

class ModifyDBResourceGroupRequestRayConfigAppConfig(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        image_selector: main_models.ModifyDBResourceGroupRequestRayConfigAppConfigImageSelector = None,
    ):
        # The application name.
        self.app_name = app_name
        # The application type.
        self.app_type = app_type
        # The image configuration.
        self.image_selector = image_selector

    def validate(self):
        if self.image_selector:
            self.image_selector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.image_selector is not None:
            result['ImageSelector'] = self.image_selector.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('ImageSelector') is not None:
            temp_model = main_models.ModifyDBResourceGroupRequestRayConfigAppConfigImageSelector()
            self.image_selector = temp_model.from_map(m.get('ImageSelector'))

        return self

class ModifyDBResourceGroupRequestRayConfigAppConfigImageSelector(DaraModel):
    def __init__(
        self,
        image: str = None,
        inference_engine: str = None,
        llm_model: str = None,
    ):
        # The image name.
        self.image = image
        # The inference engine.
        self.inference_engine = inference_engine
        # The large language model (LLM).
        self.llm_model = llm_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['Image'] = self.image

        if self.inference_engine is not None:
            result['InferenceEngine'] = self.inference_engine

        if self.llm_model is not None:
            result['LlmModel'] = self.llm_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('InferenceEngine') is not None:
            self.inference_engine = m.get('InferenceEngine')

        if m.get('LlmModel') is not None:
            self.llm_model = m.get('LlmModel')

        return self

class ModifyDBResourceGroupRequestGpuElasticPlan(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        rules: List[main_models.ModifyDBResourceGroupRequestGpuElasticPlanRules] = None,
    ):
        # Specifies whether to enable the scaling plan immediately upon creation.
        # Valid values:
        # 
        # - **true**: The plan is enabled.
        # 
        # - **false**: The plan is disabled.
        self.enabled = enabled
        # A list of rules.
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
                temp_model = main_models.ModifyDBResourceGroupRequestGpuElasticPlanRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class ModifyDBResourceGroupRequestGpuElasticPlanRules(DaraModel):
    def __init__(
        self,
        end_cron_expression: str = None,
        start_cron_expression: str = None,
    ):
        # The end time of the scaling window, specified as a cron expression.
        self.end_cron_expression = end_cron_expression
        # The start time of the scaling window, specified as a cron expression. The duration between the start and end times must be at least one hour.
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

class ModifyDBResourceGroupRequestAtmConfig(DaraModel):
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

