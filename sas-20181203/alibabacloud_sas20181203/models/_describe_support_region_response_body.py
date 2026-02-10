# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSupportRegionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        support_region: List[str] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # List of supported regions
        self.support_region = support_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.support_region is not None:
            result['SupportRegion'] = self.support_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportRegion') is not None:
            self.support_region = m.get('SupportRegion')

        return self

