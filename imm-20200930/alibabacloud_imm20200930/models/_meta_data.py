# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetaData(DaraModel):
    def __init__(
        self,
        identifier: str = None,
        provider: str = None,
        version: str = None,
    ):
        # The model type identifier.
        self.identifier = identifier
        # The model provider.
        self.provider = provider
        # The model version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

