# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchEventsRequest(DaraModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_type: int = None,
        app_type: str = None,
        current_page: int = None,
        end_time: int = None,
        is_trigger: int = None,
        page_size: int = None,
        pid: str = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.alert_id = alert_id
        self.alert_type = alert_type
        self.app_type = app_type
        self.current_page = current_page
        self.end_time = end_time
        self.is_trigger = is_trigger
        self.page_size = page_size
        self.pid = pid
        # This parameter is required.
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.is_trigger is not None:
            result['IsTrigger'] = self.is_trigger

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IsTrigger') is not None:
            self.is_trigger = m.get('IsTrigger')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

