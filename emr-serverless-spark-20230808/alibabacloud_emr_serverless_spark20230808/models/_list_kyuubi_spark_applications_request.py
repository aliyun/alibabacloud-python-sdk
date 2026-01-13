# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListKyuubiSparkApplicationsRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        max_results: int = None,
        min_duration: int = None,
        next_token: str = None,
        order_by: List[str] = None,
        resource_queue_id: str = None,
        sort: str = None,
        start_time: main_models.ListKyuubiSparkApplicationsRequestStartTime = None,
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
        self.order_by = order_by
        self.resource_queue_id = resource_queue_id
        self.sort = sort
        # The range of start time.
        self.start_time = start_time

    def validate(self):
        if self.start_time:
            self.start_time.validate()

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

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id

        if self.sort is not None:
            result['sort'] = self.sort

        if self.start_time is not None:
            result['startTime'] = self.start_time.to_map()

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
            self.order_by = m.get('orderBy')

        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')

        if m.get('sort') is not None:
            self.sort = m.get('sort')

        if m.get('startTime') is not None:
            temp_model = main_models.ListKyuubiSparkApplicationsRequestStartTime()
            self.start_time = temp_model.from_map(m.get('startTime'))

        return self

class ListKyuubiSparkApplicationsRequestStartTime(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # The end of the start time range.
        self.end_time = end_time
        # The beginning of the start time range.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

