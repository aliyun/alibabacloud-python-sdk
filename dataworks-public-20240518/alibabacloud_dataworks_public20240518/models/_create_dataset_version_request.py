# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateDatasetVersionRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        dataset_id: str = None,
        import_info: Dict[str, str] = None,
        mount_path: str = None,
        url: str = None,
    ):
        # The description of the dataset version. The length cannot exceed 1,024 characters.
        self.comment = comment
        # The ID of the dataset. Currently, only DataWorks datasets are supported.
        # 
        # This parameter is required.
        self.dataset_id = dataset_id
        # The storage import configuration of the dataset. The required configuration information varies based on the storage type.
        # <details>
        # <summary>NAS</summary>
        # For valid values, refer to the response of the DescribeFileSystems operation in the File Storage NAS API documentation.
        # 
        # ```JSON
        # {
        #   "fileSystemId": "3b6XXX89c9", // The ID of the file system.
        #   "fileSystemStorageType": "Performance", // The storage specification of the file system.
        #   "vpcId": "vpc-uf66oxxxrqge1t2gson7s" // The VPC ID of the mount target.
        # }
        # ```
        # 
        # </details>
        self.import_info = import_info
        # The mount path. It must start with /mnt/. Default value: /mnt/data.
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

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

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

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('ImportInfo') is not None:
            self.import_info = m.get('ImportInfo')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

