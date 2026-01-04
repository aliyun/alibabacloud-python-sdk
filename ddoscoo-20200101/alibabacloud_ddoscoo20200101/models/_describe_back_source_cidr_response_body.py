# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeBackSourceCidrResponseBody(DaraModel):
    def __init__(
        self,
        cidrs: List[str] = None,
        request_id: str = None,
    ):
        # An array that consists of the back-to-origin CIDR blocks of the instance.
        self.cidrs = cidrs
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

