# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPipelineRunsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        max_results: int = None,
        next_token: str = None,
        start_time: int = None,
        status: str = None,
        trigger_type: str = None,
    ):
        # The upper bound of the trigger time filter (triggered_at <= endTime). The value is a UNIX timestamp in seconds.
        self.end_time = end_time
        # The maximum number of entries to return in the current request. Default value: 50. Maximum value: 200.
        self.max_results = max_results
        # The pagination token. To retrieve the next page of results, pass the nextToken value from the previous response. Do not specify this parameter for the first request.
        self.next_token = next_token
        # The lower bound of the trigger time filter (triggered_at >= startTime). The value is a UNIX timestamp in seconds.
        self.start_time = start_time
        # Filters the results by run status. Valid values: Pending, Running, Succeeded, Failed, and Cancelled. If you do not specify this parameter, the results are not filtered by status.
        self.status = status
        # Filters the results by trigger type. Valid values: Manual, Scheduled, and RunOnce. If you do not specify this parameter, the results are not filtered by trigger type.
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

