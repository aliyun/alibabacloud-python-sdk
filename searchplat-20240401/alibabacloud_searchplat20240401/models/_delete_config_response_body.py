# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class DeleteConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DeleteConfigResponseBodyResult = None,
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
            temp_model = main_models.DeleteConfigResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class DeleteConfigResponseBodyResult(DaraModel):
    def __init__(
        self,
        config_type: str = None,
        deleted: bool = None,
        id: str = None,
        workspace_id: str = None,
    ):
        # The configuration type.
        # 
        # - prompt
        # 
        # - lark
        self.config_type = config_type
        # Indicates whether the configuration is deleted.
        self.deleted = deleted
        # The configuration ID.
        self.id = id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_type is not None:
            result['configType'] = self.config_type

        if self.deleted is not None:
            result['deleted'] = self.deleted

        if self.id is not None:
            result['id'] = self.id

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        if m.get('deleted') is not None:
            self.deleted = m.get('deleted')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

