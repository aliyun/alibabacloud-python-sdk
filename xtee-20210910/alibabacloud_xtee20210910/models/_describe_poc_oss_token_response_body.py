# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePocOssTokenResponseBody(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        host: str = None,
        key: str = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
        result_object: bool = None,
    ):
        # AccessKeyId for OSS file upload
        self.access_id = access_id
        # Host address.
        self.host = host
        # The Key required for file upload.
        self.key = key
        # OSS security policy.
        self.policy = policy
        # Request ID.
        self.request_id = request_id
        # Upload signature information.
        self.signature = signature
        # Return result.
        self.result_object = result_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

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

        if self.result_object is not None:
            result['resultObject'] = self.result_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

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

        if m.get('resultObject') is not None:
            self.result_object = m.get('resultObject')

        return self

