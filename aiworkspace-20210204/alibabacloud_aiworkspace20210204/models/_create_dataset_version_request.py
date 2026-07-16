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
        description: str = None,
        import_info: str = None,
        labels: List[main_models.Label] = None,
        options: str = None,
        property: str = None,
        source_id: str = None,
        source_type: str = None,
        uri: str = None,
    ):
        # The number of files in the dataset.
        self.data_count = data_count
        # The size of the space occupied by the dataset files. Unit: bytes.
        self.data_size = data_size
        # The type of the data source. If you specify multiple types, separate them with commas (,). Valid values:
        # 
        # - NAS: The data is stored in Alibaba Cloud File Storage (NAS).
        # 
        # - OSS: The data is stored in Alibaba Cloud Object Storage Service (OSS).
        # 
        # - CPFS
        # 
        # Note: The DataSourceType of the version must be the same as the DataSourceType of the dataset. The system verifies this consistency when you create the version.
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # A custom description for the dataset version. This helps distinguish different dataset versions.
        self.description = description
        # The storage import configuration of the dataset. Supported storage types include OSS, NAS, and CPFS.
        # 
        # <details>
        # 
        # <summary>
        # 
        # OSS
        # 
        # </summary>
        # 
        # {<br>
        # "region": "${region}",// The region ID.<br>
        # "bucket": "${bucket}",// The bucket name.<br>
        # "path": "${path}" // The file path.<br>
        # }
        # 
        # </details>
        # 
        # <details>
        # 
        # <summary>
        # 
        # NAS
        # 
        # </summary>
        # 
        # {<br>
        # "region": "${region}",// The region ID.<br>
        # "fileSystemId": "${file_system_id}", // The file system ID.<br>
        # "path": "${path}", // The file system path.<br>
        # "mountTarget": "${mount_target}" // The mount target of the file system.<br>
        # }
        # 
        # </details>
        # 
        # <details>
        # 
        # <summary>
        # 
        # CPFS
        # 
        # </summary>
        # 
        # {<br>
        # "region": "${region}",// The region ID.<br>
        # "fileSystemId": "${file_system_id}", // The file system ID.<br>
        # "protocolServiceId":"${protocol_service_id}", // The protocol service of the file system.<br>
        # "exportId": "${export_id}", // The exported directory of the file system.<br>
        # "path": "${path}", // The file system path.<br>
        # }
        # 
        # </details>
        # 
        # <details>
        # 
        # <summary>
        # 
        # Intelligent Computing CPFS
        # 
        # </summary>
        # 
        # {<br>
        # "region": "${region}",// The region ID.<br>
        # "fileSystemId": "${file_system_id}", // The file system ID.<br>
        # "path": "${path}", // The file system path.<br>
        # "mountTarget": "${mount_target}", // The mount target of the file system. This parameter is specific to the Intelligent Computing edition.<br>
        # "isVpcMount": boolean, // Specifies whether the mount target is in a VPC. This parameter is specific to the Intelligent Computing edition.<br>
        # }
        # 
        # </details>
        self.import_info = import_info
        # A list of tags for the dataset version.
        self.labels = labels
        # The extended field, which is a JSON string.
        # When DLC uses the dataset, you can configure the mountPath field to specify the default mount path for the dataset.
        self.options = options
        # The property of the dataset. Valid values:
        # 
        # - FILE: A file.
        # 
        # - DIRECTORY: A folder.
        # 
        # This parameter is required.
        self.property = property
        # The ID of the data source.
        # 
        # - If SourceType is set to USER, you can customize the SourceId.
        # 
        # - If SourceType is set to ITAG, which indicates a dataset generated from the annotation results of the iTAG module, SourceId is the task ID from iTAG.
        # 
        # - If SourceType is set to PAI_PUBLIC_DATASET, which indicates a dataset created from a public PAI dataset, SourceId is empty by default.
        self.source_id = source_id
        # The type of the data source. The default value is USER. Valid values:
        # 
        # - PAI-PUBLIC-DATASET: a public dataset from PAI.
        # 
        # - ITAG: a dataset generated from the annotation results of the iTAG module.
        # 
        # - USER: a dataset registered by a user.
        self.source_type = source_type
        # The following examples show how to configure the URI:
        # 
        # - If the data source type is OSS: `oss://bucket.endpoint/object`
        # 
        # - If the data source type is NAS:
        #   The format for a general-purpose NAS file system is `nas://<nasfisid>.region/subpath/to/dir/`.
        #   CPFS 1.0: `nas://<cpfs-fsid>.region/subpath/to/dir/`.
        #   CPFS 2.0: `nas://<cpfs-fsid>.region/<protocolserviceid>/`.
        #   CPFS 1.0 and CPFS 2.0 are distinguished by the format of the fsid. The format for CPFS 1.0 is cpfs-<8 ASCII characters>. The format for CPFS 2.0 is cpfs-<16 ASCII characters>.
        # 
        # This parameter is required.
        self.uri = uri

    def validate(self):
        if self.labels:
            for v1 in self.labels:
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

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

        return self

