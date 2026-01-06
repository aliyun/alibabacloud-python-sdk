# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBResourceGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_stop_interval: str = None,
        cluster_mode: str = None,
        cluster_size_resource: str = None,
        dbcluster_id: str = None,
        enable_spot: bool = None,
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
        self.engine_params_shrink = engine_params_shrink
        self.gpu_elastic_plan_shrink = gpu_elastic_plan_shrink
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
        self.ray_config_shrink = ray_config_shrink
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) operation to query the most recent region list.
        self.region_id = region_id
        # The job resubmission rules.
        self.rules_shrink = rules_shrink
        self.spec_name = spec_name
        self.status = status
        self.target_resource_group_name = target_resource_group_name

    def validate(self):
        pass

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

        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetResourceGroupName') is not None:
            self.target_resource_group_name = m.get('TargetResourceGroupName')

        return self

