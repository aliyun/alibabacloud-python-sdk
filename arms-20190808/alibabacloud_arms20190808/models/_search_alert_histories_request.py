# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchAlertHistoriesRequest(DaraModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_type: int = None,
        current_page: int = None,
        end_time: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # The ID of the alert rule. You can call the SearchAlertRules operation and view the `Id` parameter in the response. For more information, see [SearchAlertRules](https://help.aliyun.com/document_detail/175825.html).
        self.alert_id = alert_id
        # The type of the alert rule. Valid values:
        # 
        # *   `1`: a custom alert rule that is used to monitor drill-down data sets
        # *   `3`: a custom alert rule that is used to monitor tiled data sets
        # *   `4`: an alert rule that is used to monitor web pages, including the default alert rule for browser monitoring
        # *   `5`: an alert rule that is used to monitor applications, including the default alert rule for application monitoring
        # *   `6`: the default alert rule for browser monitoring
        # *   `7`: the default alert rule for application monitoring
        # *   `8`: a Tracing Analysis alert rule
        # *   `101`: a Prometheus alert rule
        self.alert_type = alert_type
        # The number of the page to return. Default value: `1`.
        self.current_page = current_page
        # The end of the time range to query. The value is a UNIX timestamp of the LONG data type. Unit: milliseconds. The default value is the current time.
        self.end_time = end_time
        # The number of entries to return on each page. Default value: `10`.
        self.page_size = page_size
        # The ID of the region. Default value: `cn-hangzhou`.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query. The value is a UNIX timestamp of the LONG data type. Unit: milliseconds. The default value is 10 minutes before the current time.
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

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

