# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDetectionStatisticRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # - cn-hangzhou: China (Hangzhou). Your assets reside in the Chinese mainland.
        # - ap-southeast-1: Singapore. Your assets reside outside China.
        self.region_id = region_id
        # The ID of the member to which the administrator switches the view.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

