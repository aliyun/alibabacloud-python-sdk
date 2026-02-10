# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentlessTaskRequest(DaraModel):
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
        start_time: int = None,
        status: int = None,
        target_name: str = None,
        target_type: int = None,
        task_id: str = None,
        uuid: str = None,
    ):
        # The number of the page to return.
        self.current_page = current_page
        # The end timestamp of the task.
        self.end_time = end_time
        # The public IP address of the asset that you want to query.
        self.internet_ip = internet_ip
        # The private IP address of the asset that you want to query.
        self.intranet_ip = intranet_ip
        # The language type. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The name of the instance.
        self.machine_name = machine_name
        # The number of entries to return on each page.
        self.page_size = page_size
        # Specifies whether to query main tasks. Valid values:
        # 
        # *   **true**: queries main tasks.
        # *   **false**: queries subtasks.
        self.root_task = root_task
        # The ID of the main task.
        self.root_task_id = root_task_id
        # The start timestamp of the task.
        self.start_time = start_time
        # The status of the detection task.
        # 
        # *   **1**: The detection task is in progress.
        # *   **2**: The detection task is complete.
        # *   **3**: The detection task fails.
        # *   **4**: The detection task times out.
        self.status = status
        # The name of the asset that you want to detect.
        self.target_name = target_name
        # The type of the asset that you want to detect. Valid values:
        # 
        # *   **1**: snapshot
        # *   **2**: image
        self.target_type = target_type
        # The ID of the main task. If you want to query subtasks of a main task, you must specify this parameter.
        self.task_id = task_id
        # The UUID of the server.
        self.uuid = uuid

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

