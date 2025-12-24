# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRtcMPUEventSubRecordRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        page_no: int = None,
        page_size: int = None,
        start_time: str = None,
        sub_id: str = None,
    ):
        # The ID of the application.
        # 
        # >  The ID can be up to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The page number.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the subscription.
        self.sub_id = sub_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.sub_id is not None:
            result['SubId'] = self.sub_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')

        return self

