# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgentPlatformShrinkRequest(DaraModel):
    def __init__(
        self,
        ai_platform_config_shrink: str = None,
        dbcluster_id: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.ai_platform_config_shrink = ai_platform_config_shrink
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_platform_config_shrink is not None:
            result['AiPlatformConfig'] = self.ai_platform_config_shrink

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiPlatformConfig') is not None:
            self.ai_platform_config_shrink = m.get('AiPlatformConfig')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

