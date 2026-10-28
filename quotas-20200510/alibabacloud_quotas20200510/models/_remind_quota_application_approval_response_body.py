# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from darabonba.model import DaraModel

class RemindQuotaApplicationApprovalResponseBody(DaraModel):
    def __init__(
        self,
        allow_retry: bool = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Indicates whether the request can be retried. Valid values:
        # 
        # - false: The request cannot be retried.
        # 
        # - true: The request can be retried.
        self.allow_retry = allow_retry
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The array of error parameters.
        self.error_args = error_args
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the quota application.
        self.module = module
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - true: The request was successful.
        # 
        # - false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.module is not None:
            result['Module'] = self.module

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

