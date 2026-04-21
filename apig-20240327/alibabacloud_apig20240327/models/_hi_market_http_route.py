# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HiMarketHttpRoute(DaraModel):
    def __init__(
        self,
        builtin: bool = None,
        description: str = None,
        domains: List[main_models.HiMarketDomain] = None,
        match: main_models.HiMarketHttpRouteMatch = None,
    ):
        self.builtin = builtin
        self.description = description
        self.domains = domains
        self.match = match

    def validate(self):
        if self.domains:
            for v1 in self.domains:
                 if v1:
                    v1.validate()
        if self.match:
            self.match.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.builtin is not None:
            result['builtin'] = self.builtin

        if self.description is not None:
            result['description'] = self.description

        result['domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['domains'].append(k1.to_map() if k1 else None)

        if self.match is not None:
            result['match'] = self.match.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('builtin') is not None:
            self.builtin = m.get('builtin')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.domains = []
        if m.get('domains') is not None:
            for k1 in m.get('domains'):
                temp_model = main_models.HiMarketDomain()
                self.domains.append(temp_model.from_map(k1))

        if m.get('match') is not None:
            temp_model = main_models.HiMarketHttpRouteMatch()
            self.match = temp_model.from_map(m.get('match'))

        return self

class HiMarketHttpRouteMatch(DaraModel):
    def __init__(
        self,
        headers: List[main_models.HiMarketHttpRouteMatchHeaders] = None,
        methods: List[str] = None,
        model_matches: List[main_models.HiMarketHttpRouteMatchModelMatches] = None,
        path: main_models.HiMarketHttpRouteMatchPath = None,
        query_params: List[main_models.HiMarketHttpRouteMatchQueryParams] = None,
    ):
        self.headers = headers
        self.methods = methods
        self.model_matches = model_matches
        self.path = path
        self.query_params = query_params

    def validate(self):
        if self.headers:
            for v1 in self.headers:
                 if v1:
                    v1.validate()
        if self.model_matches:
            for v1 in self.model_matches:
                 if v1:
                    v1.validate()
        if self.path:
            self.path.validate()
        if self.query_params:
            for v1 in self.query_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['headers'] = []
        if self.headers is not None:
            for k1 in self.headers:
                result['headers'].append(k1.to_map() if k1 else None)

        if self.methods is not None:
            result['methods'] = self.methods

        result['modelMatches'] = []
        if self.model_matches is not None:
            for k1 in self.model_matches:
                result['modelMatches'].append(k1.to_map() if k1 else None)

        if self.path is not None:
            result['path'] = self.path.to_map()

        result['queryParams'] = []
        if self.query_params is not None:
            for k1 in self.query_params:
                result['queryParams'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.headers = []
        if m.get('headers') is not None:
            for k1 in m.get('headers'):
                temp_model = main_models.HiMarketHttpRouteMatchHeaders()
                self.headers.append(temp_model.from_map(k1))

        if m.get('methods') is not None:
            self.methods = m.get('methods')

        self.model_matches = []
        if m.get('modelMatches') is not None:
            for k1 in m.get('modelMatches'):
                temp_model = main_models.HiMarketHttpRouteMatchModelMatches()
                self.model_matches.append(temp_model.from_map(k1))

        if m.get('path') is not None:
            temp_model = main_models.HiMarketHttpRouteMatchPath()
            self.path = temp_model.from_map(m.get('path'))

        self.query_params = []
        if m.get('queryParams') is not None:
            for k1 in m.get('queryParams'):
                temp_model = main_models.HiMarketHttpRouteMatchQueryParams()
                self.query_params.append(temp_model.from_map(k1))

        return self

class HiMarketHttpRouteMatchQueryParams(DaraModel):
    def __init__(
        self,
        case_sensitive: bool = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.case_sensitive = case_sensitive
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class HiMarketHttpRouteMatchPath(DaraModel):
    def __init__(
        self,
        case_sensitive: bool = None,
        type: str = None,
        value: str = None,
    ):
        self.case_sensitive = case_sensitive
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class HiMarketHttpRouteMatchModelMatches(DaraModel):
    def __init__(
        self,
        case_sensitive: bool = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.case_sensitive = case_sensitive
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class HiMarketHttpRouteMatchHeaders(DaraModel):
    def __init__(
        self,
        case_sensitive: bool = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.case_sensitive = case_sensitive
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

