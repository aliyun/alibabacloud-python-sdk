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
        # The number of dataset files.
        self.data_count = data_count
        # The size of the dataset file. Unit: bytes.
        self.data_size = data_size
        # The type of the data source. Separate multiple types with commas (,). Valid values:
        # 
        # *   NAS: File Storage NAS (NAS).
        # *   OSS: Object Storage Service (OSS).
        # *   CPFS
        # 
        # Note: The DataSourceType value of a dataset version must be the same as that of the dataset. When you create a dataset version, the system checks whether the values are the same.
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # The description of the dataset. Descriptions are used to differentiate datasets.
        self.description = description
        # The dataset storage import configurations, such as OSS, NAS, and CPFS.
        # 
        # **OSS**
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "bucket": "${bucket}",//The bucket name\\
        # "path": "${path}" // The file path\\
        # }\\
        # 
        # 
        # **NAS**
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "fileSystemId": "${file_system_id}", // The file system ID\\
        # "path": "${path}", // The file system path\\
        # "mountTarget": "${mount_target}" // The mount point of the file system\\
        # }\\
        # 
        # 
        # **CPFS**
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "fileSystemId": "${file_system_id}", // The file system ID\\
        # "protocolServiceId":"${protocol_service_id}", // The file system protocol service\\
        # "exportId": "${export_id}", // The file system export directory\\
        # "path": "${path}", // The file system path\\
        # }\\
        # 
        # 
        # **CPFS for Lingjun**
        # 
        # {\\
        # "region": "${region}",// The region ID\\
        # "fileSystemId": "${file_system_id}", // The file system ID\\
        # "path": "${path}", // The ile system path\\
        # "mountTarget": "${mount_target}" // The mount point of the file system, CPFS for Lingjun only\\
        # "isVpcMount": boolean, // Whether the mount point is a VPC mount point, CPFS for Lingjun only\\
        # }\\
        self.import_info = import_info
        # The tags of the dataset version.
        self.labels = labels
        # The extended field, which is of the JsonString type. When you use the dataset in Deep Learning Containers (DLC), you can use the mountPath field to specify the default mount path of the dataset.
        self.options = options
        # The property of the dataset. Valid values:
        # 
        # *   FILE
        # *   DIRECTORY
        # 
        # This parameter is required.
        self.property = property
        # The ID of the data source.
        # 
        # *   If SourceType is set to USER, the value of SourceId can be a custom string.
        # *   If SourceType is set to ITAG, the value of SourceId is the ID of the labeling job of iTAG.
        # *   If SourceType is set to PAI_PUBLIC_DATASET, SourceId is empty by default.
        self.source_id = source_id
        # The type of the data source. Default value: USER. Valid values:
        # 
        # *   PAI-PUBLIC-DATASET: a public dataset of Platform for AI (PAI).
        # *   ITAG: a dataset generated from a labeling job of iTAG.
        # *   USER: a dataset registered by a user.
        # 
        # For each job type:
        # 
        # *   PAI_PUBLIC_DATASET: PAI_PUBLIC_DATASET.
        # *   ITAG: ITAG.
        # *   USER: USER.
        self.source_type = source_type
        # Example format:
        # 
        # *   Value format when DataSourceType is set to OSS: `oss://bucket.endpoint/object`.
        # *   Value formats when DataSourceType is set to NAS: General-purpose NAS: `nas://<nasfisid>.region/subpath/to/dir/`. CPFS 1.0: `nas://<cpfs-fsid>.region/subpath/to/dir/`. CPFS 2.0: `nas://<cpfs-fsid>.region/<protocolserviceid>/`. You can distinguish CPFS 1.0 and CPFS 2.0 file systems based on the format of the file system ID: The ID for CPFS 1.0 is in the cpfs-<8-bit ASCII characters> format. The ID for CPFS 2.0 is in the cpfs-<16-bit ASCII characters> format.
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

