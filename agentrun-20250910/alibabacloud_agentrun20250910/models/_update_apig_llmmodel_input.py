# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateApigLLMModelInput(DaraModel):
    def __init__(
        self,
        address: str = None,
        api_key: str = None,
        desc: str = None,
        models: List[str] = None,
        name: str = None,
        provider: str = None,
        type: str = None,
    ):
        self.address = address
        self.api_key = api_key
        self.desc = desc
        self.models = models
        self.name = name
        self.provider = provider
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.desc is not None:
            result['desc'] = self.desc

        if self.models is not None:
            result['models'] = self.models

        if self.name is not None:
            result['name'] = self.name

        if self.provider is not None:
            result['provider'] = self.provider

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('models') is not None:
            self.models = m.get('models')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

