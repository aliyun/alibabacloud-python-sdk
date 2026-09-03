# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_umeng_push20220225 import models as main_models
from darabonba.model import DaraModel

class QueryMsgStatResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryMsgStatResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryMsgStatResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryMsgStatResponseBodyData(DaraModel):
    def __init__(
        self,
        accept: int = None,
        arrive: int = None,
        close_push: int = None,
        dismiss: int = None,
        msg_id: str = None,
        open: int = None,
        sent: int = None,
        status: int = None,
    ):
        self.accept = accept
        self.arrive = arrive
        self.close_push = close_push
        self.dismiss = dismiss
        self.msg_id = msg_id
        self.open = open
        self.sent = sent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept is not None:
            result['Accept'] = self.accept

        if self.arrive is not None:
            result['Arrive'] = self.arrive

        if self.close_push is not None:
            result['ClosePush'] = self.close_push

        if self.dismiss is not None:
            result['Dismiss'] = self.dismiss

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.open is not None:
            result['Open'] = self.open

        if self.sent is not None:
            result['Sent'] = self.sent

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accept') is not None:
            self.accept = m.get('Accept')

        if m.get('Arrive') is not None:
            self.arrive = m.get('Arrive')

        if m.get('ClosePush') is not None:
            self.close_push = m.get('ClosePush')

        if m.get('Dismiss') is not None:
            self.dismiss = m.get('Dismiss')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('Open') is not None:
            self.open = m.get('Open')

        if m.get('Sent') is not None:
            self.sent = m.get('Sent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

