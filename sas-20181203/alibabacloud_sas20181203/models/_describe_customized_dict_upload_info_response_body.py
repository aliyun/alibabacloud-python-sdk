# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomizedDictUploadInfoResponseBody(DaraModel):
    def __init__(
        self,
        accessid: str = None,
        expire: str = None,
        host: str = None,
        key: str = None,
        policy: str = None,
        request_id: str = None,
        security_token: str = None,
        signature: str = None,
    ):
        # The AccessKey ID that is required to access the OSS object.
        self.accessid = accessid
        # The time when the OSS signature expires. This value is a UNIX timestamp.
        self.expire = expire
        # The OSS endpoint.
        self.host = host
        # The key of the OSS object.
        self.key = key
        # The policy of the OSS bucket.
        self.policy = policy
        # The request ID.
        self.request_id = request_id
        # The security token.
        self.security_token = security_token
        # The OSS signature.
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessid is not None:
            result['Accessid'] = self.accessid

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.host is not None:
            result['Host'] = self.host

        if self.key is not None:
            result['Key'] = self.key

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.signature is not None:
            result['Signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        return self

