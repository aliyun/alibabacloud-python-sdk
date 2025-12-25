# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDefenseResourceNamesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resources: List[str] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The names of the protected objects.
        self.resources = resources
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

