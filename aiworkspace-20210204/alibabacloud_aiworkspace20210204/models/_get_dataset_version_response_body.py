# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class GetDatasetVersionResponseBody(DaraModel):
    def __init__(
        self,
        data_count: int = None,
        data_size: int = None,
        data_source_type: str = None,
        dataset_id: str = None,
        dataset_task_ram_role: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        import_info: str = None,
        labels: List[main_models.Label] = None,
        mount_access: str = None,
        options: str = None,
        property: str = None,
        request_id: str = None,
        source_id: str = None,
        source_type: str = None,
        uri: str = None,
        user_metrics_endpoints: List[main_models.UserMetricsEndpoint] = None,
        version_name: str = None,
    ):
        # The data volume.
        self.data_count = data_count
        # The dataset size.
        self.data_size = data_size
        # The data source type.
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # The primary resource ID.
        self.dataset_id = dataset_id
        # DatasetTaskRamRole
        self.dataset_task_ram_role = dataset_task_ram_role
        # The version description.
        self.description = description
        # The creation time.
        self.gmt_create_time = gmt_create_time
        # The last modification time.
        self.gmt_modified_time = gmt_modified_time
        # The storage import configuration of the dataset. OSS, NAS, and CPFS are supported.
        # 
        # <details>
        # <summary>OSS</summary>
        # {
        # "region": "${region}",//The region ID.
        # "bucket": "${bucket}",//The bucket name.
        # "path": "${path}" //The file path.
        # }
        # </details>
        # 
        # <details>
        # <summary>NAS</summary>
        # 
        # </details>
        # 
        # <details>
        # <summary>CPFS</summary>
        # Block content
        # </details>
        # 
        # 
        # <details>
        # <summary>Intelligent computing CPFS</summary>
        # Block content
        # </details>
        self.import_info = import_info
        # The resource labels.
        self.labels = labels
        # The permission when the dataset is mounted. Valid values:
        # - RO: read-only mount
        # - RW: read and write mount
        self.mount_access = mount_access
        # The extension field.
        self.options = options
        # The property of the dataset.
        # 
        # This parameter is required.
        self.property = property
        # Id of the request
        self.request_id = request_id
        # The dataset source ID.
        self.source_id = source_id
        # The data source type.
        self.source_type = source_type
        # The URI configuration example.
        # 
        # This parameter is required.
        self.uri = uri
        self.user_metrics_endpoints = user_metrics_endpoints
        # The dataset version.
        self.version_name = version_name

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.user_metrics_endpoints:
            for v1 in self.user_metrics_endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_count is not None:
            result['DataCount'] = self.data_count

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_task_ram_role is not None:
            result['DatasetTaskRamRole'] = self.dataset_task_ram_role

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.import_info is not None:
            result['ImportInfo'] = self.import_info

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access

        if self.options is not None:
            result['Options'] = self.options

        if self.property is not None:
            result['Property'] = self.property

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.uri is not None:
            result['Uri'] = self.uri

        result['UserMetricsEndpoints'] = []
        if self.user_metrics_endpoints is not None:
            for k1 in self.user_metrics_endpoints:
                result['UserMetricsEndpoints'].append(k1.to_map() if k1 else None)

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetTaskRamRole') is not None:
            self.dataset_task_ram_role = m.get('DatasetTaskRamRole')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('ImportInfo') is not None:
            self.import_info = m.get('ImportInfo')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Property') is not None:
            self.property = m.get('Property')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        self.user_metrics_endpoints = []
        if m.get('UserMetricsEndpoints') is not None:
            for k1 in m.get('UserMetricsEndpoints'):
                temp_model = main_models.UserMetricsEndpoint()
                self.user_metrics_endpoints.append(temp_model.from_map(k1))

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

