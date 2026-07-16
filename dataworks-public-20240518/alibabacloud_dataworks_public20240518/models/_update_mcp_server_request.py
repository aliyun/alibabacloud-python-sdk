# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateMcpServerRequest(DaraModel):
    def __init__(
        self,
        custom_headers: Dict[str, Any] = None,
        name: str = None,
        transport: str = None,
        url: str = None,
        visibility: str = None,
        visibility_scope: main_models.UpdateMcpServerRequestVisibilityScope = None,
    ):
        # The new custom request headers, specified as key-value pairs.
        self.custom_headers = custom_headers
        # The name of the MCP Server to update.
        # 
        # This parameter is required.
        self.name = name
        # The new transport protocol.
        self.transport = transport
        # The new service address. The address must start with`https://`.
        self.url = url
        # The new visibility level.
        self.visibility = visibility
        # The new visibility scope. The fields in this object depend on the value of the `Visibility` parameter.
        self.visibility_scope = visibility_scope

    def validate(self):
        if self.visibility_scope:
            self.visibility_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_headers is not None:
            result['CustomHeaders'] = self.custom_headers

        if self.name is not None:
            result['Name'] = self.name

        if self.transport is not None:
            result['Transport'] = self.transport

        if self.url is not None:
            result['Url'] = self.url

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        if self.visibility_scope is not None:
            result['VisibilityScope'] = self.visibility_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomHeaders') is not None:
            self.custom_headers = m.get('CustomHeaders')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Transport') is not None:
            self.transport = m.get('Transport')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('VisibilityScope') is not None:
            temp_model = main_models.UpdateMcpServerRequestVisibilityScope()
            self.visibility_scope = temp_model.from_map(m.get('VisibilityScope'))

        return self

class UpdateMcpServerRequestVisibilityScope(DaraModel):
    def __init__(
        self,
        project_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        # The list of workspace IDs that can access the MCP Server. This parameter takes effect only when `Visibility` is set to `PROJECT`.
        self.project_ids = project_ids
        # The list of user IDs that can access the MCP Server. This parameter takes effect only when `Visibility` is set to `USER`.
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

