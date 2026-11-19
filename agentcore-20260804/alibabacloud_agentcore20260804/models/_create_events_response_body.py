# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateEventsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateEventsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business result code.
        self.code = code
        # The operation result.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request processing description.
        self.message = message
        # The request ID used for troubleshooting.
        self.request_id = request_id
        # Indicates whether the request was successful. For batch operations, you must still check the result of each item.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateEventsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateEventsResponseBodyData(DaraModel):
    def __init__(
        self,
        results: List[main_models.CreateEventsResponseBodyDataResults] = None,
    ):
        # The write result for each item. A successful top-level response does not indicate that every item was successful.
        # 
        # This parameter is required.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.CreateEventsResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        return self

class CreateEventsResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        error: main_models.CreateEventsResponseBodyDataResultsError = None,
        event_id: str = None,
        received_at: int = None,
        status: str = None,
    ):
        # The error for the failed item.
        self.error = error
        # The event ID generated after the event is successfully saved.
        self.event_id = event_id
        # The time when the event reached the server after being successfully saved, in Unix milliseconds.
        self.received_at = received_at
        # The status. Valid values: STORED and FAILED.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['error'] = self.error.to_map()

        if self.event_id is not None:
            result['eventId'] = self.event_id

        if self.received_at is not None:
            result['receivedAt'] = self.received_at

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error') is not None:
            temp_model = main_models.CreateEventsResponseBodyDataResultsError()
            self.error = temp_model.from_map(m.get('error'))

        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')

        if m.get('receivedAt') is not None:
            self.received_at = m.get('receivedAt')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class CreateEventsResponseBodyDataResultsError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code.
        # 
        # This parameter is required.
        self.code = code
        # The error description.
        # 
        # This parameter is required.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

