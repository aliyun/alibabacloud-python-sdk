# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApsHiveJobRequest(DaraModel):
    def __init__(
        self,
        advanced_config: str = None,
        conflict_strategy: str = None,
        dbcluster_id: str = None,
        datasource_id: int = None,
        full_compute_unit: str = None,
        oss_location: str = None,
        parallelism: int = None,
        region_id: str = None,
        resource_group: str = None,
        sync_allow_expression: str = None,
        sync_deny_expression: str = None,
        target_type: str = None,
        workload_name: str = None,
    ):
        # The advanced configurations.
        self.advanced_config = advanced_config
        # The policy to handle tables with the same name in the destination cluster.
        self.conflict_strategy = conflict_strategy
        # The ID of the AnalyticDB for MySQL cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The data source ID.
        self.datasource_id = datasource_id
        # The number of AnalyticDB compute units (ACUs) required for data migration.
        # 
        # This parameter is required.
        self.full_compute_unit = full_compute_unit
        # The path of the destination data lakehouse in an Object Storage Service (OSS) bucket.
        # 
        # This parameter is required.
        self.oss_location = oss_location
        # The number of tasks that are allowed in parallel.
        self.parallelism = parallelism
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the resource group.
        # 
        # This parameter is required.
        self.resource_group = resource_group
        # The expression that allows objects to be synchronized.
        self.sync_allow_expression = sync_allow_expression
        # The expression that denies objects to be synchronized.
        self.sync_deny_expression = sync_deny_expression
        # The destination type.
        self.target_type = target_type
        # The name of the workload.
        # 
        # This parameter is required.
        self.workload_name = workload_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_config is not None:
            result['AdvancedConfig'] = self.advanced_config

        if self.conflict_strategy is not None:
            result['ConflictStrategy'] = self.conflict_strategy

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.full_compute_unit is not None:
            result['FullComputeUnit'] = self.full_compute_unit

        if self.oss_location is not None:
            result['OssLocation'] = self.oss_location

        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.sync_allow_expression is not None:
            result['SyncAllowExpression'] = self.sync_allow_expression

        if self.sync_deny_expression is not None:
            result['SyncDenyExpression'] = self.sync_deny_expression

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedConfig') is not None:
            self.advanced_config = m.get('AdvancedConfig')

        if m.get('ConflictStrategy') is not None:
            self.conflict_strategy = m.get('ConflictStrategy')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('FullComputeUnit') is not None:
            self.full_compute_unit = m.get('FullComputeUnit')

        if m.get('OssLocation') is not None:
            self.oss_location = m.get('OssLocation')

        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('SyncAllowExpression') is not None:
            self.sync_allow_expression = m.get('SyncAllowExpression')

        if m.get('SyncDenyExpression') is not None:
            self.sync_deny_expression = m.get('SyncDenyExpression')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')

        return self

