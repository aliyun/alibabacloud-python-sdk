# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateUploadFilePolicyResponseBody(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        encoded_policy: str = None,
        expire_time: str = None,
        file_dir: str = None,
        file_url: str = None,
        host: str = None,
        request_id: str = None,
        signature: str = None,
    ):
        # OSSAccessKeyId
        self.access_id = access_id
        self.encoded_policy = encoded_policy
        self.expire_time = expire_time
        self.file_dir = file_dir
        self.file_url = file_url
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
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.encoded_policy is not None:
            result['EncodedPolicy'] = self.encoded_policy

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.file_dir is not None:
            result['FileDir'] = self.file_dir

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.host is not None:
            result['Host'] = self.host

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signature is not None:
            result['Signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('EncodedPolicy') is not None:
            self.encoded_policy = m.get('EncodedPolicy')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('FileDir') is not None:
            self.file_dir = m.get('FileDir')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        return self

