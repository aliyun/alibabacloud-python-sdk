# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatasetShrinkRequest(DaraModel):
    def __init__(
        self,
        access_level: str = None,
        dataset_config_shrink: str = None,
        dataset_description: str = None,
        dataset_name: str = None,
        dataset_type: str = None,
        document_handle_config_shrink: str = None,
        invoke_type: str = None,
        search_dataset_enable: int = None,
        workspace_id: str = None,
    ):
        self.access_level = access_level
        # The dataset search configuration.
        self.dataset_config_shrink = dataset_config_shrink
        # The description of the dataset. This is the display name in the console. Use a human-readable name.
        self.dataset_description = dataset_description
        # The name of the dataset. The name must be globally unique.
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The type of the dataset. Valid values:
        # 
        # - CustomSemanticSearch: A custom semantic index. This is the default value. Upload documents to build the dataset.
        # 
        # - ThirdSearch: A third-party search source (API). Configure your own search API.
        self.dataset_type = dataset_type
        # Dataset index configuration.
        self.document_handle_config_shrink = document_handle_config_shrink
        # The invocation method. Currently, only portal is supported, which indicates an invocation from the console.
        # 
        # - If left empty: When DatasetType is ThirdSearch, datasetConfig.SearchSourceConfigs (third-party API definition) is required.
        # 
        # - If set to portal: When DatasetType is ThirdSearch, the system initializes a SearchSourceConfigs (third-party API demo) example by default for your reference.
        self.invoke_type = invoke_type
        # The dataset search switch. Valid values:
        # 
        # - 0: Disabled for all.
        # 
        # - 1: Visible only to Miao Search.
        # 
        # - 2: Visible only to Miao Bi.
        # 
        # - 3: Visible to both Miao Search and Miao Bi. This is the default value.
        self.search_dataset_enable = search_dataset_enable
        # The unique ID of the Alibaba Cloud Model Studio workspace. For more information, see [Obtain a workspace ID](https://help.aliyun.com/document_detail/2782167.html).
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_level is not None:
            result['AccessLevel'] = self.access_level

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
        if m.get('AccessLevel') is not None:
            self.access_level = m.get('AccessLevel')

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

