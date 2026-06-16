# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSuspEventsShrinkRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        sdk_request_shrink: str = None,
    ):
        self.region_id = region_id
        self.sdk_request_shrink = sdk_request_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sdk_request_shrink is not None:
            result['SdkRequest'] = self.sdk_request_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SdkRequest') is not None:
            self.sdk_request_shrink = m.get('SdkRequest')

        return self

