# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class RemoveAttendeeResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.RemoveAttendeeResponseBodyContent = None,
        error_code: str = None,
        error_ctx: Dict[str, Any] = None,
        error_msg: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.content = content
        self.error_code = error_code
        self.error_ctx = error_ctx
        self.error_msg = error_msg
        self.http_status_code = http_status_code
        # RequestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_ctx is not None:
            result['ErrorCtx'] = self.error_ctx

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.RemoveAttendeeResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorCtx') is not None:
            self.error_ctx = m.get('ErrorCtx')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class RemoveAttendeeResponseBodyContent(DaraModel):
    def __init__(
        self,
        data: Any = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        return self

