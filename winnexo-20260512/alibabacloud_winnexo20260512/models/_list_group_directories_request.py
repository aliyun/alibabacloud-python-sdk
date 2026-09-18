# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGroupDirectoriesRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        group_id: str = None,
        sort_field: str = None,
        sort_order: str = None,
        tenant_id: str = None,
    ):
        # The ID of a visible directory in the current space. If this parameter is omitted or set to root, the space root is queried. The first query reuses the existing service-initialized internal root directory.
        self.directory_id = directory_id
        # The ID of the collaborative share.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The sort field. Valid values: name, gmt_create, and gmt_modified.
        self.sort_field = sort_field
        # The sort order. Valid values: asc and desc.
        self.sort_order = sort_order
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.sort_field is not None:
            result['sortField'] = self.sort_field

        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('sortField') is not None:
            self.sort_field = m.get('sortField')

        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

