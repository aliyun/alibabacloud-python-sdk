# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatasetVersionShrinkRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        dataset_id: str = None,
        import_info_shrink: str = None,
        mount_path: str = None,
        url: str = None,
    ):
        # The description for this dataset version. Maximum length: 1,024 characters.
        self.comment = comment
        # The dataset ID. Currently supports DataWorks datasets only.
        # 
        # This parameter is required.
        self.dataset_id = dataset_id
        # The storage import configuration for the dataset. Required configuration varies by storage type.
        # 
        # **NAS**
        # 
        # For valid values, see the response from the file storage API DescribeFileSystems.
        # 
        # ```JSON
        # {
        # "fileSystemId": "3b6XXX89c9", // The file system ID.
        # "fileSystemStorageType":  "Performance" // The file system storage type.
        # "vpcId": "vpc-uf66oxxxrqge1t2gson7s" // The VPC ID for the mount point.
        # }
        # ```
        self.import_info_shrink = import_info_shrink
        # The mount path, which must start with /mnt/. Default value: /mnt/data.
        self.mount_path = mount_path
        # URL
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

        if self.import_info_shrink is not None:
            result['ImportInfo'] = self.import_info_shrink

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
            self.import_info_shrink = m.get('ImportInfo')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

