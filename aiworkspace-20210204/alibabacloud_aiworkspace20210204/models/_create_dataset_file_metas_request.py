# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateDatasetFileMetasRequest(DaraModel):
    def __init__(
        self,
        dataset_file_metas: List[main_models.DatasetFileMetaContentCreate] = None,
        dataset_version: str = None,
        workspace_id: str = None,
    ):
        # The metadata of the file.
        # 
        # This parameter is required.
        self.dataset_file_metas = dataset_file_metas
        # The dataset version name.
        # 
        # This parameter is required.
        self.dataset_version = dataset_version
        # The ID of the workspace to which the dataset belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.dataset_file_metas:
            for v1 in self.dataset_file_metas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatasetFileMetas'] = []
        if self.dataset_file_metas is not None:
            for k1 in self.dataset_file_metas:
                result['DatasetFileMetas'].append(k1.to_map() if k1 else None)

        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dataset_file_metas = []
        if m.get('DatasetFileMetas') is not None:
            for k1 in m.get('DatasetFileMetas'):
                temp_model = main_models.DatasetFileMetaContentCreate()
                self.dataset_file_metas.append(temp_model.from_map(k1))

        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

