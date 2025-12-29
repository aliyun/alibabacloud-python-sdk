# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class ListStatisticReportResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[Dict[str, Any]] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The statistical reports. Valid values:
        # 
        # *   For more information about the metrics in data quality reports, see the Upload behavioral data section of [Data collection 2.0](https://help.aliyun.com/document_detail/131547.html).
        # *   For more information about the metrics in application and A/B test reports, see the Core metrics section of [Metrics of statistical reports](https://help.aliyun.com/document_detail/187665.html).
        # *   For more information about the metrics in query analysis reports, see the Query analysis metrics section of [Metrics of statistical reports](https://help.aliyun.com/document_detail/187665.html).
        self.result = result
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
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

