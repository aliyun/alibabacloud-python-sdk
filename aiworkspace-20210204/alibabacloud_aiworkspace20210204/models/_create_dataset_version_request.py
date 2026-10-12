# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateDatasetVersionRequest(DaraModel):
    def __init__(
        self,
        data_count: int = None,
        data_size: int = None,
        data_source_type: str = None,
        dataset_task_ram_role: str = None,
        description: str = None,
        dry_run: bool = None,
        import_info: str = None,
        labels: List[main_models.Label] = None,
        options: str = None,
        property: str = None,
        source_id: str = None,
        source_type: str = None,
        uri: str = None,
        user_metrics_endpoints: List[main_models.UserMetricsEndpoint] = None,
    ):
        # The number of files in the dataset.
        self.data_count = data_count
        # The size of the space occupied by the dataset files. Unit: bytes.
        self.data_size = data_size
        # The data source type. Separate multiple values with commas. Valid values:
        # 
        # - NAS: Alibaba Cloud File Storage NAS.
        # 
        # - OSS: Alibaba Cloud Object Storage Service (OSS).
        # 
        # - CPFS
        # 
        # Note: The DataSourceType of the version must be the same as the DataSourceType of the dataset. The system validates this when you create the version.
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # UserMetricsEndpoints
        self.dataset_task_ram_role = dataset_task_ram_role
        # The custom description of the dataset version. You can use this description to distinguish between different dataset versions.
        self.description = description
        # Specifies whether to perform only a dry run without actually creating the dataset version.
        self.dry_run = dry_run
        # The storage import configuration of the dataset. OSS, NAS, and CPFS are supported.
        # 
        # <details>
        # <summary>OSS</summary>
        # {<BR>
        #   "region": "${region}",// The region ID.<BR>
        #   "bucket": "${bucket}",// The bucket name.<BR>
        #   "path": "${path}" // The file path.<BR>
        # }<BR>
        # </details>
        # 
        # <details>
        # <summary>NAS</summary>
        # {<BR>
        #   "region": "${region}",// The region ID.<BR>
        #   "fileSystemId": "${file_system_id}", // The file system ID.<BR>
        #   "path": "${path}", // The file system path.<BR>
        #   "mountTarget": "${mount_target}" // The mount target of the file system.<BR>
        # }<BR>
        # </details>
        # 
        # 
        # <details>
        # <summary>CPFS</summary>
        # {<BR>
        #   "region": "${region}",// The region ID.<BR>
        #   "fileSystemId": "${file_system_id}", // The file system ID.<BR>
        #   "protocolServiceId":"${protocol_service_id}", // The protocol service of the file system.<BR>
        #   "exportId": "${export_id}", // The export directory of the file system.<BR>
        #   "path": "${path}",  // The file system path.<BR>
        # }<BR>
        # </details>
        # 
        # <details>
        # <summary>CPFS for AI computing</summary>
        # {<BR>
        #   "region": "${region}",// The region ID.<BR>
        #   "fileSystemId": "${file_system_id}", // The file system ID.<BR>
        #   "path": "${path}",  // The file system path.<BR>
        #   "mountTarget": "${mount_target}" // The mount target of the file system. This parameter is specific to the AI computing edition.<BR>
        #   "isVpcMount": boolean, // Specifies whether the mount target is a VPC mount target. This parameter is specific to the AI computing edition.<BR>
        # }<BR>
        # </details>
        self.import_info = import_info
        # The list of labels for the dataset version.
        self.labels = labels
        # The extended field. The value is a JSON string. When DLC uses the dataset, you can configure the mountPath field to specify the default mount path for the dataset.
        self.options = options
        # The property of the dataset. Valid values:
        # - FILE: file
        # - DIRECTORY: directory
        # 
        # This parameter is required.
        self.property = property
        # The source ID.
        # - If SourceType is set to USER, you can specify a custom SourceId.
        # - If SourceType is set to ITAG, the dataset is generated from the labeling results of the iTAG module, and SourceId is the task ID in iTAG.
        # - If SourceType is set to PAI_PUBLIC_DATASET, the dataset is created from a PAI public dataset, and SourceId is empty by default.
        self.source_id = source_id
        # The source type. Default value: USER. Valid values:
        # - PAI-PUBLIC-DATASET: PAI public dataset.
        # - ITAG: dataset generated from the labeling results of the iTAG module.
        # - USER: user-registered dataset.
        self.source_type = source_type
        # The URI. Configuration examples:
        # - If the data source type is OSS: `oss://bucket.endpoint/object`
        # - If the data source type is NAS:
        #   For general-purpose NAS, the format is `nas://<nasfisid>.region/subpath/to/dir/`.
        #   For CPFS 1.0, the format is `nas://<cpfs-fsid>.region/subpath/to/dir/`.
        #   For CPFS 2.0, the format is `nas://<cpfs-fsid>.region/<protocolserviceid>/`.
        #   CPFS 1.0 and CPFS 2.0 are distinguished by the format of the fsid: the format for CPFS 1.0 is cpfs-<8 ASCII characters>, and the format for CPFS 2.0 is cpfs-<16 ASCII characters>.
        # 
        # This parameter is required.
        self.uri = uri
        # The list of user metric collection endpoints.
        self.user_metrics_endpoints = user_metrics_endpoints

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

        if self.dataset_task_ram_role is not None:
            result['DatasetTaskRamRole'] = self.dataset_task_ram_role

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.import_info is not None:
            result['ImportInfo'] = self.import_info

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.options is not None:
            result['Options'] = self.options

        if self.property is not None:
            result['Property'] = self.property

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DatasetTaskRamRole') is not None:
            self.dataset_task_ram_role = m.get('DatasetTaskRamRole')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ImportInfo') is not None:
            self.import_info = m.get('ImportInfo')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Property') is not None:
            self.property = m.get('Property')

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

        return self

