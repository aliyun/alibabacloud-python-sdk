# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBatchExportTasksRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        gateway_id: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        statuses: str = None,
    ):
        # The end of the creation time range. Format: yyyy-MM-dd\\"T\\"HH:mm:ss\\"Z\\".
        self.end_time = end_time
        # The gateway instance ID. If specified, only tasks under this gateway are returned.
        self.gateway_id = gateway_id
        # The maximum number of tasks to return in a single request.
        self.max_results = max_results
        # The paging token that indicates the start position of the next query.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The start of the creation time range. Format: yyyy-MM-dd\\"T\\"HH:mm:ss\\"Z\\".
        self.start_time = start_time
        # The list of task statuses. Separate multiple statuses with commas (,).
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.statuses is not None:
            result['statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('statuses') is not None:
            self.statuses = m.get('statuses')

        return self

