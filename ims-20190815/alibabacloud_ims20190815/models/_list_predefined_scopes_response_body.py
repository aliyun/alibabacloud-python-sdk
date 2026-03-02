# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListPredefinedScopesResponseBody(DaraModel):
    def __init__(
        self,
        predefined_scopes: main_models.ListPredefinedScopesResponseBodyPredefinedScopes = None,
        request_id: str = None,
    ):
        self.predefined_scopes = predefined_scopes
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.predefined_scopes:
            self.predefined_scopes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.predefined_scopes is not None:
            result['PredefinedScopes'] = self.predefined_scopes.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PredefinedScopes') is not None:
            temp_model = main_models.ListPredefinedScopesResponseBodyPredefinedScopes()
            self.predefined_scopes = temp_model.from_map(m.get('PredefinedScopes'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPredefinedScopesResponseBodyPredefinedScopes(DaraModel):
    def __init__(
        self,
        predefined_scope: List[main_models.ListPredefinedScopesResponseBodyPredefinedScopesPredefinedScope] = None,
    ):
        self.predefined_scope = predefined_scope

    def validate(self):
        if self.predefined_scope:
            for v1 in self.predefined_scope:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PredefinedScope'] = []
        if self.predefined_scope is not None:
            for k1 in self.predefined_scope:
                result['PredefinedScope'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.predefined_scope = []
        if m.get('PredefinedScope') is not None:
            for k1 in m.get('PredefinedScope'):
                temp_model = main_models.ListPredefinedScopesResponseBodyPredefinedScopesPredefinedScope()
                self.predefined_scope.append(temp_model.from_map(k1))

        return self

class ListPredefinedScopesResponseBodyPredefinedScopesPredefinedScope(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

