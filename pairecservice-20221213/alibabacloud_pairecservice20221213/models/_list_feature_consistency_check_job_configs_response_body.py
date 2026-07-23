# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListFeatureConsistencyCheckJobConfigsResponseBody(DaraModel):
    def __init__(
        self,
        feature_consistency_check_configs: List[main_models.ListFeatureConsistencyCheckJobConfigsResponseBodyFeatureConsistencyCheckConfigs] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of feature consistency check configurations.
        self.feature_consistency_check_configs = feature_consistency_check_configs
        # The request ID.
        self.request_id = request_id
        # The total number of configurations.
        self.total_count = total_count

    def validate(self):
        if self.feature_consistency_check_configs:
            for v1 in self.feature_consistency_check_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FeatureConsistencyCheckConfigs'] = []
        if self.feature_consistency_check_configs is not None:
            for k1 in self.feature_consistency_check_configs:
                result['FeatureConsistencyCheckConfigs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_consistency_check_configs = []
        if m.get('FeatureConsistencyCheckConfigs') is not None:
            for k1 in m.get('FeatureConsistencyCheckConfigs'):
                temp_model = main_models.ListFeatureConsistencyCheckJobConfigsResponseBodyFeatureConsistencyCheckConfigs()
                self.feature_consistency_check_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFeatureConsistencyCheckJobConfigsResponseBodyFeatureConsistencyCheckConfigs(DaraModel):
    def __init__(
        self,
        compare_feature: bool = None,
        dataset_id: str = None,
        dataset_mount_path: str = None,
        dataset_name: str = None,
        dataset_type: str = None,
        dataset_uri: str = None,
        default_route: str = None,
        eas_service_name: str = None,
        easy_rec_package_path: str = None,
        easy_rec_version: str = None,
        feature_consistency_check_job_config_id: str = None,
        feature_display_exclude: str = None,
        feature_landing_resource_id: str = None,
        feature_landing_resource_uri: str = None,
        feature_priority: str = None,
        feature_store_item_id: str = None,
        feature_store_model_id: str = None,
        feature_store_project_id: str = None,
        feature_store_project_name: str = None,
        feature_store_seq_feature_view: str = None,
        feature_store_user_id: str = None,
        fg_jar_version: str = None,
        fg_json_file_name: str = None,
        generate_zip: bool = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        item_id_field: str = None,
        item_table: str = None,
        item_table_partition_field: str = None,
        item_table_partition_field_format: str = None,
        latest_job_gmt_sampling_end_time: str = None,
        latest_job_gmt_sampling_start_time: str = None,
        latest_job_id: str = None,
        name: str = None,
        oss_bucket: str = None,
        oss_resource_id: str = None,
        predict_worker_count: int = None,
        predict_worker_cpu: int = None,
        predict_worker_memory: int = None,
        resource_config: str = None,
        sample_rate: str = None,
        scene_id: str = None,
        scene_name: str = None,
        security_group_id: str = None,
        service_id: str = None,
        service_name: str = None,
        status: str = None,
        switch_id: str = None,
        use_feature_store: str = None,
        user_id_field: str = None,
        user_table: str = None,
        user_table_partition_field: str = None,
        user_table_partition_field_format: str = None,
        vpc_id: str = None,
        workflow_name: str = None,
        workspace_id: str = None,
    ):
        # Indicates whether to enable feature comparison.
        self.compare_feature = compare_feature
        self.dataset_id = dataset_id
        self.dataset_mount_path = dataset_mount_path
        self.dataset_name = dataset_name
        self.dataset_type = dataset_type
        self.dataset_uri = dataset_uri
        self.default_route = default_route
        # The name of the EAS service.
        self.eas_service_name = eas_service_name
        # The path of the EasyRec package.
        self.easy_rec_package_path = easy_rec_package_path
        # The version of EasyRec.
        self.easy_rec_version = easy_rec_version
        # The ID of the feature consistency check configuration.
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        # The features to exclude from the results. Separate multiple features with a comma (,).
        self.feature_display_exclude = feature_display_exclude
        # The ID of the data source for feature landing.
        self.feature_landing_resource_id = feature_landing_resource_id
        # The URI of the data source for feature landing.
        self.feature_landing_resource_uri = feature_landing_resource_uri
        # The high-priority features to read from the user table. If a feature is not found, the system retrieves it from the behavior table. Separate multiple features with a comma (,).
        self.feature_priority = feature_priority
        # The primary key for the item side in the feature store.
        self.feature_store_item_id = feature_store_item_id
        # The ID of the model in the feature store.
        self.feature_store_model_id = feature_store_model_id
        # The ID of the feature store project.
        self.feature_store_project_id = feature_store_project_id
        # The name of the feature store project.
        self.feature_store_project_name = feature_store_project_name
        # The name of the feature view that contains item features within the sequence features.
        self.feature_store_seq_feature_view = feature_store_seq_feature_view
        # The primary key for the user side in the feature store.
        self.feature_store_user_id = feature_store_user_id
        # The version of the `fg_jar` file.
        self.fg_jar_version = fg_jar_version
        # The name of the `fg_json` file.
        self.fg_json_file_name = fg_json_file_name
        # Indicates whether to generate a ZIP package.
        self.generate_zip = generate_zip
        # The time when the configuration was created.
        self.gmt_create_time = gmt_create_time
        # The time when the configuration was last updated.
        self.gmt_modified_time = gmt_modified_time
        # The name of the `item_id` field.
        self.item_id_field = item_id_field
        # The name of the item table.
        self.item_table = item_table
        # The partition field of the item table.
        self.item_table_partition_field = item_table_partition_field
        # The format of the partition field of the item table. Valid values:
        # 
        # - `yyyymmdd`
        # 
        # - `yyyy-mm-dd`
        self.item_table_partition_field_format = item_table_partition_field_format
        # The end time of the latest job based on this configuration.
        self.latest_job_gmt_sampling_end_time = latest_job_gmt_sampling_end_time
        # The start time of the latest job based on this configuration.
        self.latest_job_gmt_sampling_start_time = latest_job_gmt_sampling_start_time
        # The ID of the most recent job created from this configuration.
        self.latest_job_id = latest_job_id
        # The name of the feature consistency check configuration.
        self.name = name
        # The name of the OSS bucket.
        self.oss_bucket = oss_bucket
        # The ID of the OSS data source.
        self.oss_resource_id = oss_resource_id
        self.predict_worker_count = predict_worker_count
        self.predict_worker_cpu = predict_worker_cpu
        self.predict_worker_memory = predict_worker_memory
        self.resource_config = resource_config
        # The sample rate, a value from 0 to 1.
        self.sample_rate = sample_rate
        # The ID of the scene.
        self.scene_id = scene_id
        # The name of the scene.
        self.scene_name = scene_name
        self.security_group_id = security_group_id
        # The ID of the service.
        self.service_id = service_id
        # The name of the service.
        self.service_name = service_name
        # The status of the configuration. Valid values:
        # 
        # - `Editable`: The configuration is editable.
        # 
        # - `Uneditable`: The configuration is not editable.
        self.status = status
        self.switch_id = switch_id
        # Indicates whether to use a feature store. Valid values:
        # 
        # - `true`: A feature store is used. In this case, the response includes parameters such as `FeatureStoreProjectId`, `FeatureStoreProjectName`, `FeatureStoreModelId`, `FeatureStoreUserId`, and `FeatureStoreItemId`.
        # 
        # - `false`: A feature store is not used. In this case, the response includes parameters such as `UserTable`, `UserIdField`, `UserTablePartitionField`, `UserTablePartitionFieldFormat`, `ItemTable`, `ItemIdField`, `ItemTablePartitionField`, and `ItemTablePartitionFieldFormat`.
        self.use_feature_store = use_feature_store
        # The name of the `user_id` field.
        self.user_id_field = user_id_field
        # The name of the user table.
        self.user_table = user_table
        # The partition field of the user table.
        self.user_table_partition_field = user_table_partition_field
        # The format of the partition field of the user table. Valid values:
        # 
        # - `yyyymmdd`
        # 
        # - `yyyy-mm-dd`
        self.user_table_partition_field_format = user_table_partition_field_format
        self.vpc_id = vpc_id
        # The name of the workflow.
        self.workflow_name = workflow_name
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compare_feature is not None:
            result['CompareFeature'] = self.compare_feature

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_mount_path is not None:
            result['DatasetMountPath'] = self.dataset_mount_path

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type

        if self.dataset_uri is not None:
            result['DatasetUri'] = self.dataset_uri

        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route

        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name

        if self.easy_rec_package_path is not None:
            result['EasyRecPackagePath'] = self.easy_rec_package_path

        if self.easy_rec_version is not None:
            result['EasyRecVersion'] = self.easy_rec_version

        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id

        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude

        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id

        if self.feature_landing_resource_uri is not None:
            result['FeatureLandingResourceUri'] = self.feature_landing_resource_uri

        if self.feature_priority is not None:
            result['FeaturePriority'] = self.feature_priority

        if self.feature_store_item_id is not None:
            result['FeatureStoreItemId'] = self.feature_store_item_id

        if self.feature_store_model_id is not None:
            result['FeatureStoreModelId'] = self.feature_store_model_id

        if self.feature_store_project_id is not None:
            result['FeatureStoreProjectId'] = self.feature_store_project_id

        if self.feature_store_project_name is not None:
            result['FeatureStoreProjectName'] = self.feature_store_project_name

        if self.feature_store_seq_feature_view is not None:
            result['FeatureStoreSeqFeatureView'] = self.feature_store_seq_feature_view

        if self.feature_store_user_id is not None:
            result['FeatureStoreUserId'] = self.feature_store_user_id

        if self.fg_jar_version is not None:
            result['FgJarVersion'] = self.fg_jar_version

        if self.fg_json_file_name is not None:
            result['FgJsonFileName'] = self.fg_json_file_name

        if self.generate_zip is not None:
            result['GenerateZip'] = self.generate_zip

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field

        if self.item_table is not None:
            result['ItemTable'] = self.item_table

        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field

        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format

        if self.latest_job_gmt_sampling_end_time is not None:
            result['LatestJobGmtSamplingEndTime'] = self.latest_job_gmt_sampling_end_time

        if self.latest_job_gmt_sampling_start_time is not None:
            result['LatestJobGmtSamplingStartTime'] = self.latest_job_gmt_sampling_start_time

        if self.latest_job_id is not None:
            result['LatestJobId'] = self.latest_job_id

        if self.name is not None:
            result['Name'] = self.name

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_resource_id is not None:
            result['OssResourceId'] = self.oss_resource_id

        if self.predict_worker_count is not None:
            result['PredictWorkerCount'] = self.predict_worker_count

        if self.predict_worker_cpu is not None:
            result['PredictWorkerCpu'] = self.predict_worker_cpu

        if self.predict_worker_memory is not None:
            result['PredictWorkerMemory'] = self.predict_worker_memory

        if self.resource_config is not None:
            result['ResourceConfig'] = self.resource_config

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        if self.use_feature_store is not None:
            result['UseFeatureStore'] = self.use_feature_store

        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field

        if self.user_table is not None:
            result['UserTable'] = self.user_table

        if self.user_table_partition_field is not None:
            result['UserTablePartitionField'] = self.user_table_partition_field

        if self.user_table_partition_field_format is not None:
            result['UserTablePartitionFieldFormat'] = self.user_table_partition_field_format

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareFeature') is not None:
            self.compare_feature = m.get('CompareFeature')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetMountPath') is not None:
            self.dataset_mount_path = m.get('DatasetMountPath')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')

        if m.get('DatasetUri') is not None:
            self.dataset_uri = m.get('DatasetUri')

        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')

        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')

        if m.get('EasyRecPackagePath') is not None:
            self.easy_rec_package_path = m.get('EasyRecPackagePath')

        if m.get('EasyRecVersion') is not None:
            self.easy_rec_version = m.get('EasyRecVersion')

        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')

        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')

        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')

        if m.get('FeatureLandingResourceUri') is not None:
            self.feature_landing_resource_uri = m.get('FeatureLandingResourceUri')

        if m.get('FeaturePriority') is not None:
            self.feature_priority = m.get('FeaturePriority')

        if m.get('FeatureStoreItemId') is not None:
            self.feature_store_item_id = m.get('FeatureStoreItemId')

        if m.get('FeatureStoreModelId') is not None:
            self.feature_store_model_id = m.get('FeatureStoreModelId')

        if m.get('FeatureStoreProjectId') is not None:
            self.feature_store_project_id = m.get('FeatureStoreProjectId')

        if m.get('FeatureStoreProjectName') is not None:
            self.feature_store_project_name = m.get('FeatureStoreProjectName')

        if m.get('FeatureStoreSeqFeatureView') is not None:
            self.feature_store_seq_feature_view = m.get('FeatureStoreSeqFeatureView')

        if m.get('FeatureStoreUserId') is not None:
            self.feature_store_user_id = m.get('FeatureStoreUserId')

        if m.get('FgJarVersion') is not None:
            self.fg_jar_version = m.get('FgJarVersion')

        if m.get('FgJsonFileName') is not None:
            self.fg_json_file_name = m.get('FgJsonFileName')

        if m.get('GenerateZip') is not None:
            self.generate_zip = m.get('GenerateZip')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')

        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')

        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')

        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')

        if m.get('LatestJobGmtSamplingEndTime') is not None:
            self.latest_job_gmt_sampling_end_time = m.get('LatestJobGmtSamplingEndTime')

        if m.get('LatestJobGmtSamplingStartTime') is not None:
            self.latest_job_gmt_sampling_start_time = m.get('LatestJobGmtSamplingStartTime')

        if m.get('LatestJobId') is not None:
            self.latest_job_id = m.get('LatestJobId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssResourceId') is not None:
            self.oss_resource_id = m.get('OssResourceId')

        if m.get('PredictWorkerCount') is not None:
            self.predict_worker_count = m.get('PredictWorkerCount')

        if m.get('PredictWorkerCpu') is not None:
            self.predict_worker_cpu = m.get('PredictWorkerCpu')

        if m.get('PredictWorkerMemory') is not None:
            self.predict_worker_memory = m.get('PredictWorkerMemory')

        if m.get('ResourceConfig') is not None:
            self.resource_config = m.get('ResourceConfig')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        if m.get('UseFeatureStore') is not None:
            self.use_feature_store = m.get('UseFeatureStore')

        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')

        if m.get('UserTable') is not None:
            self.user_table = m.get('UserTable')

        if m.get('UserTablePartitionField') is not None:
            self.user_table_partition_field = m.get('UserTablePartitionField')

        if m.get('UserTablePartitionFieldFormat') is not None:
            self.user_table_partition_field_format = m.get('UserTablePartitionFieldFormat')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

