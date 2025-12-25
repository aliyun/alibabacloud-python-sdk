# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatasetShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_config_shrink: str = None,
        dataset_description: str = None,
        dataset_name: str = None,
        dataset_type: str = None,
        document_handle_config_shrink: str = None,
        invoke_type: str = None,
        search_dataset_enable: int = None,
        workspace_id: str = None,
    ):
        self.dataset_config_shrink = dataset_config_shrink
        self.dataset_description = dataset_description
        # This parameter is required.
        self.dataset_name = dataset_name
        self.dataset_type = dataset_type
        self.document_handle_config_shrink = document_handle_config_shrink
        self.invoke_type = invoke_type
        self.search_dataset_enable = search_dataset_enable
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_config_shrink is not None:
            result['DatasetConfig'] = self.dataset_config_shrink

        if self.dataset_description is not None:
            result['DatasetDescription'] = self.dataset_description

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type

        if self.document_handle_config_shrink is not None:
            result['DocumentHandleConfig'] = self.document_handle_config_shrink

        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type

        if self.search_dataset_enable is not None:
            result['SearchDatasetEnable'] = self.search_dataset_enable

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetConfig') is not None:
            self.dataset_config_shrink = m.get('DatasetConfig')

        if m.get('DatasetDescription') is not None:
            self.dataset_description = m.get('DatasetDescription')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')

        if m.get('DocumentHandleConfig') is not None:
            self.document_handle_config_shrink = m.get('DocumentHandleConfig')

        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')

        if m.get('SearchDatasetEnable') is not None:
            self.search_dataset_enable = m.get('SearchDatasetEnable')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

