# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribePrinterEventsRequest(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_name: str = None,
        end_time: str = None,
        end_user_id: str = None,
        end_user_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        printer_driver: str = None,
        printer_name: str = None,
        printer_redir_type: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The cloud computer ID. If you do not specify this parameter, all cloud computers in the region are queried.
        self.desktop_id = desktop_id
        # The cloud computer name.
        self.desktop_name = desktop_name
        # The end time. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC+0. If you do not specify this parameter, the current time is used.
        self.end_time = end_time
        # The logon user information, which is a RAM user ID or an Active Directory (AD) username. If you do not specify this parameter, events of all users in the region are queried.
        self.end_user_id = end_user_id
        # The list of end user IDs.
        self.end_user_ids = end_user_ids
        # The number of entries per page in a paged query. Default value: 100.
        self.max_results = max_results
        # The pagination token. Set this parameter to the value of NextToken that was returned in the previous API call.
        self.next_token = next_token
        # The printer driver name.
        self.printer_driver = printer_driver
        # The printer name.
        self.printer_name = printer_name
        # The printer redirection type.
        self.printer_redir_type = printer_redir_type
        # The region ID. You can call DescribeRegions to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start time. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC+0. If you do not specify this parameter, the query starts from the time that is calculated backward from the time specified by `EndTime`.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.printer_driver is not None:
            result['PrinterDriver'] = self.printer_driver

        if self.printer_name is not None:
            result['PrinterName'] = self.printer_name

        if self.printer_redir_type is not None:
            result['PrinterRedirType'] = self.printer_redir_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PrinterDriver') is not None:
            self.printer_driver = m.get('PrinterDriver')

        if m.get('PrinterName') is not None:
            self.printer_name = m.get('PrinterName')

        if m.get('PrinterRedirType') is not None:
            self.printer_redir_type = m.get('PrinterRedirType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

