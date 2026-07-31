# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSQLWebSocketDomainResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        domain: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. A value of 200 indicates that the request succeeded.
        self.code = code
        # The domain name.
        self.domain = domain
        # The response message.
        # 
        # - Returns **Success** if the request succeeds.
        # 
        # - Returns a specific error code if the request fails.
        self.message = message
        # The unique identifier for the request.
        self.request_id = request_id
        # Indicates whether the API call succeeded. Valid values:
        # 
        # - **true**: The call succeeded.
        # 
        # - **false**: The call failed.
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

        if self.domain is not None:
            result['Domain'] = self.domain

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

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

