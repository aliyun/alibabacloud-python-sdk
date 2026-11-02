# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGatewayApiResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        error_field: str = None,
        http_status_code: int = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.error_field = error_field
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
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

        if self.error_field is not None:
            result['ErrorField'] = self.error_field

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('ErrorField') is not None:
            self.error_field = m.get('ErrorField')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

