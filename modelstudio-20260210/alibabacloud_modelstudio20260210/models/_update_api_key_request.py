# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class UpdateApiKeyRequest(DaraModel):
    def __init__(
        self,
        auth: main_models.UpdateApiKeyRequestAuth = None,
        description: str = None,
    ):
        # The API key permission settings.
        self.auth = auth
        # The description.
        self.description = description

    def validate(self):
        if self.auth:
            self.auth.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth is not None:
            result['auth'] = self.auth.to_map()

        if self.description is not None:
            result['description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth') is not None:
            temp_model = main_models.UpdateApiKeyRequestAuth()
            self.auth = temp_model.from_map(m.get('auth'))

        if m.get('description') is not None:
            self.description = m.get('description')

        return self

class UpdateApiKeyRequestAuth(DaraModel):
    def __init__(
        self,
        access_ips: List[str] = None,
        model_access_scope: main_models.UpdateApiKeyRequestAuthModelAccessScope = None,
        type: str = None,
    ):
        # The IP access whitelist.
        # 
        # > 
        # > - When you set custom permissions and do not specify the IP access whitelist, the server sets the whitelist to IPv4 (0.0.0.0/0) and IPv6 (::/0) by default, which allows all traffic.
        self.access_ips = access_ips
        self.model_access_scope = model_access_scope
        # Valid values:
        # 
        # - All: all permissions.
        # - Custom: custom permissions.
        self.type = type

    def validate(self):
        if self.model_access_scope:
            self.model_access_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_ips is not None:
            result['accessIps'] = self.access_ips

        if self.model_access_scope is not None:
            result['modelAccessScope'] = self.model_access_scope.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessIps') is not None:
            self.access_ips = m.get('accessIps')

        if m.get('modelAccessScope') is not None:
            temp_model = main_models.UpdateApiKeyRequestAuthModelAccessScope()
            self.model_access_scope = temp_model.from_map(m.get('modelAccessScope'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateApiKeyRequestAuthModelAccessScope(DaraModel):
    def __init__(
        self,
        accessible_models: List[str] = None,
        allow_all_models: bool = None,
    ):
        self.accessible_models = accessible_models
        self.allow_all_models = allow_all_models

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessible_models is not None:
            result['accessibleModels'] = self.accessible_models

        if self.allow_all_models is not None:
            result['allowAllModels'] = self.allow_all_models

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessibleModels') is not None:
            self.accessible_models = m.get('accessibleModels')

        if m.get('allowAllModels') is not None:
            self.allow_all_models = m.get('allowAllModels')

        return self

