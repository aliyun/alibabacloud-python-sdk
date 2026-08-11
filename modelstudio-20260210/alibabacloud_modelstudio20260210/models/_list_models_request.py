# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListModelsRequest(DaraModel):
    def __init__(
        self,
        capabilities: List[str] = None,
        context_window: int = None,
        features: List[str] = None,
        language: str = None,
        max_results: int = None,
        model: str = None,
        name: str = None,
        next_token: str = None,
        providers: List[str] = None,
    ):
        self.capabilities = capabilities
        self.context_window = context_window
        self.features = features
        self.language = language
        self.max_results = max_results
        self.model = model
        self.name = name
        self.next_token = next_token
        self.providers = providers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capabilities is not None:
            result['capabilities'] = self.capabilities

        if self.context_window is not None:
            result['contextWindow'] = self.context_window

        if self.features is not None:
            result['features'] = self.features

        if self.language is not None:
            result['language'] = self.language

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.model is not None:
            result['model'] = self.model

        if self.name is not None:
            result['name'] = self.name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.providers is not None:
            result['providers'] = self.providers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capabilities') is not None:
            self.capabilities = m.get('capabilities')

        if m.get('contextWindow') is not None:
            self.context_window = m.get('contextWindow')

        if m.get('features') is not None:
            self.features = m.get('features')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('providers') is not None:
            self.providers = m.get('providers')

        return self

