# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ApiKeyIdentityConfig(DaraModel):
    def __init__(
        self,
        apikey_source: main_models.ApiKeyIdentityConfigApikeySource = None,
        credentials: List[main_models.ApiKeyIdentityConfigCredentials] = None,
        type: str = None,
    ):
        self.apikey_source = apikey_source
        self.credentials = credentials
        self.type = type

    def validate(self):
        if self.apikey_source:
            self.apikey_source.validate()
        if self.credentials:
            for v1 in self.credentials:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey_source is not None:
            result['apikeySource'] = self.apikey_source.to_map()

        result['credentials'] = []
        if self.credentials is not None:
            for k1 in self.credentials:
                result['credentials'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apikeySource') is not None:
            temp_model = main_models.ApiKeyIdentityConfigApikeySource()
            self.apikey_source = temp_model.from_map(m.get('apikeySource'))

        self.credentials = []
        if m.get('credentials') is not None:
            for k1 in m.get('credentials'):
                temp_model = main_models.ApiKeyIdentityConfigCredentials()
                self.credentials.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ApiKeyIdentityConfigCredentials(DaraModel):
    def __init__(
        self,
        apikey: str = None,
        generate_mode: str = None,
    ):
        self.apikey = apikey
        self.generate_mode = generate_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey is not None:
            result['apikey'] = self.apikey

        if self.generate_mode is not None:
            result['generateMode'] = self.generate_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apikey') is not None:
            self.apikey = m.get('apikey')

        if m.get('generateMode') is not None:
            self.generate_mode = m.get('generateMode')

        return self

class ApiKeyIdentityConfigApikeySource(DaraModel):
    def __init__(
        self,
        source: str = None,
        value: str = None,
    ):
        self.source = source
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['source'] = self.source

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

