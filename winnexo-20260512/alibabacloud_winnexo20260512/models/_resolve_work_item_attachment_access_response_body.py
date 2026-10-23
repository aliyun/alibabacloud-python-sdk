# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResolveWorkItemAttachmentAccessResponseBody(DaraModel):
    def __init__(
        self,
        access_url: str = None,
        code: str = None,
        expires_at: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The short-term preview URL of the attachment. You can send a GET request to this URL before it expires.
        self.access_url = access_url
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The expiration time of the URL in ISO 8601 format.
        self.expires_at = expires_at
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_url is not None:
            result['accessUrl'] = self.access_url

        if self.code is not None:
            result['code'] = self.code

        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessUrl') is not None:
            self.access_url = m.get('accessUrl')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

