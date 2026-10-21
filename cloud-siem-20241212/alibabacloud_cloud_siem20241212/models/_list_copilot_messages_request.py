# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCopilotMessagesRequest(DaraModel):
    def __init__(
        self,
        ascending: bool = None,
        conversation_id: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        trace_id: str = None,
    ):
        # Used together with the SortingField parameter. A value of **true** specifies ascending order, and a value of **false** specifies descending order.
        self.ascending = ascending
        # The conversation ID.
        # 
        # This parameter is required.
        self.conversation_id = conversation_id
        # The language of the returned messages. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The maximum number of results to return when you use the NextToken-based pagination method. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query. Leave this parameter empty to query from the beginning.
        self.next_token = next_token
        # The region where the Cloud Threat Detection and Response (CTDR) data management center resides. Specify the management center based on the region where your assets reside. Valid values:
        # - cn-hangzhou: Your assets reside in the Chinese mainland or Hong Kong (China).
        # - ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id
        # The trace ID, which is used to query specific call information.
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ascending is not None:
            result['Ascending'] = self.ascending

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ascending') is not None:
            self.ascending = m.get('Ascending')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

