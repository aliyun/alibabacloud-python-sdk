# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGatewayApisRequest(DaraModel):
    def __init__(
        self,
        api_status: str = None,
        api_type: str = None,
        app_id: str = None,
        group_id: int = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        sys_name: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.api_status = api_status
        self.api_type = api_type
        # This parameter is required.
        self.app_id = app_id
        self.group_id = group_id
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.sys_name = sys_name
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_status is not None:
            result['ApiStatus'] = self.api_status

        if self.api_type is not None:
            result['ApiType'] = self.api_type

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sys_name is not None:
            result['SysName'] = self.sys_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')

        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SysName') is not None:
            self.sys_name = m.get('SysName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

