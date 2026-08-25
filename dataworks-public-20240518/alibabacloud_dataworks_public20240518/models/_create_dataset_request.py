# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateDatasetRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        data_type: str = None,
        init_version: main_models.CreateDatasetRequestInitVersion = None,
        name: str = None,
        origin: str = None,
        project_id: int = None,
        storage_type: str = None,
    ):
        # The description of the dataset. The value can be up to 1024 characters in length.
        self.comment = comment
        # The data type. Valid values:
        # - COMMON: general-purpose (default).
        # - PIC: image.
        # - TEXT: text.
        # - TABLE: table.
        # - VIDEO: video.
        # - AUDIO: audio.
        # - INDEX: index.
        self.data_type = data_type
        # The initial version of the dataset.
        # 
        # This parameter is required.
        self.init_version = init_version
        # The name of the dataset. The value must be a non-empty string that is up to 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The origin of the dataset. Only DataWorks is supported.
        self.origin = origin
        # The ID of the DataWorks workspace.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The storage type. Valid values:
        # - OSS: Object Storage Service.
        # - NAS: general-purpose NAS file storage.
        # - EXTREMENAS: extreme NAS file storage.
        # - DLF_LANCE: Data Lake Formation.
        # 
        # This parameter is required.
        self.storage_type = storage_type

    def validate(self):
        if self.init_version:
            self.init_version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.init_version is not None:
            result['InitVersion'] = self.init_version.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('InitVersion') is not None:
            temp_model = main_models.CreateDatasetRequestInitVersion()
            self.init_version = temp_model.from_map(m.get('InitVersion'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

class CreateDatasetRequestInitVersion(DaraModel):
    def __init__(
        self,
        comment: str = None,
        import_info: Dict[str, str] = None,
        mount_path: str = None,
        url: str = None,
    ):
        # The description. The value can be up to 1024 characters in length.
        self.comment = comment
        # The storage import configuration of the dataset. The required configuration varies depending on the storage type.
        # <details>
        # <summary>NAS</summary>
        # The values can be obtained from the response of the File Storage NAS API DescribeFileSystems operation.
        # 
        # ```JSON
        # {
        #   "fileSystemId": "3b6XXX89c9", // File system ID
        #   "fileSystemStorageType": "Performance", // Storage specification of the file system
        #   "vpcId": "vpc-uf66oxxxrqge1t2gson7s" // VPC ID of the mount target
        # }
        # ```
        # 
        # </details>
        self.import_info = import_info
        # The mount path. The value must start with /mnt/. Default value: /mnt/data.
        self.mount_path = mount_path
        # The URL.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.import_info is not None:
            result['ImportInfo'] = self.import_info

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ImportInfo') is not None:
            self.import_info = m.get('ImportInfo')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

