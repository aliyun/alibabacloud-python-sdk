# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpRouteMatch(DaraModel):
    def __init__(
        self,
        headers: List[main_models.HttpRouteMatchHeaders] = None,
        ignore_uri_case: bool = None,
        methods: List[str] = None,
        path: main_models.HttpRouteMatchPath = None,
        query_params: List[main_models.HttpRouteMatchQueryParams] = None,
    ):
        # The rules for matching based on HTTP request headers.
        self.headers = headers
        # Specifies whether the path is case-insensitive.
        self.ignore_uri_case = ignore_uri_case
        # The HTTP methods.
        self.methods = methods
        # The path rule.
        self.path = path
        # The rules for matching based on query parameters.
        self.query_params = query_params

    def validate(self):
        if self.headers:
            for v1 in self.headers:
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

        if self.ignore_uri_case is not None:
            result['ignoreUriCase'] = self.ignore_uri_case

        if self.methods is not None:
            result['methods'] = self.methods

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
                temp_model = main_models.HttpRouteMatchHeaders()
                self.headers.append(temp_model.from_map(k1))

        if m.get('ignoreUriCase') is not None:
            self.ignore_uri_case = m.get('ignoreUriCase')

        if m.get('methods') is not None:
            self.methods = m.get('methods')

        if m.get('path') is not None:
            temp_model = main_models.HttpRouteMatchPath()
            self.path = temp_model.from_map(m.get('path'))

        self.query_params = []
        if m.get('queryParams') is not None:
            for k1 in m.get('queryParams'):
                temp_model = main_models.HttpRouteMatchQueryParams()
                self.query_params.append(temp_model.from_map(k1))

        return self

class HttpRouteMatchQueryParams(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The parameter name.
        self.name = name
        # The match type. Valid values:
        # 
        # *   Exact: exact match
        # *   Prefix: prefix match
        # *   Regex: regular expression
        self.type = type
        # The parameter value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class HttpRouteMatchPath(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The path matching type. Valid values:
        # 
        # *   Exact: exact match
        # *   Prefix: prefix match
        # *   Regex: regular expression
        self.type = type
        # The path.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class HttpRouteMatchHeaders(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The header name.
        self.name = name
        # The match type. Valid values:
        # 
        # *   Exact: exact match
        # *   Prefix: prefix match
        # *   Regex: regular expression
        self.type = type
        # The header value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

