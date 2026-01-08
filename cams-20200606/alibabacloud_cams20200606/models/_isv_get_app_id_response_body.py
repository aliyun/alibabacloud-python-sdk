# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IsvGetAppIdResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        app_id: str = None,
        code: str = None,
        config_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The message ID.
        self.app_id = app_id
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The ID of the configuration item.
        self.config_id = config_id
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.code is not None:
            result['Code'] = self.code

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

