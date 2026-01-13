# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFeatureConsistencyCheckJobConfigRequest(DaraModel):
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
        feature_display_exclude: str = None,
        feature_landing_resource_id: str = None,
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
        instance_id: str = None,
        item_id_field: str = None,
        item_table: str = None,
        item_table_partition_field: str = None,
        item_table_partition_field_format: str = None,
        name: str = None,
        oss_resource_id: str = None,
        predict_worker_count: int = None,
        predict_worker_cpu: int = None,
        predict_worker_memory: int = None,
        resource_config: str = None,
        sample_rate: float = None,
        scene_id: str = None,
        security_group_id: str = None,
        service_id: str = None,
        switch_id: str = None,
        use_feature_store: bool = None,
        user_id_field: str = None,
        user_table: str = None,
        user_table_partition_field: str = None,
        user_table_partition_field_format: str = None,
        vpc_id: str = None,
        workflow_name: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.compare_feature = compare_feature
        self.dataset_id = dataset_id
        self.dataset_mount_path = dataset_mount_path
        self.dataset_name = dataset_name
        self.dataset_type = dataset_type
        self.dataset_uri = dataset_uri
        self.default_route = default_route
        # This parameter is required.
        self.eas_service_name = eas_service_name
        self.easy_rec_package_path = easy_rec_package_path
        self.easy_rec_version = easy_rec_version
        self.feature_display_exclude = feature_display_exclude
        # This parameter is required.
        self.feature_landing_resource_id = feature_landing_resource_id
        self.feature_priority = feature_priority
        self.feature_store_item_id = feature_store_item_id
        self.feature_store_model_id = feature_store_model_id
        self.feature_store_project_id = feature_store_project_id
        self.feature_store_project_name = feature_store_project_name
        self.feature_store_seq_feature_view = feature_store_seq_feature_view
        self.feature_store_user_id = feature_store_user_id
        self.fg_jar_version = fg_jar_version
        # This parameter is required.
        self.fg_json_file_name = fg_json_file_name
        # This parameter is required.
        self.generate_zip = generate_zip
        # This parameter is required.
        self.instance_id = instance_id
        self.item_id_field = item_id_field
        self.item_table = item_table
        self.item_table_partition_field = item_table_partition_field
        self.item_table_partition_field_format = item_table_partition_field_format
        # This parameter is required.
        self.name = name
        self.oss_resource_id = oss_resource_id
        self.predict_worker_count = predict_worker_count
        self.predict_worker_cpu = predict_worker_cpu
        self.predict_worker_memory = predict_worker_memory
        self.resource_config = resource_config
        # This parameter is required.
        self.sample_rate = sample_rate
        # This parameter is required.
        self.scene_id = scene_id
        self.security_group_id = security_group_id
        # This parameter is required.
        self.service_id = service_id
        self.switch_id = switch_id
        # This parameter is required.
        self.use_feature_store = use_feature_store
        self.user_id_field = user_id_field
        self.user_table = user_table
        self.user_table_partition_field = user_table_partition_field
        self.user_table_partition_field_format = user_table_partition_field_format
        self.vpc_id = vpc_id
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

        if self.feature_display_exclude is not None:
            result['FeatureDisplayExclude'] = self.feature_display_exclude

        if self.feature_landing_resource_id is not None:
            result['FeatureLandingResourceId'] = self.feature_landing_resource_id

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field

        if self.item_table is not None:
            result['ItemTable'] = self.item_table

        if self.item_table_partition_field is not None:
            result['ItemTablePartitionField'] = self.item_table_partition_field

        if self.item_table_partition_field_format is not None:
            result['ItemTablePartitionFieldFormat'] = self.item_table_partition_field_format

        if self.name is not None:
            result['Name'] = self.name

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

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

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

        if m.get('FeatureDisplayExclude') is not None:
            self.feature_display_exclude = m.get('FeatureDisplayExclude')

        if m.get('FeatureLandingResourceId') is not None:
            self.feature_landing_resource_id = m.get('FeatureLandingResourceId')

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')

        if m.get('ItemTable') is not None:
            self.item_table = m.get('ItemTable')

        if m.get('ItemTablePartitionField') is not None:
            self.item_table_partition_field = m.get('ItemTablePartitionField')

        if m.get('ItemTablePartitionFieldFormat') is not None:
            self.item_table_partition_field_format = m.get('ItemTablePartitionFieldFormat')

        if m.get('Name') is not None:
            self.name = m.get('Name')

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

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

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

