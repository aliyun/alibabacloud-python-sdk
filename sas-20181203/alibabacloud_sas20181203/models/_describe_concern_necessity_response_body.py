# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeConcernNecessityResponseBody(DaraModel):
    def __init__(
        self,
        concern_necessity: List[str] = None,
        request_id: str = None,
    ):
        # The priorities to fix the vulnerabilities. Valid values:
        # 
        # *   asap: high
        # *   later: medium
        # *   nntf: low
        self.concern_necessity = concern_necessity
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concern_necessity is not None:
            result['ConcernNecessity'] = self.concern_necessity

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcernNecessity') is not None:
            self.concern_necessity = m.get('ConcernNecessity')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

