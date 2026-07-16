# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkspaceRolesRequest(DaraModel):
    def __init__(
        self,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        role_ids: str = None,
        role_name: str = None,
        role_type: str = None,
        sort_by: str = None,
        status: str = None,
        verbose_fields: str = None,
    ):
        # The sort order for the specified sort field. Valid values:
        # 
        # - `ASC` (default): Ascending order.
        # 
        # - `DESC`: Descending order.
        self.order = order
        # The page number. Pages start from 1. The default value is 1.
        self.page_number = page_number
        # The number of entries per page. The default value is 20.
        self.page_size = page_size
        # A comma-separated list of role IDs.
        self.role_ids = role_ids
        # The role name.
        self.role_name = role_name
        # The role type.
        # 
        # - `custom`: A custom role.
        self.role_type = role_type
        # The sort field for paginated queries. Valid values:
        # 
        # - `GmtCreateTime` (default): Sorts by creation time.
        # 
        # - `GmtModifiedTime`: Sorts by modification time.
        self.sort_by = sort_by
        # The status. Valid values:
        # 
        # - `Creating`
        # 
        # - `Updating`
        # 
        # - `Deleting`
        # 
        # - `Succeeded`: A terminal state.
        # 
        # - `Failed`: A terminal state.
        self.status = status
        # A comma-separated list of fields to return. Currently, only `ModulePermissions` is supported, which returns the permission configuration of the role.
        self.verbose_fields = verbose_fields

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        if self.verbose_fields is not None:
            result['VerboseFields'] = self.verbose_fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VerboseFields') is not None:
            self.verbose_fields = m.get('VerboseFields')

        return self

