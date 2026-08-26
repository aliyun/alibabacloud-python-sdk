# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListRtcMPUEventSubRecordResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        has_more: bool = None,
        logs: List[main_models.ListRtcMPUEventSubRecordResponseBodyLogs] = None,
        request_id: str = None,
    ):
        # The total number of callback records returned on the current page.
        self.count = count
        # Indicates whether there is a next page.
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
                temp_model = main_models.ListRtcMPUEventSubRecordResponseBodyLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRtcMPUEventSubRecordResponseBodyLogs(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        callback_url: str = None,
        cost: int = None,
        data: str = None,
        httpcode: str = None,
        msg_id: str = None,
        sub_id: str = None,
        time: str = None,
    ):
        # The ID of the subscribed application.
        self.app_id = app_id
        # The callback URL.
        self.callback_url = callback_url
        # The callback duration. Unit: milliseconds.
        self.cost = cost
        # The callback content. For more information, see [Create a stream mixing and forwarding event callback](https://help.aliyun.com/document_detail/2804583.html).
        self.data = data
        # The error code. A value of 200 indicates that the callback was successful.
        self.httpcode = httpcode
        # The callback record ID.
        self.msg_id = msg_id
        # The event callback ID.
        self.sub_id = sub_id
        # The time when the callback was invoked.
        # Format: yyyy-MM-ddTHH:mm:ssZ (UTC).
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.cost is not None:
            result['Cost'] = self.cost

        if self.data is not None:
            result['Data'] = self.data

        if self.httpcode is not None:
            result['HTTPCode'] = self.httpcode

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.sub_id is not None:
            result['SubId'] = self.sub_id

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('Cost') is not None:
            self.cost = m.get('Cost')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('HTTPCode') is not None:
            self.httpcode = m.get('HTTPCode')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

