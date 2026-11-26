# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupDirectoryRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        description: str = None,
        group_id: str = None,
        name: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        parent_directory_id: str = None,
        tenant_id: str = None,
    ):
        # The platform application token issued by the console. If specified, the operation is performed as the user identified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The workspace description.
        self.description = description
        # The project group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The updated name of the filtered view.
        # 
        # This parameter is required.
        self.name = name
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The directory ID.
        self.parent_directory_id = parent_directory_id
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.description is not None:
            result['description'] = self.description

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.name is not None:
            result['name'] = self.name

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.parent_directory_id is not None:
            result['parentDirectoryId'] = self.parent_directory_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('parentDirectoryId') is not None:
            self.parent_directory_id = m.get('parentDirectoryId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

