# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ModifyDBResourceGroupRequest(DaraModel):
    def __init__(
        self,
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
        self.auto_stop_interval = auto_stop_interval
        # A reserved parameter.
        self.cluster_mode = cluster_mode
        # A reserved parameter.
        self.cluster_size_resource = cluster_size_resource
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable the spot instance feature for the resource group. After you enable the spot instance feature, you are charged for resources at a lower unit price but the resources are probably released. You can enable the spot instance feature only for job resource groups. Valid values:
        # 
        # *   **True**
        # *   **False**
        self.enable_spot = enable_spot
        self.engine_params = engine_params
        self.gpu_elastic_plan = gpu_elastic_plan
        # The name of the resource group.
        # 
        # > You can call the [DescribeDBResourceGroup](https://help.aliyun.com/document_detail/459446.html) operation to query the name of a resource group in a cluster.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The type of the resource group. Valid values:
        # 
        # *   **Interactive**
        # *   **Job**
        # 
        # > For information about resource groups of Data Lakehouse Edition, see [Resource groups](https://help.aliyun.com/document_detail/428610.html).
        # 
        # This parameter is required.
        self.group_type = group_type
        # A reserved parameter.
        self.max_cluster_count = max_cluster_count
        # The maximum amount of reserved computing resources.
        # 
        # *   If GroupType is set to Interactive, the maximum amount of reserved computing resources refers to the amount of resources that are not allocated in the cluster. Set this parameter to a value in increments of 16ACU.
        # *   If GroupType is set to Job, the maximum amount of reserved computing resources refers to the amount of resources that are not allocated in the cluster. Set this parameter to a value in increments of 8ACU.
        self.max_compute_resource = max_compute_resource
        self.max_gpu_quantity = max_gpu_quantity
        # A reserved parameter.
        self.min_cluster_count = min_cluster_count
        # The minimum amount of reserved computing resources.
        # 
        # *   If the GroupType parameter is set to Interactive, set the value to 16ACU.
        # *   If GroupType is set to Job, set the value to 0ACU.
        self.min_compute_resource = min_compute_resource
        self.min_gpu_quantity = min_gpu_quantity
        self.ray_config = ray_config
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) operation to query the most recent region list.
        self.region_id = region_id
        # The job resubmission rules.
        self.rules = rules
        self.spec_name = spec_name
        self.status = status
        self.target_resource_group_name = target_resource_group_name

    def validate(self):
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
        # The execution duration of the query. Unit: milliseconds.
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
        worker_groups: List[main_models.ModifyDBResourceGroupRequestRayConfigWorkerGroups] = None,
    ):
        self.app_config = app_config
        self.category = category
        self.enable_user_eni = enable_user_eni
        self.head_allocate_unit = head_allocate_unit
        self.head_disk_capacity = head_disk_capacity
        self.head_spec = head_spec
        self.head_spec_type = head_spec_type
        self.storage_mounts = storage_mounts
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
        self.allocate_unit = allocate_unit
        self.group_name = group_name
        self.max_worker_quantity = max_worker_quantity
        self.min_worker_quantity = min_worker_quantity
        self.worker_disk_capacity = worker_disk_capacity
        self.worker_spec_name = worker_spec_name
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
        self.mount_path = mount_path
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
        self.app_name = app_name
        self.app_type = app_type
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
        self.image = image
        self.inference_engine = inference_engine
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
        self.enabled = enabled
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
        self.end_cron_expression = end_cron_expression
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

