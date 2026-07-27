# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportKgSchemaRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        output_format: str = None,
        version_id: int = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.output_format = output_format
        self.version_id = version_id
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

        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

