# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSourcesRequest(DaraModel):
    def __init__(
        self,
        filter_state: bool = None,
        page_no: str = None,
        page_size: str = None,
        sort_by: str = None,
        sort_by_modified_time: str = None,
        source_location_name: str = None,
        source_name: str = None,
        source_type: str = None,
    ):
        # Specifies whether to ignore sources marked as deleted.
        self.filter_state = filter_state
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The sorting order. By default, the query results are sorted by creation time in descending order. Valid values: asc and desc.
        self.sort_by = sort_by
        # The sorting order by modification time. Valid values: asc and desc.
        self.sort_by_modified_time = sort_by_modified_time
        # The name of the source location.
        self.source_location_name = source_location_name
        # The name of the source.
        self.source_name = source_name
        # The source type. Valid values: vodSource and liveSource.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_state is not None:
            result['FilterState'] = self.filter_state

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_by_modified_time is not None:
            result['SortByModifiedTime'] = self.sort_by_modified_time

        if self.source_location_name is not None:
            result['SourceLocationName'] = self.source_location_name

        if self.source_name is not None:
            result['SourceName'] = self.source_name

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterState') is not None:
            self.filter_state = m.get('FilterState')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortByModifiedTime') is not None:
            self.sort_by_modified_time = m.get('SortByModifiedTime')

        if m.get('SourceLocationName') is not None:
            self.source_location_name = m.get('SourceLocationName')

        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

