# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListVirusFileStatusesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        department: str = None,
        dev_tag: str = None,
        dev_type: str = None,
        end_time: int = None,
        file_md_5: str = None,
        file_process_status: str = None,
        hostname: str = None,
        operations: List[str] = None,
        page_size: int = None,
        risk_levels: List[str] = None,
        sase_user_id: str = None,
        scan_task_id: str = None,
        start_time: int = None,
        username: str = None,
        virus_types: List[str] = None,
    ):
        # The page number of the current page in paging. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The department name. Matches any level of the organizational structure to which the user belongs. Specify the department name itself without the full path of the organizational structure. The value can contain Chinese characters, uppercase and lowercase letters, digits, spaces, periods (.), commas (,), forward slashes (/), at signs (@), hyphens (-), and underscores (_).
        self.department = department
        # The unique identifier of the user terminal device. Exact match. The value can be up to 64 characters in length. You can obtain the value from the following operation:
        # - [ListUserDevices](~~ListUserDevices~~): Lists user terminal devices.
        self.dev_tag = dev_tag
        # The operating system type of the user terminal device. Valid values:
        # - **windows**: Windows.
        # - **macOS**: macOS.
        self.dev_type = dev_type
        # The end time for filtering by virus file discovery time. The value is a UNIX timestamp in seconds. This parameter must be specified together with StartTime and must be later than StartTime.
        self.end_time = end_time
        # The MD5 value of the virus file. Fuzzy match is supported. The value can be up to 64 characters in length.
        self.file_md_5 = file_md_5
        # Filters by disposition status. If this parameter is not specified, no filtering by disposition status is applied. Valid values:
        # - **Pending**: Pending disposition.
        # - **Processed**: Disposed.
        self.file_process_status = file_process_status
        # The hostname of the user terminal device. Fuzzy match is supported. The value can be up to 128 characters in length.
        self.hostname = hostname
        # Filters by disposition action. Duplicate values are not allowed. If this parameter is not specified, no filtering by disposition action is applied.
        self.operations = operations
        # The number of entries per page in paging. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Filters by risk level. Duplicate values are not allowed. If this parameter is not specified, no filtering by risk level is applied.
        self.risk_levels = risk_levels
        # The user ID. Exact match. The value can be up to 128 characters in length. You can obtain the value from the following operations:
        # - [ListUserDevices](~~ListUserDevices~~): Lists user terminal devices.
        # - [GetUserDevice](~~GetUserDevice~~): Queries user terminal device details.
        self.sase_user_id = sase_user_id
        # The ID of the virus scan task that detected the virus file. This parameter is used to filter detection results of a specified task. You can obtain the value from the following operations:
        # - [ListVirusScanTasks](~~ListVirusScanTasks~~): Lists virus scan tasks.
        # - [CreateVirusScanTask](~~CreateVirusScanTask~~): Creates a virus scan task.
        self.scan_task_id = scan_task_id
        # The start time for filtering by virus file discovery time. The value is a UNIX timestamp in seconds. This parameter must be specified together with EndTime and must be earlier than EndTime.
        self.start_time = start_time
        # The username. Fuzzy match is supported. The value can be up to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), asterisks (*), hyphens (-), at signs (@), spaces, middle dots (·), and parentheses.
        self.username = username
        # Filters by virus type. Duplicate values are not allowed. If this parameter is not specified, no filtering by virus type is applied.
        self.virus_types = virus_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.department is not None:
            result['Department'] = self.department

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.dev_type is not None:
            result['DevType'] = self.dev_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.file_md_5 is not None:
            result['FileMd5'] = self.file_md_5

        if self.file_process_status is not None:
            result['FileProcessStatus'] = self.file_process_status

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.operations is not None:
            result['Operations'] = self.operations

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_levels is not None:
            result['RiskLevels'] = self.risk_levels

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.username is not None:
            result['Username'] = self.username

        if self.virus_types is not None:
            result['VirusTypes'] = self.virus_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('DevType') is not None:
            self.dev_type = m.get('DevType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileMd5') is not None:
            self.file_md_5 = m.get('FileMd5')

        if m.get('FileProcessStatus') is not None:
            self.file_process_status = m.get('FileProcessStatus')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('Operations') is not None:
            self.operations = m.get('Operations')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskLevels') is not None:
            self.risk_levels = m.get('RiskLevels')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('VirusTypes') is not None:
            self.virus_types = m.get('VirusTypes')

        return self

