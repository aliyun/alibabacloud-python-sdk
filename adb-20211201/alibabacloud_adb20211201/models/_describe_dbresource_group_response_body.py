# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeDBResourceGroupResponseBody(DaraModel):
    def __init__(
        self,
        groups_info: List[main_models.DescribeDBResourceGroupResponseBodyGroupsInfo] = None,
        request_id: str = None,
    ):
        # The list of resource group information.
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
        result['GroupsInfo'] = []
        if self.groups_info is not None:
            for k1 in self.groups_info:
                result['GroupsInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        atm_config: main_models.DescribeDBResourceGroupResponseBodyGroupsInfoAtmConfig = None,
        auto_stop_interval: str = None,
        classification: str = None,
        cluster_mode: str = None,
        cluster_size_resource: str = None,
        create_time: str = None,
        elastic_min_compute_resource: str = None,
        enable_spot: str = None,
        engine: str = None,
        engine_params: Dict[str, Any] = None,
        gpu_elastic_plan: main_models.DescribeDBResourceGroupResponseBodyGroupsInfoGpuElasticPlan = None,
        group_name: str = None,
        group_type: str = None,
        group_users: str = None,
        max_cluster_count: int = None,
        max_compute_resource: str = None,
        max_gpu_quantity: int = None,
        message: str = None,
        min_cluster_count: int = None,
        min_compute_resource: str = None,
        min_gpu_quantity: int = None,
        ray_config: main_models.DescribeDBResourceGroupResponseBodyGroupsInfoRayConfig = None,
        rules: List[main_models.DescribeDBResourceGroupResponseBodyGroupsInfoRules] = None,
        running_cluster_count: int = None,
        scale_policy: str = None,
        spec_name: str = None,
        status: str = None,
        target_resource_group_name: str = None,
        update_time: str = None,
    ):
        # The PromQL resource group configuration.
        self.atm_config = atm_config
        # The automatic stop interval, in the format of a number followed by m (minutes). The value ranges from 0m or 5m to 10080m. A value of 0m indicates that automatic stop is disabled.
        self.auto_stop_interval = auto_stop_interval
        # The classification of the resource group. Valid values:
        # 
        # - SQL
        # - SparkSQL
        # - MultiCluster
        # - AI
        self.classification = classification
        # A reserved parameter. Not applicable.
        self.cluster_mode = cluster_mode
        # A reserved parameter. Not applicable.
        self.cluster_size_resource = cluster_size_resource
        # The time when the resource group was created, in UTC. Format: <i>yyyy-MM-ddTHH:mm:ssZ</i>.
        self.create_time = create_time
        # The minimum elastic computing resources, in ACUs.
        self.elastic_min_compute_resource = elastic_min_compute_resource
        # Indicates whether the spot instance feature is enabled for the resource group. When the spot instance feature is enabled, the unit price of resources is reduced, but instances may be released. Valid values:
        # - **True**: The spot instance feature is enabled.
        # - **False**: The spot instance feature is disabled.
        # 
        # Only Job-type resource groups can be set to True.
        self.enable_spot = enable_spot
        # The engine type.
        self.engine = engine
        # The engine parameters.
        self.engine_params = engine_params
        # The GPU time-sharing elastic plan.
        self.gpu_elastic_plan = gpu_elastic_plan
        # The resource group name.
        self.group_name = group_name
        # The resource group type. Valid values:
        # - **Interactive**
        # - **Job**
        # > For more information about resource groups in Data Lakehouse Edition, see [Resource group introduction (Data Lakehouse Edition)](https://help.aliyun.com/document_detail/428610.html).
        self.group_type = group_type
        # The Resource Access Management (RAM) users attached to the resource group.
        self.group_users = group_users
        # A reserved parameter. Not applicable.
        self.max_cluster_count = max_cluster_count
        # The maximum reserved computing resources, in ACUs.
        self.max_compute_resource = max_compute_resource
        # The maximum number of GPUs.
        self.max_gpu_quantity = max_gpu_quantity
        # The job routing rule message.
        # 
        # This parameter is required.
        self.message = message
        # A reserved parameter. Not applicable.
        self.min_cluster_count = min_cluster_count
        # The minimum reserved computing resources, in ACUs.
        self.min_compute_resource = min_compute_resource
        # The minimum number of GPUs.
        self.min_gpu_quantity = min_gpu_quantity
        # The Ray configuration information.
        self.ray_config = ray_config
        # The job routing rules.
        self.rules = rules
        # A reserved parameter. Not applicable.
        self.running_cluster_count = running_cluster_count
        # The scaling policy of the resource group. Valid values:
        # 
        # - AutoScaling: enables the AutoScaling automatic scaling policy.
        # - Disable: disables automatic scaling.
        # - MultiCluster: enables the MultiCluster automatic scaling policy.
        self.scale_policy = scale_policy
        # The specification name.
        self.spec_name = spec_name
        # The resource group status. Valid values:
        # - **creating**: being created
        # - **ok**: created
        # - **pendingdelete**: pending deletion
        self.status = status
        # The name of the target resource group.
        self.target_resource_group_name = target_resource_group_name
        # The time when the resource group was last updated, in UTC. Format: <i>yyyy-MM-ddTHH:mm:ssZ</i>.
        self.update_time = update_time

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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.elastic_min_compute_resource is not None:
            result['ElasticMinComputeResource'] = self.elastic_min_compute_resource

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

        if self.group_users is not None:
            result['GroupUsers'] = self.group_users

        if self.max_cluster_count is not None:
            result['MaxClusterCount'] = self.max_cluster_count

        if self.max_compute_resource is not None:
            result['MaxComputeResource'] = self.max_compute_resource

        if self.max_gpu_quantity is not None:
            result['MaxGpuQuantity'] = self.max_gpu_quantity

        if self.message is not None:
            result['Message'] = self.message

        if self.min_cluster_count is not None:
            result['MinClusterCount'] = self.min_cluster_count

        if self.min_compute_resource is not None:
            result['MinComputeResource'] = self.min_compute_resource

        if self.min_gpu_quantity is not None:
            result['MinGpuQuantity'] = self.min_gpu_quantity

        if self.ray_config is not None:
            result['RayConfig'] = self.ray_config.to_map()

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.running_cluster_count is not None:
            result['RunningClusterCount'] = self.running_cluster_count

        if self.scale_policy is not None:
            result['ScalePolicy'] = self.scale_policy

        if self.spec_name is not None:
            result['SpecName'] = self.spec_name

        if self.status is not None:
            result['Status'] = self.status

        if self.target_resource_group_name is not None:
            result['TargetResourceGroupName'] = self.target_resource_group_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtmConfig') is not None:
            temp_model = main_models.DescribeDBResourceGroupResponseBodyGroupsInfoAtmConfig()
            self.atm_config = temp_model.from_map(m.get('AtmConfig'))

        if m.get('AutoStopInterval') is not None:
            self.auto_stop_interval = m.get('AutoStopInterval')

        if m.get('Classification') is not None:
            self.classification = m.get('Classification')

        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')

        if m.get('ClusterSizeResource') is not None:
            self.cluster_size_resource = m.get('ClusterSizeResource')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ElasticMinComputeResource') is not None:
            self.elastic_min_compute_resource = m.get('ElasticMinComputeResource')

        if m.get('EnableSpot') is not None:
            self.enable_spot = m.get('EnableSpot')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineParams') is not None:
            self.engine_params = m.get('EngineParams')

        if m.get('GpuElasticPlan') is not None:
            temp_model = main_models.DescribeDBResourceGroupResponseBodyGroupsInfoGpuElasticPlan()
            self.gpu_elastic_plan = temp_model.from_map(m.get('GpuElasticPlan'))

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('GroupUsers') is not None:
            self.group_users = m.get('GroupUsers')

        if m.get('MaxClusterCount') is not None:
            self.max_cluster_count = m.get('MaxClusterCount')

        if m.get('MaxComputeResource') is not None:
            self.max_compute_resource = m.get('MaxComputeResource')

        if m.get('MaxGpuQuantity') is not None:
            self.max_gpu_quantity = m.get('MaxGpuQuantity')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MinClusterCount') is not None:
            self.min_cluster_count = m.get('MinClusterCount')

        if m.get('MinComputeResource') is not None:
            self.min_compute_resource = m.get('MinComputeResource')

        if m.get('MinGpuQuantity') is not None:
            self.min_gpu_quantity = m.get('MinGpuQuantity')

        if m.get('RayConfig') is not None:
            temp_model = main_models.DescribeDBResourceGroupResponseBodyGroupsInfoRayConfig()
            self.ray_config = temp_model.from_map(m.get('RayConfig'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeDBResourceGroupResponseBodyGroupsInfoRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('RunningClusterCount') is not None:
            self.running_cluster_count = m.get('RunningClusterCount')

        if m.get('ScalePolicy') is not None:
            self.scale_policy = m.get('ScalePolicy')

        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetResourceGroupName') is not None:
            self.target_resource_group_name = m.get('TargetResourceGroupName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeDBResourceGroupResponseBodyGroupsInfoRules(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        query_time: str = None,
        target_group_name: str = None,
    ):
        # The resource group name.
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

class DescribeDBResourceGroupResponseBodyGroupsInfoRayConfig(DaraModel):
    def __init__(
        self,
        app_config: main_models.DescribeDBResourceGroupResponseBodyGroupsInfoRayConfigAppConfig = None,
        category: str = None,
        enable_user_eni: bool = None,
        head_allocate_unit: str = None,
        head_disk_capacity: str = None,
        head_spec: str = None,
        head_spec_type: str = None,
        ray_cluster_address: str = None,
        ray_dashboard_address: str = None,
        ray_grafana_address: str = None,
        ray_serve_public_address: str = None,
        storage_mounts: List[main_models.DescribeDBResourceGroupResponseBodyGroupsInfoRayConfigStorageMounts] = None,
        user_defined_requirements: str = None,
        worker_groups: List[main_models.DescribeDBResourceGroupResponseBodyGroupsInfoRayConfigWorkerGroups] = None,
    ):
        # The Ray application configuration.
        self.app_config = app_config
        # The Ray cluster type. Valid values:
        # 
        # - BASIC: basic type, non-high-availability
        # 
        # - HIGH_AVAILABILITY: high-availability type
        self.category = category
        # Indicates whether ENI is enabled.
        self.enable_user_eni = enable_user_eni
        # The allocation unit of the head node.
        self.head_allocate_unit = head_allocate_unit
        # The disk capacity of the head node.
        self.head_disk_capacity = head_disk_capacity
        # The node specifications of the head node.
        self.head_spec = head_spec
        # The resource type of the head node.
        self.head_spec_type = head_spec_type
        # The Ray cluster address.
        self.ray_cluster_address = ray_cluster_address
        # The Ray Dashboard address.
        self.ray_dashboard_address = ray_dashboard_address
        # The Ray Grafana address.
        self.ray_grafana_address = ray_grafana_address
        # The Ray Serve public address.
        self.ray_serve_public_address = ray_serve_public_address
        # The list of storage mounts.
        self.storage_mounts = storage_mounts
        self.user_defined_requirements = user_defined_requirements
        # The list of Ray worker groups.
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

        if self.ray_cluster_address is not None:
            result['RayClusterAddress'] = self.ray_cluster_address

        if self.ray_dashboard_address is not None:
            result['RayDashboardAddress'] = self.ray_dashboard_address

        if self.ray_grafana_address is not None:
            result['RayGrafanaAddress'] = self.ray_grafana_address

        if self.ray_serve_public_address is not None:
            result['RayServePublicAddress'] = self.ray_serve_public_address

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
            temp_model = main_models.DescribeDBResourceGroupResponseBodyGroupsInfoRayConfigAppConfig()
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

        if m.get('RayClusterAddress') is not None:
            self.ray_cluster_address = m.get('RayClusterAddress')

        if m.get('RayDashboardAddress') is not None:
            self.ray_dashboard_address = m.get('RayDashboardAddress')

        if m.get('RayGrafanaAddress') is not None:
            self.ray_grafana_address = m.get('RayGrafanaAddress')

        if m.get('RayServePublicAddress') is not None:
            self.ray_serve_public_address = m.get('RayServePublicAddress')

        self.storage_mounts = []
        if m.get('StorageMounts') is not None:
            for k1 in m.get('StorageMounts'):
                temp_model = main_models.DescribeDBResourceGroupResponseBodyGroupsInfoRayConfigStorageMounts()
                self.storage_mounts.append(temp_model.from_map(k1))

        if m.get('UserDefinedRequirements') is not None:
            self.user_defined_requirements = m.get('UserDefinedRequirements')

        self.worker_groups = []
        if m.get('WorkerGroups') is not None:
            for k1 in m.get('WorkerGroups'):
                temp_model = main_models.DescribeDBResourceGroupResponseBodyGroupsInfoRayConfigWorkerGroups()
                self.worker_groups.append(temp_model.from_map(k1))

        return self

class DescribeDBResourceGroupResponseBodyGroupsInfoRayConfigWorkerGroups(DaraModel):
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
        # The Ray worker group name.
        self.group_name = group_name
        # The maximum number of workers.
        self.max_worker_quantity = max_worker_quantity
        # The minimum number of workers.
        self.min_worker_quantity = min_worker_quantity
        # The disk capacity per worker.
        self.worker_disk_capacity = worker_disk_capacity
        # The worker specification name.
        self.worker_spec_name = worker_spec_name
        # The Ray worker resource type.
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

class DescribeDBResourceGroupResponseBodyGroupsInfoRayConfigStorageMounts(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        storage_id: int = None,
        storage_name: str = None,
    ):
        # The mount path.
        self.mount_path = mount_path
        # The storage ID.
        self.storage_id = storage_id
        self.storage_name = storage_name

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

        if self.storage_name is not None:
            result['StorageName'] = self.storage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('StorageId') is not None:
            self.storage_id = m.get('StorageId')

        if m.get('StorageName') is not None:
            self.storage_name = m.get('StorageName')

        return self

class DescribeDBResourceGroupResponseBodyGroupsInfoRayConfigAppConfig(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        image_selector: main_models.DescribeDBResourceGroupResponseBodyGroupsInfoRayConfigAppConfigImageSelector = None,
    ):
        # The Ray application name.
        self.app_name = app_name
        # The Ray application type.
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
            temp_model = main_models.DescribeDBResourceGroupResponseBodyGroupsInfoRayConfigAppConfigImageSelector()
            self.image_selector = temp_model.from_map(m.get('ImageSelector'))

        return self

class DescribeDBResourceGroupResponseBodyGroupsInfoRayConfigAppConfigImageSelector(DaraModel):
    def __init__(
        self,
        image: str = None,
        inference_engine: str = None,
        llm_model: str = None,
    ):
        # The image.
        self.image = image
        # The inference engine.
        self.inference_engine = inference_engine
        # The LLM model.
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

class DescribeDBResourceGroupResponseBodyGroupsInfoGpuElasticPlan(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        rules: List[main_models.DescribeDBResourceGroupResponseBodyGroupsInfoGpuElasticPlanRules] = None,
    ):
        # Indicates whether the plan is enabled.
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
                temp_model = main_models.DescribeDBResourceGroupResponseBodyGroupsInfoGpuElasticPlanRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeDBResourceGroupResponseBodyGroupsInfoGpuElasticPlanRules(DaraModel):
    def __init__(
        self,
        end_cron_expression: str = None,
        start_cron_expression: str = None,
    ):
        # The end time in Cron expression format. The interval must be at least 1 hour.
        self.end_cron_expression = end_cron_expression
        # The start time in Cron expression format. The interval must be at least 1 hour.
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

class DescribeDBResourceGroupResponseBodyGroupsInfoAtmConfig(DaraModel):
    def __init__(
        self,
        auth_node_num: str = None,
        auth_node_spec: str = None,
        insert_node_num: str = None,
        insert_node_spec: str = None,
        select_node_cache_size: str = None,
        select_node_num: str = None,
        select_node_spec: str = None,
        storage_node_disk_size: str = None,
        storage_node_disk_type: str = None,
        storage_node_num: str = None,
        storage_node_spec: str = None,
    ):
        # The number of authentication nodes.
        self.auth_node_num = auth_node_num
        # The authentication node specifications.
        self.auth_node_spec = auth_node_spec
        # The number of write nodes.
        self.insert_node_num = insert_node_num
        # The write node specifications.
        self.insert_node_spec = insert_node_spec
        # The cache size of query nodes.
        self.select_node_cache_size = select_node_cache_size
        # The number of query nodes.
        self.select_node_num = select_node_num
        # The query node specifications.
        self.select_node_spec = select_node_spec
        # The disk size of storage nodes.
        self.storage_node_disk_size = storage_node_disk_size
        # The disk type of storage nodes.
        self.storage_node_disk_type = storage_node_disk_type
        # The number of storage nodes.
        self.storage_node_num = storage_node_num
        # The storage node specifications.
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

