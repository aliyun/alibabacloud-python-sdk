# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ProviderSettings(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        base_url: str = None,
        model_names: List[str] = None,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.model_names = model_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.base_url is not None:
            result['baseUrl'] = self.base_url

        if self.model_names is not None:
            result['modelNames'] = self.model_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('baseUrl') is not None:
            self.base_url = m.get('baseUrl')

        if m.get('modelNames') is not None:
            self.model_names = m.get('modelNames')

        return self

