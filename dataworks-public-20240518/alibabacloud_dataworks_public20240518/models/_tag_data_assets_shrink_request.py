# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TagDataAssetsShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_trace_enabled: bool = None,
        data_asset_ids_shrink: str = None,
        data_asset_type: str = None,
        env_type: str = None,
        project_id: int = None,
        tags_shrink: str = None,
    ):
        # Specifies whether to enable lineage-based automatic backtracking.
        self.auto_trace_enabled = auto_trace_enabled
        # The data asset IDs.
        # 
        # This parameter is required.
        self.data_asset_ids_shrink = data_asset_ids_shrink
        # The type of the data asset. Valid values:
        # 
        # *   ACS::DataWorks::Table
        # *   ACS::DataWorks::Task
        # 
        # This parameter is required.
        self.data_asset_type = data_asset_type
        # The environment of the workspace to which the data asset belongs. Valid values:
        # 
        # *   Dev: development environment
        # *   Prod: production environment
        self.env_type = env_type
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The tags that you want to add to data assets.
        # 
        # This parameter is required.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_trace_enabled is not None:
            result['AutoTraceEnabled'] = self.auto_trace_enabled

        if self.data_asset_ids_shrink is not None:
            result['DataAssetIds'] = self.data_asset_ids_shrink

        if self.data_asset_type is not None:
            result['DataAssetType'] = self.data_asset_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoTraceEnabled') is not None:
            self.auto_trace_enabled = m.get('AutoTraceEnabled')

        if m.get('DataAssetIds') is not None:
            self.data_asset_ids_shrink = m.get('DataAssetIds')

        if m.get('DataAssetType') is not None:
            self.data_asset_type = m.get('DataAssetType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

