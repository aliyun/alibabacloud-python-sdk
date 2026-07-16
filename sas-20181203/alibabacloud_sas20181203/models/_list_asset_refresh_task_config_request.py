# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAssetRefreshTaskConfigRequest(DaraModel):
    def __init__(
        self,
        refresh_config_type: int = None,
        region_id: str = None,
        target_id: int = None,
    ):
        # The configuration type. Valid values:
        # - **0**: host refresh task
        # - **1**: cloud service refresh task
        # - **2**: AccessKey scheduled verification task.
        self.refresh_config_type = refresh_config_type
        # The region of the Security Center instance.
        self.region_id = region_id
        # The ID of the AccessKey record specified when querying an AccessKey scheduled verification task.
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.refresh_config_type is not None:
            result['RefreshConfigType'] = self.refresh_config_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefreshConfigType') is not None:
            self.refresh_config_type = m.get('RefreshConfigType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        return self

