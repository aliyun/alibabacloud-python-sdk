# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodDomainRealTimeDetailDataResponseBody(DaraModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned data details. The data is returned as a JSON string. The following table describes the structure and fields:
        # > If no data exists for a field, the field is not returned.
        # 
        # | Field | Type | Description |
        # | ------------- |------------ | ----------- | 
        # | domain_name | String | The accelerated domain name. |
        # | isp | String | The ISP name. |
        # | location | String | The region name. |
        # | qps | Long | The queries per second (QPS). |
        # | bps | Long | The bandwidth data. Unit: bit/s. |
        # | http_code | Map | The HTTP status code details. The key is the status code name, and the value is the count of the status code. |
        # | time_stp | String | The data timestamp. The time is in the ISO 8601 standard in UTC. |
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

