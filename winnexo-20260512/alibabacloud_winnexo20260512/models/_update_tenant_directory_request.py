# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTenantDirectoryRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        name: str = None,
        parent_id: int = None,
        path: str = None,
        tenant_id: str = None,
    ):
        # The folder description.
        self.description = description
        # The folder ID.
        self.directory_id = directory_id
        # The folder name.
        self.name = name
        # The parent label ID. Set this parameter to -**1** for the root folder.
        self.parent_id = parent_id
        # The path of the node.
        self.path = path
        # The ID of the effective tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.name is not None:
            result['name'] = self.name

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.path is not None:
            result['path'] = self.path

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

