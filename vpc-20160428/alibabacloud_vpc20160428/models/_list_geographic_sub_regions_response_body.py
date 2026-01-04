# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListGeographicSubRegionsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        geographic_sub_regions: List[str] = None,
        request_id: str = None,
    ):
        # The number of entries.
        self.count = count
        # The region list.
        self.geographic_sub_regions = geographic_sub_regions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.geographic_sub_regions is not None:
            result['GeographicSubRegions'] = self.geographic_sub_regions

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('GeographicSubRegions') is not None:
            self.geographic_sub_regions = m.get('GeographicSubRegions')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

