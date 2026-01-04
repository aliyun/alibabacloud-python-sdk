# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class BatchEventMigrateInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.BatchEventMigrateInstanceResponseBodyResults] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # The results.
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.BatchEventMigrateInstanceResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class BatchEventMigrateInstanceResponseBodyResults(DaraModel):
    def __init__(
        self,
        code: int = None,
        event_id: str = None,
        message: str = None,
        resource_id: str = None,
    ):
        # The error code.
        self.code = code
        # The ID of the event.
        self.event_id = event_id
        # When Code!=200, it indicates the specific error message.
        self.message = message
        # The resource IDs.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.message is not None:
            result['Message'] = self.message

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

