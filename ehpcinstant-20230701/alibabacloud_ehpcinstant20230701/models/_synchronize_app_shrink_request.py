# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SynchronizeAppShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        target_region_ids_shrink: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The list of arrays that are synchronized to the specified region. If \\"all\\" is included, it is synchronized to all other unsynchronized regions by default.
        self.target_region_ids_shrink = target_region_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.target_region_ids_shrink is not None:
            result['TargetRegionIds'] = self.target_region_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('TargetRegionIds') is not None:
            self.target_region_ids_shrink = m.get('TargetRegionIds')

        return self

