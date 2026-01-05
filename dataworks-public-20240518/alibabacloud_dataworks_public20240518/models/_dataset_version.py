# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class DatasetVersion(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: int = None,
        creator_id: str = None,
        dataset_id: str = None,
        id: str = None,
        import_info: Dict[str, str] = None,
        labels: List[main_models.DatasetLabel] = None,
        modify_time: int = None,
        mount_path: str = None,
        storage_type: str = None,
        url: str = None,
        version_number: int = None,
    ):
        self.comment = comment
        self.create_time = create_time
        self.creator_id = creator_id
        self.dataset_id = dataset_id
        self.id = id
        self.import_info = import_info
        self.labels = labels
        self.modify_time = modify_time
        self.mount_path = mount_path
        self.storage_type = storage_type
        self.url = url
        self.version_number = version_number

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
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.id is not None:
            result['Id'] = self.id

        if self.import_info is not None:
            result['ImportInfo'] = self.import_info

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.url is not None:
            result['Url'] = self.url

        if self.version_number is not None:
            result['VersionNumber'] = self.version_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImportInfo') is not None:
            self.import_info = m.get('ImportInfo')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.DatasetLabel()
                self.labels.append(temp_model.from_map(k1))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('VersionNumber') is not None:
            self.version_number = m.get('VersionNumber')

        return self

