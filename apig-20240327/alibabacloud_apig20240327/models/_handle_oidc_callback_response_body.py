# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HandleOidcCallbackResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.HandleOidcCallbackResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.HandleOidcCallbackResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class HandleOidcCallbackResponseBodyData(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        expires_in: int = None,
        token_type: str = None,
    ):
        # The access token returned for the current OIDC logon. The API definition marks this field as sensitive.
        self.access_token = access_token
        # The validity period value of the access token. The unit is not specified in the API definition.
        self.expires_in = expires_in
        # The type identifier of the access token. The valid values are not specified in the API definition.
        self.token_type = token_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['accessToken'] = self.access_token

        if self.expires_in is not None:
            result['expiresIn'] = self.expires_in

        if self.token_type is not None:
            result['tokenType'] = self.token_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')

        if m.get('expiresIn') is not None:
            self.expires_in = m.get('expiresIn')

        if m.get('tokenType') is not None:
            self.token_type = m.get('tokenType')

        return self

