# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOssStsTokenResponseBody(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket: str = None,
        object_key_prefix: str = None,
        oss_region: str = None,
        request_id: str = None,
        security_token: str = None,
    ):
        # The AccessKey ID of the user.
        self.access_key_id = access_key_id
        # The STS temporary AccessKey secret.
        self.access_key_secret = access_key_secret
        # The logical OSS bucket name.
        self.bucket = bucket
        # The project storage path.
        self.object_key_prefix = object_key_prefix
        # The region to which the current OSS bucket belongs.
        self.oss_region = oss_region
        # The request ID.
        self.request_id = request_id
        # The Security Token Service (STS) token.
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.object_key_prefix is not None:
            result['ObjectKeyPrefix'] = self.object_key_prefix

        if self.oss_region is not None:
            result['OssRegion'] = self.oss_region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('ObjectKeyPrefix') is not None:
            self.object_key_prefix = m.get('ObjectKeyPrefix')

        if m.get('OssRegion') is not None:
            self.oss_region = m.get('OssRegion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

