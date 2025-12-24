# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLogEventRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        end_time: int = None,
        event: str = None,
        event_type: str = None,
        job_execution_id: int = None,
        job_name: str = None,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        reverse: bool = None,
        start_time: int = None,
        workflow_execution_id: int = None,
        workflow_name: str = None,
    ):
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.end_time = end_time
        self.event = event
        self.event_type = event_type
        self.job_execution_id = job_execution_id
        self.job_name = job_name
        self.keyword = keyword
        self.page_num = page_num
        self.page_size = page_size
        self.reverse = reverse
        self.start_time = start_time
        self.workflow_execution_id = workflow_execution_id
        self.workflow_name = workflow_name

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

        if self.event is not None:
            result['Event'] = self.event

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.workflow_execution_id is not None:
            result['WorkflowExecutionId'] = self.workflow_execution_id

        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WorkflowExecutionId') is not None:
            self.workflow_execution_id = m.get('WorkflowExecutionId')

        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')

        return self

