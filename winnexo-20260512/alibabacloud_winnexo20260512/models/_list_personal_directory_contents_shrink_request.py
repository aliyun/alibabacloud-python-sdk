# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPersonalDirectoryContentsShrinkRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        operating_object_name: str = None,
        page: int = None,
        page_size: int = None,
        sort_field: str = None,
        sort_order: str = None,
        source_types_shrink: str = None,
        tenant_id: str = None,
    ):
        # The directory ID.
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # The name of the digital employee.
        self.operating_object_name = operating_object_name
        # The page number. Default value: 1. Pages start from page 1.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The field by which the results are sorted. Valid values:
        # 
        # - event_time: event creation time
        # - event_execute_start_time: event execution time
        # - event_execute_finish_time: event completion time
        self.sort_field = sort_field
        # The sort order. This parameter takes effect when sortBy is specified. Valid values: ASC, DESC (case-insensitive).
        self.sort_order = sort_order
        # The list of service source types.
        self.source_types_shrink = source_types_shrink
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.sort_field is not None:
            result['sortField'] = self.sort_field

        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order

        if self.source_types_shrink is not None:
            result['sourceTypes'] = self.source_types_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('sortField') is not None:
            self.sort_field = m.get('sortField')

        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')

        if m.get('sourceTypes') is not None:
            self.source_types_shrink = m.get('sourceTypes')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

