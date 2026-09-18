# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGroupDirectoryRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        group_id: str = None,
        name: str = None,
        tenant_id: str = None,
    ):
        # The new description. If this parameter is set to an empty string, the description is cleared. If this parameter is omitted or set to null, the description remains unchanged. At least one of name or description must be non-null.
        self.description = description
        # The ID of the physical subfolder in the current space. The internal root folder and reference folders are not allowed.
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # The ID of the collaborative share.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The new name. If this parameter is omitted or set to null, the name remains unchanged.
        self.name = name
        # The tenant ID. This is a common parameter. If this parameter is not specified, the default tenant of the caller is used.
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

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.name is not None:
            result['name'] = self.name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

