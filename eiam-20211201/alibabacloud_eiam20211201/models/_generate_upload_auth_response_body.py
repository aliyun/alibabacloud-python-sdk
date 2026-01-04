# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateUploadAuthResponseBody(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        down_load_url: str = None,
        encrypted_key: str = None,
        expire: int = None,
        host: str = None,
        key: str = None,
        plaintext_key: str = None,
        policy: str = None,
        request_id: str = None,
        security_token: str = None,
        signature: str = None,
    ):
        # 认证的AccessId
        self.access_id = access_id
        # 预下载地址
        self.down_load_url = down_load_url
        self.encrypted_key = encrypted_key
        # 过期时间
        self.expire = expire
        # bucket地址host
        self.host = host
        # 认证对应的key
        self.key = key
        self.plaintext_key = plaintext_key
        # 认证的policy
        self.policy = policy
        self.request_id = request_id
        self.security_token = security_token
        # 认证的签名
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

        if self.down_load_url is not None:
            result['DownLoadUrl'] = self.down_load_url

        if self.encrypted_key is not None:
            result['EncryptedKey'] = self.encrypted_key

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.host is not None:
            result['Host'] = self.host

        if self.key is not None:
            result['Key'] = self.key

        if self.plaintext_key is not None:
            result['PlaintextKey'] = self.plaintext_key

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
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('DownLoadUrl') is not None:
            self.down_load_url = m.get('DownLoadUrl')

        if m.get('EncryptedKey') is not None:
            self.encrypted_key = m.get('EncryptedKey')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('PlaintextKey') is not None:
            self.plaintext_key = m.get('PlaintextKey')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        return self

