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
        # The AccessKey ID of OSS.
        self.accessid = accessid
        # The expiration time of the OSS authorization, in timestamp format.
        self.expire = expire
        # The OSS domain name.
        self.host = host
        # The key of the OSS file name.
        self.key = key
        # The OSS security policy.
        self.policy = policy
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The signature information calculated based on **AccessKeySecret** and **Policy**. When you call an OSS API operation, OSS verifies this signature information to confirm the validity of the POST request.
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

