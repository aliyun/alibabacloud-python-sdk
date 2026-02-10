# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVulDefendCountStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        rasp_defended_count: int = None,
        rasp_defensible_count: int = None,
        request_id: str = None,
    ):
        # The number of defended vulnerabilities.
        self.rasp_defended_count = rasp_defended_count
        # The number of supported vulnerabilities.
        self.rasp_defensible_count = rasp_defensible_count
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rasp_defended_count is not None:
            result['RaspDefendedCount'] = self.rasp_defended_count

        if self.rasp_defensible_count is not None:
            result['RaspDefensibleCount'] = self.rasp_defensible_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RaspDefendedCount') is not None:
            self.rasp_defended_count = m.get('RaspDefendedCount')

        if m.get('RaspDefensibleCount') is not None:
            self.rasp_defensible_count = m.get('RaspDefensibleCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

