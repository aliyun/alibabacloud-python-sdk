# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySourceUsageSummaryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        retrieval_count: int = None,
        retrieved_source_count: int = None,
        source_count: int = None,
        usage_count: int = None,
        used_source_count: int = None,
    ):
        # The error code.
        self.code = code
        # The status code description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The number of retrieval recalls.
        self.retrieval_count = retrieval_count
        # The deduplicated number of sources with retrieval events.
        self.retrieved_source_count = retrieved_source_count
        # The number of rows in the source data.
        self.source_count = source_count
        # The number of times the source has been used in agents.
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
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

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
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

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

