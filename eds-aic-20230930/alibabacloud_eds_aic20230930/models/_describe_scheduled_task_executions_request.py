# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeScheduledTaskExecutionsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        scheduled_id: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The end time of the time range in ISO-8601 format.
        self.end_time = end_time
        # The instance ID.
        self.instance_id = instance_id
        # The maximum number of results to return per request. Default value: 20. Maximum value: 100.
        self.max_results = max_results
        # The pagination token. Leave this parameter empty for the first request.
        self.next_token = next_token
        # The ID of the scheduled task.
        # 
        # This parameter is required.
        self.scheduled_id = scheduled_id
        # The start time of the time range in ISO-8601 format.
        self.start_time = start_time
        # The status of the scheduled task.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.scheduled_id is not None:
            result['ScheduledId'] = self.scheduled_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ScheduledId') is not None:
            self.scheduled_id = m.get('ScheduledId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

