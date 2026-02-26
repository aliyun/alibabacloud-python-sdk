# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class RemoveStoryFilesRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        files: List[main_models.RemoveStoryFilesRequestFiles] = None,
        object_id: str = None,
        project_name: str = None,
    ):
        # The name of the dataset.
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The files that you want to delete.
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
                temp_model = main_models.RemoveStoryFilesRequestFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

class RemoveStoryFilesRequestFiles(DaraModel):
    def __init__(
        self,
        uri: str = None,
    ):
        # The URI of the Object Storage Service (OSS) bucket where you store the files that you want to delete.
        # 
        # Specify the value in the oss://${Bucket}/${Object} format. `${Bucket}` specifies the name of the OSS bucket that resides in the same region as the current project. `${Object}` specifies the complete path to the files that have an extension.
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

