# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class WebTLSConfig(DaraModel):
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
            result['CipherSuites'] = self.cipher_suites

        if self.max_version is not None:
            result['MaxVersion'] = self.max_version

        if self.min_version is not None:
            result['MinVersion'] = self.min_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CipherSuites') is not None:
            self.cipher_suites = m.get('CipherSuites')

        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')

        if m.get('MinVersion') is not None:
            self.min_version = m.get('MinVersion')

        return self

