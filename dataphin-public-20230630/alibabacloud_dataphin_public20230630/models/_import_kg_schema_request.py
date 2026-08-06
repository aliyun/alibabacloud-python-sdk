# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ImportKgSchemaRequest(DaraModel):
    def __init__(
        self,
        import_command: main_models.ImportKgSchemaRequestImportCommand = None,
        op_tenant_id: int = None,
        workspace_id: str = None,
    ):
        # The instruction for importing the knowledge graph definition.
        # 
        # This parameter is required.
        self.import_command = import_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.import_command:
            self.import_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_command is not None:
            result['ImportCommand'] = self.import_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportCommand') is not None:
            temp_model = main_models.ImportKgSchemaRequestImportCommand()
            self.import_command = temp_model.from_map(m.get('ImportCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class ImportKgSchemaRequestImportCommand(DaraModel):
    def __init__(
        self,
        content: str = None,
        input_format: str = None,
        merge_strategy: str = None,
    ):
        # The knowledge graph definition content converted based on the specified format.
        self.content = content
        # The format of the knowledge graph definition content. Valid values: json and yaml. Default value: yaml.
        self.input_format = input_format
        # The merge strategy for the knowledge graph definition content. Valid values: replace and merge. Default value: replace.
        self.merge_strategy = merge_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.input_format is not None:
            result['InputFormat'] = self.input_format

        if self.merge_strategy is not None:
            result['MergeStrategy'] = self.merge_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')

        if m.get('MergeStrategy') is not None:
            self.merge_strategy = m.get('MergeStrategy')

        return self

