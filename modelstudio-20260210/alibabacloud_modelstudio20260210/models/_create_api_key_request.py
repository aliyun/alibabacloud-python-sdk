# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class CreateApiKeyRequest(DaraModel):
    def __init__(
        self,
        auth: main_models.CreateApiKeyRequestAuth = None,
        description: str = None,
        workspace_id: str = None,
    ):
        self.auth = auth
        self.description = description
        self.workspace_id = workspace_id

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

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth') is not None:
            temp_model = main_models.CreateApiKeyRequestAuth()
            self.auth = temp_model.from_map(m.get('auth'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self



class CreateApiKeyRequestAuth(DaraModel):
    def __init__(
        self,
        access_ips: List[str] = None,
        type: str = None,
    ):
        self.access_ips = access_ips
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_ips is not None:
            result['accessIps'] = self.access_ips

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessIps') is not None:
            self.access_ips = m.get('accessIps')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

