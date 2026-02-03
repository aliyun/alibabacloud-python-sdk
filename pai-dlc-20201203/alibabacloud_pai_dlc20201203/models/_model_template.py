# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelTemplate(DaraModel):
    def __init__(
        self,
        collections: str = None,
        model_name: str = None,
        provider: str = None,
    ):
        self.collections = collections
        self.model_name = model_name
        self.provider = provider

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collections is not None:
            result['Collections'] = self.collections

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.provider is not None:
            result['Provider'] = self.provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collections') is not None:
            self.collections = m.get('Collections')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        return self

