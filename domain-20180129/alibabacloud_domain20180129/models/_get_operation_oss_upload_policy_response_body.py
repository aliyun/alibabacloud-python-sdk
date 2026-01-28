# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOperationOssUploadPolicyResponseBody(DaraModel):
    def __init__(
        self,
        accessid: str = None,
        encoded_policy: str = None,
        expire_time: str = None,
        file_dir: str = None,
        host: str = None,
        request_id: str = None,
        signature: str = None,
    ):
        self.accessid = accessid
        self.encoded_policy = encoded_policy
        self.expire_time = expire_time
        self.file_dir = file_dir
        # OSS Endpoint。
        self.host = host
        self.request_id = request_id
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

        if self.encoded_policy is not None:
            result['EncodedPolicy'] = self.encoded_policy

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.file_dir is not None:
            result['FileDir'] = self.file_dir

        if self.host is not None:
            result['Host'] = self.host

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signature is not None:
            result['Signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')

        if m.get('EncodedPolicy') is not None:
            self.encoded_policy = m.get('EncodedPolicy')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('FileDir') is not None:
            self.file_dir = m.get('FileDir')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        return self

