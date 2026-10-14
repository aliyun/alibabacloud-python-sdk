# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataPushResultRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        data_names: str = None,
        data_versions: str = None,
        max_date: str = None,
        min_date: str = None,
        page_number: int = None,
        page_size: int = None,
        region_ids: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The names of the data files. This is a filter condition for the query. Multiple values are supported and separated by commas (,). By default, all data files are queried.
        self.data_names = data_names
        # The version numbers of the data files. This is a filter condition for the query. Multiple values are supported and separated by commas (,). By default, all versions are queried.
        self.data_versions = data_versions
        # The end time of the query. Format: YYYY-MM-DD. By default, there is no time limit.
        self.max_date = max_date
        # The start time of the query. Format: YYYY-MM-DD. By default, there is no time limit.
        self.min_date = min_date
        # The page number. Pages start from 1. This parameter is not required when you export all information.
        self.page_number = page_number
        # The number of entries per page set in Settings for paging during a paged query. This parameter is not required when you export all entries.
        self.page_size = page_size
        # The IDs of the edge nodes. This is a filter condition for the query. Multiple values are supported and separated by commas (,). By default, all edge nodes are queried.
        self.region_ids = region_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.data_names is not None:
            result['DataNames'] = self.data_names

        if self.data_versions is not None:
            result['DataVersions'] = self.data_versions

        if self.max_date is not None:
            result['MaxDate'] = self.max_date

        if self.min_date is not None:
            result['MinDate'] = self.min_date

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DataNames') is not None:
            self.data_names = m.get('DataNames')

        if m.get('DataVersions') is not None:
            self.data_versions = m.get('DataVersions')

        if m.get('MaxDate') is not None:
            self.max_date = m.get('MaxDate')

        if m.get('MinDate') is not None:
            self.min_date = m.get('MinDate')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')

        return self

