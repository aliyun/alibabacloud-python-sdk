# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAsyncTasksRequest(DaraModel):
    def __init__(
        self,
        include_payload: bool = None,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
        qualifier: str = None,
        sort_order_by_time: str = None,
        started_time_begin: int = None,
        started_time_end: int = None,
        status: str = None,
    ):
        # Specifies whether to return the input parameters of the asynchronous task.
        # 
        # - true: If this parameter is set to true, the `invocationPayload` field is returned.
        # 
        # - false: If this parameter is set to false, the `invocationPayload` field is not returned.
        # 
        # > The `invocationPayload` field specifies the input parameters of the function for the asynchronous task.
        self.include_payload = include_payload
        # The number of asynchronous tasks to return. The default value is 20. The value must be in the range of [1, 100].
        self.limit = limit
        # The pagination token to return more results. You do not need to provide this parameter for the first query. Obtain the token for a subsequent query from the response to the previous query.
        self.next_token = next_token
        # The prefix of the asynchronous task ID. The system returns a list of asynchronous tasks that match the prefix.
        self.prefix = prefix
        # The version or alias of the function.
        self.qualifier = qualifier
        # The sorting order of the returned asynchronous tasks.
        # 
        # - asc: ascending order
        # 
        # - desc: descending order
        self.sort_order_by_time = sort_order_by_time
        # The start of the time range when the asynchronous task was started.
        self.started_time_begin = started_time_begin
        # The end of the time range when the asynchronous task was started.
        self.started_time_end = started_time_end
        # The execution status of the asynchronous task.
        # 
        # - Enqueued: The asynchronous message is enqueued and waits for processing.
        # 
        # - Dequeued: The asynchronous message is dequeued and waits to be triggered.
        # 
        # - Running: The invocation is in progress.
        # 
        # - Succeeded: The invocation succeeded.
        # 
        # - Failed: The invocation failed.
        # 
        # - Stopped: The invocation was stopped.
        # 
        # - Stopping: The invocation is being stopped.
        # 
        # - Expired: The task was discarded because its configured maximum queuing duration was exceeded. The task was not executed.
        # 
        # - Invalid: The execution is invalid because the function was deleted or for other reasons. The task was not executed.
        # 
        # - Retrying: The asynchronous invocation is being retried because of an execution error.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_payload is not None:
            result['includePayload'] = self.include_payload

        if self.limit is not None:
            result['limit'] = self.limit

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.prefix is not None:
            result['prefix'] = self.prefix

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.sort_order_by_time is not None:
            result['sortOrderByTime'] = self.sort_order_by_time

        if self.started_time_begin is not None:
            result['startedTimeBegin'] = self.started_time_begin

        if self.started_time_end is not None:
            result['startedTimeEnd'] = self.started_time_end

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('includePayload') is not None:
            self.include_payload = m.get('includePayload')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('sortOrderByTime') is not None:
            self.sort_order_by_time = m.get('sortOrderByTime')

        if m.get('startedTimeBegin') is not None:
            self.started_time_begin = m.get('startedTimeBegin')

        if m.get('startedTimeEnd') is not None:
            self.started_time_end = m.get('startedTimeEnd')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

