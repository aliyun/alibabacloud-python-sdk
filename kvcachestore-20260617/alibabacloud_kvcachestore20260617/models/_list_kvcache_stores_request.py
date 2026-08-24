# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKVCacheStoresRequest(DaraModel):
    def __init__(
        self,
        kvcs_ids: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        status: str = None,
        zone_id: str = None,
    ):
        # The list of KvcsId values. Separate multiple IDs with commas. A maximum of 100 IDs are supported.
        self.kvcs_ids = kvcs_ids
        # The maximum number of entries per page for cursor-based pagination. Default value: 10. Maximum value: 100. This parameter is used together with NextToken.
        self.max_results = max_results
        # The instance name filter. Prefix matching is used.
        self.name = name
        # The pagination token. Do not specify this parameter for the first request. For subsequent requests, use the NextToken value returned in the previous response. This parameter is mutually exclusive with PageNumber.
        self.next_token = next_token
        # The page number. Default value: 1. This parameter takes precedence over NextToken if both are specified.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100. This parameter is used together with PageNumber.
        self.page_size = page_size
        # The region ID, such as cn-hangzhou.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The instance status filter. Valid values: Creating, Available, InUse, Stopping, Stopped, and Deleting.
        self.status = status
        # The zone ID, such as cn-hangzhou-a.
        self.zone_id = zone_id

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

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KvcsIds') is not None:
            self.kvcs_ids = m.get('KvcsIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

