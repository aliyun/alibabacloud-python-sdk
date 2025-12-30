# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStreamTagListRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        media_id: str = None,
        namespace: str = None,
        next_token: str = None,
        page_no: int = None,
        page_size: int = None,
        search_lib_name: str = None,
        sort_by: str = None,
        start_time: str = None,
    ):
        # The end of the query time range, based on the tagging timestamp. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The ID of the media asset.
        self.media_id = media_id
        # The namespace.
        self.namespace = namespace
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The name of the search library.
        self.search_lib_name = search_lib_name
        # The sorting order for the results. Valid values:
        # 
        # *   StartTime:Desc (default): Sort by creation time in descending order.
        # *   StartTime:Asc: Sort by creation time in ascending order.
        self.sort_by = sort_by
        # The start of the query time range, based on the tagging timestamp. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

