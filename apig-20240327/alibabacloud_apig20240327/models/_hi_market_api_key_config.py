# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HiMarketApiKeyConfig(DaraModel):
    def __init__(
        self,
        credentials: List[main_models.HiMarketApiKeyConfigCredentials] = None,
        key: str = None,
        source: str = None,
    ):
        self.credentials = credentials
        self.key = key
        self.source = source

    def validate(self):
        if self.credentials:
            for v1 in self.credentials:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['credentials'] = []
        if self.credentials is not None:
            for k1 in self.credentials:
                result['credentials'].append(k1.to_map() if k1 else None)

        if self.key is not None:
            result['key'] = self.key

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.credentials = []
        if m.get('credentials') is not None:
            for k1 in m.get('credentials'):
                temp_model = main_models.HiMarketApiKeyConfigCredentials()
                self.credentials.append(temp_model.from_map(k1))

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

class HiMarketApiKeyConfigCredentials(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        mode: str = None,
    ):
        self.api_key = api_key
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.mode is not None:
            result['mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        return self

