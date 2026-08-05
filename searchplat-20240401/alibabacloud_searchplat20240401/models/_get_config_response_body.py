# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class GetConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetConfigResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.GetConfigResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class GetConfigResponseBodyResult(DaraModel):
    def __init__(
        self,
        config_data: Dict[str, Any] = None,
        config_type: str = None,
        created_at: int = None,
        updated_at: int = None,
        workspace_id: str = None,
    ):
        # The configuration content.
        self.config_data = config_data
        # The configuration type.
        # 
        # - prompt
        # 
        # - lark
        self.config_type = config_type
        # The time when the configuration was created.
        self.created_at = created_at
        # The time when the configuration was last updated.
        self.updated_at = updated_at
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_data is not None:
            result['configData'] = self.config_data

        if self.config_type is not None:
            result['configType'] = self.config_type

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configData') is not None:
            self.config_data = m.get('configData')

        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

