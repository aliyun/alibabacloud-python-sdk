# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListKVCacheStoreAttachInfoRequest(DaraModel):
    def __init__(
        self,
        kvcs_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The list of KVCacheStore KvcsId values to query. A maximum of 100 values can be specified.
        # 
        # This parameter is required.
        self.kvcs_ids = kvcs_ids
        # The maximum number of entries to return in a single request. Valid values: 1 to 500.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous call. You do not need to set this parameter for the first request. If you set NextToken, the PageSize and PageNumber request parameters become ineffective, and the TotalCount value in the response is invalid.
        self.next_token = next_token
        # The page number for a paged query. Used together with PageSize. If the value exceeds the total number of pages, the last page of data is returned.
        self.page_number = page_number
        # The number of entries per page for a paged query.
        self.page_size = page_size
        # The region ID, such as cn-hangzhou.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kvcs_ids is not None:
            result['KvcsIds'] = self.kvcs_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KvcsIds') is not None:
            self.kvcs_ids = m.get('KvcsIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

