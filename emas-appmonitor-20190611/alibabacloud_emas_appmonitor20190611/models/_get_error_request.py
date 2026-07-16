# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetErrorRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        biz_module: str = None,
        client_time: int = None,
        did: str = None,
        digest_hash: str = None,
        force: bool = None,
        os: str = None,
        uuid: str = None,
    ):
        # appKey
        # 
        # This parameter is required.
        self.app_key = app_key
        self.biz_module = biz_module
        # This parameter is required.
        self.client_time = client_time
        self.did = did
        self.digest_hash = digest_hash
        self.force = force
        self.os = os
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.biz_module is not None:
            result['BizModule'] = self.biz_module

        if self.client_time is not None:
            result['ClientTime'] = self.client_time

        if self.did is not None:
            result['Did'] = self.did

        if self.digest_hash is not None:
            result['DigestHash'] = self.digest_hash

        if self.force is not None:
            result['Force'] = self.force

        if self.os is not None:
            result['Os'] = self.os

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('BizModule') is not None:
            self.biz_module = m.get('BizModule')

        if m.get('ClientTime') is not None:
            self.client_time = m.get('ClientTime')

        if m.get('Did') is not None:
            self.did = m.get('Did')

        if m.get('DigestHash') is not None:
            self.digest_hash = m.get('DigestHash')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

