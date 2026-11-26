# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class QuerySourceUsageTrendResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        trend: List[main_models.QuerySourceUsageTrendResponseBodyTrend] = None,
    ):
        # The error code.
        self.code = code
        # The error details.
        self.message = message
        # The request tracking ID.
        self.request_id = request_id
        # The trend details.
        self.trend = trend

    def validate(self):
        if self.trend:
            for v1 in self.trend:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['trend'] = []
        if self.trend is not None:
            for k1 in self.trend:
                result['trend'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.trend = []
        if m.get('trend') is not None:
            for k1 in m.get('trend'):
                temp_model = main_models.QuerySourceUsageTrendResponseBodyTrend()
                self.trend.append(temp_model.from_map(k1))

        return self

class QuerySourceUsageTrendResponseBodyTrend(DaraModel):
    def __init__(
        self,
        bucket_start: str = None,
        retrieval_count: int = None,
        retrieved_source_count: int = None,
        source_count: int = None,
        usage_count: int = None,
        used_source_count: int = None,
    ):
        # The start time of the natural bucket with the selected time zone. The first bucket may start earlier than the startTime.
        self.bucket_start = bucket_start
        # The number of retrieval recalls.
        self.retrieval_count = retrieval_count
        # The deduplicated number of sources with retrieval events.
        self.retrieved_source_count = retrieved_source_count
        # The number of rows in the source data.
        self.source_count = source_count
        # The number of times used by the agent.
        self.usage_count = usage_count
        # The deduplicated number of sources with usage events.
        self.used_source_count = used_source_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_start is not None:
            result['bucketStart'] = self.bucket_start

        if self.retrieval_count is not None:
            result['retrievalCount'] = self.retrieval_count

        if self.retrieved_source_count is not None:
            result['retrievedSourceCount'] = self.retrieved_source_count

        if self.source_count is not None:
            result['sourceCount'] = self.source_count

        if self.usage_count is not None:
            result['usageCount'] = self.usage_count

        if self.used_source_count is not None:
            result['usedSourceCount'] = self.used_source_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketStart') is not None:
            self.bucket_start = m.get('bucketStart')

        if m.get('retrievalCount') is not None:
            self.retrieval_count = m.get('retrievalCount')

        if m.get('retrievedSourceCount') is not None:
            self.retrieved_source_count = m.get('retrievedSourceCount')

        if m.get('sourceCount') is not None:
            self.source_count = m.get('sourceCount')

        if m.get('usageCount') is not None:
            self.usage_count = m.get('usageCount')

        if m.get('usedSourceCount') is not None:
            self.used_source_count = m.get('usedSourceCount')

        return self

