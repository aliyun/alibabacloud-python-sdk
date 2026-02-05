# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCurrentConcurrencyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_concurrency: int = None,
        http_status_code: int = None,
        instance_id: str = None,
        max_concurrent_conversation: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.current_concurrency = current_concurrency
        self.http_status_code = http_status_code
        self.instance_id = instance_id
        self.max_concurrent_conversation = max_concurrent_conversation
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_concurrency is not None:
            result['CurrentConcurrency'] = self.current_concurrency

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_concurrent_conversation is not None:
            result['MaxConcurrentConversation'] = self.max_concurrent_conversation

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

        if m.get('CurrentConcurrency') is not None:
            self.current_concurrency = m.get('CurrentConcurrency')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxConcurrentConversation') is not None:
            self.max_concurrent_conversation = m.get('MaxConcurrentConversation')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

