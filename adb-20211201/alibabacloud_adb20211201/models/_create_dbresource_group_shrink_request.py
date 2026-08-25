# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBResourceGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        atm_config_shrink: str = None,
        auto_stop_interval: str = None,
        classification: str = None,
        cluster_mode: str = None,
        cluster_size_resource: str = None,
        dbcluster_id: str = None,
        enable_spot: bool = None,
        engine: str = None,
        engine_params_shrink: str = None,
        gpu_elastic_plan_shrink: str = None,
        group_name: str = None,
        group_type: str = None,
        max_cluster_count: int = None,
        max_compute_resource: str = None,
        max_gpu_quantity: int = None,
        min_cluster_count: int = None,
        min_compute_resource: str = None,
        min_gpu_quantity: int = None,
        ray_config_shrink: str = None,
        region_id: str = None,
        rules_shrink: str = None,
        scale_policy: str = None,
        spec_name: str = None,
        target_resource_group_name: str = None,
    ):
        # The PromQL resource group configuration.
        self.atm_config_shrink = atm_config_shrink
        # The automatic stop interval, in minutes (m).
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
        # The ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
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
        self.engine_params_shrink = engine_params_shrink
        # The GPU time-sharing elastic plan.
        self.gpu_elastic_plan_shrink = gpu_elastic_plan_shrink
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
        # > For more information about resource groups of the Data Lakehouse Edition, see [Resource group overview (Data Lakehouse Edition)](https://help.aliyun.com/document_detail/428610.html).
        # 
        # This parameter is required.
        self.group_type = group_type
        # A reserved parameter (not applicable).
        self.max_cluster_count = max_cluster_count
        # The maximum reserved computing resources, in ACUs.
        # - If the resource group type is Interactive, the maximum reserved computing resources is the current unallocated resources of the cluster, with a step size of 16 ACUs.
        # - If the resource group type is Job, the maximum reserved computing resources is the current unallocated resources of the cluster, with a step size of 8 ACUs.
        self.max_compute_resource = max_compute_resource
        # The maximum number of GPUs.
        self.max_gpu_quantity = max_gpu_quantity
        # A reserved parameter (not applicable).
        self.min_cluster_count = min_cluster_count
        # The minimum reserved computing resources, in ACUs.
        # - If the resource group type is Interactive, the minimum reserved computing resources is 16 ACUs.
        # - If the resource group type is Job, the minimum reserved computing resources is 0 ACUs.
        self.min_compute_resource = min_compute_resource
        # The minimum number of GPUs.
        self.min_gpu_quantity = min_gpu_quantity
        # The Ray configuration information.
        # > This parameter is required when the resource group is an AI resource group and the corresponding engine is RayCluster.
        self.ray_config_shrink = ray_config_shrink
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/612393.html) operation to query the region IDs of AnalyticDB for MySQL Data Lakehouse Edition (V3.0) clusters.
        self.region_id = region_id
        # The job routing rules.
        self.rules_shrink = rules_shrink
        # The scaling policy of the resource group. Valid values:
        # - AutoScaling: enables the AutoScaling automatic scaling policy.
        # - Disable: disables automatic scaling.
        # - MultiCluster: enables the MultiCluster automatic scaling policy.
        self.scale_policy = scale_policy
        # The specification name.
        self.spec_name = spec_name
        # The name of the target resource group.
        self.target_resource_group_name = target_resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.atm_config_shrink is not None:
            result['AtmConfig'] = self.atm_config_shrink

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

        if self.engine_params_shrink is not None:
            result['EngineParams'] = self.engine_params_shrink

        if self.gpu_elastic_plan_shrink is not None:
            result['GpuElasticPlan'] = self.gpu_elastic_plan_shrink

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

        if self.ray_config_shrink is not None:
            result['RayConfig'] = self.ray_config_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink

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
            self.atm_config_shrink = m.get('AtmConfig')

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
            self.engine_params_shrink = m.get('EngineParams')

        if m.get('GpuElasticPlan') is not None:
            self.gpu_elastic_plan_shrink = m.get('GpuElasticPlan')

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
            self.ray_config_shrink = m.get('RayConfig')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')

        if m.get('ScalePolicy') is not None:
            self.scale_policy = m.get('ScalePolicy')

        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')

        if m.get('TargetResourceGroupName') is not None:
            self.target_resource_group_name = m.get('TargetResourceGroupName')

        return self

