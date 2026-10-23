# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListActionRecordsRequest(DaraModel):
    def __init__(
        self,
        action_names: str = None,
        end_time: int = None,
        filter: str = None,
        page: int = None,
        request_id: str = None,
        size: int = None,
        start_time: int = None,
        user_id: str = None,
    ):
        # Filters records by the name of the change operation. Separate multiple names with commas.
        self.action_names = action_names
        # The upper bound of the query range for the change start time. The value is a UNIX timestamp in milliseconds. If you do not specify this parameter, the current time is used.
        self.end_time = end_time
        # The display type of change records. Default value: ACTION_RECORD.
        self.filter = filter
        # The page number of the returned results.
        self.page = page
        # Filters records by the ID of the request that triggered the change.
        self.request_id = request_id
        # The number of records returned per page.
        self.size = size
        # The lower bound of the query range for the change start time. The value is a UNIX timestamp in milliseconds.
        self.start_time = start_time
        # Filters records by the ID of the user that triggered the change.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_names is not None:
            result['actionNames'] = self.action_names

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.filter is not None:
            result['filter'] = self.filter

        if self.page is not None:
            result['page'] = self.page

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.size is not None:
            result['size'] = self.size

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionNames') is not None:
            self.action_names = m.get('actionNames')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

