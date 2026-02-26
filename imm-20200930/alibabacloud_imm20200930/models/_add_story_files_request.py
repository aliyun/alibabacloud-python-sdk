# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class AddStoryFilesRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        files: List[main_models.AddStoryFilesRequestFiles] = None,
        object_id: str = None,
        project_name: str = None,
    ):
        # The name of the dataset.
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The objects that you want to add.
        # 
        # This parameter is required.
        self.files = files
        # The ID of the story.
        # 
        # This parameter is required.
        self.object_id = object_id
        # The name of the project.
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.AddStoryFilesRequestFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

class AddStoryFilesRequestFiles(DaraModel):
    def __init__(
        self,
        uri: str = None,
    ):
        # The URI of the object.
        # 
        # Specify the OSS URI in the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

