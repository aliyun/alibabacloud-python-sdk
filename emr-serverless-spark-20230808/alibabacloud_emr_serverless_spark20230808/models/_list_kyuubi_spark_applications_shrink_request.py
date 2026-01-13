# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKyuubiSparkApplicationsShrinkRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        max_results: int = None,
        min_duration: int = None,
        next_token: str = None,
        order_by_shrink: str = None,
        resource_queue_id: str = None,
        sort: str = None,
        start_time_shrink: str = None,
    ):
        # The ID of the application that is submitted by using a Kyuubi gateway.
        self.application_id = application_id
        # The name of the Spark application that is submitted by using a Kyuubi gateway.
        self.application_name = application_name
        # The maximum number of entries to return.
        self.max_results = max_results
        self.min_duration = min_duration
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        self.order_by_shrink = order_by_shrink
        self.resource_queue_id = resource_queue_id
        self.sort = sort
        # The range of start time.
        self.start_time_shrink = start_time_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['applicationId'] = self.application_id

        if self.application_name is not None:
            result['applicationName'] = self.application_name

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.min_duration is not None:
            result['minDuration'] = self.min_duration

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.order_by_shrink is not None:
            result['orderBy'] = self.order_by_shrink

        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id

        if self.sort is not None:
            result['sort'] = self.sort

        if self.start_time_shrink is not None:
            result['startTime'] = self.start_time_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationId') is not None:
            self.application_id = m.get('applicationId')

        if m.get('applicationName') is not None:
            self.application_name = m.get('applicationName')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('minDuration') is not None:
            self.min_duration = m.get('minDuration')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('orderBy') is not None:
            self.order_by_shrink = m.get('orderBy')

        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')

        if m.get('sort') is not None:
            self.sort = m.get('sort')

        if m.get('startTime') is not None:
            self.start_time_shrink = m.get('startTime')

        return self

