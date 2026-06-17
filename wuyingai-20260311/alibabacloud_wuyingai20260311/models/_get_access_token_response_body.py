# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAccessTokenResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        access_token: str = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the authentication failure.
        self.access_denied_detail = access_denied_detail
        # The JWT used as the Authorization query parameter for the Chat operation. The token is valid for a limited period of time.
        self.access_token = access_token
        # The business status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error details. This parameter is returned only when the request fails.
        self.message = message
        # The request ID, in UUID format. The first and last characters are retained for illustration purposes.
        self.request_id = request_id
        # Indicates whether the request was successful.
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

        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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

        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

