# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetQueryAnalysisRequest(DaraModel):
    def __init__(
        self,
        functions: List[main_models.GetQueryAnalysisRequestFunctions] = None,
        history: List[main_models.GetQueryAnalysisRequestHistory] = None,
        query: str = None,
    ):
        self.functions = functions
        self.history = history
        # This parameter is required.
        self.query = query

    def validate(self):
        if self.functions:
            for v1 in self.functions:
                 if v1:
                    v1.validate()
        if self.history:
            for v1 in self.history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['functions'] = []
        if self.functions is not None:
            for k1 in self.functions:
                result['functions'].append(k1.to_map() if k1 else None)

        result['history'] = []
        if self.history is not None:
            for k1 in self.history:
                result['history'].append(k1.to_map() if k1 else None)

        if self.query is not None:
            result['query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.functions = []
        if m.get('functions') is not None:
            for k1 in m.get('functions'):
                temp_model = main_models.GetQueryAnalysisRequestFunctions()
                self.functions.append(temp_model.from_map(k1))

        self.history = []
        if m.get('history') is not None:
            for k1 in m.get('history'):
                temp_model = main_models.GetQueryAnalysisRequestHistory()
                self.history.append(temp_model.from_map(k1))

        if m.get('query') is not None:
            self.query = m.get('query')

        return self

class GetQueryAnalysisRequestHistory(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

class GetQueryAnalysisRequestFunctions(DaraModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, Any] = None,
    ):
        self.name = name
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.parameters is not None:
            result['parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        return self

