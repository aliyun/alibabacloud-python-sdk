# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class AiSearchResponseBody(DaraModel):
    def __init__(
        self,
        header: main_models.AiSearchResponseBodyHeader = None,
        payload: str = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.header is not None:
            result['header'] = self.header.to_map()

        if self.payload is not None:
            result['payload'] = self.payload

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('header') is not None:
            temp_model = main_models.AiSearchResponseBodyHeader()
            self.header = temp_model.from_map(m.get('header'))

        if m.get('payload') is not None:
            self.payload = m.get('payload')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class AiSearchResponseBodyHeader(DaraModel):
    def __init__(
        self,
        event: str = None,
        event_id: str = None,
        query_context: main_models.AiSearchResponseBodyHeaderQueryContext = None,
        response_time: int = None,
    ):
        self.event = event
        self.event_id = event_id
        self.query_context = query_context
        self.response_time = response_time

    def validate(self):
        if self.query_context:
            self.query_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event is not None:
            result['event'] = self.event

        if self.event_id is not None:
            result['eventId'] = self.event_id

        if self.query_context is not None:
            result['queryContext'] = self.query_context.to_map()

        if self.response_time is not None:
            result['responseTime'] = self.response_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')

        if m.get('queryContext') is not None:
            temp_model = main_models.AiSearchResponseBodyHeaderQueryContext()
            self.query_context = temp_model.from_map(m.get('queryContext'))

        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')

        return self

class AiSearchResponseBodyHeaderQueryContext(DaraModel):
    def __init__(
        self,
        original_query: main_models.AiSearchResponseBodyHeaderQueryContextOriginalQuery = None,
        rewrite: main_models.AiSearchResponseBodyHeaderQueryContextRewrite = None,
    ):
        self.original_query = original_query
        self.rewrite = rewrite

    def validate(self):
        if self.original_query:
            self.original_query.validate()
        if self.rewrite:
            self.rewrite.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.original_query is not None:
            result['originalQuery'] = self.original_query.to_map()

        if self.rewrite is not None:
            result['rewrite'] = self.rewrite.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalQuery') is not None:
            temp_model = main_models.AiSearchResponseBodyHeaderQueryContextOriginalQuery()
            self.original_query = temp_model.from_map(m.get('originalQuery'))

        if m.get('rewrite') is not None:
            temp_model = main_models.AiSearchResponseBodyHeaderQueryContextRewrite()
            self.rewrite = temp_model.from_map(m.get('rewrite'))

        return self

class AiSearchResponseBodyHeaderQueryContextRewrite(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        time_range: str = None,
    ):
        self.enabled = enabled
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        return self

class AiSearchResponseBodyHeaderQueryContextOriginalQuery(DaraModel):
    def __init__(
        self,
        industry: str = None,
        page: int = None,
        query: str = None,
        time_range: str = None,
    ):
        self.industry = industry
        self.page = page
        self.query = query
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.industry is not None:
            result['industry'] = self.industry

        if self.page is not None:
            result['page'] = self.page

        if self.query is not None:
            result['query'] = self.query

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        return self

