# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListEventSubEventResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        has_more: bool = None,
        logs: List[main_models.ListEventSubEventResponseBodyLogs] = None,
        request_id: str = None,
    ):
        # The total number of callback records returned on the current page.
        self.count = count
        # Indicates whether the current page is followed by a page.
        self.has_more = has_more
        # The callback records.
        self.logs = logs
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.ListEventSubEventResponseBodyLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEventSubEventResponseBodyLogs(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        code: int = None,
        cost: int = None,
        data: str = None,
        message_id: str = None,
        sub_id: str = None,
        time: str = None,
        url: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The HTTP status code. A value of 200 indicates that the callback was successful.
        self.code = code
        # The callback duration. Unit: milliseconds.
        self.cost = cost
        # The details about the callback.
        self.data = data
        # The ID of the callback record.
        self.message_id = message_id
        # The subscription ID.
        self.sub_id = sub_id
        # The time when the callback was generated.
        self.time = time
        # The callback URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.code is not None:
            result['Code'] = self.code

        if self.cost is not None:
            result['Cost'] = self.cost

        if self.data is not None:
            result['Data'] = self.data

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.sub_id is not None:
            result['SubId'] = self.sub_id

        if self.time is not None:
            result['Time'] = self.time

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Cost') is not None:
            self.cost = m.get('Cost')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

