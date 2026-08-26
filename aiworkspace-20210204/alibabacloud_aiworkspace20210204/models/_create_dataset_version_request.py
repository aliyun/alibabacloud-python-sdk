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
        import_info: str = None,
        labels: List[main_models.Label] = None,
        options: str = None,
        property: str = None,
        source_id: str = None,
        source_type: str = None,
        uri: str = None,
        user_metrics_endpoints: List[main_models.UserMetricsEndpoint] = None,
    ):
        # The number of dataset files.
        self.data_count = data_count
        # The size of space occupied by dataset files. Unit: bytes.
        self.data_size = data_size
        # The data source type. Separate multiple values with commas (,). Valid values:
        # 
        # - NAS: Alibaba Cloud Network Attached Storage (NAS).
        # 
        # - OSS: Alibaba Cloud Object Storage Service (OSS).
        # 
        # - CPFS
        # 
        # > The DataSourceType of the version must be consistent with the DataSourceType of the dataset. Validation is performed against the dataset when a version is created.
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # UserMetricsEndpoints
        self.dataset_task_ram_role = dataset_task_ram_role
        # The custom description of the dataset version, used to distinguish different dataset versions.
        self.description = description
        # The storage import configuration of the dataset. OSS, NAS, and CPFS are supported.
        # 
        # <details>
        # <summary>OSS</summary>
        # {<BR>
        #   "region": "${region}",//Region ID<BR>
        #   "bucket": "${bucket}",//Bucket name<BR>
        #   "path": "${path}" //File path<BR>
        # }<BR>
        # </details>
        # 
        # <details>
        # <summary>NAS</summary>
        # {<BR>
        #   "region": "${region}",//Region ID<BR>
        #   "fileSystemId": "${file_system_id}", //File system ID<BR>
        #   "path": "${path}", //File system path<BR>
        #   "mountTarget": "${mount_target}" //File system mount target<BR>
        # }<BR>
        # </details>
        # 
        # 
        # <details>
        # <summary>CPFS</summary>
        # {<BR>
        #   "region": "${region}",//Region ID<BR>
        #   "fileSystemId": "${file_system_id}", //File system ID<BR>
        #   "protocolServiceId":"${protocol_service_id}", //File system protocol service<BR>
        #   "exportId": "${export_id}", //File system export directory<BR>
        #   "path": "${path}",  //File system path<BR>
        # }<BR>
        # </details>
        # 
        # <details>
        # <summary>Lingjun CPFS</summary>
        # {<BR>
        #   "region": "${region}",//Region ID<BR>
        #   "fileSystemId": "${file_system_id}", //File system ID<BR>
        #   "path": "${path}",  //File system path<BR>
        #   "mountTarget": "${mount_target}" //File system mount target, specific to Lingjun edition<BR>
        #   "isVpcMount": boolean, //Whether it is a VPC mount target, specific to Lingjun edition<BR>
        # }<BR>
        # </details>
        self.import_info = import_info
        # The list of dataset version labels.
        self.labels = labels
        # The extended field in JsonString format.
        # When DLC uses a dataset, you can specify the default mount path of the dataset by configuring the mountPath field.
        self.options = options
        # The property of the dataset. Valid values:
        # - FILE: file.
        # - DIRECTORY: folder.
        # 
        # This parameter is required.
        self.property = property
        # The data source ID.
        # - If SourceType is USER, SourceId can be customized.
        # - If SourceType is ITAG, which indicates a dataset generated from iTAG annotation results, SourceId is the iTAG task ID.
        # - If SourceType is PAI_PUBLIC_DATASET, which indicates a dataset created from a PAI public dataset, SourceId is empty by default.
        self.source_id = source_id
        # The data source type. Default value: USER. Valid values:
        # - PAI-PUBLIC-DATASET: PAI public dataset.
        # - ITAG: dataset generated from iTAG annotation results.
        # - USER: user-registered dataset.
        self.source_type = source_type
        # Examples of Uri configurations:
        # - If the data source type is OSS: `oss://bucket.endpoint/object`
        # - If the data source type is NAS:
        # General-purpose NAS format: `nas://<nasfisid>.region/subpath/to/dir/`;
        # CPFS 1.0: `nas://<cpfs-fsid>.region/subpath/to/dir/`;
        # CPFS 2.0: `nas://<cpfs-fsid>.region/<protocolserviceid>/`.
        # CPFS 1.0 and CPFS 2.0 are distinguished by the format of the fsid: CPFS 1.0 format is cpfs-<8 ASCII characters>; CPFS 2.0 format is cpfs-<16 ASCII characters>.
        # 
        # This parameter is required.
        self.uri = uri
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

