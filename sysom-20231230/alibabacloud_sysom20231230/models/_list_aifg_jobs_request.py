# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAifgJobsRequest(DaraModel):
    def __init__(
        self,
        current: int = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
        region: str = None,
        service_name: str = None,
    ):
        # The current page number.
        # 
        # This parameter is required.
        self.current = current
        # The maximum number of records to retrieve in a single request.
        self.max_results = max_results
        # The pagination token.
        # 
        # > A non-empty value indicates that more data is available.
        self.next_token = next_token
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region ID.
        self.region = region
        # The service name of the diagnostic service.
        # 
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current is not None:
            result['current'] = self.current

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.region is not None:
            result['region'] = self.region

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        return self

