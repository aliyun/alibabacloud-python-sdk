# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendBatchSmsResponseBody(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The delivery receipt ID.
        # 
        # - You can use this ID to query the delivery status by calling the [QuerySendDetails](https://help.aliyun.com/document_detail/102352.html) operation.
        # 
        # - Log on to the [Short Message Service console](https://dysms.console.aliyun.com/dysms.htm#/overview) and go to **Statistics** > **Delivery Logs** to view delivery details.
        self.biz_id = biz_id
        # The request status code.
        # 
        # - A value of `OK` indicates a successful request.
        # 
        # - For a list of other error codes, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The description of the request status.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

