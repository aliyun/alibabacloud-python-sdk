# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Credential(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        policy: str = None,
        security_token: str = None,
        signature: str = None,
    ):
        # This parameter is required.
        self.access_id = access_id
        # This parameter is required.
        self.dir = dir
        # This parameter is required.
        self.expire = expire
        # This parameter is required.
        self.host = host
        # This parameter is required.
        self.policy = policy
        # This parameter is required.
        self.security_token = security_token
        # This parameter is required.
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['accessId'] = self.access_id

        if self.dir is not None:
            result['dir'] = self.dir

        if self.expire is not None:
            result['expire'] = self.expire

        if self.host is not None:
            result['host'] = self.host

        if self.policy is not None:
            result['policy'] = self.policy

        if self.security_token is not None:
            result['securityToken'] = self.security_token

        if self.signature is not None:
            result['signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessId') is not None:
            self.access_id = m.get('accessId')

        if m.get('dir') is not None:
            self.dir = m.get('dir')

        if m.get('expire') is not None:
            self.expire = m.get('expire')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('policy') is not None:
            self.policy = m.get('policy')

        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        return self

