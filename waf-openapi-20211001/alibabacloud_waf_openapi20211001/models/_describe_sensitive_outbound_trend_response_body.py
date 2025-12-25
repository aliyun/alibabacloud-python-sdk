# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeSensitiveOutboundTrendResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeSensitiveOutboundTrendResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information records involved in cross-border data transfer.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeSensitiveOutboundTrendResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSensitiveOutboundTrendResponseBodyData(DaraModel):
    def __init__(
        self,
        info_count: int = None,
        info_outbound_count: int = None,
        sensitive_outbound_count: int = None,
        timestamp: int = None,
    ):
        # The total number of personal information records.
        self.info_count = info_count
        # The total number of personal information records involved in cross-border data transfer.
        self.info_outbound_count = info_outbound_count
        # The total number of sensitive information records involved in cross-border data transfer.
        self.sensitive_outbound_count = sensitive_outbound_count
        # The time of cross-border data transfer. The value is a UNIX timestamp displayed in UTC. Unit: seconds.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_count is not None:
            result['InfoCount'] = self.info_count

        if self.info_outbound_count is not None:
            result['InfoOutboundCount'] = self.info_outbound_count

        if self.sensitive_outbound_count is not None:
            result['SensitiveOutboundCount'] = self.sensitive_outbound_count

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfoCount') is not None:
            self.info_count = m.get('InfoCount')

        if m.get('InfoOutboundCount') is not None:
            self.info_outbound_count = m.get('InfoOutboundCount')

        if m.get('SensitiveOutboundCount') is not None:
            self.sensitive_outbound_count = m.get('SensitiveOutboundCount')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

