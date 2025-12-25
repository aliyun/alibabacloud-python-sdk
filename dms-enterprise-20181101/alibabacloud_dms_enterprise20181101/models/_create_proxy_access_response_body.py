# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProxyAccessResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        proxy_access_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned to the query task.
        self.error_code = error_code
        # The error message that is returned.
        self.error_message = error_message
        # The ID of the security protection authorization. After the security protection agent authorizes the target user, the system automatically generates a security protection authorization ID. The ID is globally unique.
        self.proxy_access_id = proxy_access_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.proxy_access_id is not None:
            result['ProxyAccessId'] = self.proxy_access_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ProxyAccessId') is not None:
            self.proxy_access_id = m.get('ProxyAccessId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

