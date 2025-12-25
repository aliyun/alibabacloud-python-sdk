# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeHybridCloudSupportRegionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        support_regions: List[str] = None,
    ):
        self.request_id = request_id
        self.support_regions = support_regions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.support_regions is not None:
            result['SupportRegions'] = self.support_regions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportRegions') is not None:
            self.support_regions = m.get('SupportRegions')

        return self

