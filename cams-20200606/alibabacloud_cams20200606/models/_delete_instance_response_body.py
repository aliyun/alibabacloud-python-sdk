# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInstanceResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The request status code.
        # 
        # - A value of `OK` means the request was successful.
        # 
        # - For other error codes, see the [Error Code List](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The response message.
        self.message = message
        # The unique ID for the request. Use it for troubleshooting.
        self.request_id = request_id
        # Specifies whether the request was successful. Valid values:
        # 
        # - `true`: The request was successful.
        # 
        # - `false`: The request failed.
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

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

