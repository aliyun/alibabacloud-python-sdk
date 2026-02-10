# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListVirusScanTaskRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        lang: str = None,
        machine_name: str = None,
        page_size: int = None,
        root_task: bool = None,
        root_task_id: str = None,
        scan_type: str = None,
        start_time: int = None,
        status: int = None,
        status_list: List[int] = None,
        task_id: str = None,
    ):
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The timestamp when the virus scan task ended. Unit: milliseconds.
        self.end_time = end_time
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The name of the server.
        self.machine_name = machine_name
        # The number of entries per page. Default value: **20**.
        self.page_size = page_size
        # Specifies whether the virus scan task is the root task.
        self.root_task = root_task
        # The ID of the root task.
        # 
        # >  You can call the [GetVirusScanLatestTaskStatistic](~~GetVirusScanLatestTaskStatistic~~) operation to query the ID.
        self.root_task_id = root_task_id
        # The type of the virus scan task. Valid values:
        # 
        # *   **system**: automatic scan task
        # *   **user**: custom scan task
        self.scan_type = scan_type
        # The timestamp when the virus scan task started. Unit: milliseconds.
        self.start_time = start_time
        # The status of the virus scan task. Valid values:
        # 
        # *   **1**: running
        # *   **2**: complete
        # *   **3**: failed
        # *   **4**: timed out
        self.status = status
        # The statuses of virus scan tasks.
        self.status_list = status_list
        # The ID of the virus scan task.
        # 
        # >  You can call the [ListVirusScanTask](~~ListVirusScanTask~~) operation to query the ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.machine_name is not None:
            result['MachineName'] = self.machine_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.root_task is not None:
            result['RootTask'] = self.root_task

        if self.root_task_id is not None:
            result['RootTaskId'] = self.root_task_id

        if self.scan_type is not None:
            result['ScanType'] = self.scan_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MachineName') is not None:
            self.machine_name = m.get('MachineName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RootTask') is not None:
            self.root_task = m.get('RootTask')

        if m.get('RootTaskId') is not None:
            self.root_task_id = m.get('RootTaskId')

        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

