# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFixUsedCountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        used_count: int = None,
        used_count_cn: int = None,
        used_count_sg: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The number of vulnerabilities that are fixed by the vulnerability fixing feature.
        self.used_count = used_count
        # The number of vulnerabilities that are fixed by the vulnerability fixing feature in China.
        self.used_count_cn = used_count_cn
        # The number of vulnerabilities that are fixed by the vulnerability fixing feature outside China.
        self.used_count_sg = used_count_sg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.used_count is not None:
            result['UsedCount'] = self.used_count

        if self.used_count_cn is not None:
            result['UsedCountCn'] = self.used_count_cn

        if self.used_count_sg is not None:
            result['UsedCountSg'] = self.used_count_sg

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')

        if m.get('UsedCountCn') is not None:
            self.used_count_cn = m.get('UsedCountCn')

        if m.get('UsedCountSg') is not None:
            self.used_count_sg = m.get('UsedCountSg')

        return self

