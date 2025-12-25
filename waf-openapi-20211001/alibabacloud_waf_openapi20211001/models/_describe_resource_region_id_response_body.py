# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeResourceRegionIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_region_ids: List[str] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The region IDs of the resources that are added to Web Application Firewall (WAF) by using the SDK integration mode.
        self.resource_region_ids = resource_region_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_region_ids is not None:
            result['ResourceRegionIds'] = self.resource_region_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceRegionIds') is not None:
            self.resource_region_ids = m.get('ResourceRegionIds')

        return self

