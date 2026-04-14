# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class ListBlockSendingResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListBlockSendingResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListBlockSendingResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListBlockSendingResponseBodyData(DaraModel):
    def __init__(
        self,
        block_email: str = None,
        block_time: int = None,
        reason: int = None,
        send_time: int = None,
        sender_email: str = None,
    ):
        self.block_email = block_email
        self.block_time = block_time
        self.reason = reason
        self.send_time = send_time
        self.sender_email = sender_email

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_email is not None:
            result['BlockEmail'] = self.block_email

        if self.block_time is not None:
            result['BlockTime'] = self.block_time

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.send_time is not None:
            result['SendTime'] = self.send_time

        if self.sender_email is not None:
            result['SenderEmail'] = self.sender_email

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockEmail') is not None:
            self.block_email = m.get('BlockEmail')

        if m.get('BlockTime') is not None:
            self.block_time = m.get('BlockTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')

        if m.get('SenderEmail') is not None:
            self.sender_email = m.get('SenderEmail')

        return self

