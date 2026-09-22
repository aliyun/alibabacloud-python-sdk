# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAiAppDetailTopoShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        region_id: str = None,
        time_query_shrink: str = None,
    ):
        # The application ID that identifies a specific AI application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The region ID.
        self.region_id = region_id
        # The time query.
        self.time_query_shrink = time_query_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.time_query_shrink is not None:
            result['TimeQuery'] = self.time_query_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TimeQuery') is not None:
            self.time_query_shrink = m.get('TimeQuery')

        return self

