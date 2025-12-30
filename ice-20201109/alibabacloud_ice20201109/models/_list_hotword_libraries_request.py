# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHotwordLibrariesRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        page_no: int = None,
        page_size: int = None,
        sort_by: str = None,
        start_time: str = None,
        usage_scenario: str = None,
    ):
        # The end of the time range to query.
        self.end_time = end_time
        # The maximum number of entries to return.
        # 
        # Default value: 10. Valid values: 1 to 100.
        self.max_results = max_results
        # The name of the hotword library.
        self.name = name
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Valid values: 1 to 100.
        self.page_size = page_size
        # The sorting order. By default, the query results are sorted by creation time in descending order.
        self.sort_by = sort_by
        # The beginning of the time range to query.
        self.start_time = start_time
        # The usage scenario of the hotword library. Valid values:
        # 
        # *   ASR: Automatic Speech Recognition
        # *   StructuredMediaAssets: structured media analysis
        # *   VideoTranslation: Video translation. This field cannot be modified after the hotword library is created.
        self.usage_scenario = usage_scenario

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.usage_scenario is not None:
            result['UsageScenario'] = self.usage_scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UsageScenario') is not None:
            self.usage_scenario = m.get('UsageScenario')

        return self

