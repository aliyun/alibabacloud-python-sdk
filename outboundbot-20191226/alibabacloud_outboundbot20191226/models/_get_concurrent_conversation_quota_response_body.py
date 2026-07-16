# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConcurrentConversationQuotaResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        max_concurrent: int = None,
        message: str = None,
        remaining_concurrent: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # API status code
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Maximum number of concurrent conversations
        self.max_concurrent = max_concurrent
        # API message
        self.message = message
        # Remaining concurrent conversations
        self.remaining_concurrent = remaining_concurrent
        # Request ID
        self.request_id = request_id
        # Indicates if the call succeeded.
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.max_concurrent is not None:
            result['MaxConcurrent'] = self.max_concurrent

        if self.message is not None:
            result['Message'] = self.message

        if self.remaining_concurrent is not None:
            result['RemainingConcurrent'] = self.remaining_concurrent

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxConcurrent') is not None:
            self.max_concurrent = m.get('MaxConcurrent')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RemainingConcurrent') is not None:
            self.remaining_concurrent = m.get('RemainingConcurrent')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

