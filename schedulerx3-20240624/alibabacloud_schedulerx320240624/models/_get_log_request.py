# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLogRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        end_time: int = None,
        job_execution_id: str = None,
        keyword: str = None,
        level: str = None,
        line_num: int = None,
        log_id: int = None,
        offset: int = None,
        reverse: bool = None,
        schedule_time: int = None,
        start_time: int = None,
        worker_addr: str = None,
    ):
        # The application name.
        self.app_name = app_name
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The end time. This value is a UNIX timestamp.
        self.end_time = end_time
        # The job execution ID.
        self.job_execution_id = job_execution_id
        # The keyword to search for.
        self.keyword = keyword
        # The log level.
        self.level = level
        # The number of log entries to return.
        self.line_num = line_num
        # The log ID.
        self.log_id = log_id
        # The offset.
        self.offset = offset
        # Specifies whether to sort the results in descending order.
        # 
        # - **true**: sorts the results in descending order.
        # 
        # - **false**: sorts the results in ascending order.
        self.reverse = reverse
        # The time when the job was scheduled. This value is a UNIX timestamp.
        self.schedule_time = schedule_time
        # The start time. This value is a UNIX timestamp.
        self.start_time = start_time
        # The worker address.
        self.worker_addr = worker_addr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.level is not None:
            result['Level'] = self.level

        if self.line_num is not None:
            result['LineNum'] = self.line_num

        if self.log_id is not None:
            result['LogId'] = self.log_id

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.worker_addr is not None:
            result['WorkerAddr'] = self.worker_addr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('LineNum') is not None:
            self.line_num = m.get('LineNum')

        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WorkerAddr') is not None:
            self.worker_addr = m.get('WorkerAddr')

        return self

