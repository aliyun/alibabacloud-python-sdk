# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class GetDatasetFileMetaResponseBody(DaraModel):
    def __init__(
        self,
        dataset_file_meta: main_models.DatasetFileMetaContentGet = None,
        dataset_id: str = None,
        dataset_version: str = None,
        request_id: str = None,
        workspace_id: str = None,
    ):
        # The queried metadata records of dataset files.
        self.dataset_file_meta = dataset_file_meta
        # The dataset ID.
        self.dataset_id = dataset_id
        # The dataset version.
        self.dataset_version = dataset_version
        # The request ID.
        self.request_id = request_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.dataset_file_meta:
            self.dataset_file_meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_file_meta is not None:
            result['DatasetFileMeta'] = self.dataset_file_meta.to_map()

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_version is not None:
            result['DatasetVersion'] = self.dataset_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetFileMeta') is not None:
            temp_model = main_models.DatasetFileMetaContentGet()
            self.dataset_file_meta = temp_model.from_map(m.get('DatasetFileMeta'))

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetVersion') is not None:
            self.dataset_version = m.get('DatasetVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

