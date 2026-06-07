# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateMcpServerRequest(DaraModel):
    def __init__(
        self,
        config: main_models.CreateMcpServerRequestConfig = None,
        name: str = None,
        visibility: str = None,
        visibility_scope: main_models.CreateMcpServerRequestVisibilityScope = None,
    ):
        self.config = config
        # This parameter is required.
        self.name = name
        self.visibility = visibility
        self.visibility_scope = visibility_scope

    def validate(self):
        if self.config:
            self.config.validate()
        if self.visibility_scope:
            self.visibility_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        if self.visibility_scope is not None:
            result['VisibilityScope'] = self.visibility_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.CreateMcpServerRequestConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('VisibilityScope') is not None:
            temp_model = main_models.CreateMcpServerRequestVisibilityScope()
            self.visibility_scope = temp_model.from_map(m.get('VisibilityScope'))

        return self

class CreateMcpServerRequestVisibilityScope(DaraModel):
    def __init__(
        self,
        project_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        self.project_ids = project_ids
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

class CreateMcpServerRequestConfig(DaraModel):
    def __init__(
        self,
        custom_headers: Dict[str, Any] = None,
        transport: str = None,
        url: str = None,
    ):
        self.custom_headers = custom_headers
        self.transport = transport
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_headers is not None:
            result['CustomHeaders'] = self.custom_headers

        if self.transport is not None:
            result['Transport'] = self.transport

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomHeaders') is not None:
            self.custom_headers = m.get('CustomHeaders')

        if m.get('Transport') is not None:
            self.transport = m.get('Transport')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

