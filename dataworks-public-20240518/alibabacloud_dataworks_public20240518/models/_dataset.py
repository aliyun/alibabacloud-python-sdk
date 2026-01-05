# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class Dataset(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: int = None,
        creator_id: str = None,
        data_type: str = None,
        id: str = None,
        labels: List[main_models.DatasetLabel] = None,
        latest_version: main_models.DatasetVersion = None,
        modify_time: int = None,
        name: str = None,
        origin: str = None,
        project_id: int = None,
        readme: str = None,
        storage_type: str = None,
    ):
        self.comment = comment
        self.create_time = create_time
        self.creator_id = creator_id
        self.data_type = data_type
        self.id = id
        self.labels = labels
        self.latest_version = latest_version
        self.modify_time = modify_time
        self.name = name
        self.origin = origin
        self.project_id = project_id
        self.readme = readme
        self.storage_type = storage_type

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.latest_version:
            self.latest_version.validate()

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

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.id is not None:
            result['Id'] = self.id

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version.to_map()

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.readme is not None:
            result['Readme'] = self.readme

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.DatasetLabel()
                self.labels.append(temp_model.from_map(k1))

        if m.get('LatestVersion') is not None:
            temp_model = main_models.DatasetVersion()
            self.latest_version = temp_model.from_map(m.get('LatestVersion'))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Readme') is not None:
            self.readme = m.get('Readme')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

