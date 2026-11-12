# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRdUsersRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region of the data management center for Threat Analysis. Select the region of the data management center based on the region where your assets reside. Valid values:
        # - cn-hangzhou: Assets reside in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: Assets reside in regions outside China.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

