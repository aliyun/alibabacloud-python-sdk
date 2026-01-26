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
        # The ID of the alert rule. You can call the SearchAlertRules operation and view the `Id` parameter in the response. For more information, see [SearchAlertRules](https://help.aliyun.com/document_detail/175825.html).
        self.alert_id = alert_id
        # The type of the alert rule. Valid values:
        # 
        # *   `1`: custom alert rules to monitor drill-down data sets
        # *   `3`: custom alert rules to monitor tiled data sets
        # *   `4`: alert rules to monitor the frontend, including the default frontend alert rules
        # *   `5`: alert rules to monitor applications, including the default application alert rules
        # *   `6`: the default frontend alert rules
        # *   `7`: the default application alert rules
        # *   `8`: Tracing Analysis alert rules
        # *   `101`: Prometheus alert rules
        self.alert_type = alert_type
        # The type of the application that is associated with the alert rule. Valid values:
        # 
        # *   `TRACE`: application monitoring
        # *   `RETCODE`: frontend monitoring
        self.app_type = app_type
        # The number of the page to return. Default value: `1`.
        self.current_page = current_page
        # The end of the time range to query. Specify a UNIX timestamp of the LONG data type, in milliseconds. The default value is the current time.
        self.end_time = end_time
        # Specifies whether the alert event is triggered. If you do not set this parameter, all alert events are queried. Valid values:
        # 
        # *   `1`: The event is triggered.
        # *   `0`: The event is not triggered.
        self.is_trigger = is_trigger
        # The number of entries to return on each page. Default value: `10`.
        self.page_size = page_size
        # The process identifier (PID) of the application that is associated with the alert rule.
        self.pid = pid
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query. Specify a UNIX timestamp of the LONG data type, in milliseconds. The default value is 10 minutes before the current time.
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

