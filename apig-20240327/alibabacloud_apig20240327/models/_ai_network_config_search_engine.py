# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class AiNetworkConfigSearchEngine(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        content_mode: str = None,
        count: int = None,
        endpoint: str = None,
        industry: str = None,
        option_args: Dict[str, str] = None,
        start: int = None,
        time_range: str = None,
        timeout_millisecond: int = None,
        type: str = None,
    ):
        # Required. The API key to authenticate requests to the search engine service.
        self.api_key = api_key
        # The search content mode, which determines how the service interprets the query and returns results.
        self.content_mode = content_mode
        # The number of search results to return. If this parameter is omitted, the service uses a default value.
        self.count = count
        # The endpoint URL for the search engine service.
        self.endpoint = endpoint
        # The industry context for tailoring search results to a specific domain.
        self.industry = industry
        # Optional. A key-value map for service-specific parameters not covered by the standard configuration.
        self.option_args = option_args
        # The starting offset for the search results, used for pagination. For example, a value of 10 skips the first 10 results. The default is 0.
        self.start = start
        # The time range for filtering results by their creation or modification date.
        self.time_range = time_range
        # The request timeout in milliseconds. If a request exceeds this time, the service terminates it.
        self.timeout_millisecond = timeout_millisecond
        # Specifies the search engine service to use.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.content_mode is not None:
            result['contentMode'] = self.content_mode

        if self.count is not None:
            result['count'] = self.count

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.industry is not None:
            result['industry'] = self.industry

        if self.option_args is not None:
            result['optionArgs'] = self.option_args

        if self.start is not None:
            result['start'] = self.start

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        if self.timeout_millisecond is not None:
            result['timeoutMillisecond'] = self.timeout_millisecond

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('contentMode') is not None:
            self.content_mode = m.get('contentMode')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('optionArgs') is not None:
            self.option_args = m.get('optionArgs')

        if m.get('start') is not None:
            self.start = m.get('start')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        if m.get('timeoutMillisecond') is not None:
            self.timeout_millisecond = m.get('timeoutMillisecond')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

