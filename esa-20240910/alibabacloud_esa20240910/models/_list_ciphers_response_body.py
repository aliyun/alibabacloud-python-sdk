# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCiphersResponseBody(DaraModel):
    def __init__(
        self,
        ciphers_group: str = None,
        request_id: str = None,
        result: List[str] = None,
        total_count: int = None,
    ):
        # Name of the cipher suite group.
        self.ciphers_group = ciphers_group
        # Request ID.
        self.request_id = request_id
        # Returned result.
        self.result = result
        # Total number of cipher suites.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ciphers_group is not None:
            result['CiphersGroup'] = self.ciphers_group

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphersGroup') is not None:
            self.ciphers_group = m.get('CiphersGroup')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

