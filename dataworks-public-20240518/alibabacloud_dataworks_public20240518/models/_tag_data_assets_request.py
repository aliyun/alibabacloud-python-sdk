# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class TagDataAssetsRequest(DaraModel):
    def __init__(
        self,
        auto_trace_enabled: bool = None,
        data_asset_ids: List[str] = None,
        data_asset_type: str = None,
        env_type: str = None,
        project_id: int = None,
        tags: List[main_models.TagDataAssetsRequestTags] = None,
    ):
        # Specifies whether to enable automatic data lineage backtracking.
        self.auto_trace_enabled = auto_trace_enabled
        # The list of unique IDs of the data assets. You can call the ListDataAssets operation to query the IDs of data assets to which tags can be attached.
        # 
        # This parameter is required.
        self.data_asset_ids = data_asset_ids
        # The data asset type. Valid values:
        # - DataWorks table (ACS::DataWorks::Table)
        # - DataWorks scheduled task (ACS::DataWorks::Task)
        # 
        # This parameter is required.
        self.data_asset_type = data_asset_type
        # The workspace environment to which the data asset belongs. Valid values:
        # - Dev (development environment)
        # - Prod (production environment)
        self.env_type = env_type
        # The ID of the workspace.
        self.project_id = project_id
        # The list of data asset tags to attach.
        # 
        # This parameter is required.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_trace_enabled is not None:
            result['AutoTraceEnabled'] = self.auto_trace_enabled

        if self.data_asset_ids is not None:
            result['DataAssetIds'] = self.data_asset_ids

        if self.data_asset_type is not None:
            result['DataAssetType'] = self.data_asset_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoTraceEnabled') is not None:
            self.auto_trace_enabled = m.get('AutoTraceEnabled')

        if m.get('DataAssetIds') is not None:
            self.data_asset_ids = m.get('DataAssetIds')

        if m.get('DataAssetType') is not None:
            self.data_asset_type = m.get('DataAssetType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.TagDataAssetsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class TagDataAssetsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # This parameter is required.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

