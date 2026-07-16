# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddChatGroupResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        unique_code: str = None,
    ):
        # Details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code. Valid values:
        # 
        # - `OK`: The request was successful.
        # 
        # - For other error codes, see the [error code list](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The response message.
        self.message = message
        # The unique identifier for the request.
        self.request_id = request_id
        # Indicates if the API call succeeded. Valid values:
        # 
        # - **true**: The API call was successful.
        # 
        # - **false**: The API call failed.
        self.success = success
        # The unique request code.
        self.unique_code = unique_code

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

        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code

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

        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')

        return self

