# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDingtalkMeetingListShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        current_page: int = None,
        end_time: int = None,
        org_id: str = None,
        page_size: int = None,
        room_code: str = None,
        room_name: str = None,
        start_time: int = None,
        work_no: str = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        self.current_page = current_page
        self.end_time = end_time
        self.org_id = org_id
        self.page_size = page_size
        self.room_code = room_code
        self.room_name = room_name
        self.start_time = start_time
        self.work_no = work_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.org_id is not None:
            result['orgId'] = self.org_id

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.room_code is not None:
            result['roomCode'] = self.room_code

        if self.room_name is not None:
            result['roomName'] = self.room_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.work_no is not None:
            result['workNo'] = self.work_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('roomCode') is not None:
            self.room_code = m.get('roomCode')

        if m.get('roomName') is not None:
            self.room_name = m.get('roomName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('workNo') is not None:
            self.work_no = m.get('workNo')

        return self

