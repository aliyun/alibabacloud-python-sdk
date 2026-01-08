# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateFlowVersionResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        response: Dict[str, Any] = None,
        success: bool = None,
    ):
        # Details of access denial.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Content of the returned data.
        self.response = response
        # Indicates whether the operation was successful. Values: true for success, false for failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.response is not None:
            result['Response'] = self.response

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Response') is not None:
            self.response = m.get('Response')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

