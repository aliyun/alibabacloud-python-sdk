# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScanNumRequest(DaraModel):
    def __init__(
        self,
        buckets: str = None,
        media_type: int = None,
        region_id: str = None,
    ):
        # Storage space.
        self.buckets = buckets
        # Media type.
        self.media_type = media_type
        # Region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buckets is not None:
            result['Buckets'] = self.buckets

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

