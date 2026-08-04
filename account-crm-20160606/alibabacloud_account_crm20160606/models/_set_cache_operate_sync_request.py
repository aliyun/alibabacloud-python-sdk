# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetCacheOperateSyncRequest(DaraModel):
    def __init__(
        self,
        except_version: int = None,
        expire_seconds: int = None,
        key: str = None,
        set_type: str = None,
        value_clazz: str = None,
        value_string: str = None,
    ):
        self.except_version = except_version
        self.expire_seconds = expire_seconds
        self.key = key
        self.set_type = set_type
        self.value_clazz = value_clazz
        self.value_string = value_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.except_version is not None:
            result['ExceptVersion'] = self.except_version

        if self.expire_seconds is not None:
            result['ExpireSeconds'] = self.expire_seconds

        if self.key is not None:
            result['Key'] = self.key

        if self.set_type is not None:
            result['SetType'] = self.set_type

        if self.value_clazz is not None:
            result['ValueClazz'] = self.value_clazz

        if self.value_string is not None:
            result['ValueString'] = self.value_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptVersion') is not None:
            self.except_version = m.get('ExceptVersion')

        if m.get('ExpireSeconds') is not None:
            self.expire_seconds = m.get('ExpireSeconds')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('SetType') is not None:
            self.set_type = m.get('SetType')

        if m.get('ValueClazz') is not None:
            self.value_clazz = m.get('ValueClazz')

        if m.get('ValueString') is not None:
            self.value_string = m.get('ValueString')

        return self

