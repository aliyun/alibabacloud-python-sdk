# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class DescribeRegionResourceTypeAutoEnableResponseBody(DaraModel):
    def __init__(
        self,
        region_resource_auto_enable: Dict[str, dict] = None,
        request_id: str = None,
    ):
        self.region_resource_auto_enable = region_resource_auto_enable
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_resource_auto_enable is not None:
            result['RegionResourceAutoEnable'] = self.region_resource_auto_enable

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionResourceAutoEnable') is not None:
            self.region_resource_auto_enable = m.get('RegionResourceAutoEnable')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

