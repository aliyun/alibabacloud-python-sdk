# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOssUploadTokenResponseBody(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        expire_time: str = None,
        host: str = None,
        key: str = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
        url: str = None,
    ):
        self.access_id = access_id
        self.expire_time = expire_time
        self.host = host
        self.key = key
        self.policy = policy
        self.request_id = request_id
        self.signature = signature
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.host is not None:
            result['Host'] = self.host

        if self.key is not None:
            result['Key'] = self.key

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

