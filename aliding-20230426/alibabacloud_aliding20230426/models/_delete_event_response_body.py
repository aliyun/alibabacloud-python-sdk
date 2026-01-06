# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class DeleteEventResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.DeleteEventResponseBodyContent = None,
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
        # requestId
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
            result['content'] = self.content.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_ctx is not None:
            result['errorCtx'] = self.error_ctx

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            temp_model = main_models.DeleteEventResponseBodyContent()
            self.content = temp_model.from_map(m.get('content'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorCtx') is not None:
            self.error_ctx = m.get('errorCtx')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class DeleteEventResponseBodyContent(DaraModel):
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
            result['data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        return self

