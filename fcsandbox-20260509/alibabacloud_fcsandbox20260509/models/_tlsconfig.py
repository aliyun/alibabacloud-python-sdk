# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class TLSConfig(DaraModel):
    def __init__(
        self,
        cipher_suites: List[str] = None,
        max_version: str = None,
        min_version: str = None,
    ):
        self.cipher_suites = cipher_suites
        self.max_version = max_version
        self.min_version = min_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cipher_suites is not None:
            result['cipherSuites'] = self.cipher_suites

        if self.max_version is not None:
            result['maxVersion'] = self.max_version

        if self.min_version is not None:
            result['minVersion'] = self.min_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cipherSuites') is not None:
            self.cipher_suites = m.get('cipherSuites')

        if m.get('maxVersion') is not None:
            self.max_version = m.get('maxVersion')

        if m.get('minVersion') is not None:
            self.min_version = m.get('minVersion')

        return self

