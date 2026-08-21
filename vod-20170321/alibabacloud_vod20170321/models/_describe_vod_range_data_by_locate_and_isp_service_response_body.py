# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodRangeDataByLocateAndIspServiceResponseBody(DaraModel):
    def __init__(
        self,
        json_result: str = None,
        request_id: str = None,
    ):
        # The result in JSON format. From left to right, the fields are: UNIX timestamp, region, ISP, HTTP status code distribution, response duration, bandwidth (unit: bit/s), average response rate, page views, cache hit ratio, and request hit ratio.
        self.json_result = json_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.json_result is not None:
            result['JsonResult'] = self.json_result

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

