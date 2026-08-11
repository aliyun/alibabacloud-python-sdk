# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class ListModelPermissionsRequest(DaraModel):
    def __init__(
        self,
        authorization_scope: str = None,
        filter: main_models.ListModelPermissionsRequestFilter = None,
        max_results: int = None,
        model_action: str = None,
        next_token: str = None,
        workspace_id: str = None,
    ):
        # The authorization query dimension. Valid values:
        # 
        # - **AUTHORIZED**: models that have been authorized for the specified modelAction. Use this value together with modelAction.
        # - **AUTHORIZABLE**: full authorizable catalog.
        self.authorization_scope = authorization_scope
        # The filter conditions.
        self.filter = filter
        # The maximum number of entries to return per page. Default value: 20. If the upper limit is exceeded, the error code InvalidParameter.maxResults is returned.
        self.max_results = max_results
        # The authorization action dimension. Valid values:
        # 
        # - **INFERENCE**: model inference authorization.
        self.model_action = model_action
        # The pagination token (offset) for the next page. Do not pass this parameter for the first page.
        self.next_token = next_token
        # The workspace ID. This parameter is required and cannot be empty.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_scope is not None:
            result['authorizationScope'] = self.authorization_scope

        if self.filter is not None:
            result['filter'] = self.filter.to_map()

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.model_action is not None:
            result['modelAction'] = self.model_action

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizationScope') is not None:
            self.authorization_scope = m.get('authorizationScope')

        if m.get('filter') is not None:
            temp_model = main_models.ListModelPermissionsRequestFilter()
            self.filter = temp_model.from_map(m.get('filter'))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('modelAction') is not None:
            self.model_action = m.get('modelAction')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ListModelPermissionsRequestFilter(DaraModel):
    def __init__(
        self,
        model: str = None,
        name: str = None,
    ):
        # The exact match for a single model.
        self.model = model
        # The fuzzy match for the model name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['model'] = self.model

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

