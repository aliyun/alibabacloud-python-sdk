# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDynamicDictUploadInfoResponseBody(DaraModel):
    def __init__(
        self,
        accessid: str = None,
        expire: str = None,
        host: str = None,
        key: str = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
    ):
        # The AccessKey ID that is used to access OSS.
        self.accessid = accessid
        # The validity period of the signature. The value is a UNIX timestamp.
        self.expire = expire
        # The OSS endpoint.
        self.host = host
        # The name of the OSS object.
        self.key = key
        # The OSS security policy.
        self.policy = policy
        # The request ID.
        self.request_id = request_id
        # The signature that is calculated based on **AccessKeySecret** and **Policy**. When you call an OSS API operation, OSS uses the signature information to check the validity of the POST request.
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

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        return self

