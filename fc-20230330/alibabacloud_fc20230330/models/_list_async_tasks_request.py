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
        # Specifies whether to return input parameters of the asynchronous tasks. Valid values:
        # 
        # *   true: returns the `invocationPayload` parameter in the response.
        # *   false: does not return the `invocationPayload` parameter in the response.
        # 
        # >  The `invocationPayload` parameter indicates the input parameters of an asynchronous task.
        self.include_payload = include_payload
        # The number of asynchronous tasks to return. The default value is 20. Valid values: [1,100].
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The ID prefix of asynchronous tasks. If this parameter is specified, a list of asynchronous tasks whose IDs match the prefix is returned.
        self.prefix = prefix
        # The version or alias of the function.
        self.qualifier = qualifier
        # The order in which the returned asynchronous tasks are sorted.
        # 
        # *   asc: in ascending order.
        # *   desc: in descending order.
        self.sort_order_by_time = sort_order_by_time
        # The start time of the period during which the asynchronous tasks are initiated.
        self.started_time_begin = started_time_begin
        # The end time of the period during which the asynchronous tasks are initiated.
        self.started_time_end = started_time_end
        # The state of asynchronous tasks. The following items list the states of an asynchronous task:
        # 
        # *   Enqueued: The asynchronous invocation is enqueued and waiting to be executed.
        # *   Dequeued: The asynchronous invocation is dequeued and waiting to be triggered.
        # *   Running: The invocation is being executed.
        # *   Succeeded: The invocation is successful.
        # *   Failed: The invocation fails.
        # *   Stopped: The invocation is terminated.
        # *   Stopping: The invocation is being terminated.
        # *   Expired: The maximum validity period of messages is specified for asynchronous invocation. The invocation is discarded and not executed because the specified maximum validity period of messages expires.
        # *   Invalid: The invocation is invalid and not executed due to specific reasons. For example, the function is deleted.
        # *   Retrying: The asynchronous invocation is being retried due to an execution error.
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

