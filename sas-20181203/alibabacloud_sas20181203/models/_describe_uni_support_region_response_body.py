# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeUniSupportRegionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        uni_support_region: List[str] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array consisting of the region that is supported by anti-ransomware for databases.
        self.uni_support_region = uni_support_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.uni_support_region is not None:
            result['UniSupportRegion'] = self.uni_support_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UniSupportRegion') is not None:
            self.uni_support_region = m.get('UniSupportRegion')

        return self

