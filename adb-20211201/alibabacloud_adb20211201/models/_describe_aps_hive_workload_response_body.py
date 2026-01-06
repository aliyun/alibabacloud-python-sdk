# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeApsHiveWorkloadResponseBody(DaraModel):
    def __init__(
        self,
        aps_workload: main_models.DescribeApsHiveWorkloadResponseBodyApsWorkload = None,
        request_id: str = None,
    ):
        # The queried job.
        self.aps_workload = aps_workload
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.aps_workload:
            self.aps_workload.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aps_workload is not None:
            result['ApsWorkload'] = self.aps_workload.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApsWorkload') is not None:
            temp_model = main_models.DescribeApsHiveWorkloadResponseBodyApsWorkload()
            self.aps_workload = temp_model.from_map(m.get('ApsWorkload'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeApsHiveWorkloadResponseBodyApsWorkload(DaraModel):
    def __init__(
        self,
        advanced_config: str = None,
        conflict_strategy: str = None,
        create_time: str = None,
        dbcluster_id: str = None,
        datasource_id: int = None,
        datasource_name: str = None,
        emr_cluster_id: str = None,
        full_compute_unit: str = None,
        meta_store_uri: str = None,
        oss_location: str = None,
        parallelism: int = None,
        region_id: str = None,
        resource_group: str = None,
        state: str = None,
        sync_allow_expression: str = None,
        sync_deny_expression: str = None,
        target_type: str = None,
        vswitch: str = None,
        workload_id: str = None,
        workload_name: str = None,
        workload_type_name: str = None,
    ):
        # The advanced configurations.
        self.advanced_config = advanced_config
        # The policy to handle tables with the same name in the destination cluster.
        self.conflict_strategy = conflict_strategy
        # The time when the workload was created.
        self.create_time = create_time
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The data source ID.
        self.datasource_id = datasource_id
        # The name of the data source.
        self.datasource_name = datasource_name
        # The ID of the E-MapReduce (EMR) cluster.
        self.emr_cluster_id = emr_cluster_id
        # The number of AnalyticDB compute units (ACUs) required for migration.
        self.full_compute_unit = full_compute_unit
        # The URL of the Hive Metastore.
        self.meta_store_uri = meta_store_uri
        # The Object Storage Service (OSS) URL of the AnalyticDB for MySQL cluster data.
        self.oss_location = oss_location
        # The number of tasks that are allowed in parallel.
        self.parallelism = parallelism
        # The region ID.
        self.region_id = region_id
        # The resource group to which the SQL statement belongs.
        self.resource_group = resource_group
        # The status of the workload.
        self.state = state
        # The expression that manually matches the source database table whitelist.
        self.sync_allow_expression = sync_allow_expression
        # Manually match the blacklist expressions for source database tables.
        self.sync_deny_expression = sync_deny_expression
        # The destination type.
        self.target_type = target_type
        # The name of the vSwitch.
        self.vswitch = vswitch
        # The job ID.
        self.workload_id = workload_id
        # The name of the workload.
        self.workload_name = workload_name
        # The name of the workload.
        self.workload_type_name = workload_type_name

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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.emr_cluster_id is not None:
            result['EmrClusterId'] = self.emr_cluster_id

        if self.full_compute_unit is not None:
            result['FullComputeUnit'] = self.full_compute_unit

        if self.meta_store_uri is not None:
            result['MetaStoreUri'] = self.meta_store_uri

        if self.oss_location is not None:
            result['OssLocation'] = self.oss_location

        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.state is not None:
            result['State'] = self.state

        if self.sync_allow_expression is not None:
            result['SyncAllowExpression'] = self.sync_allow_expression

        if self.sync_deny_expression is not None:
            result['SyncDenyExpression'] = self.sync_deny_expression

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch

        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id

        if self.workload_name is not None:
            result['WorkloadName'] = self.workload_name

        if self.workload_type_name is not None:
            result['WorkloadTypeName'] = self.workload_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedConfig') is not None:
            self.advanced_config = m.get('AdvancedConfig')

        if m.get('ConflictStrategy') is not None:
            self.conflict_strategy = m.get('ConflictStrategy')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('EmrClusterId') is not None:
            self.emr_cluster_id = m.get('EmrClusterId')

        if m.get('FullComputeUnit') is not None:
            self.full_compute_unit = m.get('FullComputeUnit')

        if m.get('MetaStoreUri') is not None:
            self.meta_store_uri = m.get('MetaStoreUri')

        if m.get('OssLocation') is not None:
            self.oss_location = m.get('OssLocation')

        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('SyncAllowExpression') is not None:
            self.sync_allow_expression = m.get('SyncAllowExpression')

        if m.get('SyncDenyExpression') is not None:
            self.sync_deny_expression = m.get('SyncDenyExpression')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')

        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')

        if m.get('WorkloadName') is not None:
            self.workload_name = m.get('WorkloadName')

        if m.get('WorkloadTypeName') is not None:
            self.workload_type_name = m.get('WorkloadTypeName')

        return self

