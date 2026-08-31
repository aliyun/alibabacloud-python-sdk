# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportKgSchemaRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        output_format: str = None,
        version_id: int = None,
        workspace_id: str = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id
        # The format of the exported content. Valid values: json and yaml. Default value: yaml.
        self.output_format = output_format
        # The version number. If this parameter is empty or set to -1, the model metadata in draft state is returned. If this parameter is set to 0, the model metadata of the latest version is returned.
        self.version_id = version_id
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
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.output_format is not None:
            result['OutputFormat'] = self.output_format

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

