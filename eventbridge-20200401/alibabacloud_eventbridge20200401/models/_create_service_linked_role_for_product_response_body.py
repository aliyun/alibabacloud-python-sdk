# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceLinkedRoleForProductResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code
        self.http_code = http_code
        # The returned message. If the request is successful, success is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. If the operation was successful, the value true is returned.
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

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

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

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

