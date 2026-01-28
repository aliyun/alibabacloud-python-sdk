# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQualificationUploadPolicyResponseBody(DaraModel):
    def __init__(
        self,
        accessid: str = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        policy: str = None,
        prefix: str = None,
        request_id: str = None,
        signature: str = None,
    ):
        self.accessid = accessid
        self.dir = dir
        self.expire = expire
        self.host = host
        self.policy = policy
        self.prefix = prefix
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

        if self.dir is not None:
            result['Dir'] = self.dir

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.host is not None:
            result['Host'] = self.host

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signature is not None:
            result['Signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')

        if m.get('Dir') is not None:
            self.dir = m.get('Dir')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        return self

