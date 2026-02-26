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
        # Weboffice access token.
        self.access_token = access_token
        # Expiration time of the access token. The expiration time is 30 minutes.
        self.access_token_expired_time = access_token_expired_time
        # Weboffice refresh token.
        self.refresh_token = refresh_token
        # Expiration time of the refresh token. The expiration time is 1 day.
        self.refresh_token_expired_time = refresh_token_expired_time
        # Request ID.
        self.request_id = request_id
        # Weboffice entry URL. Used for online preview or editing of documents.
        # > Cannot be opened directly in a browser; it needs to be used with the Weboffice JS-SDK and access token (AccessToken) to preview or edit documents. For more information, see [Getting Started](https://help.aliyun.com/document_detail/468066.html).
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

