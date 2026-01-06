# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDatasetFileMetasRequest(DaraModel):
    def __init__(
        self,
        dataset_file_meta_ids: str = None,
        dataset_version: str = None,
        workspace_id: str = None,
    ):
        # The metadata ID of the dataset file.
        # 
        # This parameter is required.
        self.dataset_file_meta_ids = dataset_file_meta_ids
        # The dataset version.
        self.dataset_version = dataset_version
        # The ID of the workspace to which the dataset belongs. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_file_meta_ids is not None:
            result['DatasetFileMetaIds'] = self.dataset_file_meta_ids

        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetFileMetaIds') is not None:
            self.dataset_file_meta_ids = m.get('DatasetFileMetaIds')

        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

