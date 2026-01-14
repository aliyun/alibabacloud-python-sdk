# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyApiDatasourceParametersRequest(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        parameters: str = None,
        workspace_id: str = None,
    ):
        # The ID of the API data source.
        # 
        # This parameter is required.
        self.api_id = api_id
        # The configuration of API data parameters in the JSONArray format. You can modify a maximum of 10 parameters.
        # 
        # *   name: the name of a common parameter or a parameter in a query statement
        # *   value: the value of a common parameter or a parameter in a query statement.
        # 
        # This parameter is required.
        self.parameters = parameters
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

