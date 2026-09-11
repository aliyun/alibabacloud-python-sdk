# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAliDingMinutesRequest(DaraModel):
    def __init__(
        self,
        cursor: str = None,
        end_time: str = None,
        page_size: int = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        # The cursor for the paged query. Set this parameter to 0 for the first request. For subsequent requests, set this parameter to the **nextCursor** value returned in the previous response. For more information about paging, see the response parameters.
        self.cursor = cursor
        # The actual end timestamp of the live session, in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The number of entries per page.
        self.page_size = page_size
        # The query start time. This value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The tenant ID. This is a common parameter. Pass it explicitly through the winnexo-cli --tenant-id option.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cursor is not None:
            result['cursor'] = self.cursor

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

