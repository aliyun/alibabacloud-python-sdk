# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateWebofficeTokenResponseBody(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        access_token_expired_time: str = None,
        refresh_token: str = None,
        refresh_token_expired_time: str = None,
        request_id: str = None,
        weboffice_url: str = None,
    ):
        # The Weboffice access credential.
        self.access_token = access_token
        # The expiration time of the access credential. The credential expires in 30 minutes. Format: YYYY-MM-DDTHH:mm:ss.
        self.access_token_expired_time = access_token_expired_time
        # The Weboffice refresh credential.
        self.refresh_token = refresh_token
        # The expiration time of the refresh credential. The credential expires in 1 day. Format: YYYY-MM-DDTHH:mm:ss.
        self.refresh_token_expired_time = refresh_token_expired_time
        # The request ID.
        self.request_id = request_id
        # The Weboffice entry URL for previewing or editing documents online.
        # > This URL cannot be opened directly in a browser. You must use it together with the Weboffice JS-SDK and the access credential (AccessToken) to preview or edit documents. For more information, see [Getting Started](https://help.aliyun.com/document_detail/468066.html).
        self.weboffice_url = weboffice_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time

        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token

        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.weboffice_url is not None:
            result['WebofficeURL'] = self.weboffice_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')

        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')

        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WebofficeURL') is not None:
            self.weboffice_url = m.get('WebofficeURL')

        return self

