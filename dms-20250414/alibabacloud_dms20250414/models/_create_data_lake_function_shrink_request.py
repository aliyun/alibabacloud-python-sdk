# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataLakeFunctionShrinkRequest(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        function_input_shrink: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.function_input_shrink = function_input_shrink
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.function_input_shrink is not None:
            result['FunctionInput'] = self.function_input_shrink

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('FunctionInput') is not None:
            self.function_input_shrink = m.get('FunctionInput')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

