# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFileMetaShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        file_shrink: str = None,
        project_name: str = None,
    ):
        # The name of the dataset. You can obtain the name of the dataset from the response of the [CreateDataset](https://help.aliyun.com/document_detail/478160.html) operation.
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The file and its metadata items to be updated. The value must be in the JSON format.
        # 
        # This parameter is required.
        self.file_shrink = file_shrink
        # The name of the project. You can obtain the name of the project from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.file_shrink is not None:
            result['File'] = self.file_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('File') is not None:
            self.file_shrink = m.get('File')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

