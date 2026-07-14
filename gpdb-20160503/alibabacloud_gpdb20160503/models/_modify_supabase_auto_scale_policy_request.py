# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySupabaseAutoScalePolicyRequest(DaraModel):
    def __init__(
        self,
        auto_scale: bool = None,
        project_id: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable **automatic start and stop**. Valid values:
        # - true: Enabled. After this feature is enabled, Supabase automatically pauses and resumes based on traffic conditions.
        # - false: Disabled. After this feature is disabled, the automatic start and stop feature of Supabase is turned off.
        # 
        # This parameter is required.
        self.auto_scale = auto_scale
        # The ID of the Supabase project. You can obtain the workspace ID from the Supabase page in the console.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID of the instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_scale is not None:
            result['AutoScale'] = self.auto_scale

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoScale') is not None:
            self.auto_scale = m.get('AutoScale')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

