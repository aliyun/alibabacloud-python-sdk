# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadInfo(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        host: str = None,
        key: str = None,
        policy: str = None,
        policy_signature: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.access_id = access_id
        # This parameter is required.
        self.host = host
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.policy = policy
        # This parameter is required.
        self.policy_signature = policy_signature
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['accessId'] = self.access_id

        if self.host is not None:
            result['host'] = self.host

        if self.key is not None:
            result['key'] = self.key

        if self.policy is not None:
            result['policy'] = self.policy

        if self.policy_signature is not None:
            result['policySignature'] = self.policy_signature

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessId') is not None:
            self.access_id = m.get('accessId')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('policy') is not None:
            self.policy = m.get('policy')

        if m.get('policySignature') is not None:
            self.policy_signature = m.get('policySignature')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

