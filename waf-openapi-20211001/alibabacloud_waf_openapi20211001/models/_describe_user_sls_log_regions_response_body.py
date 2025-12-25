# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeUserSlsLogRegionsResponseBody(DaraModel):
    def __init__(
        self,
        log_regions: List[str] = None,
        request_id: str = None,
    ):
        # The region IDs.
        self.log_regions = log_regions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_regions is not None:
            result['LogRegions'] = self.log_regions

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogRegions') is not None:
            self.log_regions = m.get('LogRegions')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

